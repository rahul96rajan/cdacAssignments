# Q22. Write a program to generate and print another tuple
# whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).


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


def input_tuple():
    num = input_positive_integer("Input number of desired values: ")
    return tuple([input_positive_integer("Input %d value: "%(x+1)) for x in range(0,num)])


def even_tuple(tup):
    return tuple(x for x in tup if x % 2 == 0)


def main():
    print("\nEven Tuple:\n=>", even_tuple(input_tuple()))


main()
