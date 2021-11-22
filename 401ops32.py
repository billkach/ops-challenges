#!/usr/bin/env python3

# Script Name                           401ops32.py
# Author                                Bill Kachersky
# Date of last revision                 11/21/2021
# Description of purpose                Signature-based Malware Detection Part 2 of 3


# Resources and Thanks
# https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/
# https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/
# https://github.com/CourtHans/401-Ops-Challenges/blob/main/31_FileSearch.py
# https://www.delftstack.com/howto/python/python-conditional-assignment-operator/
# https://www.programiz.com/python-programming/examples/hash-file


import platform
import os
from time import sleep
import hashlib
import datetime
import math


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

def os_check():
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



# timestamp function
def currentime():
    rn=datetime.datetime.now()
    return rn.strftime('%m-%d-%Y %H:%M:%S')

# hashing function 
def hash_file(filename):
   """"This function returns the MD5 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.md5()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()


   # use os.walk to crawl through directories and display hash of all files
def hash_getter():

    print("Let's take a look at the hashes of all of our files in a given directory today")
    print("This can be useful for taking the hashes and sharing them on a site like VirusTotal..")
    print("To run them against any known hashes out there of malware! Let's begin..")

    sleep(1)

    dir_count = 0
    file_count = 0
    start_path = input("Please enter the absolute path to the directory you want to get the file hashes in: ")
    for (path,dirs,files) in os.walk(start_path):
        print('DIRECTORY: {:s}'.format(path))
        print("")
        dir_count += 1
        #Repeat for each file in directory     
        for file in files:
            fstat = os.stat(os.path.join(path,file))

            # Convert file size to MB, KB or Bytes
            if (fstat.st_size > 1024 * 1024):
                fsize = math.ceil(fstat.st_size / (1024 * 1024))
                unit = "MB"
            elif (fstat.st_size > 1024):
                fsize = math.ceil(fstat.st_size / 1024)
                unit = "KB"
            else:
                fsize = fstat.st_size
                unit = "B"

            file_count += 1
            filename = os.path.join(path,file)
            md5 = hash_file(filename)
            timestamp = currentime()
            print(timestamp)
            print(f"FILENAME: {file}\tSIZE: {str(fsize) + unit}\tPATH: {filename}")
            print("HASH: " + md5 + "\n")

           
    # Print total files and directory count
    print('Summary: hashed {} files in {} directories'.format(file_count,dir_count))
    dir_count = 0
    file_count = 0   



# Main

print("Hello! Welcome to Space Treasury: Malware Analysis and Removal Tool")
sleep(1)
print("What would you like to do today?")
if __name__ == "__main__": # when my computer runs this file...do this stuff
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Check OS, Search for File
2 - Get File Hashes for all Files in a Folder
3 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            os_check()
        elif (mode == "2"):
            hash_getter()
        elif (mode == '3'):
            break
        else:
            print("Invalid selection...")



# End