import os
from datetime import datetime

def load_contacts():
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
            return {line.split(',')[0]: {"phone": line.split(',')[1], "email": line.split(',')[2], "date_added": line.split(',')[3].strip()} for line in lines}
    return {}

def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for name, details in contacts.items():
            file.write(f"{name},{details['phone']},{details['email']},{details['date_added']}\n")

def backup_contacts(contacts):
    with open("contacts_backup.txt", "w") as file:
        for name, details in contacts.items():
            file.write(f"{name},{details['phone']},{details['email']},{details['date_added']}\n")
    print("Contacts backed up successfully!")

def search_contact(contacts):
    search_name = input("Enter the name of the contact to search: ")
    if search_name in contacts:
        details = contacts[search_name]
        print(f"Name: {search_name}, Phone: {details['phone']}, Email: {details['email']}, Date Added: {details['date_added']}")
    else:
        print("Contact not found!")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    date_added = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    contacts[name] = {"phone": phone, "email": email, "date_added": date_added}
    save_contacts(contacts)

def view_contacts(contacts):
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Date Added: {details['date_added']}")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name] = {"phone": phone, "email": email, "date_added": contacts[name]['date_added']}
        save_contacts(contacts)
    else:
        print("Contact not found!")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
    else:
        print("Contact not found!")

def main():
    contacts = load_contacts()
    while True:
        choice = input("\n1. Add Contact\n2. View Contacts\n3. Update Contact\n4. Delete Contact\n5. Search Contact\n6. Backup Contacts\n7. Exit\nEnter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            search_contact(contacts)
        elif choice == "6":
            backup_contacts(contacts)
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
