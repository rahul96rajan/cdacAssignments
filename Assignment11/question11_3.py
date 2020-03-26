'''Q. 3. Write a version of a palindrome recognizer that also accepts phrase
palindromes such as "Go hang a salami I'm a lasagna hog.",
"Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa
Bonet ate no basil", "Satan, oscillate my metallic sonatas",
"I roamed under it as a tired nude Maori", "Rise to vote sir",
or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization,
and spacing are usually ignored
'''

from string import punctuation


def is_pallindrome(param_str):
    param_str = ''.join(char for char in param_str
                        if char not in set(punctuation+" "))
    return True if param_str.lower() == param_str[::-1].lower() else False


def main():
    string = input("Please type in a string: ")
    print("Pallindrome Status :", is_pallindrome(string))


if __name__ == "__main__":
    main()
