# Q26. Write a program which can filter() to make a list
# whose elements are even number between 1 and 20 (both included).


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
    return [int(input("Input %d value: " % (x + 1))) for x in range(0, num)]


def main():
    # list(filter(lambda x: x % 2 == 0, input_list()))
    print("\nEven List (between 0 to 20):\n=>", list(filter(lambda x: x % 2 == 0 and 0 <= x <= 20, input_list())))


main()