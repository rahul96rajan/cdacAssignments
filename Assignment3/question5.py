# Q5: Write a Python program to print out a set containing all the colors from a list which are not present in
# another list
from builtins import set


def input_list(my_list):
    my_list = []
    number = int(input("Please enter desired number of elements : ").strip())
    for i in range(0, number):
        my_list.append(input("Please index {} colour : ".format(i)).strip().lower())
    my_list.sort()
    return my_list


def get_exclusive_colors(list1, list2):
    return set(list1) - (set(list1) & (set(list2)))


def main():
    list1 = input_list()
    list2 = input_list()
    print(list1)
    print(list2)
    print("List 2's exclusive colors are : ", get_exclusive_colors(list1, list2))


main()
