# Question 2 : Write a Python Program to calculate the square root


from math import sqrt


def convert_to_float(num):
    try:
        return float(num)
    except ValueError:
        return float(input("Please enter a number (integers or decimals): "))


def calculate_sq_root():
    flag = "y"
    while flag.upper() == "Y":
        number = input("\nPlease enter a number: ")
        number = convert_to_float(number)
        print("Square Root =>", sqrt(number))
        flag = input("Do you want to continue (Y/N)? ")
    print("Thank You!")


calculate_sq_root()
