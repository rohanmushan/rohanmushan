# Implement a simple address book using a dictionary.
address_book={}
def add_contact(name, address, phone):
    address_book[name]={'Address':address,'Phone':phone}
    print(f"Contact'{name}'added to the address book.")

def view_contact(name):
    if name in address_book:
        contact_info = address_book[name]
        print(f"Contact:{name}")
        print(f"Address:{contact_info['Address']}")
        print(f"Phone:{contact_info['Phone']}")
    else:
        print(f"'{name}'not found in the address book.")

def list_contacts():
    print("Address Book:")
    for name, contact_info in address_book.items():
        print(f"Name: {name},Address:{contact_info['Address']},Phone:{contact_info['Phone']}")

def remove_contact(name):
    if name in address_book:
        del address_book[name]
        print(f"Contact '{name}' removed from the address book.")
    else:
        print(f"'{name}' not found in the address book.")

while True:
    print("\nAddress Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. List Contacts")
    print("4. Remove Contact")
    print("5. Quit")

    choice=input("Enter your choice (1/2/3/4/5): ")

    if choice=='1':
        name=input("Enter the name: ")
        address=input("Enter the address: ")
        phone=input("Enter the phone number: ")
        add_contact(name, address, phone)
    elif choice=='2':
        name=input("Enter the name to view: ")
        view_contact(name)
    elif choice=='3':
        list_contacts()
    elif choice=='4':
        name=input("Enter the name to remove: ")
        remove_contact(name)
    elif choice=='5':
        break
    else:
        print("Invalid choice. Please select a valid option.")
