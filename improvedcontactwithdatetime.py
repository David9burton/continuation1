import datetime

def load_contacts():
    # ... [No changes here]

def save_contacts(contacts):
    # ... [No changes here]

def add_contact(contacts):
    # ... [No changes here]

def view_contacts(contacts):
    # Sort contacts by name before displaying
    sorted_contacts = dict(sorted(contacts.items()))
    for name, details in sorted_contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Date Added: {details['date']}, Notes: {details['notes']}")

def search_contact(contacts):
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Date Added: {details['date']}, Notes: {details['notes']}")
    else:
        print("Contact not found!")

def update_contact(contacts):
    # ... [No changes here]

def delete_contact(contacts):
    # ... [No changes here]

def main():
    contacts = load_contacts()
    while True:
        choice = input("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit\nEnter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
