# Question 3 : Write a Python Program to Solve the quadratic equation ax**2 + bx + c = 0
# Coeffients a, b and c are provided by the user
# [Hint: import complex math module - import cmath]
# from builtins import print
from cmath import sqrt


def sridharacharya_rule(a, b, c):
    discriminant = (b**2) - (4*a*c)
    sol1 = (-b - sqrt(discriminant)) / (2 * a)
    sol2 = (-b + sqrt(discriminant)) / (2 * a)
    return sol1, sol2


def solve_quadratic_eq():
    flag = "y"
    while flag.upper() == "Y":
        print("\nPlease enter value of a, b and c [ax**2 + bx + c = 0]")
        a = float(input("Please enter value of a: "))
        b = float(input("Please enter value of b: "))
        c = float(input("Please enter value of c: "))
        s1, s2 = sridharacharya_rule(a, b, c)
        print("Solution1 : ", s1, "\nSolution2 : ", s2)
        flag = input("Do you want to continue (Y/N)? ")
    print("Thank You!")


solve_quadratic_eq()