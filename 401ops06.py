#!/usr/bin/env python3

# Script Name                           401ops06.py
# Author                                Bill Kachersky
# Date of last revision                 10/11/2021
# Description of purpose                Encryption/Decryption Script


# Imports
from cryptography.fernet import Fernet


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

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
         file.write(encrypted_data)


def stren():
    msg = input("Type your message: ")
    message = msg.encode()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    print("Alright, encrypted! Let's see how it looks...")
    print(encrypted)






def main():
    while True:
        slct ='0'
        while slct =='0':
            print("Main Choice: Choose 1 of 5 choices")
            print("Choose 1 for something")
            print("Choose 2 for something")
            print("Choose 3 for something")
            print("Choose 4 for something")
            print("Choose 5 to go to another menu")

  
    ## Displays menu
            slct = input("Enter your choice [1-5]: ")
     
            if slct == "1":     
                print("Alright, let's encrypt a file!")
                write_key()
                key = load_key()
                filename = input("Please input the filename of the file in the current directory you would like to encrypt: ")
                encrypt(filename, key)
        
        
            elif slct == "2":
                print("Alright, let's decrypt a file!")
        ## You can add your code or functions here
            elif slct==3:
                print("Alright, let's encrypt a message!")
                write_key()
                key = load_key()
                

            elif slct==4:
                print("Alright, let's decrypt a message!")
        ## You can add your code or functions here
            elif slct==5:
                print("See ya!")
        ## You can add your code or functions here
                loop=False # This will make the while loop to end as not value of loop is set to False
            else:
        # Any integer inputs other than values 1-5 we print an error message
                input("Wrong option selection. Enter any key to try again..")


main()