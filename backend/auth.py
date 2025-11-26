from backend.database import get_factories, save_factories
from backend.models.user_model import User
from backend.utils.hashing import hash_password, check_password
from backend.utils.validator import validate_email, validate_password, validate_factory_id

def signup_user(factory_name, factory_id, email, password):
    if not validate_email(email):
        return {"error": "Invalid email format"}
    if not validate_password(password):
        return {"error": "Password must be at least 6 characters"}
    if not validate_factory_id(factory_id):
        return {"error": "Factory ID is required"}

    factories_data = get_factories()
    
    # Check if user already exists
    for f in factories_data:
        if f['factory_id'] == factory_id or f['mail_id'] == email:
            return {"error": "User already exists"}

    hashed_pw = hash_password(password)
    new_user = User(factory_name, factory_id, email, hashed_pw)
    
    factories_data.append(new_user.to_dict())
    save_factories(factories_data)
    
    return {"success": "User created successfully"}

def login_user(email, password):
    factories_data = get_factories()
    
    for f in factories_data:
        if f['mail_id'] == email:
            if check_password(password, f['password']):
                return {"success": "Login successful", "user": f}
            else:
                return {"error": "Invalid password"}
    
    return {"error": "User not found"}
