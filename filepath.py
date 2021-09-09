#! /usr/bin/env python3

# Script Name                           filepath.py
# Author                                Bill Kachersky
# Date of last revision                 09/08/2021
# Description of purpose                Take user input of file path and display all directories, sub directories and files in path.


# Import libraries

import os

# Declaration of variables

folder_path=input("Please specify a directory path: ")


### Read user input here into a variable

# Declaration of functions
def filepath():
    for (path, dirs, files) in os.walk(folder_path):

        print(path)

        dirs[:] = [x for x in dirs if not x.startswith('.')]

        for dir in dirs:
            print(os.path.join(path, dir))

        for file in files:
            print(os.path.join(path, file))


# Main

### Pass the variable into the function here

filepath()

# End
