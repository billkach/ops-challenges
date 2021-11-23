#!/usr/bin/env python3

# Script Name                           401ops36.py
# Author                                Bill Kachersky
# Date of last revision                 11/22/2021
# Description of purpose                Fingerprinting Tool


# Resources and Thanks
# https://www.codegrepper.com/code-examples/python/pass+variable+in+subprocess+run+python
# https://python.land/operating-system/python-subprocess#Create_a_Python_subprocess_with_subprocessrun
# https://www.instructables.com/Netcat-in-Python/



# Modules
import socket
import time
import subprocess

# Variables



# Functions
# netcat fingerprinting function
def netcat(a, p):


    print("let's do netcat first..")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((a, int(p)))

    run = "nc " + a + " " + p
    sock.sendall(run.encode())
    time.sleep(.5)
    sock.shutdown(socket.SHUT_WR)

    res = ""

    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()

    print(res)

    sock.close()

# telnet fingerprinting function
def telnet(a, p):
    print("Now we'll run telnet")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((a, int(p)))

    run = "telnet " + a + " " + p
    sock.sendall(run.encode())
    time.sleep(.5)
    sock.shutdown(socket.SHUT_WR)

    res = ""

    while True:
        data = sock.recv(1024)
        if (not data):
            break
        res += data.decode()

    print(res)

    sock.close()


def nmap(a):

    print("last but not least, let's give this address the old once over with nmap.")
    
    # turn our linux command into a variable for processing
    nmap = "nmap"
    run = a
    result = subprocess.run([nmap, run])




# Main
print("Welcome to the Web Application Finger Printing Utility!")


time.sleep(1)


a = input("Type in a URL or IP address you'd like to fingerprint: ")
p = input("What port(s) would you like to check?: ")


netcat(a, p)

telnet(a, p)

nmap(a)



# End
