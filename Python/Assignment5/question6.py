# Question 6


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


def print_pattern(limit):
    for x in range(0, limit):
        for y in range(0, limit-x-1):
            print("-", end=" ")
        for y in range(1, (x+1)*2, 1):
            print("*", end=" ")
        print("")


def main():
    lim = input_positive_integer("Please Enter the number of terms : ")
    print_pattern(lim)

main()