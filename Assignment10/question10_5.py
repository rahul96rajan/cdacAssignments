'''Exercise 5: Define a class called Lunch.Its __init__() method should have
two arguments:selfanf menu.Where menu is a string. Add a method called
menu_price.It will involve a ifstatement:
•	if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2"
print "Your choice:", menu, "Price 13.40", else print "Error in menu".
To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().
'''


class Lunch:
    def __init__(self, menu):
        self.menu = menu

    def menu_price(self):
        if self.menu == "menu 1":
            return "Your choice: Aloo Parantha\nPrice: 12.00"
        elif self.menu == "menu 2":
            return "Your choice: Again Aloo Parantha\nPrice: 12.00"
        else:
            return "Error in menu"


def main():
    paul = Lunch(input("Enter food menu (menu 1 or menu 2) : "))
    print(paul.menu_price())


if __name__ == "__main__":
    main()
