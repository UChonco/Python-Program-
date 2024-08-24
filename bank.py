class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited into {self.account_holder}'s account.")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! {self.account_holder}'s account balance is ${self.balance:.2f}.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn from {self.account_holder}'s account.")

    def show_balance(self):
        print(f"{self.account_holder}'s account balance: ${self.balance:.2f}")

def main():
    # Get user input to create an account
    account_holder = input("Enter the account holder's name: ")
    initial_balance = float(input(f"Enter the initial balance for {account_holder}'s account: "))
    account = BankAccount(account_holder, initial_balance)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.show_balance()
        elif choice == "4":
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
