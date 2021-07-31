#!/bin/bash

# Script Name                           My First Loop
# Author                                Bill Kachersky
# Date of last revision                 07/30/2021
# Description of purpose                To Create and Test a While Loop, with USER INTERACTION!


# WARNING MESSAGE
sleep 2
echo Don't do anything I wouldn't do...
sleep 2
echo ....which is not much!
sleep 2

# WHILE LOOP to DISPLAY RUNNING PROCESSES
while true 
do 

ps -aux

echo Enter PID number to end, but be careful...

read PID
kill $PID

sleep 2 

echo Now you have really gone and done it!

sleep 2

break

done



# END