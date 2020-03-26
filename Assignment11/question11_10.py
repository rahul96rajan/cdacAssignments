'''Q. 9.Write a function filter_long_words() that takes a list of words and an
integer n and returns the list of words that are longer than n'''
from sys import path


def find_longest_word(lst, length):
    return list(filter(lambda x: len(x) > length, lst))


def main():
    path.insert(1, r"/home/rahulrajan/Documents/dev/scripts/"
                r"cdacAssignments/Assignment9")
    from question2 import input_positive_integer

    length = input_positive_integer("Enter the limiting lenght of word : ")
    input_lst = input("Please enter a string (comma-separated) : ").\
        strip().split(",")
    print("Words longer than length "
          "'{0}' are {1}".format(length, find_longest_word(input_lst, length)))


if __name__ == "__main__":
    main()
