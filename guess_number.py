#Number Guessing game 

import random

secret_number= random.randint(1 , 10)

guess = 0

while guess != secret_number:
    guess = int(input("guess a number between 1 and 10:" ))

    if guess < secret_number:
        print("too low!")
    elif guess > secret_number:
        print("too high!")
    else:
        print("correct! you guested it!")