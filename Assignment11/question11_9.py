'''Q. 8. Define a function overlapping() that takes two lists and returns True
if they have at least one
member in common, False otherwise.

Write a function find_longest_word() that takes a list of words and returns
the length of the longest
one.'''


def overlapping(lst1, lst2):
    lst1 = set(lst1)
    lst2 = set(lst2)
    return True if lst1 & lst2 == set() else False


def find_longest_word(lst):
    lst.sort(key=len)
    return lst[-1]


def main():
    input_lst1 = input("Please enter a string 1 (comma-separated) : ").\
        strip().split(",")
    input_lst2 = input("Please enter a string 2 (comma-separated) : ").\
        strip().split(",")
    print("Overlapping item : ", overlapping(input_lst1, input_lst2))
    print("Longest item "
          "in '{}' is '{}'".format(input_lst1, find_longest_word(input_lst1)))
    print("Longest item "
          " in '{}' is '{}'".format(input_lst2, find_longest_word(input_lst2)))


if __name__ == "__main__":
    main()
