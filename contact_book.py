import json
from pathlib import Path

file = Path(__file__).with_name("contacts.json")


def load_contacts():
    if file.exists():
        try:
            with open(file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return []


def save_contacts(contacts):
    with open(file, "w") as f:
        json.dump(contacts, f, indent=4)


def find_contact(contacts, contact_id):
    for contact in contacts:
        if contact["id"] == contact_id:
            return contact
    return None


def add_contact(contacts):
    print("\nAdd Contact")

    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    if not name or not phone:
        print("Name and phone are required.")
        return

    new_id = 1
    if contacts:
        new_id = max(contact["id"] for contact in contacts) + 1

    contacts.append({
        "id": new_id,
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    save_contacts(contacts)
    print("Contact added.")


def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\nContact List")
    print("-" * 40)

    for contact in contacts:
        print("ID:", contact["id"])
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Address:", contact["address"])
        print("-" * 40)


def search_contact(contacts):
    search = input("Enter name or phone number: ").lower().strip()

    found = False

    for contact in contacts:
        if (
            search in contact["name"].lower()
            or search in contact["phone"].lower()
        ):
            print("\nID:", contact["id"])
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            print("-" * 40)
            found = True

    if not found:
        print("No contact found.")


def update_contact(contacts):
    try:
        contact_id = int(input("Enter contact ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    contact = find_contact(contacts, contact_id)

    if not contact:
        print("Contact not found.")
        return

    name = input(f'Name [{contact["name"]}]: ').strip()
    phone = input(f'Phone [{contact["phone"]}]: ').strip()
    email = input(f'Email [{contact["email"]}]: ').strip()
    address = input(f'Address [{contact["address"]}]: ').strip()

    if name:
        contact["name"] = name
    if phone:
        contact["phone"] = phone
    if email:
        contact["email"] = email
    if address:
        contact["address"] = address

    save_contacts(contacts)
    print("Contact updated.")


def delete_contact(contacts):
    try:
        contact_id = int(input("Enter contact ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    contact = find_contact(contacts, contact_id)

    if not contact:
        print("Contact not found.")
        return

    confirm = input(
        f'Delete {contact["name"]}? (y/n): '
    ).lower().strip()

    if confirm == "y":
        contacts.remove(contact)
        save_contacts(contacts)
        print("Contact deleted.")
    else:
        print("Deletion cancelled.")


def main():
    contacts = load_contacts()

    while True:
        print("""
========== CONTACT BOOK ==========

1. Add contact
2. View contacts
3. Search contact
4. Update contact
5. Delete contact
6. Exit
""")

        choice = input("Enter your choice: ").strip()

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
