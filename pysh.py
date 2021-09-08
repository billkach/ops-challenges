#!/usr/bin/env python3

# Script Name                           pysh.py
# Author                                Bill Kachersky
# Date of last revision                 09/07/2021
# Description of purpose                CUSTOM HARDWARE LIST AND BIOS REPORT


# Here, I have taken a nice subprocess command and imported my previous script.
# This was the best solution I could come up with for today, feeling foggy.
# I will return to this tomorrow to figure it out more.

# Libraries
import subprocess

# Variables
compstats = subprocess.call('./compstats.sh')


# Main

print(compstats)

# End


# Resources
# https://geekflare.com/python-run-bash/