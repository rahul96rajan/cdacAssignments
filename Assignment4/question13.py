# Q13: write a Python program to find the largest number among the three input numbers


def input_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input integers only!")
        num = int(input(msg))
    return num


def input_float(msg):
    try:
        num = float(input(msg).strip())
    except ValueError:
        print("Please input integers or decimals only!")
        num = float(input(msg))
    return num


def input_vals():
    num_value = input_integer("Please enter number of values you desire (ex: 3): ")
    if num_value < 0:
        print("Incorrect selection, please try again!")
        num_value = input_integer("Please enter number of values you desire : ")
    num_list = []
    for x in range(0, num_value):
        num = input_float("Enter %d number :" % (x + 1))
        num_list.append(num)
    return num_list


def largest_in_list(num_list):
    num_list.sort()
    return num_list[-1]


def main():
    print("Largest number => ", largest_in_list(input_vals()))


main()
