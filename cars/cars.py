class Car:
    def __init__(self, doors, color):
        self.doors = doors
        self.color = color
        self.wheels = 4


    # def number_of_doors(self, doors=0):
    #     return "Your car has {} doors.".format(self.doors(doors))
    #
    #
    def color(self, color):
        return "You car is the color {}.".format(self.color)
    #
    #
    # def wheels(self, wheels=4):
    #     return "Your car has {} wheels".format(self.wheels)
    #
    #
    # def honk(self, honk):
    #     honk = input("Would you like your car to honk? [Y/N]: ").upper()
    #     if honk == 'Y':
    #         return 'HONK!'
    #     elif honk == 'N':
    #         return 'No Honk for YOU!'
