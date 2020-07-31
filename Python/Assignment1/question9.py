# Question 9 - Write a Python program to calculate number of days between two dates.

from datetime import date


def diff_date(d1, d2):
    date11 = date(int(date1.split("/")[0]), int(date1.split("/")[1]), int(date1.split("/")[2]))
    date22 = date(int(date2.split("/")[0]), int(date2.split("/")[1]), int(date2.split("/")[2]))
    return abs(date11-date22)


print("NOTE: Please input the value in [yyyy/mm/dd] format only")
date1 = input("Please input date 1 : ")
date2 = input("Please input date 2 : ")


print("The Difference in dates =>", diff_date(date1, date2))


