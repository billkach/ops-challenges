#!/bin/bash

# Script Name                           My First Loop
# Author                                Bill Kachersky
# Date of last revision                 07/30/2021
# Description of purpose                To Create and Test a While Loop, with USER INTERACTION!


# warning message
sleep 2
echo Don't do anything I wouldn't do...
sleep 2
echo ....which is not much!
sleep 2

# while loop for displaying running processes
while true 
do 

ps -aux

# user prompt
echo Enter PID number to end, but be careful...

# user input
read PID
kill $PID

sleep 2 
# reply
echo Now you have really gone and done it!

sleep 2

break

# loop end
done

# END