import json
import os
import hashlib
import getpass

users_file = os.path.join("data", "users.json")

def hash_password(password: str) -> str:
    """
    Returns a SHA-256 hash of the given password.

    Args:
        password (str): Plain text password.

    Returns:
        str: Hashed password.
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def load_users() -> dict[str, str]:
    """
    Loads users from the JSON file.

    Returns:
        dict: A dictionary mapping usernames to passwords.
    """
    try:
        with open(users_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(e)
        return {}

def save_users(users: dict[str, str]) -> None:
    """
    Saves the given users dictionary to the JSON file.

    Args:
        users (dict): A dictionary mapping usernames to passwords.
    """
    with open(users_file, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=8)

def register() -> None:
    """
    Registers a new user by prompting for username and password.
    Saves the user data to the JSON file.
    """
    users = load_users()

    while True:
        username = input("Enter username: ")
        if username in users:
            print("Username already exists. Try a different one.")
            continue
        password = getpass.getpass("Create password: ")
        confirm_password = getpass.getpass("Confirm password: ")

        if password == confirm_password:
            hashed = hash_password(password)
            users[username] = hashed
            save_users(users)
            print("Account created successfully!")
            break
        else:
            print("Password do not match!")

def login() -> None:
    """
    Logs in an existing user by verifying their credentials.
    """
    users = load_users()

    while True:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        hashed = hash_password(password)

        if username in users and users[username] == hashed:
            print("Welcome to EduCLI system")
            break
        else:
            print("Invalid username or password")