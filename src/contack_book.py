
import os
import pickle

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None

class ContactBook:
    def __init__(self, filename="contacts.pkl"):
        self.head = None
        self.filename = filename
        self.load_contacts()

    def add_contact(self, name, phone):
        new_contact = Contact(name, phone)
        if self.head is None or self.head.name.lower() > name.lower():
            new_contact.next = self.head
            self.head = new_contact
        else:
            current = self.head
            while current.next and current.next.name.lower() < name.lower():
                current = current.next
            new_contact.next = current.next
            current.next = new_contact
        self.save_contacts()
        print(f"Contact {name} saved.")

    def search_contact(self, name):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                print(f"Found: {current.name} - {current.phone}")
                return
            current = current.next
        print("Contact not found.")

    def update_contact(self, name, new_phone):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                current.phone = new_phone
                self.save_contacts()
                print("Contact updated.")
                return
            current = current.next
        print("Contact not found.")

    def delete_contact(self, name):
        prev = None
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.save_contacts()
                print("Contact deleted.")
                return
            prev = current
            current = current.next
        print("Contact not found.")

    def display_contacts(self):
        current = self.head
        if not current:
            print("No contacts to display.")
            return
        while current:
            print(f"{current.name} - {current.phone}")
            current = current.next

    def save_contacts(self):
        contacts = []
        current = self.head
        while current:
            contacts.append((current.name, current.phone))
            current = current.next
        with open(self.filename, "wb") as f:
            pickle.dump(contacts, f)

    def load_contacts(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "rb") as f:
            contacts = pickle.load(f)
            for name, phone in reversed(contacts):
                self.add_contact(name, phone)

def main():
    cb = ContactBook()
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Display all")
        print("6. Quit")
        choice = input("Choice: ")
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            cb.add_contact(name, phone)
        elif choice == "2":
            name = input("Name to search: ")
            cb.search_contact(name)
        elif choice == "3":
            name = input("Name to update: ")
            phone = input("New phone: ")
            cb.update_contact(name, phone)
        elif choice == "4":
            name = input("Name to delete: ")
            cb.delete_contact(name)
        elif choice == "5":
            cb.display_contacts()
        elif choice == "6":
            print("Bye")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()


#Output

--- Contact Book Menu ---
1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. Display all
6. Quit
Choice: 1
Name: Alice
Phone: 12345
Contact Alice saved.

--- Contact Book Menu ---
1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. Display all
6. Quit
Choice: 1
Name: Bob
Phone: 67890
Contact Bob saved.

--- Contact Book Menu ---
1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. Display all
6. Quit
Choice: 5
Alice - 12345
Bob - 67890

--- Contact Book Menu ---
1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. Display all
6. Quit
Choice: 2
Name to search: Alice
Found: Alice - 12345

--- Contact Book Menu ---
1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. Display all
6. Quit
Choice: 3
Name to update: Bob
New phone: 22222
Contact updated.

--- Contact Book Menu ---
1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. Display all
6. Quit
Choice: 4
Name to delete: Alice
Contact deleted.

--- Contact Book Menu ---
1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. Display all
6. Quit
Choice: 6
Bye
