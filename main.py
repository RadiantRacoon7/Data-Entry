import json
import hashlib
import os
import subprocess

def registerUser(username, password):
    try:
        with open("users.json", "r") as file:
            for line in file:
                user_data = json.loads(line)
                if user_data.get("username") == username:
                    print("Username already exists.")
                    return
    except FileNotFoundError:
        pass

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

while True:
    user_files = [
        name[:-4]
        for name in os.listdir(f"./data/{username}")
        if name.endswith(".txt") and os.path.isfile(f"./data/{username}/{name}")
    ]
    print("Files:")
    for file_name in user_files:
        print(f" - {file_name}")
    print("Choose an operation to perform: ")
    print("1. Create a file")
    print("2. Edit a file")
    print("3. Delete a file")
    print("4. Exit")
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
    elif option == '4':
        print("Exiting the program.")
        quit()
    else:
        print("Invalid Option")
        continue
