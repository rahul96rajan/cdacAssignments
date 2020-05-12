'''A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will
check them according to the above criteria. Passwords that match the criteria
are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1'''
import re


def is_password_valid(password):
    reg_lower_case_char = re.compile(r"[a-z]")
    reg_upper_case_char = re.compile(r"[A-Z]")
    reg_digit_char = re.compile(r"[0-9]")
    reg_special_char = re.compile(r"[$#@]")
    return ((re.search(reg_lower_case_char, password) is not None) and
            (re.search(reg_upper_case_char, password) is not None) and
            (re.search(reg_digit_char, password) is not None) and
            (re.search(reg_special_char, password) is not None) and
            (6 <= len(password) <= 12))


def valid_passwords(password_list):
    return ", ".join([pas for pas in password_list if is_password_valid(pas)])


def main():
    passwords = input("Please enter passwords: ").strip().split(",")
    print("DEBUG = ", passwords)
    print("Valid Passwords are : ", valid_passwords(passwords))


if __name__ == "__main__":
    main()
