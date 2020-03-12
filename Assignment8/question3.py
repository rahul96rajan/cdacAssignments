# Q3: Define a class Person and its two child classes: Male and Female.
# All classes have a method "getGender" which can print "Male" for Male class
# and "Female" for Female class.


class Person(object):
    def __init__(self, name):
        self.name = name

    def set_gender():
        pass

    def __str__(self):
        return self.name + " is a " + self.gender


class Male(Person):
    def __init__(self, name):
        super().__init__(name)
        self.set_gender()

    def set_gender(self):
        self.gender = "Male"

    def getGender(self):
        return self.gender


class Female(Person):
    def __init__(self, name):
        super().__init__(name)
        self.set_gender()

    def set_gender(self):
        self.gender = "Female"

    def getGender(self):
        return super().gender


if __name__ == "__main__":
    male = Male(input("Enter the name of a man (Ex: Luke) : "))
    female = Female(input("Enter the name of a man (Ex: Leia) : "))
    print(male)
    print(female)
