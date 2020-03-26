'''Q. 4. A pangram is a sentence that contains all the letters of the English
alphabet at least once, for example: The quick brown fox jumps over the lazy
dog. Your task here is to write a function to check a sentence to see if it is
a pangram or not.'''

from string import ascii_lowercase


def is_pangram(param_str):
    alphabets = set(ascii_lowercase)
    return True if alphabets & set(param_str) == alphabets else False


def main():
    string = input("Please type in a string: ")
    print("Pangram Status :", is_pangram(string))


if __name__ == "__main__":
    main()
