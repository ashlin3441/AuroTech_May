import datetime

class Account:
    def __init__(self, card_num, pin, firstname, lastname, balance=0):
        self.card_num = card_num
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(Transaction("Withdrawal", amount))
            return True
        else:
            return False

    def transfer(self, recipient, amount):
        if self.withdraw(amount):
            recipient.deposit(amount)
            self.transactions.append(Transaction("Transfer to " + recipient.firstname, amount))
            recipient.transactions.append(Transaction("Received from " + self.firstname, amount))
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.datetime.now()


class User:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.card_num] = account

    def authenticate(self, card_num, pin):
        if card_num in self.accounts and self.accounts[card_num].pin == pin:
            return self.accounts[card_num]
        else:
            return None


class ATM:
    def __init__(self, bank):
        self.bank = bank
        self.current_user = None

    def authenticate_user(self, card_num, pin):
        self.current_user = self.bank.authenticate(card_num, pin)
        if self.current_user:
            return True
        else:
            return False

    def deposit(self, amount):
        if self.current_user:
            self.current_user.deposit(amount)
            print("Money deposited Successfully.")
            print("Your new Balance is :", self.current_user.get_balance())
        else:
            print("Please insert your debit card and enter your PIN first.")

    def withdraw(self, amount):
        if self.current_user:
            if self.current_user.withdraw(amount):
                print("Money Withdrew Successfully.")
                print("Your new Balance is ", self.current_user.get_balance())
            else:
                print("Insufficient Funds")
        else:
            print("Please insert your debit card and enter your PIN first.")

    def transfer(self, recipient_card_num, amount):
        if self.current_user:
            recipient = self.bank.accounts.get(recipient_card_num)
            if recipient:
                if self.current_user.transfer(recipient, amount):
                    print("Transfer successful")
                else:
                    print("Insufficient Funds for Transfer")
            else:
                print("Recipient card number not recognized")
        else:
            print("Please insert your debit card and enter your PIN first.")

    def check_balance(self):
        if self.current_user:
            print("Your Current balance is :", self.current_user.get_balance())
        else:
            print("Please insert your debit card and enter your PIN first.")

    def transaction_history(self):
        if self.current_user:
            print("Transaction History:")
            for transaction in self.current_user.get_transactions():
                print(transaction.transaction_type, "-", transaction.amount, "-", transaction.timestamp)
        else:
            print("Please insert your debit card and enter your PIN first.")

# Example usage:
bank = Bank()

# Adding accounts
bank.add_account(Account("67364414569", 7025, "Ashlin", "K s", 643.25))
bank.add_account(Account("67364413597", 6238, "Arjun", "Babu", 215.30))
bank.add_account(Account("67364413789", 8844, "Prajun", "K p", 1520.60))
bank.add_account(Account("67364416984", 4181, "Karthika", "R", 2364.12))
bank.add_account(Account("67364419647", 4052, "Sneha", "Dileep", 12.6))

# Starting ATM
atm = ATM(bank)
while True:
    print("Welcome to the ATM!")
    card_num = input("Please insert your debit card: ")
    pin = int(input("Please enter your PIN: "))
    if atm.authenticate_user(card_num, pin):
        print("Authentication successful!")
        break
    else:
        print("Invalid card number or PIN. Please try again.")

while True:
    print("\nPlease choose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == "3":
        recipient_card_num = input("Enter recipient's card number: ")
        amount = float(input("Enter amount to transfer: "))
        atm.transfer(recipient_card_num, amount)
    elif choice == "4":
        atm.check_balance()
    elif choice == "5":
        atm.transaction_history()
    elif choice == "6":
        print("Thank you for using the ATM. Have a nice day!")
        break
    else:
        print("Invalid choice. Please try again.")
