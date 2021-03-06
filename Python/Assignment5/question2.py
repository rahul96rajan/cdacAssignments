# Question 1


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
    for x in range(1, limit + 1):
        for y in range(x+1, 1, -1): # start, stop, step
            print(y-1, end=" ")
        print("")


def main():
    lim = input_positive_integer("Please Enter the number of terms : ")
    print_pattern(lim)

main()