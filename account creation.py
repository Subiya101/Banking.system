
#Account Creation

class BankAccount:
    def __init__(self,name,account_number,balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        self.balance +=amount
        print(f"Amount Deposited: {amount}")

    def withdraw(self,amount):
        if self.balance >=amount:
            self.balance = amount
            print(f"Amount Withdraw: {amount}")
        else:
            print("Insufficient Amount")

    def display_balance(self):
        print(f"Account Balance: {self.balance}")
def main():
    account = BankAccount("Subiya Uruje","123456789",10000)

    print("Welcome to SBI bank")
    username = input("Enter the username: ")
    password = input("Enter your password: ")
    if username =="subiya" and password =="password":
        print("login successful")
    else:
        print("Incorrect username and password")
        return

    while True:
        print("What you like to do?")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Balance Inquery")
        print("4.Exit")
        x = int(input("Enter your choice: "))

        if x ==1:
            amount = float(input("Enter amount to be deposited: "))
            account.deposit(amount)
        elif x ==2:
            amount = float(input("Enter amount to be withdraw"))
            account.withdraw(amount)
        elif x ==3:
            account.display_balance()
        elif x ==4:
            print("Thankyou for using our banking system")
            break
        else:
            print("Invalid.please try again")

if __name__ =="__main__":
    main()



