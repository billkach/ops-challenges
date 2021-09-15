#!/usr/bin/env python3

# Script Name                           301opschallenge11.py
# Author                                Bill Kachersky
# Date of last revision                 09/14/2021
# Description of purpose                Learning how to use file handling commands

# Imports
import os
import time

# Variables


# Functions



# Main


# File Creation
file_create = open('test.txt','w')
file_create.write('This is just a test\n')
file_create.close
print()
print("Creating test.txt")
time.sleep(1)
print()


# Appending the File
file_create = open('test.txt','a')
file_create.write('But why stop there?\n')
file_create.write('Lets have some fun with this\n')
file_create.close
print()
print("Appending test.txt")
time.sleep(1)
print()

# Reading the File
file_create = open('test.txt','r')
content = file_create.readlines()
# Reading Line 3
print("Printing the third line of the file:")
print (*content[2:3])
print()
time.sleep(1)

# Removing the file
print("Removing the file now.")
time.sleep(1)
os.remove("test.txt")
print("File successfully deleted!")




# End