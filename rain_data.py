# Download one of these files and write a function to load the file.
# The two columns that are most important are the date and the daily total.
# The simplest representation of this data is a list of tuples,
# but you may also use a list of dictionaries, or a list of instances
# of a custom class.

# To parse the dates, use datetime.strptime. This allows for easy access to
# the year, month, and day as ints. Below I’ve shown how to parse an example
# string, resulting in a datetime object. We can then access the year, month,
# and day on that datetime as ints. Later, if you want to print the datetime
# in a more human-readable format, you can use datetime.strftime.

import datetime
# import operator
# import matplotlib.pyplot as plt



with open('hayden_island.txt.rain', 'r', encoding='utf-8') as f:
    print(f.readlines())













# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016



