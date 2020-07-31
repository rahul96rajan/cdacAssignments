# Question 10 : Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.


def add_is_to_start_if_not_present(string):
    string.strip()
    if not (string.startswith("Is") or string.startswith("is") or string.startswith("IS")):
        string = "Is " + string

    return string


input_str = input("Please enter a string :")

print(add_is_to_start_if_not_present(input_str))
