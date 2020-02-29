# Question 4: Write a Python Program to find the area of triangle
# Three sides of the triangle a, b and c are provided by the user

from math import sqrt


def is_positive(num):
    if num > 0:
        return True
    else:
        return False


def input_positive_float(msg):
    # num = 0 <<DOUBT>> scope of the variable
    try:
        num = float(input(msg))
        if not (is_positive(num)):
            num = float(input("Please enter a positive value :"))
    except ValueError:
        num = float(input("Please enter a positive number (integer or decimal) :"))
    return num


def input_value():
    a = input_positive_float("Please enter value of side 1 : ")
    b = input_positive_float("Please enter value of side 2 : ")
    c = input_positive_float("Please enter value of side 3 : ")
    return a, b, c


def get_valid_values():
    a, b, c = input_value()
    while a + b < c or a + c < b or b + c < a:
        print("Invalid output! Please try again")
        input_value()
    return a, b, c


def herons_formula(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))


def main():
    flag = "y"
    while flag.upper() == "Y":
        a, b, c = get_valid_values()
        print("Area of the triangle => ", herons_formula(a, b, c))
        flag = input("Do you want to continue (Y/N)? ")
    print("Thank You!")


main()
