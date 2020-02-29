# Q17. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


def input_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input integers only!")
        num = int(input(msg))
    return num


def generate_matrix():
    row = (input_integer("Please enter number of rows (ex: 5) : "))
    column = (input_integer("Please enter number of columns (ex: 3) : "))
    lis = lambda a, b: [a * b for y in range(0, b)]
    return [lis(x, row) for x in range(0, column)]


print(generate_matrix())
