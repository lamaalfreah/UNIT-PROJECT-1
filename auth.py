
import json
import os

users_file = os.path.join("data", "users.json")
def load_users():
    with open(users_file, "r", encoding="utf-8") as file:
        return json.load(file)
    

def save_users(users):
    with open(users_file, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=8)

def register():
    users = load_users()

    while True:
        username = input("Enter username: ")
        if username in users:
            print("Username already exists. Try a different one.")
            continue
        password = input("Create password: ")
        confirm_password = input("Confirm password: ")

        if password == confirm_password:
            users[username] = password
            save_users(users)
            print("Account created successfully!")
            break
        else:
            print("Password do not match!")


def login():
    users = load_users()

    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print("Welcome to EduCLI system")
            break
        else:
            print("Invalid username or password")


while True:
    reg_or_login= input("Enter 'reg' for register and 'login' for login: " )

    if reg_or_login == "login":
        login()
        break
    elif reg_or_login == "reg":
        register()
        break
    else:
        print("Invalid input.")
        
