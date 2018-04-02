#version 2

import random

while True:
    numbers = [1, 2, 3]
    computer = random.choice(numbers)

    choice = input("Select 1 for Rock, 2 for Paper, or 3 for Scissors: ")
    choice = int(choice)

    def player_selection():
        if choice == 1:
            print("You choose Rock.")
        elif choice == 2:
            print("You choose Paper.")
        elif choice == 3:
            print("You choose Scissors.")
        else:
            print("That is not a valid choice.")


    def winner():
        if computer == 1 and choice == 1:
            print("Computer chooses Rock.\n Rock vs. Rock.\n Tie!")
        elif computer == 1 and choice == 2:
            print("Computer chooses Rock.\n Rock vs. Paper.\n Paper wraps rock. You win! ")
        elif computer == 1 and choice == 3:
            print("Computer chooses Rock.\n Rock vs. Scissors.\n Rock crushes scissors. Computer wins!")
        elif computer == 2 and choice == 1:
            print("Computer chooses Paper.\n Paper vs. Rock.\n  Paper wraps Rock. Computer wins!")
        elif computer == 2 and choice == 2:
            print("Computer chooses Paper.\n Paper vs. Paper.\n Tie! ")
        elif computer == 2 and choice == 3:
            print("Computer chooses Paper.\n Paper vs. Scissors.\n Scissors cuts Paper. You win!")
        elif computer == 3 and choice == 1:
            print("Computer chooses Scissors.\n Scissors vs. Rock.\n Rock crushes Scissors. You win!")
        elif computer == 3 and choice == 2:
            print("Computer chooses Scissors.\n Scissors vs. Paper.\n Scissors cuts Paper. Cmputer wins!")
        elif computer == 3 and choice == 3:
            print("Computer chooses Scissors.\n Scissors vs. Scissors.\n Tie!")
        else:
            print("Game Over!")
            quit()



    def play_again():
        new_game = input("Would you like to play another game? Y or N?: ")
        if new_game == 'Y':
            print("Here we go again!")
        elif new_game == 'N':
            print("Game Over.")
            quit()
        else:
            print("Game Over.")
            quit()


    player_selection()
    winner()
    play_again()
