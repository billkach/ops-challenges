#!/bin/bash

# Script Name                           ops301d3-opschallenge02
# Author                                Bill Kachersky
# Date of last revision                 09/01/2021
# Description of purpose                Ops 301 Class 03 Ops Challenge



# Functions

challenge() {
    echo "hey there, $USER!"
        sleep 2
        
    echo "lets try modifying some permissions in a directory today!"
        sleep 1

    echo "Take care to only perform this operation in user-created directories. Changing permissions in system files/directories is not advised, as this can cause malfunctions in the OS."
        sleep 1

    echo "So don't do anything foolish! Let's just have some fun!"
        sleep 1

    echo "In case you're not sure where we are, here's a reminder:"
        sleep 1 

    pwd
        sleep 2

    read -p "please specify the absolute path to the directory you'd like to modify permissions on: " -r path
        sleep 1

    read -p "Great, thanks for the input. Now what permissions should we set on the files in $path?: " rwx
        sleep 1

    echo "Alright, thanks again! Working..."
        sleep 2
    
    # Function for recursively modifying folder contents
    recursivefoldermod() {
    chmod -R $rwx $path
        }
    recursivefoldermod

    echo "All done! The proof is in the pudding, as they say, so let's have a look at what we've done here;"
        sleep 2

    # Function which displays the folder contents and their permissions
        pudding() {
    ls -lh $path
        }
    pudding
        sleep 1

    echo "There you go! If you'd like to start over, just rerun the script. You can also check out a copy of the output of our session in your user directory. Take care!"
        sleep 1

}


##############################

# Main

##############################



challenge



##############################

# End

##############################



    











