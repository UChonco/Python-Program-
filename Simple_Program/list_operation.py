class List:
    def __init__(self):
        self.list = []

    def add_list(self,num):
        self.list.append(num)
        print(f"Successful added {num} to list")

    def maximum(self):
        number = self.list
        max_num = max(number)
        print(f"The maximum number in the list is {max_num}")

    def minimum(self):
        number = self.list
        min_num = min(number)
        print(f"The minimum number in the list is {min_num}")

    def sums(self):
        number = self.list
        total_sum = sum(number)
        print(f"The Total Sum of the list is {total_sum}")

    def average(self):
        number = self.list
        average = max(number) / len(number)
        print(f"The average number in the list is {average: .2f}")

    def display_list(self):
        for lists in self.list:
            print(lists)

        


def main():
    obj =List()

    while True:
        print("1. Add number")
        print("2. Find Maximum")
        print("3. Find Minimum")
        print("4. Find Sum")
        print("5. Find Average")
        print("6. Display List")
        print("7. Exit")
        
        op = input("Enter your choice: ")
        if op == "1":
            num = int(input("Enter number to list: "))
            obj.add_list(num)
        elif op == "2":
            obj.maximum() 
        elif op == "3":
            obj.minimum() 
        elif op == "4":
            obj.sums() 
        elif op == "5":
            obj.average() 
        elif op == "6":
            obj.display_list() 
        elif op == "7":
            print("Exiting Loop")
            break 
        else:
            print("Invalid Input Please valid input")
if __name__=="__main__":
    main()