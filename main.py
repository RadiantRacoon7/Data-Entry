import json
import hashlib
import os
import subprocess

def registerUser(username, password):
    user_data = {
        "username": username,
        "password": hashlib.sha256(password.encode()).hexdigest()
    }
    with open("users.json", "a") as file:
        json.dump(user_data, file)
        file.write("\n")
    os.makedirs(f"./data/{username}", exist_ok=True)
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
    username = input("Enter your username: ")
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

print("Choose an operation to perform: ")
print("1. Create a file")
print("2. Edit a file")
print("3. Delete a file")

while True:
    option = input()
    if option == '1':
        while True:
            file_name = input("What is the name of the file? ")
            if not file_name.isalpha():
                print("Invalid file name, please try again.")
                continue
            break
        with open(f"./data/{username}/{file_name}.txt", "a") as file:
            file.write("")
        print("File created successfully!")
        continue
    elif option == '2':
        file_name = input("What is the name of the file you would like to edit? ")
        if not file_name.isalpha() or not os.path.exists(f"./data/{username}/{file_name}.txt"):
            continue
        subprocess.run(["nano", f"./data/{username}/{file_name}.txt"])
        continue
    elif option == '3':
        file_name = input("What is the name of the file you want to delete? ")
        if not file_name.isalpha() or not os.path.exists(f"./data/{username}/{file_name}.txt"):
            continue
        os.remove(f"./data/{username}/{file_name}.txt")
        print("File successfully deleted!")
        continue
    else:
        print("Invalid Option")
        continue
    {"username": "test", "password": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"}
