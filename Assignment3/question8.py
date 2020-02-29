# Q8: Write a Python program to get a single string from two given strings, separated by a space and swap the first
# two characters of each string.
# Sample String : 'abc', 'xyz' Expected Result : 'xyc abz'


def fusion_with_char_change(string1, string2):
    if len(string1) < 2 or len(string1) < 2:
        print("Stings is too short, input 2 or more characters.")
        return None
    return string2[0]+string1[1:]+string1[0]+string2[1:]


def main():
    string1, string2 = input("Enter two strings (tab separated) : ").split("\t")
    print("Sting '{0}' and '{1}' have been merged and modified as '{2}'".format(string1, string2, fusion_with_char_change(string1, string2)))


main()
