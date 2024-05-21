#print the game rules! 
print("WELCOME TO GUESS THE NUMBER!!!")
print("""
      The rules are simple. 
      I will think of a number, 
      and you will try to guess it ;)!
      """)

# import random 
import random

# male valuable to choose a number from 1 to 99
number = random.randint(1,99)

#Track whether the user guessed your number by creating a variable called guessRight
guessRight = False

# while loop until gamer can guess correct number
while guessRight != True:
    guess = input("Guess a number between 1 and 99: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        guessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))