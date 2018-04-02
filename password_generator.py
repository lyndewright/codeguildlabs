#version 3

import random
import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

print("Welcome to the password generator.")

def password_gen():
    lc_length = int(input("How many lower case letters would you like your password to have?: "))
    n_length = int(input("How many numbers would you like your password to have?: "))
    uc_length = int(input("How many upper case letters would you like your password to have?: "))
    sym_length = int(input("How many symbols would you like your password to have?: "))


    password_length = lc_length + n_length + uc_length + sym_length
    print(("Your password will hold {} characters.").format(password_length))

    lc = ''.join(random.sample(lower_case, lc_length))
    uc = ''.join(random.sample(upper_case, uc_length))
    dig = ''.join(random.sample(digits, n_length))
    sym = ''.join(random.sample(symbols, sym_length))

    password_lst = '{}{}{}{}'.format(lc, uc, dig, sym)
    password = ''.join(random.sample(password_lst, password_length))
    print(("Your password is : {}").format(password))
    new()
def new():
    new_password = input("Would you like to generate a different password? [Y/N]: ").upper()
    if new_password == 'Y':
        password_gen()
    elif new_password == 'N':
        print("Exiting password generator.")
        exit()
    else:
        print("I didn't understand.")
        new()


while True:
    password_gen()
    new()
