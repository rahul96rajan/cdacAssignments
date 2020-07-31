# Q11: Write a Python program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
#
# 'Python' -> onononon
# 'Exercises' -> eseseses


def last_char_four_copies(string):
    string = string.strip()
    if len(string) < 0:
        print("Invalid Entry: Empty String!")
        return None
    return string[-2:]*4


def main():
    string = input("Enter a string : ")
    print("Sting '{0}' have been modified as '{1}'".format(string, last_char_four_copies(string)))


main()