#  Question 1 : Write a Python program which accept the radius of a circle from the user and compute the area.

from math import pi

radii = input("Please enter the radius of the circle : ")
area = pi * (float(radii)**2)
print("Area of the circle having radii '" + str(radii) + "' is : " + str(round(area, 2)))