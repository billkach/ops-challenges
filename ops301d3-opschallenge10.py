#!/usr/bin/env python3

# Script Name                           ops301d3-opschallenge10.py
# Author                                Bill Kachersky
# Date of last revision                 09/13/2021
# Description of purpose                Learning how to create and work with Python conditionals


# Imports
import time


# Variables 
b = 6
c = -1
d = 21



# Function
def number_line():
    
    a = int(input("Pick a number: ")) # Another variable here
    
    if a <= c:
        print("Don't be so negative, try again..")
        number_line()

    if a >= d:
        print("I'm sorry Dave, I can't do that.")
        number_line()


    if a != b:
        print("That's not it! But I'll give you a clue..")
        time.sleep(1)

        if a < b:            
            print("the number you chose is lower than the number I'm thinking of")
            time.sleep(1)
            number_line()

        elif a > b:
            print("the number you chose is higher than the number I'm thinking of")
            time.sleep(1)
            number_line()
        

        

    elif a == b:
        print("Bingo! Nice work.")
        exit(1)



# Main
print()

print("Hi! I'm thinking of a number between one and twenty")
time.sleep(1)

print("Can you guess what number I'm thinking of?")
time.sleep(2)

print()

number_line()
# End