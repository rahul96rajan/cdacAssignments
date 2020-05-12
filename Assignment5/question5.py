# Question 5



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


def print_table(limit):
    print("  ", *range(1, limit))
    print("+--"+"-"*2*limit)
    for i in range(1, limit):
        yield (str(i), "|", *range(i, i*limit, i))

# " ".join(["%d"%i for i in range(i, i*limit, i)])

def main():
    lim = input_positive_integer("Please Enter the number of terms : ")
    print_table(lim)
    for x in print_table(lim+1):
        print(*x)

main()
