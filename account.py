

class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawals = [] 
        self.loan = 0
        self.frozen = False
        self.min_balance = 0
        self.closed = False

    def deposit(self, amount):
        if self.closed:
            return "Account is closed. No deposits allowed."
        if self.frozen:
            return "Account is frozen. No deposits allowed."
        if amount <= 0:
            return "Deposit amount must be positive."
        self.balance += amount
        self.deposits.append(amount)
        return f"Confirmed. You have received {amount}. New balance is {self.balance}."

    def withdraw(self, amount):
        if self.closed:
            return "Account is closed. No withdrawals allowed."
        if self.frozen:
            return "Account is frozen. No withdrawals allowed."
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if self.balance - amount < self.min_balance:
            return "Insufficient funds. Cannot go below minimum balance."
        self.balance -= amount
        self.withdrawals.append(amount)
        return f"Confirmed. You have withdrawn {amount}. New balance is {self.balance}."

    def transfer_funds(self, amount, other_account):
        if self.closed:
            return "Account is closed. No transfers allowed."
        if self.frozen or other_account.frozen:
            return "One or both accounts are frozen. No transfers allowed."
        if amount <= 0:
            return "Transfer amount must be positive."
        if self.balance - amount < self.min_balance:
            return "Insufficient funds. Cannot go below minimum balance."
        self.withdraw(amount)
        other_account.deposit(amount)
        return f"Transferred {amount} to {other_account.name}. New balance is {self.balance}."

    def get_balance(self):
        return self.balance

    def request_loan(self, amount):
        if self.closed:
            return "Account is closed. No loans allowed."
        if self.frozen:
            return "Account is frozen. No loans allowed."
        if amount <= 0:
            return "Loan amount must be positive."
        self.balance += amount
        self.loan += amount
        return f"Loan of {amount} granted. New balance is {self.balance}."

    def repay_loan(self, amount):
        if self.closed:
            return "Account is closed. No loan repayments allowed."
        if self.frozen:
            return "Account is frozen. No loan repayments allowed."
        if amount <= 0:
            return "Repayment amount must be positive."
        if amount > self.loan:
            amount = self.loan
            self.balance -= amount
            self.loan = 0
            return f"Loan fully repaid. {amount} paid. New balance is {self.balance}."
        self.loan -= amount
        self.balance -= amount
        return f"Loan repayment of {amount}. Remaining loan: {self.loan}. New balance is {self.balance}."

    def view_account_details(self):
        return f"Account Owner: {self.name}\nCurrent Balance: {self.balance}"

    def change_account_owner(self, new_name):
        if self.closed:
            return "Account is closed. Cannot change owner."
        self.name = new_name
        return f"Account owner updated to {new_name}."

    def account_statement(self):
        if self.closed:
            return "Account is closed. No statement available."
        print("Account Statement:")
        print(f"Owner: {self.name}")
        print("Deposits:")
        for dep in self.deposits:
            print(f" +{dep}")
        print("Withdrawals:")
        for wd in self.withdrawals:
            print(f" -{wd}")
        print(f"Current Balance: {self.balance}")

    def calculate_interest(self):
        if self.balance > 0:
            interest = 0.05 * self.balance
            self.balance += interest
            return f"Interest of {interest} applied. New balance is {self.balance}."
        return "No interest applied (zero or negative balance)."

    def freeze_account(self):
        self.frozen = True
        return "Account frozen."

    def unfreeze_account(self):
        self.frozen = False
        return "Account unfrozen."

    def set_minimum_balance(self, amount):
        if amount < 0:
            return "Minimum balance cannot be negative."
        self.min_balance = amount
        return f"Minimum balance set to {amount}."

    def close_account(self):
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.frozen = False
        self.closed = True
        return "Account closed. All balances and transactions cleared."

