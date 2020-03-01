# Q2. write a Program to display the Fibonacci sequence up to n-th term where n is provided by the user


def fibonacci_series(lim):
    print("-- Fibonacci Series --")
    a = b = 1
    for x in range(0, lim):
        yield a
        a, b = b, a + b


def main():
    num = int(input("Please input the limiting factor: "))
    for x in fibonacci_series(num):
        print(x, end=" ")
    print()


main()
