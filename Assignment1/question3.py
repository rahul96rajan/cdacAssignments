#  Question 3 : Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary.

basic = float(input("Please enter basic salary : "))
dearAllow = 0.4*basic
HRA = 0.2*basic
grossSalary = basic + dearAllow + HRA
print("Ramesh's Gross Salary => " + str(round(grossSalary, 2)) + "")
