# functions
numeros = [1,2,3,4,5]

def cubico(number):
    return number **3

# map()??
result = map(cubico, numeros)
resultLambda = map(lambda x : x **3,numeros)

print(list(result))
print(list(resultLambda))

# ~~~~~~~~~
numeros = [1,2,3,4,5,6,7,8,9]

result = filter(lambda x: x > 5, numeros)
print(list(result))


# ~~~~~~~~
from functools import reduce
numeros = [1,2,3,4,5,6,7,8,9]
result = reduce(lambda x,y: x+y, numeros)

print(result)


