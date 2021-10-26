#!/usr/bin/env python3

# Script Name                           401ops16.py
# Author                                Bill Kachersky
# Date of last revision                 10/25/2021
# Description of purpose                Brute Force Tool Part 1

# Resources and Thanks:
# https://github.com/codefellows/seattle-cyber-401d3/blob/main/class-16/challenges/DEMO.md
# https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/

# Import libraries
import time, getpass

# Declare functions
def iterator():
    filepath = input("Enter your dictionary filepath:\n")
    #filepath = '/home/billkach/rockyou.txt' #test filepath
    
    file = open(filepath)
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()

def check_password():
    user_pass = input("Input the most common password you can think of, and see if we can find it:\n")
    filepath = input("Enter your dictionary filepath:\n")

    file1 = open(filepath, "r")

    flag = 0
    index = 0

    for line in file1:
        index += 1

        if user_pass in line:

            flag = 1
            break

    if flag == 0:
        print('Password', user_pass, 'not found')
    else:
        print('Password', user_pass, 'found on line', index)



# Add password recognition code here
#
#
#

# Main

if __name__ == "__main__": # when my computer runs this file...do this stuff
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            check_password()
        elif (mode == '3'):
            break
        else:
            print("Invalid selection...") 


# End
