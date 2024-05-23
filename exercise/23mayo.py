#funcion
def saludar():
    print("bon dia")
#llamar function 
saludar()

# pass argument
def say_hi(name):
    print('bon dia', name)
# there is other options f"bon dia {name}" // "bon dia " + name
say_hi("Victoria")

# math time ah!
def cubico(a):
    return a*a*a # return devuelve valor

valor =cubico(5)
print(valor)

def sumar(a:int,b:int)->int:
    return a+b

def saludar_persona(persona="mundo"):
    print(f"buenos dias {persona}")

saludar_persona() # devuelve default -> mundo
saludar_persona("Mio") 

# lambda
multiplica = lambda a,b: a*b
print(multiplica(3,5))

#   ||
#  \  /
#   V     mismo

def multiplica(a,b):
    return a*b

#calcular el volmen de cilindro
def volume_cilinder(r:float, h:float)-> float:
    return((3.14159)*r*r*h)

print(volume_cilinder(5,3))

cylinder_vol = lambda rad, h: 3.14 * rad * rad * h
print(cylinder_vol(5,3))
