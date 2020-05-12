'''Q. 10.Define a simple "spelling correction" function correct() that takes a
string and sees to it that
1)two or more occurrences of the space character is compressed into one, and
2)inserts an extra space after a period if the period is directly followed by
a letter.
e.g. correct("This is very funny and  cool.Indeed!") should return
"This is very funny and cool. Indeed!"'''
from re import sub, compile


def correct(string):
    reg = compile(r"(?<=\w)\.(?=\w)")
    string = string.replace("  ", " ")
    string = sub(reg, ". ", string)
    return string


def main():
    input_str = input("Please enter a string : ")
    print("Corrected string : ", correct(input_str))


if __name__ == "__main__":
    main()
