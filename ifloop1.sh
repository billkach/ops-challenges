#!/bin/bash

# Script Name                           My First If Loop
# Author                                Bill Kachersky
# Date of last revision                 08/02/2021
# Description of purpose                To Create and Test If Loops

# Functions
Query () {
    echo "What should we name it?"
}

# Arrays
workingdir=(ls)

# Friendly Greeting
echo "We need that directory up and running yesterday, otherwise we're going to miss our deadline, are you ready?"
sleep 2


echo "Well? (Y)es or (N)o?"
read rpl

if [[ $rpl == Y || $rpl == Yes ]]
then
Query

else
echo "Way to be a team player, $USER."
exit
fi


read cfm


if [ ! -d "$cfm" ]
then
sleep 2
echo "Directory $cfm DOES NOT exist."
sleep 2
echo "Great, let's create it then."
sleep 2
mkdir $cfm
echo "Complete!" 
sleep 2
${workingdir[@]}
sleep 2
echo "Thanks for your help."
elif [ -d "$cfm" ]
then
echo "Hmmm.. already taken."
sleep 2




fi













