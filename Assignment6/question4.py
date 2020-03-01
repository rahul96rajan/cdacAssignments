# Q4. write a Program to sort alphabetically the words form a string provided by the user. [You can use split() method to split string into a list of words. ]


def sort_list(string):
    str_list = string.split(" ")
    str_list.sort()
    return str_list


def main():
    string = input("Please enter a sentence: ").strip()
    print("Sorted Sentence :", " ".join(sort_list(string)))


main()
