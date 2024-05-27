# fizzbuzz: una funcion que recibe una lista de enteros y devuelve
#Si el numero es divisible por 3, se devuelve "Fizz"
# - Si el numero es divisible por 5, se devuelve "Buzz"
# - Si el numero es divisible por 3 y 5, se devuelve "FizzBuzz"
# - En cualquier otro caso, se devuelve el numero
def fizzbuzz(numero):
    if numero % 3 ==0 and numero % 5 == 0:
        return "FizzBuzz"
    if numero % 3 == 0:
        return "Fizz"
    if numero % 5 == 0:
        return "Buzz"
    
    return numero
    

def fizzbuzz_list(list):
    for number in list:
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        if number % 3 == 0:
            return "Fizz"
        if number % 5 == 0:
            return "Buzz"
        return number
    