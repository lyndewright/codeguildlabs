name = input('What is your name?: ')
age = input('How old are you?: ')
birth_year = 2018 - int(age)
print('Hey, {}!'.format(name))

if birth_year < 1985:
    print("Soooooo ooollllld")
elif birth_year < 1990:
    print('Not so old.')
else:
    print('You are super young yo!')


print('You were born in {}'.format(birth_year))

#int()
#float()
#str()
