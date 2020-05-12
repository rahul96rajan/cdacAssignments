# Q24. Write a program which can map() to make a list
# whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].


def input_positive_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input positive integers only!")
        num = int(input(msg))
    if num < 0:
        print("Please input positive integers only!")
        num = int(input(msg))
    return num


def input_list():
    num = input_positive_integer("Input number of desired values: ")
    return [input_positive_integer("Input %d value: " % (x + 1)) for x in range(0, num)]


def main():
    print("\nSquared List:\n=>", list(map(lambda x: x**2, input_list())))


main()