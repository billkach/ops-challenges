# Script Name                           syseventtasker.ps1
# Author                                Bill Kachersky
# Date of last revision                 08/05/2021
# Description of purpose                PULL SYS EVENT LOGS TASKS




# VARIABLES
$Begin=Get-Date -Date '8/4/2021'
$End=Get-Date -Date '8/5/2021'

# FUNCTIONS
function Last-24-Out { 
    Get-EventLog -LogName System -After $Begin -Before $End | format-table -wrap | Out-File -FilePath .\last_24.txt
    }
    
    function Syslog-Error-Out {
    Get-EventLog -LogName System -EntryType Error | format-table -wrap | Out-File -filepath .\errors.txt
    }
    
    function Syslog-EventID-16 {
    Get-EventLog -LogName System -InstanceId 16 | format-table -wrap
    }
    
    function Syslog-Top-20 {
    Get-EventLog -LogName System -Newest 20 | format-table -wrap
    }
    
    function Syslog-Fortune500 {
    Get-EventLog -LogName System -Newest 500 | Group-Object -Property Source | format-table -auto -wrap
    }




# MAIN BODY


# Task 1: Output all events from the System event log that occurred in the last 24 hours to a file on your desktop named last_24.txt
Last-24-Out


# Task 2: Output all “error” type events from the System event log to a file on your desktop named errors.txt
Syslog-Error-Out


# Task 3: Print to the screen all events with ID of 16 from the System event log.
Syslog-EventID-16


# Task 4: Print to the screen the most recent 20 entries from the System event log.’
Syslog-Top-20


# Task 5: Print to the screen all sources of the 500 most recent entries in the System event log. 
Syslog-Fortune500






# END

# NOTE - ALL STRETCH OBJECTIVES SHOULD BE COVERED IN THE CODE ABOVE.