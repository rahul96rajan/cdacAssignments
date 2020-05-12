# Q16. With a given integral number n,
# write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


def input_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input integers only!")
        num = int(input(msg))
    return num


def generate_list():
    end = (input_integer("Please enter ending point of list (ex: 10) : ") + 1)
    my_list = list(range(1, end))
    return my_list


def map_square(lst):
    return {val: val**2 for val in lst}


def main():
    print("Squared Map : \n", map_square(generate_list()))


main()