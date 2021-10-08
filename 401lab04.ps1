# Script Name                           401lab04.ps1
# Author                                Bill Kachersky
# Date of last revision                 10/07/2021
# Description of purpose                Ops 401 Lab 04 PS Script





# Main

# Disable SMB1
Set-SmbServerConfiguration -EnableSMB1Protocol $true

# Enable Password Complexity Requirements
secedit /export /cfg c:\secpol.cfg
(GC C:\secpol.cfg) -Replace "PasswordComplexity = 0","PasswordComplexity = 1" | Out-File C:\secpol.cfg
secedit /configure /db c:\windows\security\local.sdb /cfg c:\secpol.cfg /areas SECURITYPOLICY
Remove-Item C:\secpol.cfg -Force

# End