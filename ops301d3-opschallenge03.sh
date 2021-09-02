#!/bin/bash

# Script Name                           ops301d3-opschallenge03.sh
# Author                                Bill Kachersky
# Date of last revision                 09/03/2021
# Description of purpose                Class 04 Ops Challenge



########################
# Declarations
########################


# Functions

menureturn() {
    echo "Alright, anything else?"
    echo "1. Hello World; 2. ping self; 3. IP info; 4. Exit"
}

conditional() {

if [ $course -eq 1 ]

then 

    hello_world
        sleep 1

            menureturn
            read course

                sleep 1
                conditional

else

    if [ $course -eq 2 ]

    then

        sleep 1

        echo "This one is our bottomless breadsticks special, be sure to hit ^C when you're satisfied." 
        
        sleep 1

        self_ping

            sleep 1
    
            menureturn

            read course

                sleep 1

                conditional

    else

        if [ $course -eq 3 ]

        then 

            netadapt

                sleep 1

                menureturn

                read course

                    sleep 1

                    conditional

        else

            if [ $course -eq 4 ]

            then

                echo "You sure we can't interest you in anything else?"

                    sleep 1

                    echo "1. Hello World; 2. ping self; 3. IP info; 4. Exit"

                        read course
                        
                        if [ $course -eq 4 ]
                        
                        then
                        
                            sleep 1
                        
                            echo "See ya later!"
                        
                            exit 0
                        
                        fi
                        
            else

                echo "Hmmm, I don't think we serve that here.."

                exit 3
            

            fi

        fi

    fi

fi
}

hello_world() {
    echo "Hello World!"
}

self_ping() {
    ping localhost
}

netadapt() {
    sudo lshw -c network
}






########################
# Main
########################



    echo "Greetings, $USER!"

sleep 1
        echo "Bottle of red, bottle of white, it all depends upon yoooouuurrrrr appetite..."
        sleep 2
        echo "ahem... excuse me... Welcome to my new restaurant, Command Line & Dine"

    sleep 2
            echo "Here's what on the menu, pick whichever 'dish' you'd prefer by inputting the number next to it.."

        sleep 1
                echo "1. Hello World; 2. ping self; 3. IP info; 4. Exit"

            sleep 1

read course

conditional


########################
# END
########################









