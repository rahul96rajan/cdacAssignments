# Q2: Write a Python class which has two methods get_String and print_String.
# get_String accept a string from the user and print_String print the string
# in upper case.


class MyString(object):
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Please enter a string : ")

    def print_sting_upper(self):
        print("String in upper case : ", self.string.upper())


if __name__ == "__main__":
    string = MyString()
    string.get_string()
    string.print_sting_upper()
