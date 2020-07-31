# Q5. write a Program to Remove Punctuations from a String provided by the user

import re


def remove_punctuation(string):
    su = re.sub(r"[-\[\]\{\}\(\)\*\+\?\.,;\\^$\|#]", "", string)
    return su


def main():
    string = input("Please enter a sentence: ").strip()
    print("Sentence without punctuation : " + remove_punctuation(string))


main()
