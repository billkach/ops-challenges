#!/bin/bash

# Script Name                           ops301d3-opschallenge01
# Author                                Bill Kachersky
# Date of last revision                 08/31/2021
# Description of purpose                Ops 301 Class 02 Ops Challenge

# VARIABLES DECLARATION
date=$(date +"%Y%m%d%H%M%S")

# MAIN

echo "Copying syslog file and appending file with current date/time to current directory..."
    
    sleep 1

cp /var/log/syslog syslog$date

    sleep 1

echo "complete!"

    sleep 1

echo "here's the contents of the directory"

    sleep 1
    
ls

# END