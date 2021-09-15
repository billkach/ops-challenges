#!/usr/bin/env python3

# Script Name                           ops301d3-opschallenge10.py
# Author                                Bill Kachersky
# Date of last revision                 09/13/2021
# Description of purpose                Learning how to create and work with Python conditionals


# Imports
import time
import random


# Variables 



c = 0
d = 21
yes = "y"
no = "n"



# Function
def generator():
    return random.randint(1, 20)



def number_line():

    b = generator()

    guess_left = 5

    flag = 0
    
    while guess_left > 0:
    
        a = int(input("Pick a number: ")) # Another variable here         
            

        if a == b:

            flag = 1
            break

        else:
                

        

            if a <= c:
                print("Don't be so negative, try again..")
                

            if a >= d:
                print("I'm sorry Dave, I can't do that.")
            


            if a != b:
                print("That's not it! But I'll give you a clue..")
                time.sleep(1)

                if a < b:            
                    print("the number you chose is lower than the number I'm thinking of")
                    time.sleep(1)
                

                elif a > b:
                    print("the number you chose is higher than the number I'm thinking of")
                    time.sleep(1)

        guess_left -= 1    

    if flag == 1:
        return True

    else:
        return False   
            
if __name__=='__main__':
    if number_line() is True:
        print("YES!!!! Nice work.")

        close = input("Well, I think we're all done here, would you like to do it again? [y/n/idk]: ")

        if close == yes:
                    print("Okay! Let's try again..")
                    number_line()

        else:
                    print("Sure! Thanks for playing!")
                    exit(1)
    else :
        print("Sorry, you lost!")

        close = input("Would you like to do it again? [y/n/idk]: ")

        if close == yes:
                    print("Okay! Let's try again..")
                    number_line()

        else:
                    print("Sure! Thanks for playing!")
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