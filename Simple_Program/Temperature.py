def celsius_to_fahrenheits(celsius):
    F = (9/5 * celsius) + 32
    print(f"{celsius} °C in Fahrenheit is: {F} °F")

def fahrenheit_to_celsius(fahrenhiet):
    C = (fahrenhiet- 32) * 9/5
    print(f"{fahrenhiet} °F in Celsius {C} °C")

def main():

    while True:
        print(f"{"*"*20} Welcome {"*"*20}")
        print("1. Convert Celsius to fahrenheit")
        print("2. Convert fahrenheit to celsius")
        print("3. Exit")

        choice =input("Enter your Choice: ")

        if choice == "1":
            C = float(input("Enter Temperature in °C "))
            celsius_to_fahrenheits(C)
        elif choice == "2":
            F = float(input("Enter Temperature in °F "))
            fahrenheit_to_celsius(F)
        elif choice == "3":
            print("Thank you for using our system ")
            break
        else:
            print("Invalid Input ! Please enter valid input")
        
        
if __name__ == "__main__":
    main()