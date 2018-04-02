# version 1

phonebook = {'Jenny': {'Name': 'Jenny',
                        'Number': 8675309,
                        'Phrase': 'I\'ve got your number!'},
             'Simpson':{'Name': 'Simpson',
                        'Number': 1234567,
                        'Phrase': 'Mmmmm... donuts!'}
                        }


def create_contact(na, nu, ph):
    add_contact = phonebook[name] = {'Name': name, 'Number': number, 'Phrase': phrase}

def retrieve_contact(na):
    find_name = phonebook[retrieve]

    print(find_name)

def update_existing_contact(na, nu, ph):
    phonebook[name] = {'Name': name, 'Number': number, 'Phrase': phrase}

def delete_contact(na):
    del phonebook[delete_name]

def reveal_current_phonebook():
    print("Here is the updated phone book:\n ")
    print(phonebook)

print("*****Phonebook/Directory*****\n")
print("Current Phonebook/Directory: \n")
print(phonebook)

while True:

    new_contact = input("Would you like to create a new contact? (Y/N): ")
    if new_contact == 'Y':
        name = input("Name: ")
        number = input("Number: ")
        phrase = input("Phrase: ")
        create_contact(name, number, phrase)
        reveal_current_phonebook()
    elif new_contact == 'N':
        retrieve = input("Would you like to retrieve info from an existing contact? (Y/N): ")
        if retrieve == 'Y':
            retrieve = input("Please input full or partial name, number, or phrase:)
            retrieve_contact(retrieve)
        elif retrieve == 'N':
            update_existing = input("Would you like to update information from an existing contact? (Y/N): ")
            if update_existing == 'Y':
                name = input("Name: ")
                number = input("Number: ")
                phrase = input("Phrase: ")
                update_existing_contact(name, number, phrase)
                reveal_current_phonebook()
            elif update_existing == 'N':
                delete = input("Would you like to delete a contact? (Y/N): ")
                if delete == 'Y':
                    delete_name = input("Name: ")
                    delete_contact(delete_name)
                    reveal_current_phonebook()
                elif delete == 'N':
                    print("Closing Phonebook")
                quit()
    else:
        ("Closing Phonebook")
        quit()
