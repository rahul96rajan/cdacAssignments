"""Problem 1.
A newly opened multinational brand has decided to base their company logo on
the three most common characters in the company name. They are now trying out
various combinations of company names and logos based on this condition.
Given a string , which is the company name in lowercase letters, your task
is to find the top three most common characters in the string.
Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,
 would have it's logo with the letters .
Input Format
A single line of input containing the string .
Constraints

Output Format
Print the three most common characters along with their occurrence count each
on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
Sample Input 0
aabbbccde
Sample Output 0
b 3
a 2
c 2
Explanation 0
Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the
third line because a comes before c in the alphabet.
Note: The string  has at least 3 distinct characters."""


def sort_lexicographically(lst):
    """Parameter : A 2D list which is sorted based on the number of occurances.
       Returns: An lexicographically internally sorted list."""
    i = 0
    length = len(lst)
    for x in range(1, length):
        if(lst[x][0] != lst[x-1][0] or x == length-1):
            if x == length-1:
                lst[i:] = sorted(lst[i:], key=lambda x: x[1])
            else:
                lst[i: x] = sorted(lst[i: x], key=lambda x: x[1])
            i = x
        elif x == length-1:
            i = x
    return lst


def get_top_n(s, n):
    """Parameter1: Any String of alphabets(ex: company name)
       Parameter2: Top n number
       Returns: An 2D list of top n numbers and occurrences."""
    s = s.lower()
    st = set(s)
    count_and_char = sort_lexicographically(sorted([[s.count(x), x] for
                                                    x in st], reverse=True))
    return count_and_char[:n]


def print_top_n(string, nth_number):
    """ Parameter1: Any String of alphabets(ex: company name)
        Parameter2: top n character required.
        Returns: None
        Action: Prints top 3 characters and occurrences."""
    lst = get_top_n(string, nth_number)
    for counter in range(nth_number):
        print("{0} {1}".format(lst[counter][1], lst[counter][0]))


if __name__ == '__main__':
    string = input()
    print_top_n(string, 3)
