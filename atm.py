# atm version 1

atm = {'balance': 0, 'interest_rate': .01}

# returns the account balance
def check_balance():
    print("Your balance is: {}".format(atm['balance']))


# deposits the given amount in the account
def deposit(amount):
    atm['balance'] = atm['balance'] + dep
    return atm['balance']

# returns true if the withdrawn amount won’t put the account in the negative
def check_withdrawl(amount):
    if wd <= atm['balance']:
        return True
    else:
        return False

# withdraws the amount from the account and returns it
def withdraw(amount):
    atm['balance'] = atm['balance'] - wd
    return atm['balance']

# returns the amount of interest calculated on the account
def calc_interest():
    interest = atm['balance'] * atm['interest_rate']
    return interest



while True:
    features = input("Check Balance [B] \ Deposit[D] \ Make Withdraw [W] \ Check Interest [I] \ Exit [E]: ").upper()
    if features == 'B':
        check_balance()
    elif features == 'D':
        dep = int(input("Enter amount you are depositing: "))
        deposit(dep)
        check_balance()
    elif features == 'W':
        wd = int(input("Enter amount you are withdrawing: "))
        check_withdrawl(wd)
        if check_withdrawl(wd) == True:
            withdraw(wd)
            check_balance()
        elif check_withdrawl(wd) == False:
            print("You do not have sufficient funds to withdraw that amount.")
    elif features == 'I':
        print("Interest earned: ${} ".format(int(calc_interest())))
    elif features == 'E':
        print("Exiting ATM")
        quit()

