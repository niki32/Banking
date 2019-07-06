class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def account (Self):
        self.name = str(input("Enter the owner's name: "))
        self.balance = float(input("Enter the initial balance: $"))

    def deposit (self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance = self.balance + amount
        print ("Amount Deposited:", amount)
        return amount

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You withdrew: ", amount)
        else:
            print ("Insufficient balance.")
        return amount

    def showBalance (self):
        print("Account name: ", self.name)
        print("Current balance: ", self.balance)
        return

    def showTransactions (self):
        print("Transaction type", end="     ")
        print("Amount", end="     ")
        print("Date/Time")