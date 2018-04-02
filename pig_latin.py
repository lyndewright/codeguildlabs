#pig latin version 1

print("Translate a word into Pig Latin!\n")


def converter():
    word = input("Type in word here: ")

    if (word[0]) == 'a' or (word[0]) == 'e' or (word[0]) == 'i' or (word[0]) == 'o' or (word[0]) == 'u':
        print(word + ' in Pig Latin is ' + word + 'yay')
    elif (word[0]) != 'a' or (word[0]) == 'e' or (word[0]) == 'i' or (word[0]) == 'o' or (word[0]) == 'u':
        print(word + ' in Pig Latin is ' + word[1:] + word[0] + 'ay')
    ask_again()


def ask_again():
    repeat = input("Would you like to translate another word? ")
    if repeat == "yes":
        converter()
    elif repeat == "no":
        print("Goodbye.")
        quit()
    else:
        print("Invalid... closing.")
        quit()

while True:
    converter()
    ask_again()
