'''Exercise 6: Define a Point3D class that inherits from object Inside the
Point3D class, define an __init__() function that accepts self, x, y, and z,
and assigns these numbers to the member variables self.x,self.y,self.z.
Define a __repr__() method that returns
"(%d, %d, %d)" % (self.x, self.y, self.z).
This tells Python to represent this object in the following
format: (x, y, z). Outside the class definition, create a variable named
my_point containing a new instance of Point3D with x=1, y=2, and z=3.
Finally, print my_point.'''

import sys


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Point({0}i\u0302, {1}j\u0302, {2}k\u0302)".\
                format(self.x, self.y, self.z)


def main():
    sys.path.insert(1, r"/home/rahulrajan/Documents/dev/scripts/"
                    r"cdacAssignments/Assignment9")
    from question5 import get_float_tuple
    p = Point3D(*get_float_tuple(input("Please enter 3-D point components"
                                       "(x, y, z) (comma-separated) : ")))
    print(p)


if __name__ == "__main__":
    main()
