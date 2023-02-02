

# <User>
#   - name
#   - email
#   - number_of_accounts (2 accounts -> savings, chekcing)
#   - accounts[] -> [<savings>, <chekcing>]

# <Bank Account> 
#   - init_rate
#   - balance
#   - account_number


# guido.accounts[0].deposit(100)
# guido.accounts[1].deposit(50)

# -----------------------
# Bank Account Class
# -----------------------

class BankAccount:
    
    # I.1) Class Attributes
    accounts = []
    # II) Class Constructor
    def __init__(self,int_rate=0,balance=0):
        # I.2) Instance Attributes
        self.int_rate = int_rate
        self.balance = balance
        # I.3) Others 
        BankAccount.accounts.append(self) 

    # III) Methods
    # III.1) Instance Methods
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self): 
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    # III.2) Class Methods
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:

    #  I.1) Class Attributes
    # None  

    # II) Class Constructor
    
    # Way 1
    # def __init__(self, name, email, number_of_accounts=1):
    #     # I.2) Instance Attributes
    #     self.name = name
    #     self.email = email
    #     self.accounts = [] # <---- Composition (One-to-Many)
    #     # I.3) Others
    #     for i in range(number_of_accounts):
    #         self.accounts.append(BankAccount())

    # Way 2
    # def __init__(self, name, email):
    #     # I.2) Instance Attributes
    #     self.name = name
    #     self.email = email
    #     self.accounts = [BankAccount(0.01,1000),BankAccount(0.05,5000)]

    # Way 3
    # def __init__(self, name, email, accounts = []):
    #     # I.2) Instance Attributes
    #     self.name = name
    #     self.email = email
    #     self.accounts = accounts # <---- Composition (One-to-Many)

    # Way 4
    def __init__(self, name, email, account = None):
        # I.2) Instance Attributes
        self.name = name
        self.email = email
        self.account = account # <---- Composition (One-to-One)

    # Way 5
    def __init__(self, name, email):
        # I.2) Instance Attributes
        self.name = name
        self.email = email
        self.accounts = {  # <---- Composition (One-to-Many)
            "checking": BankAccount(0.01,1000),
            "savings":  BankAccount(0.05,1000)
        }
         

    

# ***************
# Driver Code
# ***************

# savings = BankAccount(.05,1000)
# checking = BankAccount(.02,5000)

# print("*"*50)

# savings.deposit(10).deposit(20).deposit(40).withdraw(600).yield_interest().display_account_info()
# checking.deposit(100).deposit(200).deposit(400).withdraw(60).yield_interest().display_account_info()

# Way 1

# sara = User("Sara Miller", "sara@email.com")

# print("--- Types ---")
# print(f"{User} ---> {type(User)}")
# print(f"{sara} ---> {type(sara)}")
# print("--- User Name & Email ---")
# print(f"{sara.name} - {sara.email}")
# print("--- User Bank Accounts ---")
# print(sara.accounts)

# print("*"*50)

# Way 2

# sara = User("Sara Miller", "sara@email.com")

# print(f"{sara} --- {type(sara)}")
# print(f"{sara.accounts} --- {type(sara.accounts)}")
# print(f"{sara.accounts[0]} --- {type(sara.accounts[0])}")
# sara.accounts[0].deposit(10).deposit(20).deposit(40).withdraw(600).yield_interest().display_account_info()
# sara.accounts[1].deposit(100).deposit(200).deposit(400).withdraw(60).yield_interest().display_account_info()

# Way 3

# savings = BankAccount(.05,1000)
# checking = BankAccount(.02,5000)
# retirement = BankAccount(.02,10000000)
# bank_accounts = [savings, checking]
# sara = User("Sara Miller", "sara@email.com", bank_accounts)
# sara.accounts.append(retirement)

# print(f"{sara} --- {type(sara)}")
# print(f"{sara.accounts} --- {type(sara.accounts)}")
# print(f"{sara.accounts[0]} --- {type(sara.accounts[0])}")
# print(f"{sara.accounts[0].balance} --- {sara.accounts[0].int_rate*100}%")

# Way 4

# savings = BankAccount(.05,1000)
# sara = User("Sara Miller", "sara@email.com", savings)

# print(f"{sara} --- {type(sara)}")
# print(f"{sara.account} --- {type(sara.account)}")
# print(f"{sara.account.balance} --- {sara.account.int_rate*100}%")

# Way 5
sara = User("Sara Miller", "sara@email.com")

sara.accounts["savings"].deposit(10).deposit(20).deposit(40).withdraw(600).yield_interest().display_account_info()
sara.accounts["checking"].deposit(100).deposit(200).deposit(400).withdraw(60).yield_interest().display_account_info()

print("*"*50)