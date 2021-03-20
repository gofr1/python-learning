#!/usr/bin/env python3

#! Special Methods
#
# A variety of instance methods that are reserved by Python, which affect an object’s high 
# level behavior and its interactions with operators. 

class Account:

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        print(f'(__init__) Account for {self.name} is reated with {self.balance} balance')

    def getBalance(self):
        return self.balance

    def __repr__(self):
        return f'(__repr__) Account({self.name}, {self.balance})'

    def __str__(self):
        return f'(__str__) Account Name = {self.name}, Account Balance = {self.balance}'

    def __lt__(self, other_object):
        try:
            return self.balance < other_object.getBalance()
        except:
            return None

    def __del__(self):
        self.balance = 0
        print(f'(__del__) Account of {self.name} is deleted')


account_0 = Account('Jack Smith', 500)
#* (__init__) Account for Jack Smith is reated with 500 balance
account_1 = Account('Jim Somerly', 700)
#* (__init__) Account for Jim Somerly is reated with 700 balance

print(account_0)
#* (__str__) Account Name = Jack Smith, Account Balance = 500
print(repr(account_1))
#* (__repr__) Account(Jim Somerly, 700)
print(account_0 < account_1)
#* True

del(account_0)
#* (__del__) Account of Jack Smith is deleted
del(account_1)
#* (__del__) Account of Jim Somerly is deleted