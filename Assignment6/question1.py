# Q1. write a Python program to check if the input year is a leap year or not.


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


def leap_or_not(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True


def main():
    year = input_positive_integer("Please input an year : ")
    print("It's Leap Year." if leap_or_not(year) else "It's not a leap year")


main()
