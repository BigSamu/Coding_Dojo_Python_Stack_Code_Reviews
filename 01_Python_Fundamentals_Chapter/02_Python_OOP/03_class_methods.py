# Class Definition
class User:

    # I.1) Class Attributes
    bank_name = "First National Dojo"
    all_users = []

    # II) Class Constructor
    def __init__(self, name, email_address="no_email_given"):
        # I.2) Instance Attributes
        self.name = name
        self.email = email_address
        self.account_balance = 0
        User.all_users.append(self)

    # III) Methods
    # III.1) Instance Methods
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdraw(self, amount):
        if User.can_withdraw(self.account_balance, amount):
            self.account_balance -= amount 
        return self
    
    def transfer_money(self, amount, user):
        if User.can_withdraw(self.account_balance, amount):
            self.account_balance -= amount
            user.account_balance += amount
        return self
    

    # III.2) Class Method
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        return cls

    @classmethod
    def list_users(cls):
        out = ""
        for each in cls.all_users:
            out = out + each.name + " - "
        return out[0 : len(out) - 3]

    # III.3) Static Method
    @staticmethod
    def can_withdraw(balance,amount):
        if(balance-amount)<0:
            print("Insufficient Funds!!!")
            return False
        else:
            return True

print("*" * 50)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python")
print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")
print(f"{monty.name} - {monty.email} - ${monty.account_balance} - {monty.bank_name}")

print("*" * 50)

print(guido.make_deposit(200))
monty.make_deposit(200).make_deposit(50)
print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")
print(f"{monty.name} - {monty.email} - ${monty.account_balance} - {monty.bank_name}")

print("*" * 50)

guido.bank_name = "ABC"
User.change_bank_name("XYZ")
peter = User("Peter Phillips", "peter@python.com")
print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")
print(f"{monty.name} - {monty.email} - ${monty.account_balance} - {monty.bank_name}")
print(f"{peter.name} - {peter.email} - ${peter.account_balance} - {peter.bank_name}")

print("*" * 50)

print("Listing Users:")
print(User.list_users())

print("*" * 50)

print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")
print("Guido withdrawing 100 from its account")
guido.make_withdraw(100)
print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")

print("*" * 50)

print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")
print("Guido withdrawing 150 from its account")
guido.make_withdraw(150)
print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")

print("*" * 50)

print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")
print("Guido withdrawing 25 twice from its account")
guido.make_withdraw(25).make_withdraw(25)
print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")

print("*" * 50)

print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")
print(f"{monty.name} - {monty.email} - ${monty.account_balance} - {monty.bank_name}")
guido.transfer_money(5, monty)
print("Guido transfering 5 to Monty")
print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")
print(f"{monty.name} - {monty.email} - ${monty.account_balance} - {monty.bank_name}")

print("*" * 50)

print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")
print(f"{peter.name} - {peter.email} - ${peter.account_balance} - {peter.bank_name}")
print(f"Guido transfering 50 to Peter")
guido.transfer_money(50, peter)
print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")
print(f"{peter.name} - {peter.email} - ${peter.account_balance} - {peter.bank_name}")

print("*" * 50)