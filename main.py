from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from threading import Thread
import queue
import time

global tid

tid = ""

resultsdict = {}

liveresultsQueue = queue.SimpleQueue()
analysisresultsQueue = queue.SimpleQueue()

def update_results_live(): #logic for getting data from remote
    i = 1
    while (i < 101):
        #pull in data here and put into proper vars
        name = i
        hits = i
        lat = i
        long = i 
        datadict = {
            "name": "Data {0}".format(name),
            "hits": hits,
            "lat": lat,
            "long": long
        }   
        if (datadict['name'] in resultsdict):
            resultsdict[datadict['name']]['hits'] += 1
            break
        liveresultsQueue.put(datadict)
        if (i%5 == 0):
            root.event_generate("<<new_live_results>>")
        i = i+1       

def update_list_of_results_live(*args):
    print("Starting to empty live results queue")
    while (liveresultsQueue.empty() == False):
        p = liveresultsQueue.get()
        resultsdict[p['name']] = p
        listofresults.insert("end", p['name'])

def update_results_analysis():
    print("Analysis getter thread started...")
    analysisresultsQueue.put(["analysisresult1", "analysisresult2"])
    print("Analysis results retreived")
    root.event_generate("<<analysis_results_ready>>")

def update_list_of_results_analysis(*args):
    print("Main thread received analysis results: ")
    r = analysisresultsQueue.get()
    print(r)
    for x in r:
        listofresults.insert("end", x)

def get_tn():
    print("Getting TNs...")
    tn = [1,2,3,4,5] #replace with actual function to retrieve tns
    print("TNs retrieved: ")
    print(tn)
    return tn 

def get_fn(tn):
    print("Getting FNs...")
    fn = tn #replace with actual function to get fn from tn
    print("FNs retrieved: ")
    print(fn)
    return fn 

def get_tid(tn, fn):
    print("Getting TID...")
    tid = tn + fn #replace fn + tn with real logic to get tid from fn an tn
    print("TID is: " + tid)
    tid_label['text'] = "TID: " + tid 
    if(is_live == False):
        thread_update_results_analysis.start()
    if(is_live == True):
        thread_update_results_live.start()

def set_window_title(*args):
    if(is_live == True):
        print("Setting window title to: MID: {0} TID: {1}".format(mid.get(), tid))
        root.title(" MID: " + mid.get() + " " + tid_label['text'])
    if(is_live == False):
        print("Setting window title to: Analysis mode... {0}".format(tid_label['text']))
        root.title("Analysis mode... " + tid_label['text'])

def get_selection_details():
    current = listofresults.curselection()
    print(resultsdict[listofresults.get(current)]['name'])
    val1_label['text'] = resultsdict[listofresults.get(current)]['name']
    val2_label['text'] = resultsdict[listofresults.get(current)]['hits']
    val3_label['text'] = resultsdict[listofresults.get(current)]['lat']
    val4_label['text'] = resultsdict[listofresults.get(current)]['long']
    

def tn_selected():
    print("TN selected: {0}".format(selected_tn.get()))
    fn_combo.selection_clear
    tid_label['text'] = "TID: "
    set_window_title()
    fn_combo['values'] = get_fn(selected_tn.get())

def fn_selected():
    print("FN selected: {0}".format(selected_fn.get()))
    get_tid(selected_tn.get(), selected_fn.get())
    set_window_title()

tns = get_tn()

is_live = messagebox.askyesno("Live or Analysis?", "Choose Yes to stay in Live mode, or no for Analysis mode")

root = Tk()
root.title("")
root.attributes("-topmost", True)
settingsframe = ttk.Frame(root, padding="2")
settingsframe.grid(column=0, row=0, columnspan=4, sticky=(N, E, W))
resultsframe = ttk.Frame(root, padding="2")
resultsframe.grid(column=0, row=1, sticky=(N, W))
detailsframe = ttk.Frame(root, padding="2")
detailsframe.grid(column=1, row=1, sticky=(N, W))
canvasFrame = ttk.Frame(root)
canvasFrame.grid(column=2, row=0, sticky=(N, S, E, W))
root.columnconfigure(4, weight=1)
root.rowconfigure(4, weight=1)

mid = StringVar()
selected_tn = StringVar()
selected_fn = StringVar()

ttk.Label(settingsframe, text="MID:").grid(column=0, row=0)
mid_entry = ttk.Entry(settingsframe, width=7, textvariable=mid)
mid_entry.grid(column=1, row=0)
mid.trace_add('write', set_window_title)

ttk.Label(settingsframe, text="TN:").grid(column=2, row=0)
tn_combo = ttk.Combobox(settingsframe, values=tns, state= 'readonly', textvariable=selected_tn, width=6)
tn_combo.grid(column=3, row=0)
tn_combo.bind("<<ComboboxSelected>>", lambda event: tn_selected())

ttk.Label(settingsframe, text="FN:").grid(column=4, row=0)
fn_combo = ttk.Combobox(settingsframe, state='readonly', textvariable=selected_fn, width=5)
fn_combo.grid(column=5, row=0)
fn_combo.bind("<<ComboboxSelected>>", lambda event: fn_selected())

tid_label = ttk.Label(settingsframe, text="TID: ")
tid_label.grid(column=1, row=1, columnspan=8)

ttk.Label(resultsframe, text="Results:").grid(column=0, row=0)
listofresults = Listbox(resultsframe)
listofresults.grid(column=0, row=1, rowspan=10)
listofresults.bind("<<ListboxSelect>>", lambda event: get_selection_details())
ttk.Label(detailsframe).grid(column=0, row=0, columnspan=2)
ttk.Label(detailsframe, text="Name: ").grid(column=0,row=1, sticky=(E))
ttk.Label(detailsframe, text="Hits: ").grid(column=0,row=2, sticky=(E))
ttk.Label(detailsframe, text="Lat:  ").grid(column=0,row=3, sticky=(E))
ttk.Label(detailsframe, text="Long: ").grid(column=0,row=4, sticky=(E))
val1_label = ttk.Label(detailsframe, text = "")
val1_label.grid(column=1,row=1, sticky=(W))
val2_label = ttk.Label(detailsframe, text = "")
val2_label.grid(column=1,row=2, sticky=(W))
val3_label = ttk.Label(detailsframe, text = "")
val3_label.grid(column=1,row=3, sticky=(W))
val4_label = ttk.Label(detailsframe, text = "")
val4_label.grid(column=1,row=4, sticky=(W))
refresh_button = ttk.Button(detailsframe, text = "Refresh", command=get_selection_details)
refresh_button.grid(column=0, row=5, columnspan=2)

for child in settingsframe.winfo_children(): 
    child.grid_configure(padx=1, pady=1)

thread_update_results_live = Thread(target = update_results_live)

root.bind("<<new_live_results>>", update_list_of_results_live)

thread_update_results_analysis = Thread(target = update_results_analysis)

root.bind("<<analysis_results_ready>>", update_list_of_results_analysis)

if(is_live == False):
    mid_entry.config(state = 'disabled')
    set_window_title()
if(is_live == True):
    mid_entry.config(state = 'enabled')
    set_window_title()

canvas = Canvas(canvasFrame, width=500, height=500, background='black')
canvas.create_line(10, 5, 200, 50)

root.mainloop()