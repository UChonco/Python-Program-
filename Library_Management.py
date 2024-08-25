class Book:
    def __init__(self,title,author,year,isbn):
        self.title =title
        self.author = author
        self.year = year
        self.isbn = isbn
    def display_info(self):
        print(f"{"*"*20} Book Information {"*"*20}")
        print(f"Title: {self.title} \n Author: {self.author} \n Year: {self.year} Isbn: {self.isbn}")
class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
        print(f"Book {book.title}by {book.author} Successful Added ")
    def remove_book():
        pass
    def search_by_title():
        pass
    def search_by_author():
        pass
    def display_book():
        pass

def main():
    
    is_still_running =True
    while is_still_running:
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search for Book by title")
        print("4. Search for Book by author")
        print("5. Display All bbok")
        print("6. Exit")

        choice = input("Enter your choice 1-6 : ")
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            print("Thank you for visiting our program")
            break
        else:
            print("Invalid Input ! Please Enter valid input")
if __name__ == "__main__":
    main()