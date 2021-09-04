#!/bin/bash

# Script Name                           ops301d3-opschallenge04
# Author                                Bill Kachersky
# Date of last revision                 09/03/2021
# Description of purpose                Ops 301 Class 05 Ops Challenge



# Functions

replay() {

    echo "We can either..."
        sleep 1

    echo "1) output the contents of the logs to the terminal"
        sleep 1

    echo "2) spare ourselves of the verbosity and simply check the number of lines in each log"
        sleep 1

    read -p "Which would you prefer? 1 or 2: " output

    

    if [ $output -eq 1 ]

    then 
        
        echo "Okay, get ready!"
        
                cat /var/log/$call
            

    elif [ $output -eq 2 ]

    then 

                ls | wc -l /var/log/$call



    else
            
                echo "having trouble understanding me? let's start over."

                replay

    fi
   

}


deletion() {

    sudo truncate -s 0 /var/log/$call

        sleep 2

    echo "deleted! let's verify that this was successful.."

    replay
}




####################
# MAIN
####################

echo "Oi $USER!"
    sleep 1
    
        echo "Let's clear some logz aye?"
            sleep 1

echo "I'm thinking that our syslog and our wtmp is the way to go"
    sleep 1

echo "Let's take an inventory and see how populated they are first though.."
    sleep 1

echo "Which log would you like to check first?"

read -p "syslog or wtmp?: " call

    sleep 1

replay

    sleep 1

echo "Alright, now that we've squared that bit away, let's get on with the show!"

    sleep 1

deletion

    sleep 1 

echo "alright, would you like to delete anything else?"

    sleep 1

echo "We can do anything in the /var/log/ folder, have a look!"

    sleep 1

echo "Just make sure you know what you're deleting in case you needed it for something"

    sleep 1

ls -a /var/log

    sleep 1

read -p "Which log would you like to delete?: " call

    sleep 1

deletion

    sleep 1

echo "Phew! I feel lighter already.. I'm done for now, feel free to check back in a few days."

    sleep 1

echo "Take care!"

    sleep 1


####################
# END
####################
