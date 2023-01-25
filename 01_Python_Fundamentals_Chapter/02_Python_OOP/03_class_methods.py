# Class Definition
class User:

    # I.1) Class Attributes
    bank_name = "First National Dojo"
    all_users = []

    # II) Class Initializer
    def __init__(self, name, email_address="no_email_given"):
        # I.2) Instance Attributes
        self.name = name
        self.email = email_address
        self.account_balance = 0
        User.all_users.append(self)

    # III) Class Methods
    # III.1) Instance Methods
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdraw(self, amount):
        pass

    # III.2) Class Method
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        return

    @classmethod
    def list_users(cls):
        out = ""
        for each in cls.all_users:
            out = out + each.name + " - "
        return out[0 : len(out) - 3]


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

User.change_bank_name("XYZ")
peter = User("Peter Phillips", "peter@python.com")
print(f"{guido.name} - {guido.email} - ${guido.account_balance} - {guido.bank_name}")
print(f"{monty.name} - {monty.email} - ${monty.account_balance} - {monty.bank_name}")
print(f"{peter.name} - {peter.email} - ${peter.account_balance} - {peter.bank_name}")

print("*" * 50)

print("Listing Users:")
print(User.list_users())

print("*" * 50)
