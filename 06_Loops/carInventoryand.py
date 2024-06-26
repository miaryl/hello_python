# import csv
import csv
import copy

#define a dictionary 
vehcle ={
    "vin" : "<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# iterate over the inicial keys and values of the diccionary
for key, value in vehcle.items():
    print("{} : {}" .format(key,value))

# define an empty list to hold the car inventory that you will read
myInventoryList = []


try:
    with open('c:/Users/gusw0/Desktop/hello_python/06_Loops/car_fleet.csv', 'r') as file:
        print("File opened successfully!")
except FileNotFoundError:
    print("File not found.")
    
# cory the CSV file into memory

with open('c:/Users/gusw0/Desktop/hello_python/06_Loops/car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(vehcle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

    currentVehicle = copy.deepcopy(vehcle)

