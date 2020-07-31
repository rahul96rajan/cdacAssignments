# Question 8 : Write a Python program to concatenate all elements in a list into a string and return it.


def input_list(my_list=[]):
    num_of_val = int(input("Please enter the number of values you desire to be in the list : "))
    for x in range(num_of_val):
        my_list.append(input("Enter {} index value : ".format(x)))
    return my_list


def concat_list(lst):
    return "".join(lst)


def main():
    my_lst = input_list()
    print("Concatenation of list :", concat_list(my_lst))


main()
