'''Exercise 3: Follow the steps:
•	Create a class, Triangle. Its __init__() method should take self, angle1,
     angle2, and angle3 as arguments. Make sure to set these appropriately in
     the body of the __init__()method.
•	Create a variable named number_of_sides and set it equal to 3.
•	Create a method named check_angles. The sum of a triangle's three angles is
    It should return True if the sum of self.angle1, self.angle2, and self.
    angle3 is equal 180, and False otherwise.
•	Create a variable named my_triangle and set it equal to a new instance of
    your Triangle class. Pass it three angles that sum to 180 (e.g 90, 30, 60).
•	Print my_triangle.number_of_sides and print my_triangle.check_angles().'''

import sys


class Traingle(object):
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        return True if (self.angle1 + self.angle2 +
                        self.angle3) <= 180 else False

    def __str__(self):
        return "Number of Sides : {0}".format(Traingle.number_of_sides) +\
                "\nIs angle less or equal to 180\N{DEGREE SIGN} : " +\
                str(Traingle.check_angles(self))


def main():
    sys.path.insert(1, r"/home/rahulrajan/Documents/dev/scripts/"
                    r"cdacAssignments/Assignment9")
    from question5 import get_float_tuple
    my_triangle = Traingle(*get_float_tuple(input("Enter angles of triangle "
                                                  "(comma-separated) : ")))
    print(my_triangle)


if __name__ == '__main__':
    main()
