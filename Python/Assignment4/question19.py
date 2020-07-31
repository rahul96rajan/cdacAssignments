# Q19. Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9
import re


def input_comma_separated_list():
    list_string = input("Please enter comma separated list values: ").strip()
    return ",".join(str(x) for x in [x for x in re.split("\s*,\s*", list_string) if int(x) % 2 == 1])


def main():
    print("Odd list: ", input_comma_separated_list())


main()