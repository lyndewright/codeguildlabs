# version 2

print("*****Money Return*****")

money_type = {'dollars': 100, 'quarters': 25, 'dimes': 10, 'nickels': 5}

while True:

    money_request = input("How much money would you like [total cents]? \n: ")
    pennies = int(money_request)

    money_type = {'dollars': 100, 'quarters': 25, 'dimes': 10, 'nickels': 5}

    dollar_results = pennies // money_type['dollars']
    print("Dollars: ")
    print(dollar_results)

    quarter_results = (pennies - (dollar_results) * money_type['dollars']) // money_type['quarters']
    print("Quarters: ")
    print(quarter_results)

    dime_results = (pennies - (dollar_results * money_type['dollars']) - \
    (quarter_results * money_type['quarters'])) // money_type['dimes']
    print("Dimes: ")
    print(dime_results)

    nickel_results = (pennies - (dollar_results * money_type['dollars']) - \
     (quarter_results * money_type['quarters']) - (dime_results * money_type['dimes'])) \
      // money_type['nickels']
    print("Nickels: ")
    print(nickel_results)

    penny_results = (pennies - (dollar_results * money_type['dollars']) - \
    (quarter_results * money_type['quarters']) - \
     (dime_results * money_type['dimes']) - (nickel_results * money_type['nickels']))
    print("Pennies: ")
    print(penny_results)


    repeat = input("Would you like more change? (Y/N): ").lower()
    if repeat == 'y':
        pass
    elif repeat == 'n':
        print("Exiting Money Return")
        quit()
quit()
