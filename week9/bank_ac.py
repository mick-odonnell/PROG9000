# This is a program to manage money for a school back
# We have built some classes and some methods which we will want
# to use again

import os
import csv

# Create a bank account class that contains the following attributes and methods: Attributes: name , address,
# account_number, balance, pending_pos, pending_neg Methods: funds_available (balance+pending_pos – pending_neg)

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

def main():
    # this is where i will test stuff

if __name__ == '__main__':
    main()
