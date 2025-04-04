import json
import bcrypt
import os
from protection_utils import sanitize_input, trapdoor_check
from otp_utils import generate_otp, send_otp, verify_otp

USER_DB = "user_data.json"

# Ensure the user_data file exists
def load_users():
    if not os.path.exists(USER_DB):
        return {}
    with open(USER_DB, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f, indent=4)

# Register user
def register_user(username, password, email):
    username = sanitize_input(username)
    trapdoor_check(username)

    users = load_users()
    if username in users:
        return False, "User already exists."

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    users[username] = {
        "password": hashed_pw,
        "email": email
    }
    save_users(users)
    return True, "User registered successfully."

# Authenticate user with password + OTP
def authenticate_user(username, password):
    username = sanitize_input(username)
    trapdoor_check(username)

    users = load_users()
    if username not in users:
        return False, "User not found."

    stored_pw = users[username]["password"].encode()
    if not bcrypt.checkpw(password.encode(), stored_pw):
        return False, "Invalid password."

    # Step 2: OTP verification
    email = users[username]["email"]
    otp = generate_otp()
    send_otp(email, otp)

    print(f"OTP sent to {email}.")
    user_input = input("Enter the OTP: ")
    if verify_otp(user_input.strip(), otp):
        return True, "Authentication successful!"
    else:
        return False, "OTP verification failed."
