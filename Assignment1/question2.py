#  Question 2 : Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program to convert this temperature into Centigrade degrees.
# Degree Celsius to Degree Fahrenheit and vice-versa

import re
from builtins import print


def temperature_converter(tmp):
    absolute_temp = float(re.findall("[0-9]*", tmp)[0])
    degree_unit = re.findall("[a-zA-Z]", tmp)[0].upper()
    final_temp = ""
    if degree_unit == "C":
        absolute_temp = (absolute_temp*9/5) + 32
        final_temp = str(round(absolute_temp, 2)) + " " + "F"
    elif degree_unit == "F":
        absolute_temp = (absolute_temp - 32) * (5 / 9)
        final_temp = str(round(absolute_temp, 2)) + " " + "C"
    return final_temp


print("---Temperature Converter---")
input_temp = input("Please enter the temperature in degree  : ")
print(temperature_converter(input_temp))


