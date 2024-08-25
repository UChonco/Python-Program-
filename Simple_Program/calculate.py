def add(num1,num2):
   answer= num1 + num2
   print(f"{num1} + {num2} = {answer}")


def subtract(num1,num2):
    answer = num1 - num2
    print(f"{num1} - {num2} = {answer}")


def multiply(num1,num2):
    answer = num1 * num2
    print(f"{num1} * {num2} = {answer}")


def divide(num1,num2):
    answer = num1 / num2
    print(f"{num1} / {num2} = {answer}")


num1 = int(input("Enter  First number: "))
op =input("Select an operation (+,-,*,/) : ")
num2 = int(input("Enter  Second number: "))

if op =="+":
    add(num1,num2)
elif op =="-":
    subtract(num1,num2)
elif op =="*":
    multiply(num1,num2)
elif op =="/":
    divide(num1,num2)
else:
    print("Invalid Operation ")
