# Q10. . Write a python program to extract all the email addresses
# from the given string and print the output as shown below:
# Input String:
# “email address alibaba1_@google.com  second email address abc_12@gmail.com”
# Output String: email address : alibaba1_@google.com
# Email id: alibaba1_
# Domain: google.com
# Email address: abc_!2@gmail.com
# Email id: abc_12
# Domain: gmail.com

import re


def fetch_ID_and_domain(string):
    reg_ID = re.compile(r"\b\w+(?=@)")
    reg_domain = re.compile(r"(?<=@)\w+(?=\.)")
    # (\b\w+)@(\w+\.(\w+))


def main():
    string = input("Please input a string : ")
    fetch_ID_and_domain(string)


main()
