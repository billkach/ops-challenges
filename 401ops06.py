#!/usr/bin/env python3

# Script Name                           401ops06.py
# Author                                Bill Kachersky
# Date of last revision                 10/11/2021
# Description of purpose                Encryption/Decryption Script


# Imports
import time
from cryptography.fernet import Fernet


# Functions
def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def main():
    while True:
        slct ='0'
        while slct =='0':
            print("Choose 1 of 5 choices")
            time.sleep(1)
            print("1. Encrypt a file")
            print("2. Decrypt a file")
            print("3. Encrypt a message")
            print("4. Decrypt a message")
            print("5. Exit Menu")
            time.sleep(1)

  
    ## Displays menu
            slct = input("Enter your choice [1-5]: ")
     
            if slct == "1":
                key = load_key()
                f = Fernet(key)
                print("Alright, let's encrypt a file!")
                time.sleep(1)
                filename = input("Please input the filename of the file in the current directory you would like to encrypt: ")
                time.sleep(1)
                with open(filename, "rb") as file:
                    file_data = file.read()
                    encrypted_data = f.encrypt(file_data)
                with open(filename, "wb") as file:
                    file.write(encrypted_data)
                    time.sleep(1)
                print("Encrypted! What next?")
                time.sleep(1)
                main()
        
            elif slct == "2":
                key = load_key()
                f = Fernet(key)
                print("Alright, let's decrypt a file!")
                write_key()
                key = load_key()
                filename = input("Please input the filename of the file in the current directory you would like to decrypt: ")
                time.sleep(1)
                with open(filename, "rb") as file:
                    encrypted_data = file.read()
                    decrypted_data = f.decrypt(encrypted_data)
                with open(filename, "wb") as file:
                    file.write(decrypted_data)
                time.sleep(1)
                print("Decrypted! What next?")
                time.sleep(1)
                main()

            elif slct == "3":
                key = load_key()
                f = Fernet(key)
                print("Alright, let's encrypt a message!")
                time.sleep(1)
                msg = input("Type your message: ")
                time.sleep(1)
                message = msg.encode()
                encrypted = f.encrypt(message)
                print("Alright, encrypted! Let's see how it looks...")
                print(encrypted)
                dcrpt = input("Would you like to decrypt this message too? Y/N: ")
                if dcrpt == "Y":
                    de = f.decrypt(encrypted)
                    print(de)
                else:
                     print("What would you like to do next?")
                     main()
                

            elif slct == "4":
                key = load_key()
                f = Fernet(key)
                print("Alright, let's decrypt a message!")
                time.sleep(1)
                print("First, we need to encrypt a message, though :D")
                time.sleep(1)
                msgt = input("Type your message: ")
                time.sleep(1)
                message = msgt.encode()
                encrypted = f.encrypt(message)
                print("Alright, encrypted! Let's see how it looks...")
                print(encrypted)
                print("Encrypted!")
                time.sleep(1)
                print("Now, we'll decrypt it.")
                time.sleep(1)
                decrypted_encrypted = f.decrypt(encrypted)
                print(decrypted_encrypted)
                time.sleep(1)
                print("What would you like to do next?")
                main()

            elif slct == "5":
                time.sleep(1)
                print("See ya!")
                exit()

            else:
        # Any integer inputs other than values 1-5 we print an error message
                input("Wrong option selection. Enter any key to try again..")


# Main

write_key()
print("Welcome to the encrypt/decrypt-ionary!!!")
time.sleep(1)
main()

# End