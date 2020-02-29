# Q11: write a python program to swap two variables provided by the user.


def swap(x, y):
    return y, x


def main():
    x = input("Enter value of X : ")
    y = input("Enter value of Y : ")
    x, y = swap(x, y)
    print("\nSwapped Values!\nValue of X = %s\nValue of Y= %s"%(x,y))


main()