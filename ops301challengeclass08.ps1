# Script Name                           ops301challengeclass08.ps1
# Author                                Bill Kachersky
# Date of last revision                 09/10/2021
# Description of purpose                301 Ops Challenge Class 08

# Main

# Create New OU
New-ADOrganizationalUnit `
-Name "Compliance" `
-Path "DC=corp,DC=globexpower,DC=com"


# Create New AD User in newly created OU
New-ADUser `
-Name "Franz Ferdinand" `
-SamAccountName "ffedri" `
-GivenName "Franz" `
-Surname "Ferdinand" `
-AccountPassword (Read-Host -AsSecureString "Input User Password") `
-ChangePasswordAtLogon $True `
-Company "GlobeX USA" `
-Title "TPS Reporting Lead" `
-State "Oregon" `
-City "Springfield" `
-Country "USA" `
-PostalCode "97475" `
-Description "Ops Challenge Class 08" `
-EmployeeNumber "1" `
-Department "TPS Department" `
-DisplayName "Franz Ferdinand" `
-EmailAddress "ferdi@globexpower.com" `
-Path "OU=Compliance,DC=corp,DC=globexpower,DC=com" `
