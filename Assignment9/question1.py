# Q1: Write a Python Program To Display Powers of 2 Using Anonymous Function.
# Take number of terms from user


def input_float(msg):
    try:
        num = float(input(msg))
    except ValueError:
        print("Please input floating points only!")
        num = float(input(msg))
    return num


def main():
    pow = lambda x, y: x**y
    num = input_float("Enter a number : ")
    power = input_float("Enter the power : ")
    print(pow(num, power))


if __name__ == "__main__":
    main()
