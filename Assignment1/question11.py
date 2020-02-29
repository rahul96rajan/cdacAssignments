# Question 11 : Write a Python program to test whether a passed letter is a vowel or not.


def is_vowel(val):
    vowel_set = set(["a", "e", "i", "o", "u"])
    if len(val.strip()) > 1:
        print("Please enter a single character only!")
        return False
    if val.lower() in vowel_set:
        return True
    else:
        return False


input_char = input("Please enter a character : ")
print("Is Vowel Status =>", is_vowel(input_char))
