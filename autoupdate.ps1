# Script Name                       autoupdate.ps1
# Author                            Bill Kachersky
# Date of last revision             10/04/2021
# Description of purpose            Ops 401 Lab 01 script component


# Main

set-executionpolicy -ExecutionPolicy remotesigned -scope Process -force

Write-Host "Let's automate the installation of Windows Updates on this machine"

Start-Sleep -Seconds 1

Import-Module -Name PSWindowsUpdate

Install-Module -Name PSWindowsUpdate

Get-WindowsUpdate

Get-WUInstall -AcceptAll -AutoReboot