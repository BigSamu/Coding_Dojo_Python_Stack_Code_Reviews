
# Class Definition
class User:

    # I.1) Class Attributes
    bank_name = "First National Dojo"

    # II) Class Initializer
    def __init__(self,name,email_address='no_email_given'):
        # I.2) Instance Attributes
        self.name = name
        self.email = email_address
        self.account_balance = 0


    # III) Class Methods
    # pending

class Admin:

    # I.1) Class Attributes
    bank_name = "World Kyoto"

    # II) Class Initializer
    def __init__(self,name,email_address='admin@python.com'):
        # I.2) Instance Attributes
        self.name = name
        self.email = email_address
        self.account_balance = 10000

    # III) Class Methods
    # pending...



# Class Instantiation 

print("*"*50)

guido = User("Guido van Rossum", "guido@python.com")
monty = Admin("Monty Python")
print(f"{guido.name} - {guido.email} - {guido.account_balance} - {guido.bank_name}")
print(f"{monty.name} - {monty.email} - {monty.account_balance} - {monty.bank_name}")

print("*"*50)

guido.name = "Peter"
guido.email = "peter@python.com"
guido.account_balance = 10000
guido.bank_name = "XYZ Bank"

print(f"{guido.name} - {guido.email} - {guido.account_balance} - {guido.bank_name}")

print("*"*50)

print(User.bank_name)
print(Admin.bank_name)

print("*"*50)


