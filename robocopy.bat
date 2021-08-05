

:: Script Name                           robocopy.bat
:: Author                                Bill Kachersky
:: Date of last revision                 08/05/2021
:: Description of purpose                Batch Script for Copying files using Robocopy


@echo off
ROBOCOPY C:\Users\j.thompson\Desktop\Data E:\Backups /LOG:backuplog.txt
pause