'''Q. 7.We can define sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as
follows for integer x ≥ 1:
1, if x = 1
x + sum from 1 to x-1 if x > 1
Complete the following Python program to compute
the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 recursively:
def main():
# compute and print 1 + 2 + ... + 10
print sum(10)
def sum(x):
# you complete this function recursively main()
'''
import sys


def sum(x):
    if x == 1:
        return 1
    else:
        return x + sum(x-1)


def main():
    sys.path.insert(1, r"/home/rahulrajan/Documents/dev/scripts/"
                    r"cdacAssignments/Assignment9")
    from question2 import input_positive_integer
    num = input_positive_integer("Enter the limiting number : ")
    print("Sum until ", num, ":", sum(num))


if __name__ == "__main__":
    main()
