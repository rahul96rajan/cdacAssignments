# Q7: Write a Python program to get a string from a given string where all occurrences of its first char have been
# changed to '$', except the first char itself.


def mutate_string(string):
    if len(string) < 2:
        print("Stings is too short, input 2 or more characters.")
        return None
    return string[0] + string[1:].replace(string[0], "$")


def main():
    string = input("Please input a string : ")
    print("The replaced String : ", mutate_string(string))


main()
