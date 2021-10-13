#!/usr/bin/env python3

# Script Name                           401ops06.py
# Author                                Bill Kachersky
# Date of last revision                 10/11/2021
# Description of purpose                Encryption/Decryption Script


# Imports
from posixpath import dirname
import time
import os, os.path
from cryptography.fernet import Fernet


# Functions
def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        return key

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()


def key_check():
    key = load_key()
    if key == None:
        key = write_key()
    return Fernet(key)

def msg_en():
    msg = input("Type your message: ")
    f = key_check()
    message = msg.encode()
    encrypted = f.encrypt(message)
    print("Alright, encrypted! Let's see how it looks...")
    print(encrypted)

def msg_de():
    msgt = input("Type your message: ")
    time.sleep(1)
    message = str.encode(msgt)
    f = key_check()
    decrypted_encrypted = f.decrypt(message)
    print(str(decrypted_encrypted))

def file_en():
    filename = input("Please input the filepath for the file you would like to encrypt: ")
    time.sleep(1)
    f = key_check()
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def file_de():
    filename = input("Please input the filepath for the file you'd like to decrypt: ")
    time.sleep(1)
    f = key_check()
    with open(filename, "rb") as file:
        encrypted_data = file.read()          
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def recursive_en(filename):
    f = key_check()
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def recursive_de(filename):
    f = key_check()
    with open(filename, "rb") as file:
        en_data = file.read()         
    decrypted_data = f.decrypt(en_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def dir_encrypt():
    enpath = input("Enter the absolute path to the directory you want to encrypt: ")
    for dirpath, dirnames, filenames in os.walk(enpath):
        print('Directory: {:s}'.format(dirpath))
        for file in filenames:
            filename = os.path.join(dirpath,file)
            recursive_en(filename)

def dir_decrypt():
    depath = input("Enter the absolute filepath to the directory you would like to decrypt: ")
    for dirpath, dirnames, filenames in os.walk(depath):
        print('Directory: {:s}'.format(dirpath))
        for file in filenames:
            filename = os.path.join(dirpath,file)
            recursive_de(filename)



def main():
    while True:
        slct ='0'
        while slct =='0':
            print("Choose 1 of 6 choices")
            time.sleep(1)
            print("1. Encrypt a file")
            print("2. Decrypt a file")
            print("3. Encrypt a message")
            print("4. Decrypt a message")
            print("5. Recursively Encrypt a Directory")
            print("6. Recursively Decrypt a Directory")
            print("7. Exit Menu")
            time.sleep(1)

  
    ## Displays menu
            slct = input("Enter your choice [1-5]: ")
     
            if slct == "1":
                print("Alright, let's encrypt a file!")
                time.sleep(1)
                file_en()
                print("Encrypted! What next?")
                time.sleep(1)
        
            elif slct == "2":
                print("Alright, let's decrypt a file!")
                file_de()
                print("Decrypted! What next?")
                time.sleep(1)

            elif slct == "3":
                print("Alright, let's encrypt a message!")
                time.sleep(1)
                msg_en()
                print("What would you like to do next?")

            elif slct == "4":
                print("Alright, let's decrypt a message!")
                time.sleep(1)
                msg_de()
                print("What would you like to do next?")

            elif slct == "5":
                print("Alright, lettuce recursively encrypt directory!")
                dir_encrypt()
                print("What would you like to do next?")

            elif slct == "6":
                print("Alright, lettuce recursively encrypt directory!")
                dir_decrypt()
                print("What would you like to do next?")

            elif slct == "7":
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