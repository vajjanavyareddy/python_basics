class BankAccount:
    def __init__(self,balance=0):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
        print(f"Amount deposited {amount} then balance is {self.__balance}")
    def withdraw(self,amount):
        if amount>self.__balance:
            print("No sufficient balance")
        else:
            self.__balance-=amount
            print(f"Amount withdrawn {amount} then balance is {self.__balance}")
    def get_balance(self):
        return self.__balance
b = BankAccount()
b.deposit(5000)
b.withdraw(2000)
print("Balance amount: ",b.get_balance())


    
    

            
