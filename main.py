from crud import create_user, read_users, update_user, delete_user

def menu():
    while True:
        print("\n--- User Management ---")
        print("1. Create a new user")
        print("2. Read users")
        print("3. Update a user")
        print("4. Delete a user")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            read_users()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
