# Q6. Define a class Person with the following member functions:
#      Getdata() :  to take name and age of a person as an input from the user
#      Showdata(): to display name and age
#      Define a class Student (this class inherits Person class), with the
# following functions:
# Getdata(): calls Getdata() of Person class to take input as name and age.
# And also takes an extra input from user that is Student_id.
# Showdata(): calls Showdata() of Person class and also displays Student_id
# Create the object of Student class and enter the name, age and student_id
# and also display      all the information of a student.

from question4 import input_positive_integer


class Person(object):
    def get_data(self):
        self.name = input("Please Enter Your Name : ")
        self.age = input_positive_integer("Please Enter Your Age : ")

    def show_data(self):
        print("\nNAME : {0}\nAGE : {1}".format(self.name, self.age))


class Student(Person):
    def get_data(self):
        super().get_data()
        self.student_id = input("Please Enter Your Student ID : ")

    def show_data(self):
        super().show_data()
        print("STUDENT ID :", self.student_id)


if __name__ == "__main__":
    aadmi = Person()
    aadmi.get_data()
    aadmi.show_data()
    print("-"*40)
    baccha = Student()
    baccha.get_data()
    baccha.show_data()
