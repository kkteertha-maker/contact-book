while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        file = open("contacts.txt", "a")
        file.write(f"{name},{phone}\n")
        file.close()

        print("✅ Contact Saved Successfully!")

    elif choice == "2":
        try:
            file = open("contacts.txt", "r")
            contacts = file.read()

            if contacts == "":
                print("No contacts found.")
            else:
                print("\n===== CONTACTS =====")
                print(contacts)

            file.close()

        except FileNotFoundError:
            print("No contacts found.")

    elif choice == "3":
        search = input("Enter name to search: ")

        try:
            file = open("contacts.txt", "r")
            found = False

            for line in file:
                if search.lower() in line.lower():
                    print("Found:", line.strip())
                    found = True

            file.close()

            if not found:
                print("❌ Contact not found.")

        except FileNotFoundError:
            print("No contacts found.")

    elif choice == "4":
        update_name = input("Enter name to update: ")

        try:
            file = open("contacts.txt", "r")
            contacts = file.readlines()
            file.close()

            file = open("contacts.txt", "w")
            found = False

            for line in contacts:
                name, phone = line.strip().split(",")

                if name.lower() == update_name.lower():
                    new_phone = input("Enter new phone number: ")
                    file.write(f"{name},{new_phone}\n")
                    found = True
                else:
                    file.write(line)

            file.close()

            if found:
                print("✅ Contact Updated Successfully!")
            else:
                print("❌ Contact not found.")

        except FileNotFoundError:
            print("No contacts found.")

    elif choice == "5":
        delete_name = input("Enter name to delete: ")

        try:
            file = open("contacts.txt", "r")
            contacts = file.readlines()
            file.close()

            file = open("contacts.txt", "w")
            found = False

            for line in contacts:
                name, phone = line.strip().split(",")

                if name.lower() == delete_name.lower():
                    found = True
                else:
                    file.write(line)

            file.close()

            if found:
                print("🗑️ Contact Deleted Successfully!")
            else:
                print("❌ Contact not found.")

        except FileNotFoundError:
            print("No contacts found.")

    elif choice == "6":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid Choice!")