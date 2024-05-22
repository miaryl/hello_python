# for loops challenge
hijos = [ "juan", "Marta", "Laura", "Pedro"]

for hijo in hijos:
    print(hijo, "se está haciendo la cama")

# Range 
for numero in range(4):
    print(hijos[numero])

for numero in range(len(hijos)):
    print(numero)

# range(start,end,...)
for numero in range(2,10,2):
    print(numero)

# while loops -> mientras pasa A, hagamos B
lluvia = True
horas = 0 

while lluvia == True:
    print("Usamos paraguas")
    horas += 1
    if horas == 5 :
        lluvia = False
if lluvia == True:
    print("El suelo está mojado")

print("Hace sol")

# add all the numbers in show the result
numeros = [25, 55, 98, 10]

total_num = 0

for numero in numeros:
    total_num += numero
# if i write print() in for loop, show each result of calculation
# if only want total number, print() should be out of for loop
print(total_num)


# Or sum() is more easy
suma_lista = sum(numeros)
print(total_num)
