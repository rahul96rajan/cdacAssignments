# Q12: Write a Python program to add key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}


def input_dict():
    my_dict = dict()
    number = int(input("Please enter desired number of elements : ").strip())
    for i in range(0, number):
        key = input("Please index %d Key : " % i)
        val = input("Please index %d Value : " % i)
        my_dict[key] = val
    return my_dict


def main():
    print(input_dict())


main()
