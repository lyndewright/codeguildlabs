#mad lib version 3
import random

def collection():
    story_prompt = input("Would you like to write a madlib? [Y/N]: ").upper()

    if story_prompt == 'Y':
        adjective = input('Give me four adjectives, separated by commas: ').split()
        name = input('Give me a name: ')
        noun = input('Give me four nouns, separated by commas: ').split()
        number = input('Give me two numbers, separated by a comma: ').split()
        plural_shape = input('Give me a plural shape: ')
        food = input('Give me two types of food, separated by a comma: ').split()


        adjectives = random.shuffle(adjective)
        nouns = random.shuffle(noun)
        numbers = random.shuffle(number)
        foods = random.shuffle(food)


        madlib = '''Pizza was invented by a {} chef named {}. To make a pizza,
        you need to take a lump of {}, and make a thin, round {} {}. Then you
        cover it with {} sauce, {} cheese, and fresh chopped {}. Next you have
        to bake it in a very hot {}. When it is done, cut into {} {}. Some kids
        like {} pizza the best but my favorite is the {} pizza. If I could,
        I would eat pizza {} times a day!
        '''.format(adjective[0].strip(','), name, noun[0].strip(','),\
        adjective[1].strip(','), noun[1].strip(','), adjective[2].strip(','),\
        adjective[3], noun[2].strip(','), noun[3], number[0].strip(','),\
        plural_shape, food[0].strip(','), food[1], number[1])


        print("Here is your madlib:")
        print(madlib)
    elif story_prompt == 'N':
        print("Closing.")
        quit()


collection()
start_over = input("Would you like to start over? [Y/N]: ").upper()
if start_over == 'Y':
    collection()
elif start_over == 'N':
    print("Closing.")
    quit()
else:
    print("I didn't understand...")
