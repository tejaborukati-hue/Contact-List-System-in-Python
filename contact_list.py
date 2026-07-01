import csv
import os

FILE_NAME = "contacts.csv"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

    print("Contact added successfully!\n")


def view_contacts():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\n--- Contact List ---")
        found = False
        for row in reader:
            print(f"Name : {row[0]}")
            print(f"Phone: {row[1]}")
            print(f"Email: {row[2]}")
            print("-" * 20)
            found = True

        if not found:
            print("No contacts found.")


def search_contact():
    keyword = input("Enter Name to Search: ").lower()

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        found = False
        for row in reader:
            if keyword in row[0].lower():
                print("\nContact Found")
                print(f"Name : {row[0]}")
                print(f"Phone: {row[1]}")
                print(f"Email: {row[2]}")
                found = True

        if not found:
            print("Contact not found.")


def delete_contact():
    name = input("Enter Name to Delete: ").lower()

    contacts = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        deleted = False
        for row in reader:
            if row[0].lower() != name:
                contacts.append(row)
            else:
                deleted = True

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(contacts)

    if deleted:
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


while True:
    print("\n===== Contact List System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
