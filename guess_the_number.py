# Guess the number versions 1 and 3

import random


x = random.randint(1,10)
guesses = 0



def number():
    print("The number I picked was {}.".format(x))

print("Pick a number between 1 and 10")


while guesses < 10:
    guess = int(input("Your Guess: "))
    guesses = guesses + 1
    if guess == x:
        print("You've got it!")
        number()
        print("You guessed {} times.".format(guesses))
        break
    elif guess > x:
        print("Too high. Try again.")
    elif guess < x:
        print("Too low. Try again.")
    else:
        number()
        break
if guess != x:
    print("Too bad, you only got 10 chances...")
    number()
