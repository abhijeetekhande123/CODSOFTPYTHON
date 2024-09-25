import json
import os

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.contacts = json.load(file)
        else:
            self.contacts = []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file)

    def add_contact(self, name, phone, email, address):
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(self.contacts):
                print(f"{index + 1}. {contact['name']} - {contact['phone']}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
        if results:
            for contact in results:
                print(f"{contact['name']} - {contact['phone']}")
        else:
            print("No matching contacts found.")

    def update_contact(self, index, name, phone, email, address):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = {
                'name': name,
                'phone': phone,
                'email': email,
                'address': address
            }
            self.save_contacts()
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            self.contacts.pop(index)
            self.save_contacts()
        else:
            print("Invalid contact index.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)
            print("Contact added!")
        elif choice == '2':
            print("\nContact List:")
            contact_manager.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_manager.search_contact(query)
        elif choice == '4':
            contact_manager.view_contacts()
            try:
                index = int(input("Enter the contact number to update: ")) - 1
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                contact_manager.update_contact(index, name, phone, email, address)
                print("Contact updated!")
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            contact_manager.view_contacts()
            try:
                index = int(input("Enter the contact number to delete: ")) - 1
                contact_manager.delete_contact(index)
                print("Contact deleted!")
            except ValueError:
                print("Invalid input.")
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
