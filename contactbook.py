contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

def search_contact():
    query = input("Search by name or phone: ").lower()
    found = False
    for c in contacts:
        if query in c['name'].lower() or query in c['phone']:
            print_contact(c)
            found = True
    if not found:
        print("Contact not found.")

def print_contact(contact):
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}")

def update_contact():
    query = input("Enter name of contact to update: ").lower()
    for c in contacts:
        if query == c['name'].lower():
            c['name'] = input("New name: ") or c['name']
            c['phone'] = input("New phone: ") or c['phone']
            c['email'] = input("New email: ") or c['email']
            c['address'] = input("New address: ") or c['address']
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    query = input("Enter name of contact to delete: ").lower()
    for i, c in enumerate(contacts):
        if query == c['name'].lower():
            del contacts[i]
            print("Contact deleted.")
            return
    print("Contact not found.")

def menu():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")

menu()
