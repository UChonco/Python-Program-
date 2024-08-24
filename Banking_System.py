class bankaccount:
    def __init__(self,acc_holder):
        self.acc_holder = acc_holder
        self.balance = 0

    def Deposit(self,acc_holder,amount ):
        name = self.acc_holder
        balance =self.balance
        balance += amount
        print(f"\n {"_"*60} \n Successful Deposit R{amount:.2f} from {name} Account \n(Account Balance : R{balance:.2f})\n {"_"*60}")

    def Withdrawl(self,acc_holder,amount):
        name =self.acc_holder
        balance= self.balance
        if amount > balance:
            print(f"\n {"_"*60} \n Insufficient Funds !{name}  Account balance R{balance:.2f} \n {"_"*60}" )
        else:
            balance -= amount
            print(f"\n {"_"*60} \n Successful widthdraw {amount:.2f} from {name} Account \n Account Balance: R{balance:.2f}\n {"_"*60}")

    def check_balance(self,acc_holder):
        name =self.acc_holder
        balance =self.balance
        print(f" \n {"_"*60} {name} \n Account Balance: R{balance:.2f} \n {"_"*60}")

def main():
    user = input("Enter Name")
    obj = bankaccount(user)
    amount = float(input("Enter Desposit Amount: "))
    obj.Deposit(user,amount)
    amount1 = float(input("Enter Withdrawl Amount: "))
    obj.Withdrawl(user,amount1)
     
if __name__ == "__main__":
     main()