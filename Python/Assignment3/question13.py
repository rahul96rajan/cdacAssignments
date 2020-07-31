# Q13: Write a Python program to concatenate following dictionaries to create a new one.


def input_dict():
    my_dict = dict()
    number = int(input("Please enter desired number of elements : ").strip())
    for i in range(0, number):
        key = input("Please index %d Key : " % i)
        val = input("Please index %d Value : " % i)
        my_dict[key] = val
    return my_dict


def dict_merger(d1, d2):
    return dict(d1, **d2)


def main():
    dic1 = input_dict()
    print("Dict 1 : ", dic1)
    dic2 = input_dict()
    print("Dict 2 : ", dic2)
    dic3 = input_dict()
    print("Dict 3 : ", dic3)
    print("Merged dictionary => ", dict_merger(dict_merger(dic1, dic2),dic3))


main()
