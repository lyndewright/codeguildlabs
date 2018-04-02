# version 2

from random import choice

print("Welcome to the Magic 8 Ball.")

def magic_8_ball():
    question = input("What is your question?: ")
    answers = ['It is certain', 'Not a chance', 'It\'s possible, you\'ll have to wait and see.']
    print("Your answer is...\n: {}".format(choice(answers)))

while True:
    magic_8_ball()
    ask_again = input("Would you like to ask again? [Y/N]: ").upper()
    if ask_again == 'Y':
        continue
    elif ask_again == 'N':
        print("Closing.")
        quit()
    else:
        print("Closing.")
        quit()
