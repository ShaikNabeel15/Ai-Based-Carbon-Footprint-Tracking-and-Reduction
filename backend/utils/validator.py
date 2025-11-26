import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.search(regex, email)

def validate_password(password):
    # Basic validation: at least 6 characters
    return len(password) >= 6

def validate_factory_id(factory_id):
    return len(factory_id) > 0
