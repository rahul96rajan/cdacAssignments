# Q1: Write a Python class to implement pow(x, n)


class MyNumber(object):
    def __init__(self, a=0):
        self.a = a

    def pow(self, b):
        return self.a**b

    def __str__(self):
        return "My Number is " + str(self.a)


def input_integer(msg):
    try:
        num = int(input(msg))
    except ValueError:
        print("Please input integers only!")
        num = int(input(msg))
    return num


if __name__ == "__main__":
    num = MyNumber(input_integer("Enter a number : "))
    num_power = input_integer("Enter the power to which"
                              "number is to be raised : ")
    print(num, "\nMy number raised to power '%d' is : " % num_power,
          num.pow(num_power))
