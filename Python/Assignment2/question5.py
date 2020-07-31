# Question 5 : Write a Python program to convert decimal number into binary, octal and hexadecimal number system


def is_positive(num):
    if num > 0:
        return True
    else:
        return False


def input_positive_int(msg):
    try:
        num = int(input(msg))
        if not (is_positive(num)):
            num = int(input(msg))
    except ValueError:
        num = int(input(msg))
    return num


def select_an_option():
    number = input_positive_int("\nPlease enter a positive integer : ")
    print("Please select from a given option below:")
    print("\t1. Decimal to binary\n\t2. Decimal to Octal\
    \n\t3. Decimal to Hexadecimal")
    option = input_positive_int("Input the desired option : ")
    if option == 1:
        print("Binary => ", bin(number)[2:])
    elif option == 2:
        print("Octal => ", oct(number)[2:])
    elif option == 3:
        print("Hexadecimal => ", hex(number)[2:])
    else:
        print("You have entered an invalid option")


def main():
    flag = "y"
    while flag.upper() == "Y":
        select_an_option()
        flag = input("Do you want to continue (Y/N)? ")
    print("Thank You!")


main()
