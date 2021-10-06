#!/usr/bin/env python3

# Script Name                           401ops02.py
# Author                                Bill Kachersky
# Date of last revision                 10/05/2021
# Description of purpose                Uptime Sensor Tool

# Imports
import os
import time
from datetime import datetime

# Getting the current date and time
dt = datetime.now()

# User input for IP address
ipaddr = input("Enter an IP address to check the status of: ")


# Main

for ip in ipaddr:
    response = os.system("ping -c 1 " + ipaddr)
    p=1
    while p <= 5000:
        time.sleep(2)
        if response == 0:
            print("ping successful for", ipaddr, dt)
        
        else:
            print("ping failed for", ipaddr, dt)
        

# End