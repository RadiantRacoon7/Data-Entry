import json
import hashlib

def registerUser(username, password):
    user_data = {
        "username": username,
        "password": hashlib.sha256(password.encode()).hexdigest()
    }
    with open("users.json", "a") as file:
        json.dump(user_data, file)
        file.write("\n")
    print(f"User {username} registered successfully.")

print("DATA ENTRY PROGRAM ALPHA")

print("Please choose an option:")
print("1. Register")
print("2. Login")
while True:
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        registerUser(username, password)
    elif choice == '2':
        print("Login functionality is not implemented yet.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

while True:
    username = input("Enter your username (or type 'exit' to quit): ")
    if not username.isalpha():
        print("Invalid username. Please use only letters.")
        continue

    password = input("Enter your password: ")