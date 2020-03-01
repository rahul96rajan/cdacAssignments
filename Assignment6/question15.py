# Q15. Write a Python program to search a literals string in a string and also
# find the location within the original string where the pattern occurs.
# import re


def matching_string_in_string(string1, string2):
    # reg = re.compile(string2)
    # found = re.search(reg, string2)
    # print(found, found.group(), found.span())
    # if found is None:
    #     return string2 + " is not present in " + string1
    # else:
    #     return string2 + " is present in " + string1 + " at " +\
    #          str(found.span())
    if string1.find(string2) == -1:
        return string2 + " is not present in " + string1
    else:
        return string2 + " is present in " + string1 + " at index " +\
             str(string1.find(string2))


def main():
    string1 = input("Please enter a sentence: ")
    string2 = input("Please enter a strings: ")
    print(matching_string_in_string(string1, string2))


main()
