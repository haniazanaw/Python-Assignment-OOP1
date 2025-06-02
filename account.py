from datetime import datetime

class Transaction:
    def __init__(self, amount, narration, transaction_type):
        self.amount = amount
        self.narration = narration
        self.transaction_type = transaction_type  
        self.date = datetime.now()
    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.transaction_type.upper()} | {self.narration} | Amount: {self.amount}"
class Account:
    def __init__(self, name,account_number):
        self.name = name
        self.__account_number = account_number
        self.__transactions = []
        self.__loan = 0
        self.__frozen = False
        self.__min_balance = 0
        self.__closed = False
   
    def __calculate_balance(self):
        balance = 0
        for i in self.__transactions:
            if i.transaction_type in ['deposit', 'loan']:
                balance += i.amount
            elif i.transaction_type in ['withdrawal', 'repayment', 'transfer_out']:
                balance -= i.amount
        return balance
 
    def deposit(self, amount):
        if self.__closed:
            return "Account is closed. No deposits allowed."
        if self.__frozen:
            return "Account is frozen. No deposits allowed."
        if amount <= 0:
            return "Deposit amount must be positive."
        i = Transaction(amount, "Deposit", "deposit")
        self.__transactions.append(i)
        return f"Confirmed. You have received {amount}. Your new balance is {self.get_balance()}."
   
    def withdraw(self, amount):
        if self.__closed:
            return "Account is closed. No withdrawals allowed."
        if self.__frozen:
            return "Account is frozen. No withdrawals allowed."
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if self.get_balance() - amount < self.__min_balance:
            return "Insufficient funds. Cannot go below minimum balance."
        i = Transaction(amount, "Withdrawal", "withdrawal")
        self.__transactions.append(i)
        return f"Confirmed. You have withdrawn {amount}. Your new balance is {self.get_balance()}."
    
    def transfer_funds(self, amount, other_account):
        if self.__closed:
            return "Account is closed. No transfers allowed."
        if self.__frozen or other_account.__frozen:
            return "One or both accounts are frozen. No transfers allowed."
        if amount <= 0:
            return "Transfer amount must be positive."
        if self.get_balance() - amount < self.__min_balance:
            return "Insufficient funds. Cannot go below minimum balance."
        self.__transactions.append(Transaction(amount, f"Transfer to {other_account.name}", "transfer_out"))
        other_account.__transactions.append(Transaction(amount, f"Transfer from {self.name}", "deposit"))
        return f"You transferred {amount} to {other_account.name}. Your new balance is {self.get_balance()}."
   
    def request_loan(self, amount):
        if self.__closed:
            return "Account is closed. No loans allowed."
        if self.__frozen:
            return "Account is frozen. No loans allowed."
        if amount <= 0:
            return "Loan amount must be positive."
        self.__loan += amount
        self.__transactions.append(Transaction(amount, "Loan received", "loan"))
        return f"Loan of {amount} granted. Your new balance is {self.get_balance()}."
  
    def repay_loan(self, amount):
        if self.__closed:
            return "Account is closed. No loan repayments allowed."
        if self.__frozen:
            return "Account is frozen. No loan repayments allowed."
        if amount <= 0:
            return "Repayment amount must be positive."
        repayment = min(amount, self.__loan)
        self.__loan -= repayment
        self.__transactions.append(Transaction(repayment, "Loan repayment", "repayment"))
        return f"Loan repayment of {repayment}. Remaining loan: {self.__loan}. Your new balance is {self.get_balance()}."
    
    def get_balance(self):
        return self.__calculate_balance()
    def get_account_number(self):
        return self.__account_number
    def get_loan_balance(self):
        return self.__loan
   
    def freeze_account(self):
        self.__frozen = True
        return "Account frozen."
    def unfreeze_account(self):
        self.__frozen = False
        return "Account unfrozen."
    def close_account(self):
        self.__transactions.clear()
        self.__loan = 0
        self.__frozen = False
        self.__closed = True
        return "Account closed. All balances and transactions cleared."
    def set_minimum_balance(self, amount):
        if amount < 0:
            return "Minimum balance cannot be negative."
        self.__min_balance = amount
        return f"Minimum balance set to {amount}."
    def change_account_owner(self, new_name):
        if self.__closed:
            return "Account is closed. Cannot change owner."
        self.name = new_name
        return f"Account owner updated to {new_name}."
   
    def view_account_details(self):
        return f"Account Owner: {self.name}\nAccount Number: {self.__account_number}\nCurrent Balance: {self.get_balance()}"
    def account_statement(self):
        if self.__closed:
            return "Account is closed. No statement available."
        print("Account Statement:")
        print(f"Owner: {self.name} | Account #: {self.__account_number}")
        for i in self.__transactions:
            print(i)
    def calculate_interest(self):
        balance = self.get_balance()
        if balance > 0:
            interest = 0.05 * balance
            self.__transactions.append(Transaction(interest, "Interest earned", "deposit"))
            return f"Interest of {interest} applied. Your new balance is {self.get_balance()}."
        return "No interest applied (zero or negative balance)."


acc1 = Account("Hani Azanaw",1000427276288)
acc2 = Account("Hasset Abera",1000264849371)


print(acc1.view_account_details()) 


print(acc1.deposit(50000))
print(acc1.deposit(30000))


print(acc1.withdraw(1500))


print(acc1.transfer_funds(1000, acc2))


print(acc1.request_loan(3000))


print(acc1.repay_loan(1000))


print(acc1.calculate_interest())


print(acc1.freeze_account())


print(acc1.unfreeze_account())

print(acc1.deposit(1000))  

print(acc1.set_minimum_balance(500))

print(acc1.withdraw(7000))  
print(acc1.withdraw(2000)) 

acc1.account_statement()
acc2.account_statement()
