import os

CONTACTS_FILE = 'contacts.txt'

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address (optional): ")
    with open(CONTACTS_FILE, 'a') as f:
        f.write(f"{name},{phone},{email}\n")
    print("Contact added successfully.\n")

def view_contacts():
    if not os.path.exists(CONTACTS_FILE):
        print("No contacts found.\n")
        return
    with open(CONTACTS_FILE, 'r') as f:
        contacts = f.readlines()
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    print("Name\t\tPhone\t\tEmail")
    print("-" * 40)
    for contact in contacts:
        name, phone, email = contact.strip().split(',')
        print(f"{name}\t\t{phone}\t\t{email}")
    print()

def search_contacts():
    search_term = input("Enter name or number to search: ").lower()
    found = False
    with open(CONTACTS_FILE, 'r') as f:
        for contact in f:
            if search_term in contact.lower():
                name, phone, email = contact.strip().split(',')
                print(f"Found: Name: {name}, Phone: {phone}, Email: {email}")
                found = True
    if not found:
        print("Contact not found.\n")

def menu():
    while True:
        print("== Contact Book Menu ==")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    menu() 