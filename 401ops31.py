#!/usr/bin/env python3

# Script Name                           401ops31.py
# Author                                Bill Kachersky
# Date of last revision                 11/15/2021
# Description of purpose                Signature-based Malware Detection Part 1 of 3


# Resources and Thanks
# https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/
# https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/
# https://github.com/CourtHans/401-Ops-Challenges/blob/main/31_FileSearch.py
# https://www.delftstack.com/howto/python/python-conditional-assignment-operator/


import platform
import os
from time import sleep

# Variables

my_os = platform.system()



# Functions

# linux os
def linux():
    filename = input("Please enter the filename you'd like to search for: ")
    filepath = input("Please specify the filepath of the directory you'd like to search in: ")
    print("Thank you! Stand by please...")
    sleep(1)
    # count and print number of files searched
    os.system("ls " + str(filepath) + " | echo \"$(wc -l) files searched.\"")
    # count and print number of files discovered
    os.system("find " + str(filepath) + ' -name ' + str(filename) + " -print | echo \"Found $(grep -c /) files that matched:\"")
    os.system("find " + str(filepath) + ' -name ' + str(filename))


# windows os
def windows():
    filename = input("Please enter the filename you'd like to search for: ")
    filepath = input("Please specify the filepath of the directory you'd like to search in: ")
    print("Thank you! Stand by please...")
    sleep(1)
    # count the number of files searched and store number in variable
    searchCount = os.popen("dir /a:-d /s /b " + str(filepath) + " | find /c \":\\\"").read()
    print("Files searched: " + searchCount)
    # count the number of files searched and store number in variable
    foundCount = os.popen("dir /b/s " + str(filepath) + "\\" + str(filename) + " | find /c \":\\\"").read()
    print("Files found: " + foundCount)
    os.system("dir /b/s " + str(filepath) + "\\" + str(filename))


# Main

print("Hello! Welcome to Space Treasury: Malware Analysis and Removal Tool")
sleep(1)
print("We'll start by scanning your machine to determine what operating system you're currently running.")
sleep(1)
print("Please stand by...")


print("OS in my system: ",my_os)
sleep(1)
print("Now that we've established your OS, we're ready to begin scanning.")
sleep(1)

if my_os == "Linux":
    linux()

elif my_os == "win32" or "win64":
    windows()


# End