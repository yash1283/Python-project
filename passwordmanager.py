import os
import json
from cryptography.fernet import Fernet
from getpass import getpass

# Step 1: Generate a Key (for the first time use)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Step 2: Load the Key from the File
def load_key():
    return open("key.key", "rb").read()

# Step 3: Encrypt a Password
def encrypt_password(key, password):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Step 4: Decrypt a Password
def decrypt_password(key, encrypted_password):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

# Step 5: Add a New Password
def add_password(key, account, password):
    encrypted_password = encrypt_password(key, password)
    # Store the encrypted password in a file
    with open("passwords.json", "r+") as file:
        data = json.load(file)
        data[account] = encrypted_password.decode()  # Save as string for JSON compatibility
        file.seek(0)
        json.dump(data, file, indent=4)

# Step 6: Retrieve a Password
def retrieve_password(key, account):
    with open("passwords.json", "r") as file:
        data = json.load(file)
        encrypted_password = data.get(account, None)
        if encrypted_password:
            return decrypt_password(key, encrypted_password.encode())
        else:
            return None

# Main function to handle user interaction
def main():
    # Load or generate the encryption key
    if not os.path.exists("key.key"):
        generate_key()
    key = load_key()

    # Load or create the password file
    if not os.path.exists("passwords.json"):
        with open("passwords.json", "w") as file:
            json.dump({}, file)

    # Ask for the master password
    master_password = getpass("Enter your master password: ")

    # Verify master password (simple version for this example)
    # In production, use hashed password and compare securely.
    if master_password != "your_master_password":  # Replace with hashed version
        print("Invalid master password!")
        return

    while True:
        print("\nOptions: add, retrieve, quit")
        choice = input("What would you like to do? ").lower()

        if choice == "add":
            account = input("Enter the account name: ")
            password = getpass("Enter the password: ")
            add_password(key, account, password)
            print(f"Password for {account} added.")
        elif choice == "retrieve":
            account = input("Enter the account name: ")
            password = retrieve_password(key, account)
            if password:
                print(f"The password for {account} is {password}")
            else:
                print(f"No password found for {account}")
        elif choice == "quit":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
