from tkinter import *
from math import *

def draw_rotated_elipse_in_order(major:float,minor:float, center_x:float, center_y:float, rotation:float, color:str):
    points = [0]*58
    rot_points = [0]*58
    rotation = radians(rotation)
    #q1
    points[12] = major / 2
    points[13] = ((minor * sqrt(major**2 - points[12]**2)) / major)
    points[10] = points[12] + ((major - points[12]) / 2)
    points[11] = ((minor * sqrt(major**2 - points[10]**2)) / major)
    points[8] = points[10] + ((major - points[10]) / 2)
    points[9] = ((minor * sqrt(major**2 - points[8]**2)) / major)
    points[6] = points[8] + ((major - points[8]) / 2)
    points[7] = ((minor * sqrt(major**2 - points[6]**2)) / major)
    points[4] = points[6] + ((major - points[6]) / 2)
    points[5] = ((minor * sqrt(major**2 - points[4]**2)) / major)
    points[2] = points[4] + ((major - points[4]) / 2)
    points[3] = ((minor * sqrt(major**2 - points[2]**2)) / major)
    points[0] = major
    points[1] = 0
    #Q2
    points[14] = 0
    points[15] = minor
    points[16] = points[12] * -1
    points[17] = points[13]
    points[18] = points[10] * -1
    points[19] = points[11]
    points[20] = points[8] * -1
    points[21] = points[9]
    points[22] = points[6] * -1
    points[23] = points[7]
    points[24] = points[4] * -1
    points[25] = points[5]
    points[26] = points[2] * -1
    points[27] = points[3]
    points[28] = major * -1
    points[29] = 0
    #q3
    points[30] = points[2] * -1
    points[31] = points[3] * -1
    points[32] = points[4] * -1
    points[33] = points[5] * -1
    points[34] = points[6] * -1
    points[35] = points[7] * -1
    points[36] = points[8] * -1
    points[37] = points[9] * -1
    points[38] = points[10] * -1
    points[39] = points[11] * -1
    points[40] = points[12] * -1
    points[41] = points[13] * -1
    points[42] = 0
    points[43] = minor * -1
    #Q4
    points[44] = points[12]
    points[45] = points[13] * -1
    points[46] = points[10]
    points[47] = points[11] * -1
    points[48] = points[8]
    points[49] = points[9] * -1
    points[50] = points[6]
    points[51] = points[7] * -1
    points[52] = points[4]
    points[53] = points[5] * -1
    points[54] = points[2]
    points[55] = points[3] * -1
    points[56] = points[0]
    points[57] = points[1]

    #rotate
    n = 0
    while n < len(points):
        if n%2 == 0: #x
            rot_points[n] = (points[n] * cos(rotation)) - (points[n + 1] * sin(rotation))
        else: #y
            rot_points[n] = (points[n] * cos(rotation)) + (points[n - 1] * sin(rotation))
        n += 1

    #translate
    n = 0
    while n < len(points):
        if n%2 == 0:
            rot_points[n] = rot_points[n] + center_x
        else:
            rot_points[n] = rot_points[n] + center_y
        n += 1

    canvas.create_line(rot_points, smooth="True", fill=color)

root = Tk()
root.title("Canvas Testing")
canvasFrame = Frame(root)
canvasFrame.grid(column=2, row=0, sticky=(N, S, E, W))
canvas = Canvas(canvasFrame, width=500, height=500, background='black')
canvas.grid(column=0, row=0, sticky=(N, S, E, W))
canvas.create_line(10, 5, 200, 50)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

draw_rotated_elipse_in_order(160, 55, 160, 250, 20, "Blue")
draw_rotated_elipse_in_order(80, 40, 160, 250, 20, "Red")

root.mainloop()