# define a list with different types, see the example in the lab
mixedTypeList = [50, 290587, 1.02, True, "My dog...Ah, I don't have.", "72" ]

# use for loop to traverse the list and print the data type for each item in the list
for item in mixedTypeList:
    print("Data type of {} is {}" .format(item, type(item)))