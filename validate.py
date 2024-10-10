import re

def validate_name(name):
    return len(name.strip()) > 0

def validate_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def validate_phone(phone):
    return phone.isdigit() and len(phone) >= 10

def validate_address(address):
    return len(address.strip()) > 0

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")
