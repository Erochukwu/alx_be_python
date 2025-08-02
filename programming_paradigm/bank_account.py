class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self, amount):
        if amount > self.account_balance:
            self.account_balance = amount
    
        def withdraw(amount):
            if amount <= self.account_balance:
                self.account_balance -= amount
                print("your new account balance is, {self.account_balance}")
            else:
                print("You do not have sufficient balance for this withdrawal")

    def display_balance(self):
        print("Current balance is, {self.account_balance}")