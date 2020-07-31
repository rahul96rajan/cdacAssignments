# Question 1 : Write a Python Program to make a simple calculator that can add, subtract, multiply
# and divide


def calculate(operand1, operand2, operator):
    operand1 = float(operand1)
    operand2 = float(operand2)
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "%":
        return operand1 % operand2
    else:
        return "Please input a valid operator"


def calculator(_continue):
    while _continue.upper() == "Y":
        oprnd1 = input("\nPlease enter operand 1: ")
        oprnd2 = input("Please enter operand 2: ")
        print("Operation supported are +, -, /, *, %")
        oprtr = input("Please enter the operation to perform :")
        print("Result : ", calculate(oprnd1, oprnd2, oprtr))
        _continue = input("Do you want to continue (Y/N)? ")


calculator("y")
