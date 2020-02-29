# Q6:  Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.


def start2_end2_string(string):
    if len(string) < 4:
        print("Stings' too short, input more than 3 characters.")
        return None
    return string[:2] + string[-2:]


def main():
    string = input("Please enter a string with 4 or more chars : ")
    print("String generated using start 2 and last 2 chars : ", start2_end2_string(string))


main()
