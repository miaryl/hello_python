from fizzbuzz import fizzbuzz
# fizzbuzz: una funcion que recibe una lista de enteros y devuelve
#Si el numero es divisible por 3, se devuelve "Fizz"
# - Si el numero es divisible por 5, se devuelve "Buzz"
# - Si el numero es divisible por 3 y 5, se devuelve "FizzBuzz"
# - En cualquier otro caso, se devuelve el numero

def test_se_devuelve_fizz_if_use_3_Div():
   assert fizzbuzz(3) == "Fizz"
  
def test_5_div():
   assert fizzbuzz(5) == "Buzz"
  
def test_pass_3_5_div():
   assert fizzbuzz(30)== "FizzBuzz"

def test_pass_number():
   assert fizzbuzz(2) == 2

from fizzbuzz import fizzbuzz_list
   
def test_fizzbuzz_list():
   list = [1,2,3,4,5,15]
   assert fizzbuzz_list(list) == [1, 2,"Fizz", 4, "Buzz", "FizzBuzz"]