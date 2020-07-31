# Question 4


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
        for y in range(0, x):
            print("*", end=" ")
        print("")
    for x in range(limit-1, 0, -1):
        for y in range(0, x):
            print("*", end=" ")
        print("")


def main():
    lim = input_positive_integer("Please Enter the number of terms : ")
    print_pattern(lim)

main()

# deep
# nlp
# reinforement