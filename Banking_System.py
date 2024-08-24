class bankaccount:
    def __init__(self,acc_holder,balance):
        self.acc_holder = acc_holder
        self.balance = balance

    def Deposit(self,amount ):
        name = self.acc_holder
        if amount >0:
            self.balance += amount
            print(f"\n {"_"*60} \n Successful Deposit R{amount:.2f} from {name} Account \n(Account Balance : R{self.balance:.2f})\n {"_"*60}")
        else:
            print("invalid amount ! Please Enter valid amout")

    def Withdrawl(self,amount):
        name =self.acc_holder

        if amount > self.balance:
            print(f"\n {"_"*60} \n Insufficient Funds !{name}  Account balance R{self.balance:.2f} \n {"_"*60}" )
        elif amount <=0:
            print("invalid amount! Please  valid amount")
        else:
            self.balance -= amount
            print(f"\n {"_"*60} \n Successful widthdraw {amount:.2f} from {name} Account \n Account Balance: R{self.balance:.2f}\n {"_"*60}")

    def check_balance(self):
        name =self.acc_holder
     
        print(f" \n {"_"*60} \n {name} Account Balance: R{self.balance:.2f} \n {"_"*60}")


def main():


   user = input("Enter account holder name : ")
   balance = 0
   obj = bankaccount(user,balance)
       
   while True:
     
 

       print(f"{"_"*60}")
       print("1. Desposit")
       print("2. withdraw")
       print("3. Show Balance")
       print("4. Exit")
       print(f"{"_"*60}")
       
       choice = input("Enter your choice 1-4: ")
       if choice == "1":
           amount = float(input("Enter deposit amount :R"))
           obj.Deposit(amount)
       elif choice == "2":
            amount =float(input("Enter withdraw amount :R "))
            obj.Withdrawl(amount) 
       elif choice == "3":
            obj.check_balance()
       elif choice == "4":
            print("Thank You for banking with us ...")
            break
       
if __name__ == "__main__":
    main()
          
      