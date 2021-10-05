# Script Name                       autoupdatewu.ps1
# Author                            Bill Kachersky
# Date of last revision             10/04/2021
# Description of purpose            Ops 401 Lab 01 script component


# Main


$AUSettings=(New-Object -com "Microsoft.Update.AutoUpdate").Settings

$AUSettings.NotificationLevel=2

$AUSettings.FeaturedUpdatesEnabled=True

$AUSettings.Save()