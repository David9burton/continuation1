import os

def load_contacts():
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
            return {line.split(',')[0]: {"phone": line.split(',')[1], "email": line.split(',')[2].strip()} for line in lines}
    return {}

def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for name, details in contacts.items():
            file.write(f"{name},{details['phone']},{details['email']}\n")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)

def view_contacts(contacts):
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name] = {"phone": phone, "email": email}
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
        choice = input("\n1. Add Contact\n2. View Contacts\n3. Update Contact\n4. Delete Contact\n5. Exit\nEnter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
