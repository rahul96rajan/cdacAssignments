# Q5. Define a class Triangle which inherits from Polygon (use class of Q4).
# This class consists of the following function:
#   CalculateArea method: to calculate the area of the triangle

from question4 import Polygon
from functools import reduce


class Traingle(Polygon):
    def __init__(self):
        super().__init__(3)

    def calculate_area(self):
        return reduce(lambda x, y: x*y, self.sides.values())


tr = Traingle()
tr.input_sides()
print("Area of the triangle : ", tr.calculate_area())
