# Script Name                           opschallenge10.ps1
# Author                                Bill Kachersky
# Date of last revision                 08/06/2021
# Description of purpose                Fun Tasks for Powershell



# BEGIN CHALLENGE



# Task 1 - Print to the terminal screen all active
# processes ordered by highest CPU time consumption at the top.

Get-Process | Sort-Object CPU -Descending


# Task 2 - Print to the terminal screen all active
# processes ordered by highest Process Identification Number at the top.

Get-Process | Sort-Object ID -Descending


# Task 3 - Print to the terminal screen the top five
# active processes ordered by highest Working Set (WS(K)) at the top.

Get-Process | Sort-Object WS -Descending | Select-Object -First 5


# Task 4 - Start the process Internet Explorer (iexplore.exe) 
# and have it open https://owasp.org/www-project-top-ten/

Start-Process "iexplore" "https://owasp.org/www-project-top-ten/"


# Start the process Internet Explorer (iexplore.exe) 
# ten times using a for loop. Have each instance 
# open https://owasp.org/www-project-top-ten/.

# Loop Begin

for ($i = 1 ; $i -lt 11 ; $i++)
{
    Start-Process "iexplore.exe" "https://owasp.org/www-project-top-ten/"
    sleep 1
}

# End




# Close all Internet Explorer windows.

Get-Process "iexplore" | Stop-Process



# Kill a process by its Process Identification Number. 
# Choose a process whose termination won’t destabilize 
# the system, such as Internet Explorer or MS Edge.

Stop-Process -ID 25404

# (this was for notepad)


# END CHALLENGE
