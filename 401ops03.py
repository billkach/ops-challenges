#!/usr/bin/env python3

# Script Name                           401ops02.py
# Author                                Bill Kachersky
# Date of last revision                 10/05/2021
# Description of purpose                Uptime Sensor Tool

# Imports
import os
import time
import sys
import io 
from io import StringIO
from time import gmtime, strftime
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Mail address info
sender_address = 'billisatechie@gmail.com'
sender_pass = 'L10n1z3r@$G!'
receiver_address = 'billisatechie@gmail.com'




# User input for IP address
ipaddr = input("Enter an IP address to check the status of: ")


# Variable
server_status=1
# response
# response = os.system("ping -c 1 " + ipaddr)

# Main

while True:
        time.sleep(2)
        response = os.system("ping -c 1 " + ipaddr)
        dt = datetime.now()
        current_time=strftime("%x %X", gmtime())
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        if response == 0:
            print(dt, "ping successful for", ipaddr)
        
        else:
            print(dt, "ping failed for", ipaddr)


        output = new_stdout.getvalue()
        sys.stdout = old_stdout
        
        if response != server_status:
            message=MIMEMultipart()
            message['From']=sender_address
            message['To']=receiver_address
            message['Subject']='A status change has occurred on a server'
            if response == 0:
                mail_contentup=(output + "Server is AVAILABLE")
                message.attach(MIMEText(mail_contentup, 'plain'))
                session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                session.starttls() #enable security
                session.login(sender_address, sender_pass) #login with mail_id and password
                text = message.as_string()
                session.sendmail(sender_address, receiver_address, text)
                session.quit()
            else:
                mail_contentdown=(output + "Server is UNAVAILABLE")
                message.attach(MIMEText(mail_contentdown, 'plain'))
                session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                session.starttls() #enable security
                session.login(sender_address, sender_pass) #login with mail_id and password
                text = message.as_string()
                session.sendmail(sender_address, receiver_address, text)
                session.quit()

        server_status=response
# End