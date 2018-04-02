#wall painting version 2
import math

while True:
    width = int(input("What is the width of the wall in feet?: "))
    height = int(input("What is the height of the wall in feet?: "))
    coats = int(input("How many coats of paint will you apply?: "))
    paint_cost = int(input("How much does paint cost per gallon in dollars?: "))


    area = width * height * coats
    num_gallons = area/400
    num_of_gallons = math.floor(area / 400) + 1
    total_1 = num_gallons * paint_cost
    total_2 = num_of_gallons * paint_cost


    if area % 400 == 0:
        print(("You need {} gallons of paint.".format(num_gallons)))
        print("That will cost you {} dollars.".format(total_1))
        quit()
    elif area % 400 != 0:
        print(("You need {} gallons of paint.".format(num_of_gallons)))
        print("That will cost you {} dollars.".format(total_2))
        quit()
