
class BankAccount:
    def __init__(self, name , address, account_number, balance, overdraft = 0):
        self.ac_name = name
        self.ac_address = address
        self.id = account_number
        self.ac_balance = balance
        self.overdraft = overdraft

    def withdraw(self, amount):
        print("Your current balance is ", self.ac_balance)
        if self.ac_balance + self.overdraft >= amount:
            self.ac_balance -= amount
        print("-------------------------")
        print("Your new balance is ", self.ac_balance)
