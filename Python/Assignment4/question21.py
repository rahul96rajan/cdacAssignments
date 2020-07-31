# Q21. Define a function that can accept two strings as input and print the string with maximum length in console. If
# two strings have the same length, then the function should print all strings line by line.


def longest_string(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str1) < len(str2):
        return str2
    else:
        return str1 + "\n" + str2


def main():
    str1 = input("Please enter string 1 : ")
    str2 = input("Please enter string 2 : ")
    print(longest_string(str1, str2))


main()
