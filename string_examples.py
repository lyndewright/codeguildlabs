greeting = 'Hello, {}!'
name = input('What is your name?: ')
total_greeting = greeting.format(name.capitalize())

print(total_greeting)
print(total_greeting.count('1'))
print(greeting.index('y'))
