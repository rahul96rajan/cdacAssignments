# Q4: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a
# tuple with those numbers.


def str_to_list(string=""):
    my_list = string.split(",")
    for i in range(len(my_list)):
        my_list[i] = my_list[i].strip()
    return my_list


def list_to_tuple(my_list):
    return tuple(my_list)


def main():
    input_string = input("Please enter a comma-separated string : ")
    my_list = str_to_list(input_string)
    print("List = > ", my_list)
    print("Tuple = > ", list_to_tuple(my_list))


main()

