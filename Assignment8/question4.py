# Q4. Define a class Polygon with the following functions:
# __init__ method:  to take the take the number of sides of a polygon  and
# initialize all the sides with the value 0.
# Inputside method: to take the input values of sides from the user
# DispSide method: to display all the sides of the polygon


def input_positive_integer(msg):
    try:
        num = int(input(msg))
    except ValueError:
        print("Please input positive integers only!")
        num = int(input(msg))
    if num < 0:
        print("Please input positive integers only!")
        num = int(input(msg))
    return num


class Polygon(object):
    def __init__(self, no_of_side):
        if(no_of_side < 3):
            print("Polygon can not have less than 3 side.")
            raise ValueError("A polygon must have number of side equal "
                             "or greater than 3.")
        else:
            self.sides = {x: 0 for x in range(1, no_of_side+1)}

    def input_sides(self):
        for x in range(1, len(self.sides)+1):
            side = input_positive_integer("Enter side '{0}' : ".format(x))
            self.sides[x] = side

    def display_sides(self):
        print("\nValue of sides of polygon:")
        for x in range(1, len(self.sides)+1):
            print("\tSide {0} : {1}".format(x, self.sides[x]))


if __name__ == "__main__":
    pol = Polygon(input_positive_integer("Enter the number of side: "))
    # pol.display_sides()
    pol.input_sides()
    pol.display_sides()
