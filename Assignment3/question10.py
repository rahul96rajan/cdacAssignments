# Q10:  Write a Python program to change a given string to a new string where the first and last chars have been
# exchanged.


def interchange_first_and_last(string):
    string = string.strip()
    if len(string) < 0:
        print("Invalid Entry: Empty String!")
        return None
    return string[-1] + string[1:-1] + string[0]


def main():
    string = input("Enter a string : ")
    print("Sting '{0}' have been modified as '{1}'".format(string, interchange_first_and_last(string)))


main()
