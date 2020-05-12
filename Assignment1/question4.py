# Question 4 : Write a Python program which accept the user's first and last name and print them in reverse order with a space between them.


def reverse_string(string):
    length = len(string)
    rev = ""
    i = length - 1
    while i >= 0:
        rev += string[i]
        i -= 1

    return rev


FN = input("Please enter the first name : ")
LN = input("Please enter the last name : ")

print("Here's your name in reverse \n=>" + reverse_string(FN) + " " + reverse_string(LN))
print(FN[::-1], LN[::-1])
