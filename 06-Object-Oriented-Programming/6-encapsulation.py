# Encapsulation: Private attributes and methods

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance  # Getter for private variable

# Creating an account
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)

# Accessing private variable (will cause an error)
# print(account.__balance)
