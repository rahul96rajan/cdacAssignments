# Q3. write a Program to check if a string is palindrome or not


def palindrome_or_not(string):
    string = string.strip()
    if string == string[::-1]:
        return "It is a Pallindrome."
    else:
        return "It's not a Pallindrome."


def main():
    string = input("Please input a string : ")
    print(palindrome_or_not(string))


main()
