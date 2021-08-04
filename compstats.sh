#!/bin/bash

# Script Name                           compstats.sh
# Author                                Bill Kachersky
# Date of last revision                 08/03/2021
# Description of purpose                CUSTOM HARDWARE LIST AND BIOS REPORT


# REPORT INTIALIZE MSG
echo
echo "CURRENT STATE OF CPU AND RAM PERFORMANCE REPORT WITH BIOS INFO"
sleep 2
echo "STAND BY... GENERATING REPORT"
echo
sleep 3



# SYSTEM STATS
echo "Name and Model of Host Computer:"
sudo lshw | grep -B 1 -Em1 'description:'
echo

# CPU STATS
echo "CPU Info:"
sudo lshw -C cpu | grep -E 'product:|vendor|physical id|bus info|width'
echo

# RAM STATS
echo "Memory:"
lshw -c memory | grep -A 2 -Em1  'System memory'  
echo

# DISPLAY ADAPTER STATS
echo "Display Adapter:"
sudo lshw -C display | grep -E 'description:|product|vendor|physical id|bus info|width|clock|capabilities|configuration|resources'
echo

# NETWORK ADAPTER STATS
echo "Network Adapter:"
sudo lshw -c network | grep -E 'description:|product|vendor|physical id|bus info|logical name|version|serial|size|capacity|width|clock|capabilities|configuration|resources'

sleep 3
echo
echo



# REPORT STATUS UPDATE
echo "STAND BY, GENERATING BIOS STATUS REPORT"
echo
sleep 5



# BIOS STATS
dmidecode -t bios
sleep 2




# REPORT STATUS UPDATE
echo "REPORTING COMPLETE!"
echo



# END