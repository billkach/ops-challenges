#!/usr/bin/python3

# Script Name                           401ops44.py
# Author                                Bill Kachersky
# Date of last revision                 12/06/2021
# Description of purpose                Create a Port Scanner


# Resources and Thanks
# https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/class-44/challenges/DEMO.html
# https://github.com/CourtHans/401-Ops-Challenges/blob/main/44_PortScan.py
# https://www.kite.com/python/answers/how-to-check-if-a-network-port-is-open-in-python#:~:text=To%20check%20if%20a%20network%20port%20is%20open%2C%20call%20socket,connect_ex()%20returns%200%20



# Import Modules
import socket


# Variables
sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 2
sockmod.settimeout(timeout)


# Functions
def portScanner(h, p):
    # connect_ex function returns error indicator instead of raising exception, this is how we establish the port is "closed" in this instance.
    sock = sockmod.connect_ex((h, int(p)))
    if sock:
        # if connect_ex returns an error, that will trigger our if statement here
        print("Port closed")
    else:
        # if connect_ex returns a 0, this means the port is open, triggering our else statement here
        print("Port open")

    # close the connection
    sockmod.close()


# Main

print("")
print("")
# Greeting
print("Hello! Welcome to the Space Treasury Port Scanning Tool.")

print("")
# Gather user input
hostip = input("Please specify which IP address you'd like to scan: ")
portno = input("Please specify which port number you'd like to scan: ")

print("")
# Run our function using the gathered user input
portScanner(hostip, portno)

print("")

# End