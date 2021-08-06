# Script Name                           syseventtasker.ps1
# Author                                Bill Kachersky
# Date of last revision                 08/05/2021
# Description of purpose                PULL SYS EVENT LOGS TASKS




# Task 1 Variables
$Begin=Get-Date -Date '8/4/2021'
$End=Get-Date -Date '8/5/2021'




# Task 1: Output all events from the System event log that occurred in the last 24 hours to a file on your desktop named last_24.txt
Get-EventLog -LogName System -After $Begin -Before $End | format-table -wrap | Out-File -FilePath C:\Users\TEST\Desktop\last_24.txt


# Task 2: Output all “error” type events from the System event log to a file on your desktop named errors.txt
Get-EventLog -LogName System -EntryType Error | format-table -wrap | Out-File -filepath C:\Users\TEST\Desktop\errors.txt


# Task 3: Print to the screen all events with ID of 16 from the System event log.
Get-EventLog -LogName System -InstanceId 16 | format-table -wrap


# Task 4: Print to the screen the most recent 20 entries from the System event log.’
Get-EventLog -LogName System -Newest 20 | format-table -wrap


# Task 5: Print to the screen all sources of the 500 most recent entries in the System event log. 
Get-EventLog -LogName System -Newest 500 | Group-Object -Property Source | format-table -auto -wrap






# END