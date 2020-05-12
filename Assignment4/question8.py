# Q8: Write a python program  to display ascii characters from 65 to 90


def input_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input integers only!")
        num = int(input(msg))
    return num


def generate_list():
    start = input_integer("Please enter starting point of list (ex: 65) : ")
    end = (input_integer("Please enter ending point of list (ex: 90) : ") + 1)
    my_list = list(range(start, end))
    return my_list


def ascii_to_chars(lst):
    return {val: chr(val) for val in lst}


def main():
    print("ASCII Map : \n", ascii_to_chars(generate_list()))


main()
