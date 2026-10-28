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

while True:
    username = input("Enter your username (or type 'exit' to quit): ")
    if not username.isalpha():
        print("Invalid username. Please use only letters.")
        continue

    password = input("Enter your password: ")