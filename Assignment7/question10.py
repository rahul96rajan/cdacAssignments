# Q10. Write a python program to extract all the email addresses
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
    reg_email = re.compile(r"(\b\S+)@(\S+\.(\S+))")
    counter = 1
    for match in re.finditer(reg_email, string):
        print(
                "\nEmail ID %d: " % counter, match.group(0),
                "\nUsername %d: " % counter, match.group(1),
                "\nDomain %d: " % counter, match.group(2))
        counter += 1


def main():
    string = input("Please input a string : ")
    fetch_ID_and_domain(string)


main()
