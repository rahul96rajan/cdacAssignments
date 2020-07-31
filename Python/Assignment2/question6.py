# Question 6 : Write a python Program to convert kilometers into miles
# Input is provided by the user in kilometers

import re


def convert_km_to_miles_and_vice_versa(dist):
    measurement = float(re.findall("[0-9]+", dist)[0])
    unit = re.findall("[a-zA-Z]+", dist)[0]
    if unit.upper() == "MILES" or unit.upper() == "MILE":
        measurement = measurement * 1.609344
        unit = " Km"
    elif unit.upper() == "KM" or unit.upper() == "KMS":
        measurement = measurement * 0.6214
        unit = " Mile"
    else:
        return "Wrong Input!"
    return str(measurement) + unit


def main():
    flag = "y"
    while flag.upper() == "Y":
        dist = input("Please enter distance and unit(Km or miles) : ")
        print("=>", convert_km_to_miles_and_vice_versa(dist))
        flag = input("Do you want to continue (Y/N)? ")
    print("Thank You!")


main()

