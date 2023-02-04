import random
import string

# ----------------------------
# Bank Account Class - Parent
# ----------------------------


class BankAccount:

    # I.1) Class Attributes
    accounts = []

    # II) Class Constructor
    def __init__(self, balance):
        # I.2) Instance Attributes
        self.balance = balance
        self.account_number = "".join(random.choices(string.digits, k=10))
        # I.3) Others
        BankAccount.accounts.append(self)

    # III) Methods

    # III.1) Instance Methods
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

    def display_account_info(self, name="No Name"):
        print(
            f"Name: {name} - Account: {self.account_number} - Balance: {self.balance}"
        )
        return self

    # III.2) Class Methods
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            print(f"Balance: {account.balance}")


# ----------------------------
# CheckingAccount - Child
# ----------------------------


class CheckingAccount(BankAccount):
    def __init__(self, balance=0):
        super().__init__(balance)


class SavingAccount(BankAccount):
    def __init__(self, balance=0, int_rate=0.01):
        super().__init__(balance)
        self.int_rate = int_rate  # <---- adding specialized attr

    def yield_interest(self):  # <---- adding specialized method
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate)
        else:
            print("Account overdrwan: No interests given")
        return self
    
    def withdraw(self, amount, is_early = True): # <---- changing functionality parent method
        if is_early:                             # <----- POLYMORPHISM
            amount = amount * 1.10
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

# ----------------------------
# User
# ----------------------------

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {  # <---- Composition (One-to-Many)
            "checking": CheckingAccount(balance = 1000),
            "savings":  SavingAccount(balance = 1000, int_rate = 0.05)
        }

# ***************
# Driver Code
# ***************

# checking_account = CheckingAccount(balance=1000)
# saving_account = SavingAccount(balance=1000, int_rate=0.03)
# checking_account.deposit(amount=50).withdraw(amount=100).display_account_info()
# saving_account.deposit(amount=50).withdraw(amount=100,is_early=False).display_account_info()

sara = User("Sara Miller", "sara@email.com")

sara.accounts["checking"].deposit(100).display_account_info(sara.name)
sara.accounts["savings"].yield_interest().display_account_info(sara.name)

sara.accounts["checking"].withdraw(100).display_account_info(sara.name)
sara.accounts["savings"].withdraw(100).display_account_info(sara.name)