# Question 7: Write a Python program to check whether a specified value is contained in a group of values.


def input_list(my_list=[]):
    num_of_val = int(input("Please enter the number of values you desire to be in the list : "))
    for x in range(num_of_val):
        my_list.append(input("Enter {} index value : ".format(x)))
    return my_list


def is_val_present_in_list(lst, val):
    return True if val in lst else False


def main():
    my_lst = input_list()
    val = input("Please input value to be searched : ")
    print("Containment Status =>", is_val_present_in_list(my_lst, val))


main()
