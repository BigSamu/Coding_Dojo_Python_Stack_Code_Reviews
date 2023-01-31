

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
    def __init__(self,int_rate,balance):
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

    def yeild_interest(self): 
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    # III.2) Class Methods
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()






# ***************
# Driver Code
# ***************

savings = BankAccount(.05,1000)
checking = BankAccount(.02,5000)

BankAccount.print_all_accounts()

print("*"*50)

savings.deposit(10).deposit(20).deposit(40).withdraw(600).yeild_interest().display_account_info()
checking.deposit(100).deposit(200).deposit(400).withdraw(60).yeild_interest().display_account_info()

print("*"*50)

BankAccount.print_all_accounts().print_all_accounts()