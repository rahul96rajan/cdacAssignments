# Q4: Write a python program to display a Multiplication table of a number enter from keyboard.


def input_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input integers only!")
        num = int(input(msg))
    return num


def generate_math_table():
    num = input_integer("Please enter the number : ")
    end = (input_integer("Up to which point you want the table : ")+1)
    my_list = list(range(1, end))
    for x in range(1, end):
        print("%d X %d = %d "%(x, num, num*x))


generate_math_table()
