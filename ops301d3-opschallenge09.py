#!/usr/bin/env python3

# Script Name                           automation.py
# Author                                Bill Kachersky
# Date of last revision                 09/10/2021
# Description of purpose                Make a list of string elements, then pull and modify certain elements



# Variable(s)

automation = ('carrot', 'pumpkin', 'zucchini', 'corn', 'cucumber', \
              'ginger', 'shallot', 'pepper', 'celery', 'tomato')
print ()


# Main

# Print the list to the screen.
print ("Here's a list of ten string elements... I think?")

print (*automation)

print()


# Print the fourth element of the list.
print("Here's the fourth element: ")

print(*automation[3:4])

print()


# Print the sixth through tenth element of the list.
print("Here's 6 through 10: ") 

print(*automation[5:10])

print()


# Change the value of the seventh element to “onion”.
print ("And for my final trick, let's change element 7 to 'onion':")
res = [sub.replace('shallot', 'onion')for sub in automation]

print(*res)

print()


# Acknowledge completion
print("done")

print()


# End