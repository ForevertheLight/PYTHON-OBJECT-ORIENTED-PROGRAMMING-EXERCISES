#Encapsulation means restricting direct access to certain parts of an object 
# and using methods to modify or view the data safely.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
