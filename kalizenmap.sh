#!/bin/bash

# Script Name                        kalizenmap.sh
# Author                             Bill Kachersky
# Date of last revision              10/22/2021
# Purpose                            Zenmap Install Script for Kali Linux


# This script is meant for Zenmap version 7.92 specifically, please be sure to check 
# Nmap's downloads page at their website first @ https://nmap.org/downloads.html
# to ensure you're downloading the latest version, if there is a more recent distro
# please be sure to run through this script and adjust the filename before executing it 
# to reflect the version you wish to install!




# Main



# Run a full update and upgrade on your kali system first
sudo apt update && sudo apt full-upgrade -y

# Download Zenmap (check version here)
wget https://nmap.org/dist/zenmap-7.92-1.noarch.rpm

# Download the required dependencies
sudo wget http://archive.ubuntu.com/ubuntu/pool/universe/p/pygtk/python-gtk2_2.24.0-5.1ubuntu2_amd64.deb
sudo wget http://azure.archive.ubuntu.com/ubuntu/pool/universe/p/pygobject-2/python-gobject-2_2.28.6-14ubuntu1_amd64.deb
sudo wget http://security.ubuntu.com/ubuntu/pool/universe/p/pycairo/python-cairo_1.16.2-2ubuntu2_amd64.deb
sudo dpkg -i python-gobject-2_2.28.6-14ubuntu1_amd64.deb
sudo dpkg -i python-cairo_1.16.2-2ubuntu2_amd64.deb
sudo dpkg -i python-gtk2_2.24.0-5.1ubuntu2_amd64.deb

# Change the permissions for the dependencies to prepare for installation
sudo chmod +777 python-*

# Install the dependencies
sudo apt install ./python-*

# Install Alien package to convert our .rpm to a .deb
sudo apt install alien

# Convert Zenmap .rpm package to .deb (check version here)
sudo alien --to-deb zenmap-7.92-1.noarch.rpm

# Make our new .deb executable (check version here)
sudo chmod 777 zenmap_7.92-2_all.deb

# Install our new .deb (check version here)
sudo apt install ./zenmap_7.92-2_all.deb

# Open Zenmap
sudo zenmap



# End
