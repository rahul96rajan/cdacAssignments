# Q10. In the above class create a method to overload add operator to add two
# complex number and return the sum.Q10. In the above class create a method to
# overload add operator to add two complex number and return the sum.

from question4 import input_positive_integer


class ComplexNumbers(object):
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        return "({0}+{1}i)".format(self.real, self.img)

    def __add__(self, cn2):
        return ComplexNumbers((self.real + cn2.real), (self.img + cn2.img))


if __name__ == "__main__":
    cn1 = ComplexNumbers(input_positive_integer("Enter the real part : "),
                         input_positive_integer("Enter the imaginary part : "))
    cn2 = ComplexNumbers(input_positive_integer("Enter the real part : "),
                         input_positive_integer("Enter the imaginary part : "))
    print("Complex number 1 : {0}\nComplex number 2 : {1}".format(cn1, cn2))
    print("Addition Results :", cn1+cn2)
