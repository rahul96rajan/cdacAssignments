# Q23. Write a program which can filter even numbers in a list by using filter function.
# The list is: [1,2,3,4,5,6,7,8,9,10].


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
    print("\nEven List:\n=>", list(filter(lambda x: x%2==0, input_list())))


main()
