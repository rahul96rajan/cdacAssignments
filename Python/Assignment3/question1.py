# Q1: Write a Python program to sum all the items in a list.


def input_list(my_list=[]):
    number = int(input("Please enter desired number of elements : ").strip())
    for i in range(0, number):
        my_list.append(float(input("Please index {} value : ".format(i))))
    return my_list


def sum_of_list(my_list):
    sum_list = 0
    for i in range(0, len(my_list)):
        sum_list += my_list[i]
    return sum_list


def main():
    print("Sum of the list =>", sum_of_list(input_list()))


main()
