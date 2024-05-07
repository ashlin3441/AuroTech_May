class cardHolder():
    def __init__(self,cardNum,pin,firstname,lastname,balance):
        self.cardNum = cardNum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
        self.transactions = []

    #Getter Methods:
    def get_cardNum(self):
        return self.cardNum
    def get_pin(self):
        return self.pin
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_balance(self):
        return self.balance

    #Setter Methods:
    def set_cardNum(self,newVal):
        self.cardNum = newVal
    def set_pin(self,newVal):
        self.pin = newVal
    def set_firstname(self,newVal):
        self.firstname = newVal
    def set_lastname(self,newVal):
        self.lastname = newVal
    def set_balance(self,newVal):
        self.balance = newVal
    def add_transaction(self,transaction_type):
        self.transactions.append(transaction_type)

    def print_out(self):
        print("Card No :", self.cardNum)
        print("Pin :", self.pin)
        print("First Name :", self.firstname)
        print("Last Name :", self.lastname)
        print("Balance :", self.balance)

    
