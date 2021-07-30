#!/bin/bash

# Script Name                           My First Array
# Author                                Bill Kachersky
# Date of last revision                 07/29/2021
# Description of purpose                To Create and Test Array and For Loop

# Make directories
mkdir dir1 dir2 dir3 dir4

# Make an array to call up the directories with
disarray=("dir1" "dir2" "dir3" "dir4")

#MAIN
for jellydonuts in "${disarray[@]}"
do
    touch ${jellydonuts}/test.txt 
done

#END