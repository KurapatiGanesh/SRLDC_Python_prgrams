class BankAccount:
    def __init__(self,account_number,holder_name,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance
    
    def deposit(self,amount):  # amount Deposit Method
        if amount>0:
            self.balance += amount 
            print(f"{amount} deposit Sucessfully")
        else:
            print("Amount Must be in positive")


    def withdrow(self,amount):  # amount Withdrow Method
        if 0<amount<=self.balance:
            self.balance -= amount
            print(f"{amount} withdrow sucessfully")
        elif amount>self.balance:
            print("insuffient balance")
        else:
            print("your account balance in nagative")

    def display_balance(self): # balance Display Method
        print(f"Account Balance:{self.balance}")

account=BankAccount("1700150282","Ganesh Kurapati",2000)
account.deposit(5000)
account.withdrow(3000)
account.display_balance()
        