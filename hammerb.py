

time = input('What time is it (HH:AM/PM:)?: ')
time_split = time.split(':')
hour = int(time_split[0])
meridian = time_split[1].lower()


if hour in range(7, 10):
    if meridian =='am':
        print("It's Breakfast!")
    else:
        print("It's Dinner!")
elif hour in [12, 1, 2] and meridian == 'pm':
    print("It's lunch!")
elif hour in range(10, 12) and meridian == 'pm' or hour == 12 or hour in range (1, 5) and meridian == 'am':
    print("It's hammer time!")
