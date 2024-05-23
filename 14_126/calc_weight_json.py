# EX3 creating the main program
import jsonFileHandler

#Retrieve the the JSON data and store it in a data variable.
data = jsonFileHandler.read_json_file('files/insulin.json')

#Test if the returned data is not empty and obtain the insulin data.
if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
else:
    print("Error. Exiting program")
    