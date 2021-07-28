#!/bin/bash


#Script Name:                             My first script attempt
#Author:                                  Bill Kachersky
#Date of last revision                    7/27/2021


#This script was created to see if I can run network adapter info using a variable, then print it to a text file

#variables are myvar



myvar=$(sudo lshw -class network -short)

touch output.txt

echo $myvar >> output.txt