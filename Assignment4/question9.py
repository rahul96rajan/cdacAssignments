# Q9: Display ascii characters from 48 to 57.


def generate_list():
    my_list = list(range(48, 58))
    return my_list


def ascii_to_chars(lst):
    return {val: chr(val) for val in lst}


def main():
    print("ASCII Map : \n", ascii_to_chars(generate_list()))


main()