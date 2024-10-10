from mongo_connection import get_database
from validate import get_valid_input, validate_name, validate_email, validate_phone, validate_address
from datetime import datetime

db = get_database()
if db is not None:
    collection = db["user_collection"]
else:
    collection = None
    print("Failed to connect to the database.")

def create_user():
    if collection is None:
        print("No collection found. Make sure the database connection is established.")
        return

    name = get_valid_input("Enter name: ", validate_name)
    email = get_valid_input("Enter email: ", validate_email)
    phone = get_valid_input("Enter phone: ", validate_phone)
    address = get_valid_input("Enter address: ", validate_address)
    created_at = datetime.now()

    user = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "created_at": created_at
    }

    try:
        collection.insert_one(user)
        print("User created successfully.")
    except Exception as e:
        print("Error creating user:", e)

def read_users():
    if collection is None:
        print("No collection found. Make sure the database connection is established.")
        return

    users = collection.find()
    for user in users:
        print(user)

def update_user():
    if collection is None:
        print("No collection found. Make sure the database connection is established.")
        return

    name = get_valid_input("Enter name of the user to update: ", validate_name)
    user = collection.find_one({"name": name})
    if user:
        print(f"Current user details: {user}")
        field = input("Which field would you like to update (name, email, phone, address)? ")
        new_value = ""
        if field == "name":
            new_value = get_valid_input("Enter new name: ", validate_name)
        elif field == "email":
            new_value = get_valid_input("Enter new email: ", validate_email)
        elif field == "phone":
            new_value = get_valid_input("Enter new phone: ", validate_phone)
        elif field == "address":
            new_value = get_valid_input("Enter new address: ", validate_address)

        try:
            collection.update_one({"name": name}, {"$set": {field: new_value}})
            print(f"User {name}'s {field} updated successfully.")
        except Exception as e:
            print("Error updating user:", e)
    else:
        print("User not found.")

def delete_user():
    if collection is None:
        print("No collection found. Make sure the database connection is established.")
        return

    name = get_valid_input("Enter the name of the user to delete: ", validate_name)
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"User {name} deleted successfully.")
        else:
            print(f"No user found with the name {name}.")
    except Exception as e:
        print("Error deleting user:", e)
