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
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")
        continue

while True:
    username = input("Enter your username (or type 'exit' to quit): ")
    if not username.isalpha():
        print("Invalid username. Please use only letters.")
        continue

    password = input("Enter your password: ")
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    try:
        with open("users.json", "r") as file:
            for line in file:
                user_data = json.loads(line)
                if user_data.get("username") == username and user_data.get("password") == password_hash:
                    print("Login successful.")
                    break
            else:
                print("Invalid username or password.")
                continue
            break
    except FileNotFoundError:
        print("Invalid username or password.")

