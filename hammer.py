#hamer time version 1

time = input('What time is it?: ')

breakfast = ['7AM', '8AM', '9AM']
lunch = ['12PM', '1PM', '2PM']
dinner = ['7PM', '8PM', '9PM']
hammer_time = ['10PM', '11PM', '12AM', '1AM', '2AM', '3AM', '4AM']

if time in breakfast:
    print("It's breakfast time!")
elif time in lunch:
    print("It's lunch time!")
elif time in dinner:
    print("It's dinner time!")
elif time in hammer_time:
    print("It's HAMMER TIME!")
else:
    print("No food for you!")
