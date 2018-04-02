#version 2

import random

balance = 0
balance2 = 0
winnings = 0

def pick6():
    num_pick = random.sample(range(1,99), 6)
    return(num_pick)

wt = pick6()


for i in range (100000):
    tic = pick6()
    balance = balance - 2

    if wt[0] == tic[0]:
        winnings += 1
    if wt[1] == tic[1]:
        winnings += 1
    if wt[2] == tic[2]:
        winnings += 1
    if wt[3] == tic[3]:
        winnings += 1
    if wt[4] == tic[4]:
        winnings += 1
    if wt[5] == tic[5]:
        winnings += 1

    if winnings == 1:
        balance2 = balance2 + 4
    if winnings == 2:
        balance2 = balance2 + 7
    if winnings == 3:
        balance2 = balance2 + 100
    if winnings == 4:
        balance2 = balance2 + 50000
    if winnings == 5:
        balance2 = balance2 + 1000000
    if winnings == 6:
        balance2 = balance2 + 25000000

roi= balance2 + balance


print("Winning Numbers: {}".format(wt))
print("Number of times you won: {}".format(winnings))
print("Your spending balance is ${}. You won ${}. Your ROI is: ${}".format(balance, balance2, roi))
