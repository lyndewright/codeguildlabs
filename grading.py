# version 2

score = input("What is your score?: ")
grade = int(score)

if grade >= 97:
    print("You got an A+!")
elif grade >= 93:
    print("You got an A!")
elif grade >= 90:
    print("You got an A-!")
elif grade >= 87:
    print("You got a B+!")
elif grade >= 83:
    print("You got a B!")
elif grade >= 80:
    print("You got a B-!")
elif grade >= 77:
    print("You got a C+!")
elif grade >= 73:
    print("You got a C!")
elif grade >= 70:
    print("You got a C-!")
elif grade >= 67:
    print("You got a D+!")
elif grade >= 63:
    print("You got a D!")
elif grade >= 60:
    print("You got a D-!")
else:
    print("You got an F!")

satisfaction = input("Are you happy with your grade? Type '1' for 'Yes.' Type '2' for 'No.' 1 or 2?: ")
happy = int(satisfaction)
if happy == 1:
    print("I'm happy for you!")
elif happy == 2:
    print("That's too bad. There's always next time.")
else:
    print("Maybe your grade would be different if you followed directions better!")
