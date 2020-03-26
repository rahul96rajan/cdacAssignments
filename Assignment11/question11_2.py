'''Q. 2. Define a procedure histogram() that takes a list of integers and
 prints a histogram to the screen. For example, histogram([4, 9, 7]) should
 print the following:
****
*********
*******
'''
from math import ceil


def get_int_tuple(string):
    lst = string.strip().split(",")
    for i in range(len(lst)):
        try:
            lst[i] = int(lst[i].strip())
            if lst[i] < 0:
                print("[WARNING] String contains negative value(s)!")
                return None
        except ValueError:
            print("[WARNING] String contains non integer value(s)!")
            return None
    return tuple(lst)


def plot_histogram(lst):
    print("Histogram\n^\n|")
    for x in lst:
        print("|", "*"*x, sep="")
    lst.sort()
    print("-"*ceil(lst[-1]*1.2), ">", sep="")


def main():
    points = list(get_int_tuple(input("Enter values of histogram "
                                      "(comma-separated) : ")))
    print(points)
    plot_histogram(points)


if __name__ == '__main__':
    main()
