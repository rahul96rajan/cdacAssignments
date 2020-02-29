# Question 10: Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)

from math import sqrt


def dist_between_two_points(x1, y1, x2, y2):
    return sqrt(((x2-x1)**2) + ((y2-y1)**2))


def main():
    x1 = float(input("Please enter value for x1: "))
    y1 = float(input("Please enter value for y1: "))
    x2 = float(input("Please enter value for x2: "))
    y2 = float(input("Please enter value for y2: "))
    print("Distance between the point :", dist_between_two_points(x1, y1, x2, y2))


main()
