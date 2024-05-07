from cardHolder import cardHolder

def print_menu():
    ### Print options to the user
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transactiion History")
    print("4. Transfer")
    print("5. Show Balance")
    print("6. Exit")

def deposit(cardHolder):
    try:
        deposit_amt = float(input("How much $$ would you want to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit_amt)
        cardHolder.add_transaction(f"Deposited {deposit_amt}")
        print("Money deposited Successfully.")
        print("Your new Balance is :", str(cardHolder.get_balance()))
    except:
        print("Invalid Input")

def withdraw(cardHolder):
    try:
        withdraw_amt = float(input("How much $$ would you want to withdraw: "))
        ### Check if user has enough Money
        if(cardHolder.get_balance() < withdraw_amt):
            print("Insufficient Funds :")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw_amt)
            cardHolder.add_transaction(f"Withdrawn {withdraw_amt}")
            print("Money Withdrew Successfully.")
            print("Your new Balance is ",str(cardHolder.get_balance()))
    except:
        print("Invalid Input")

def check_balance(cardHolder):
    print("Your Current balance is :",cardHolder.get_balance())
        
def transaction_history(cardHolder):
    print("Transaction History:")
    for transaction in cardHolder.transactions:
        print(transaction)

def transfer(sender,recipient):
    try:
        transfer_amt = float(input("How much money would you like to tramsfer:"))
        if sender.get_balance() < transfer_amt:
            print("Insufficient Funds for Transfer")
        else:
            sender.set_balance(sender.get_balance() - transfer_amt)
            recipient.set_balance(recipient.get_balance() + transfer_amt)
            sender.add_transaction(f"Transferred {transfer_amt} to {recipient.get_firstname()}")
            recipient.add_transaction(f"Received {transfer_amt} from {sender.get_firstname()}")
            print("Transfer successfull")    
    except:
        print("Invalid input..")

if __name__ == "__main__":
    current_user = cardHolder("","","","","")

### create a repo of cardHolders
list_of_cardHolders = []
list_of_cardHolders.append(cardHolder("67364414569",7025,"Ashlin","K s",643.25))
list_of_cardHolders.append(cardHolder("67364413597",6238,"Arjun","Babu",215.30))
list_of_cardHolders.append(cardHolder("67364413789",8844,"Prajun","K p",1520.60))
list_of_cardHolders.append(cardHolder("67364416984",4181,"Karthika","R",2364.12))
list_of_cardHolders.append(cardHolder("67364419647",4052,"Sneha","Dileep",12.6))

### Prompt user for debit card
# debitCardNum = ""
while True:
    try:
        debitCardNum = input("Please insert your debit card: ")
        ### check against repo
        debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
        if(len(debitMatch) > 0):
            current_user = debitMatch[0]
            break
        else:
            print("Card Number not recognized.Please try again.")
    except:
        print("Card Number not recognized.Please try again.")

### Prompt for pin
while True:
    try:
        userPin = int(input("Please enter yout pin : "))
        if(current_user.get_pin() == userPin):
            break
        else:
            print("Invalid Pin.Please try again..")
    except:
        print("Invalid Pin.Please try again..")

### Print options
print("Welcome" , current_user.get_firstname(),":")
option = 0
while True:
    print_menu()
    try:
        option = int(input())
    except:
        print("Invalid input.Please try again")
    if(option == 1):
        deposit(current_user)
    elif(option == 2):
        withdraw(current_user)
    elif(option == 3):
        transaction_history(current_user)
    elif(option == 4):
        recipient_card_num = input("Please enter recipient's card number:")
        recipient_match = [holder for holder in list_of_cardHolders if holder.cardNum == recipient_card_num]
        if len(recipient_match) > 0:
            transfer(current_user,recipient_match[0])
        else:
            print("Recipient card number not recognized")
    elif(option == 5):
        check_balance(current_user)
    elif(option == 6):
        break
    else:
        option = 0
print("Thank You , Have a nice day !!")
