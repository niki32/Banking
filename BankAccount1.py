from my-bank1 import Bankaccount
def main():
    print(" ")
    print("Please choose 1 of the following options: ")
    print("   1. Open an account")
    print("   2. Deposit")
    print("   3. Withdraw")
    print("   4. Show balance")
    print("   5. Exit")
    return eval(input("Enter your option: "))

loop = 1
while loop == 1:
    choice = main () #default menu is displayed
    if choice == 1:
        Bankaccount.account() #option 1 to create and account
    elif choice == 2:
        Bankaccount.deposit() #option 2 to deposit money
    elif choice == 3:
        Bankaccount.withdraw() #option 3 to withdraw money
    elif choice == 4:
        Bankaccount.showbalance() #option 4 to show account balance
    elif choice = 5:
        Bankaccount.showTransactions ()
    elif choice == 6:
        loop = 0
        print ("Thank you for using the my bank application.") #end the application
    elif choice <= 0:
        print("Invalid selection. Please try again.") #error checking
    elif choice > 5:
        print ("Invalid selection. Please try again.") #error checking
