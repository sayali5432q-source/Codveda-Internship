def encrypt_file():
    filename = input("Enter the file name to encrypt: ")

    try:
        with open(filename, "r") as file:
            data = file.read()

        encrypted_data = ""

        for char in data:
            encrypted_data += chr(ord(char) + 3)

        with open("encrypted_file.txt", "w") as file:
            file.write(encrypted_data)

        print("File encrypted successfully!")

    except FileNotFoundError:
        print("File not found!")


def decrypt_file():
    filename = input("Enter the encrypted file name: ")

    try:
        with open(filename, "r") as file:
            data = file.read()

        decrypted_data = ""

        for char in data:
            decrypted_data += chr(ord(char) - 3)

        with open("decrypted_file.txt", "w") as file:
            file.write(decrypted_data)

        print("File decrypted successfully!")

    except FileNotFoundError:
        print("File not found!")


while True:
    print("\n--- File Encryption and Decryption ---")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        encrypt_file()

    elif choice == "2":
        decrypt_file()

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")