# Una lista de usuarios, name, number, age con tres usuarios
user_list = [
    {"name" :"Emily", "phoneNum" : "845786921", "age" : 45},
    {"name" : "JJ", "phoneNum" : "264831587", "age": 40},
    {"name" : "Penelope", "phoneNum" : "555555645", "age" : 42 }]

print(user_list)
print(type(user_list))
print(user_list[1])

# add a new user
user_list.append({"name" : "Luke", "phoneNum": "75841235","age" :38})

print(user_list[3])

# Escribir por consola los nombres de la lista
for user in user_list:
    print(user["name"])

# show like that-> Alice | 25 | 628546595
for user in user_list:
    print(user["name"], "|", user["phoneNum"], "|", user["age"])

# also you can use format
for user in user_list:
    print(f"{user['name']} | {user['phoneNum']} | {user['age']}")

# Que os pida el nombre, la edad y el telefono lo guarde en la lista de usuarios
name = input("Name?: ")
phone = input("Phone?: ")
age = input("age?: ")

user_list.append({"name" : name, "phoneNum": phone, "age" : age})

for user in user_list:
    print(f"{user['name']} | {user['phoneNum']} | {user['age']}")