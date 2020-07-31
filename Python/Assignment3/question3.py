# Q3: Write a Python program to get the smallest number from a list.


def input_list(my_list=[]):
    number = int(input("Please enter desired number of elements : ").strip())
    for i in range(0, number):
        my_list.append(float(input("Please index {} value : ".format(i))))
    return my_list


def largest_in_list(my_list):
    my_list.sort()
    return my_list[0]


def main():
    print("Smallest number in the list =>", largest_in_list(input_list()))


main()
