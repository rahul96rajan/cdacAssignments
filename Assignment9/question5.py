'''Q5: Write a Program to make a simple calculator that can add, subtract,
 multiply and divide using functions '''

from question2 import input_positive_integer


def get_integer_tuple(string):
    lst = string.strip().split(",")
    for i in range(len(lst)):
        try:
            lst[i] = int(lst[i])
        except ValueError:
            print("[WARNING] String contains not integer value(s)!")
            return None
    return tuple(lst)


def add(a, b, *args):
    sum = a + b
    for num in args:
        sum += num
    return sum


def mult(a, b, *args):
    prod = a * b
    for num in args:
        prod *= num
    return prod


def div(a, b, *args):
    prod = a/b
    for num in args:
        prod /= num
    return prod


def sub(a, b, *args):
    diff = a-b
    for num in args:
        diff -= num
    return diff


def wrongOption(*agrs):
    return "WRONG OPTION! PLEASE SELECT A VALID OPTION."


def printMenu():
    print("--"*40 + "\n"
          "********* Calculator *********\n"
          "\t1. Multiply\n"
          "\t2. Divide\n"
          "\t3. Add\n"
          "\t4. Substract\n"
          "\tSelect option between 1 and 4.\n")


def calculator():
    calc_func = {
        1: mult,
        2: div,
        3: add,
        4: sub
    }
    while(True):
        printMenu()
        option = input_positive_integer("Select an option : ")
        numbers = get_integer_tuple(input("Please input the values "
                                          "(comma-separated): "))
        print(numbers)
        print(calc_func.get(option, wrongOption)(*tuple(numbers)))
        if(input("Do you wish to continue? Press any key other than 'N' or 'n'"
                 " to continue : ").strip() in ('n', 'N')):
            break


if __name__ == "__main__":
    calculator()
