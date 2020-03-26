'''Write a program that computes the net amount of a bank account based a
transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500'''


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Balance! Can not withdraw amount!"
                  " Please open a credit A/C with us.")
        else:
            self.balance -= amount
            # print("Deducted: {0}, Net Balance: {1}".
            #       format(amount, self.balance))

    def deposit(self, amount):
        self.balance += amount
        # print("Added: {0}, Net Balance: {1}".
        #       format(amount, self.balance))

    def __str__(self):
        return "Current Balance : " + str(self.balance)


def main():
    my_account = Account(0)
    flag = True
    while(flag):
        input_command = input("Please enter command : ").split(" ")
        if input_command[0].upper() == "D":
            my_account.deposit(int(input_command[1]))
        elif input_command[0].upper() == "W":
            my_account.withdraw(int(input_command[1]))
        else:
            print("Wrong Command!")
        flag = True if input("Continue(Y/N)? ").strip().upper()=="Y" else False
    print(my_account)


if __name__ == "__main__":
    main()
