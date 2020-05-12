# Q7. Define a class Employee with the following functions:
#    __init__() : to initialize all the variables with appropriate
#     default values
#    Displaycount(): to count the number of objects of employee class and
#     display the count
#    Displayemp(): to display the employee details


class Employee(object):
    num_of_employees = 0

    def __init__(self):
        Employee.num_of_employees += 1
        self.emp_name = "null_name"
        self.emp_age = -1
        self.emp_department = "null_department"
        self.emp_ID = "null_ID"

    def display_count(self):
        print("Total employees created : ", Employee.num_of_employees)

    def display_emp_detail(self):
        print("\nNAME : {0}\nAGE : {1}\nDEPARTMENT : {2}\nID : {3}".format(
              self.emp_name, self.emp_age, self.emp_department, self.emp_ID))


if __name__ == "__main__":
    print("\n#Employee when no employeee created :", Employee.num_of_employees)
    adam = Employee()
    adam.display_emp_detail()
    adam.display_count()
    cain = Employee()
    abel = Employee()
    adam.display_count()
