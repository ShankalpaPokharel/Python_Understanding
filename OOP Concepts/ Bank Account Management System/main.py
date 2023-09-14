class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        # Initialize a Bank Account with an account number, account holder, and balance
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Deposit money into the account
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        # Withdraw money from the account
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        # Display the current balance of the account
        print(f"Account Balance: ${self.balance}")

    def __str__(self):
        # Define how the account information is represented as a string
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.03):
        # Initialize a Savings Account with additional interest rate parameter
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        # Apply interest to the account balance
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"Interest applied. New balance: ${self.balance}")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):
        # Initialize a Checking Account with an overdraft limit
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # Override withdraw method to account for overdraft limit
        if amount > 0 and self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or exceeded overdraft limit.")



print("-----------------------------------------------------")
# Create a savings account
savings_acc = SavingsAccount("SAV123", "John Doe")
savings_acc.deposit(1000)
savings_acc.apply_interest()
savings_acc.display_balance()
print("-----------------------------------------------------")
# Create a checking account
checking_acc = CheckingAccount("CHK456", "Jane Smith")
checking_acc.deposit(500)
checking_acc.withdraw(700)  # Exceeding overdraft limit
checking_acc.withdraw(200)
checking_acc.display_balance()
print("-----------------------------------------------------")


# Output
'''
-----------------------------------------------------
Deposited $1000. New balance: $1000
Interest applied. New balance: $1030.0
Account Balance: $1030.0
-----------------------------------------------------
Deposited $500. New balance: $500
Invalid withdrawal amount or exceeded overdraft limit.
Withdrew $200. New balance: $300
Account Balance: $300
-----------------------------------------------------


'''