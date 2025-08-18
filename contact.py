import json

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def display(self):
        print(f"\n📇 Name: {self.name}")
        print(f"📞 Phone: {self.phone}")
        print(f"📧 Email: {self.email}")
        print(f"🏠 Address: {self.address}")

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if any(c.name.lower() == contact.name.lower() for c in self.contacts):
            print(f"⚠️ Contact with name '{contact.name}' already exists.")
        else:
            self.contacts.append(contact)
            print(f"✅ {contact.name} has been added.")

    def view_contacts(self):
        if not self.contacts:
            print("📭 No contacts to display.")
        else:
            print("\n📒 All Contacts:")
            for contact in self.contacts:
                contact.display()

    def search_contact(self, search_term):
        matches = [c for c in self.contacts if search_term.lower() in c.name.lower()]
        if matches:
            print("\n🔍 Matching Contacts:")
            for contact in matches:
                contact.display()
        else:
            print("❌ No matching contacts found.")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"\n🛠️ Updating contact: {contact.name}")
                new_phone = input("New phone (leave blank to keep current): ")
                new_email = input("New email (leave blank to keep current): ")
                new_address = input("New address (leave blank to keep current): ")

                if new_phone: contact.phone = new_phone
                if new_email: contact.email = new_email
                if new_address: contact.address = new_address

                print(f"✅ {contact.name}'s details updated.")
                return
        print("❌ Contact not found.")

    def delete_contact(self, name):
        original_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]
        if len(self.contacts) < original_count:
            print(f"🗑️ {name} has been deleted.")
        else:
            print("❌ Contact not found.")

    def save_to_file(self, filename="contacts.json"):
        with open(filename, "w") as f:
            json.dump([c.__dict__ for c in self.contacts], f)
        print("💾 Contacts saved.")

    def load_from_file(self, filename="contacts.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.contacts = [Contact(**item) for item in data]
            print("📂 Contacts loaded.")
        except FileNotFoundError:
            print("📁 No saved contacts found.")

def main():
    book = ContactBook()
    book.load_from_file()

    while True:
        print("\n📱 Contact Book Menu:")
        print("1️⃣ Add Contact")
        print("2️⃣ View Contacts")
        print("3️⃣ Search Contact")
        print("4️⃣ Update Contact")
        print("5️⃣ Delete Contact")
        print("6️⃣ Save & Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            book.add_contact(Contact(name, phone, email, address))

        elif choice == "2":
            book.view_contacts()

        elif choice == "3":
            term = input("Search by name: ")
            book.search_contact(term)

        elif choice == "4":
            name = input("Enter name to update: ")
            book.update_contact(name)

        elif choice == "5":
            name = input("Enter name to delete: ")
            book.delete_contact(name)

        elif choice == "6":
            book.save_to_file()
            print("👋 Goodbye!")
            break

        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
