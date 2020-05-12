# Q8. Create a class named 'Rectangle' with two data members 'length'
# and 'breadth' and two methods to print the area and perimeter of the
# rectangle respectively. Its constructor having parameters for length and
# breadth is used to initialize length and breadth of the rectangle.
# Let class 'Square' inherit the 'Rectangle' class
# with its constructor having a parameter for its side (suppose s) calling the
# constructor of its parent class as 'super(s,s)'. Print the area and
# perimeter of a rectangle and a square.

from question4 import input_positive_integer


class Rectangle(object):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area : ", self.length*self.breadth)

    def perimeter(self):
        print("Perimeter : ", 2*(self.length + self.breadth))


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


if __name__ == "__main__":
    a_rectangle = Rectangle(input_positive_integer("Input Length : "),
                            input_positive_integer("Input Breadth : "))
    a_rectangle.area()
    a_rectangle.perimeter()
    print("-"*40)
    a_square = Square(input_positive_integer("Input Side length : "))
    a_square.area()
    a_square.perimeter()
