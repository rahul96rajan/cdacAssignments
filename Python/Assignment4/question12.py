# Q12: The marks obtained by a student in 5 different Subjects are input through a keyboard.
# The Student gets a division as per the following rules.
# 1.	Percentage above or equal to 60 – First Division
# 2.	Percentage between 50 and 59 – Second Division
# 3.	Percentage between 40 and 49 – Third Division
# 4.	Percentage less than 40 – Fail
# Write a python program to Display the result based on the above Criteria.


def input_integer(msg):
    try:
        num = int(input(msg).strip())
    except ValueError:
        print("Please input integers only!")
        num = int(input(msg))
    return num


def input_float(msg):
    try:
        num = float(input(msg).strip())
    except ValueError:
        print("Please input integers or decimals only!")
        num = float(input(msg))
    return num


def input_score():
    num_subjects = input_integer("Please enter number of subjects : ")
    if num_subjects < 0:
        print("Incorrect selection, please try again!")
        num_subjects = input_integer("Please enter number of subjects : ")
    subject_list = []
    for x in range(0, num_subjects):
        score = input_float("Enter score for subject %d :" % (x + 1))
        if score < 0:
            print("Incorrect score please try again!")
            score = input_float("Enter score for subject %d :" % (x + 1))
        subject_list.append(score)
    return subject_list


def division_calc(score_list):
    total = sum(score_list) / len(score_list)
    if 60 <= total <= 100:
        return "First Division"
    elif 50 <= total <= 59:
        return "Second Division"
    elif 40 <= total <= 49:
        return "Third Division"
    elif total < 40:
        return "Fail"
    else:
        return "Incorrect score! Please verify entries."


def main():
    print("Division acquired => ", division_calc(input_score()))


main()
