"""
Python program that uses both classes and lists. This example models a Library Management System, where you can add books, view available books, and borrow or return books.

Book class: Models a book with title, author, book_id, and an is_borrowed status.

Library class: Manages a list of Book objects. It allows adding books, viewing the library collection, borrowing books, and returning books.

The program demonstrates the use of classes and a list (to store multiple book objects). Each Book object has a status (is_borrowed), which changes when the book is borrowed or returned.

"""

class Book:
    def __init__(self,book_id,title,author):
        self.title=title
        self.author =author
        self.book_id = book_id
        self.is_borrowed =False
    
    def __str__(self):
        status = "Borrowed " if self.is_borrowed else "Available"
        return f"ID: {self.book_id}, Title:{self.title}, Authors: {self.author} "
    
class Libarary:
    def __init__(self):
        self.books =[] # empty list that will store books
        
    def add_book(self,book_id,title,author):
        book = Book(book_id,title,author)
        self.books.append(book)
        print(f"Book: {title} Added Successfully")

    def view_book(self):
        if not self.books:
            print("There is no books available")
        else:
            print("Available books are :")
            for book in self.books:
                print(book)

    def borrow_book(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_borrowed:
                    book.is_borrowed =True
                    print(f"You have borrow Book ID{book_id}")
                else:
                    print(f"Sorry book is already Borrowed")
    def return_book(self,book_id):
         for book in self.books:
            if book.book_id == book_id:
                if book.is_borrowed:
                    book.is_borrowed =False
                    print(f"You have returned Book ID: {book_id}")
                else:
                    print(f"Book was not borrowed")
                return
         print(f"Book Id {book_id} not found")

lms =Libarary()
while True:

    print("\nOptions")
    print("1. Add Book")
    print("2. View Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    op = int(input("Enter your option 1-5: "))

    if op == 1:
        book_id = input("Enter book ID: ")
        book_title = input("Enter book Title: ")
        book_author = input("Enter book Author: ")
        lms.add_book(book_id,book_title,book_author)
        
    elif op == 2:
        lms.view_book()
    elif op == 3:
         book_id = input("Enter book ID: ")
         lms.borrow_book(book_id)
    elif op == 4:
         book_id = input("Enter book ID: ")
         lms.return_book(book_id)
    elif op == 5:
        print("Thank You for Visiting ...!")
        break
    else:
        print("invalid Input")

