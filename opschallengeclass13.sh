#!/bin/bash

# Script Name                           opschallengeclass13
# Author                                Bill Kachersky
# Date of last revision                 08/11/2021
# Description of purpose                Class 13 Ops Challenge



# Variables are generated in functions (except environmental)
# Variable names: $USER, $donuts, $rpl, $cfm

# Functions
query () {
    echo "Please enter a domain name that you'd like to pull up information about now."
    read donuts
}

output () {
    whois $donuts > webinfo.txt
    dig $donuts >> webinfo.txt
    host $donuts >> webinfo.txt
    nslookup $donuts >> webinfo.txt
}

confirm () {
    echo "Complete! Check your working directory for a file called webinfo.txt," 
sleep 2
    echo "that will contain all of the information I was able to gather."
sleep 2
    echo "Redirecting you to view contents in nano"
sleep 3
    nano webinfo.txt 
}

sendoff () {
            echo "Okay, hope you find the information you've obtained here to be useful, $USER."
        sleep 2
        exit
}



# Main

sleep 2
    echo "Hello, $USER!"
sleep 2
        echo "The purpose of this program is to provide useful network information about domains."
sleep 2
            echo "To execute this command, simply enter the domain name in the following format;"
sleep 2
                echo "domain-name.com"
sleep 2
    # Function
    query


    # Function
    output

sleep 3
    # Function
    confirm

sleep 2
echo "Would you like to obtain the same information about another domain?"
sleep 1
echo "Y/N"
read rpl

# Nested if/else statements!
if [ $rpl == Y ]
 then
 echo "WARNING! This will save to the same file, overwriting the previous contents"
 sleep 2
 echo "Well, still want to? (Y/N)"
    read cfm

    if [ $cfm == Y ]
     then 
            sleep 1
            echo "Okay, here we go!"

                query

                sleep 3 

                output

                sleep 3

                confirm

                sleep 3

                echo "Please run the script again if you'd like to gather information about any additional domains :)"
                echo "Cheers!"

                    sleep 2
        else
        sendoff
    fi
 else
        sendoff
fi

# End