# Q9: Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given
# string is already ends with 'ing' then add 'ly' instead.


def fusion_with_char_change(string=""):
    string = string.strip()
    if len(string) < 0:
        print("Invalid Entry: Empty String!")
        return None
    if string.endswith("ing"):
        string = string[:-2] + "ly"
    else:
        string = string + "ing"
    return string


def main():
    string = input("Enter a string : ")
    print("Sting '{0}' have been modified as '{1}'".format(string, fusion_with_char_change(string)))


main()
