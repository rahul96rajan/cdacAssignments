'''Q.1. Write a program that asks the user how many days are in a particular
month, and what day of the
week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints
a calendar for that month.
For example, here is the output for a 30-day month that begins on day 4
(Thursday):
S M T W T F S
1 2 3
4 5 6 7 8 9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30
'''
import sys


def plot_calendar(num_of_days, starts_on):
    if num_of_days > 31:
        raise ValueError("Number of days in a month should bebetween 0 & 31")
    day = {
        "SUN": 0,
        "MON": 1,
        "TUE": 2,
        "WED": 3,
        "THU": 4,
        "FRI": 5,
        "SAT": 6
    }.get(starts_on, -1)
    if day == -1:
        raise ValueError("[ERROR] Invalid Day Selected!")
    print("-"*50, "\nS\tM\tT\tW\tT\tF\tS\n", "-"*50, sep="")
    counter = 1
    while(counter <= num_of_days+day):
        for j in range(7):
            if counter <= day:
                print("\t", end="")
            else:
                print(counter-day, "\t", end='')
            counter += 1
            if (counter-day-1) == num_of_days:
                break
        print("")


def main():
    sys.path.insert(1, r"/home/rahulrajan/Documents/dev/scripts/"
                    r"cdacAssignments/Assignment9")
    from question2 import input_positive_integer
    month_days = input_positive_integer("Please enter the number days in the"
                                        " month : ")
    day = input("Which days the the first day of the month ?\n"
                "Please select from [Sun, Mon, Tue, Wed, Thu, Fri, Sat] : ")\
                .upper()
    plot_calendar(month_days, day)
    print("-"*50)


if __name__ == "__main__":
    main()
