# Q9. Define a class ComplexNumbers with the following functions:
#    Constructor: to initialize an initial value to a complex number
#    __str__(): to display complex number
# Create two objects of this class and display the result.

from question4 import input_positive_integer


class ComplexNumbers(object):
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        return "({0}+{1}i)".format(self.real, self.img)


if __name__ == "__main__":
    cn1 = ComplexNumbers(input_positive_integer("Enter the real part : "),
                         input_positive_integer("Enter the imaginary part : "))
    cn2 = ComplexNumbers(input_positive_integer("Enter the real part : "),
                         input_positive_integer("Enter the imaginary part : "))
    print("Complex number 1 : {0}\nComplex number 2 : {1}".format(cn1, cn2))
