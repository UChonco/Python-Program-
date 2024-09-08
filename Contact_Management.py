"""
 Python program that uses both classes and dictionaries. This program models a Contact Manager, where you can add, view, and search for contacts by their name.

"""
class Contact :
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"Name {self.name}| Phone: {self.phone}| Email: {self.email}"

class ContactManager:
    def __init__(self):

        self.contacts = {"name":"values"}
    def add_contact(self,name,phone,email):
        if name in self.contacts:
            print(f"Contact with name '{name}' exists")
        else:
            contact = (name,phone,email)
            self.contacts.update({"name":contact})
            print("Contact successful added")
    def view_contact(self):
        if not self.contacts:
            print("No Contacts to display")
        else:
            print("Your Contact:")
            for contact in self.contacts.values():
                print(contact)

    def search_contact(self,name):
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print(f"No contact found with the name '{name}'")

cm =ContactManager()
while True:

    print("\nOptions")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search for contact")
    print("4. Exit")

    op = int(input("Enter your option 1-4: "))

    if op == 1:
        name = input("Enter contact name: ")
        phone = input("Enter contact number: ")
        email= input("Enter contact email: ")
        cm.add_contact(name,phone,email)
        
    elif op == 2:
        cm.view_contact()
    elif op == 3:
         name = input("Enter contact name: ")
         cm.search_contact(name)
    elif op == 4:
        print("Thank You for Visiting ...!")
        break
    else:
        print("invalid Input")