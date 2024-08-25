class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"ISBN: {self.isbn}")
        print("-" * 40)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title} by {book.author}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed book: {book.title} by {book.author}")
                return
        print("Book not found.")

    def search_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("\nBooks found by title:")
            for book in found_books:
                book.display_info()
        else:
            print("No books found with that title.")

    def search_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        if found_books:
            print("\nBooks found by author:")
            for book in found_books:
                book.display_info()
        else:
            print("No books found by that author.")

    def display_books(self):
        if self.books:
            print("\nAll books in the library:")
            for book in self.books:
                book.display_info()
        else:
            print("The library is empty.")


def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book by Title")
        print("4. Search for a Book by Author")
        print("5. Display All Books")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            year = input("Enter the year of publication: ")
            isbn = input("Enter the ISBN number: ")
            book = Book(title, author, year, isbn)
            library.add_book(book)
        elif choice == "2":
            isbn = input("Enter the ISBN number of the book to remove: ")
            library.remove_book(isbn)
        elif choice == "3":
            title = input("Enter the title of the book to search: ")
            library.search_by_title(title)
        elif choice == "4":
            author = input("Enter the author of the book to search: ")
            library.search_by_author(author)
        elif choice == "5":
            library.display_books()
        elif choice == "6":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
