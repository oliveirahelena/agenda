# Lista para armazenar os contatos
contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    favorite = False
    contacts.append({'name': name, 'phone': phone, 'email': email, 'favorite': favorite})
    print("Contact added successfully!")

def list_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Favorite: {'Yes' if contact['favorite'] else 'No'}")

def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    for contact in contacts:
        if contact['name'] == name:
            new_name = input("Enter new name (or leave blank): ")
            new_phone = input("Enter new phone (or leave blank): ")
            new_email = input("Enter new email (or leave blank): ")
            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def toggle_favorite():
    name = input("Enter the name of the contact to toggle favorite status: ")
    for contact in contacts:
        if contact['name'] == name:
            contact['favorite'] = not contact['favorite']
            print("Favorite status changed!")
            return
    print("Contact not found.")

def list_favorites():
    favorites = [contact for contact in contacts if contact['favorite']]
    if not favorites:
        print("No favorite contacts.")
    else:
        for contact in favorites:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Favorite: {'Yes' if contact['favorite'] else 'No'}")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for i in range(len(contacts)):
        if contacts[i]['name'] == name:
            del contacts[i]
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    while True:
        print("\n1. Add Contact\n2. List Contacts\n3. Edit Contact\n4. Toggle Favorite\n5. List Favorites\n6. Delete Contact\n7. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            list_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            toggle_favorite()
        elif choice == '5':
            list_favorites()
        elif choice == '6':
            delete_contact()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
