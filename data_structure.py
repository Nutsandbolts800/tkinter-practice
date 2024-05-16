data_structure = {}

def add_data_instance(new_data):
    if (new_data['name'] in data_structure):
        data_structure[new_data['name']].append(new_data)
    else:
        data_structure[new_data['name']] = []
        data_structure[new_data['name']].append(new_data)

add_data_instance({'name': 'data1', 'time':'today','data':'6usfon457jfdsgj'})
add_data_instance({'name': 'data2', 'time':'yesterday','data':'6uojgrs'})
add_data_instance({'name': 'data4', 'time':'wednesday','data':'sdfgysgj'})
add_data_instance({'name': 'data7', 'time':'tfridy','data':'ytegrsf'})
add_data_instance({'name': 'data3', 'time':'tyh','data':'dfcvgjbh'})
add_data_instance({'name': 'data3', 'time':'today','data':'6usfon457jfdsgj'})
add_data_instance({'name': 'data2', 'time':'yesterday','data':'6uojgrs'})
add_data_instance({'name': 'data4', 'time':'wednesday','data':'sdfgysgj'})
add_data_instance({'name': 'data5', 'time':'tfridy','data':'ytegrsf'})
add_data_instance({'name': 'data6', 'time':'tyh','data':'dfcvgjbh'})

print("Data structure current state: {0}".format(data_structure))

add_data_instance({'name': 'data1', 'time':'today','data':'6usfon457jfdsgj'})
print(data_structure['data1'][0]['data'])