# Script Name                           opschallengeclass11.ps1
# Author                                Bill Kachersky
# Date of last revision                 08/09/2021
# Description of purpose                Ops Challenge Class 11

# OPS CHALLENGE TASKS BEGIN



# 1. Enable File and Printer Sharing
Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True

# Allow ICMP traffic
netsh advfirewall firewall add rule name="Allow incoming ping requests IPv4" dir=in action=allow protocol=icmpv4

# Enable Remote management
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

# Remove bloatware - this will open a menu
iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/debloat'))

# Enable Hyper-V
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All


# Disable SMBv1, an insecure protocol
Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol



# END CHALLENGE
