# Q11. Write a Python program where a string will start with a specific number.


def input_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input integers only!")
        num = int(input(msg))
    return num


def starts_with(dig, string):
    return "YES" if string.startswith(str(dig)) else "NO"


def main():
    dig = input_integer("Please enter an integer : ")
    string = input("Please input a string : ")
    print("Does your string starts with your digit?", starts_with(dig, string))


main()
