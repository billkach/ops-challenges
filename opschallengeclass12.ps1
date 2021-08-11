# Script Name                           opschallengeclass12.ps1
# Author                                Bill Kachersky
# Date of last revision                 08/10/2021
# Description of purpose                Ops Challenge Class 12



# OPS CHALLENGE TASKS BEGIN




# VARIABLES

$NetRepFull=ipconfig /all
$DesktopPath=[Environment]::GetFolderPath("Desktop")



# FUNCTIONS

    # Task 1, 2 & 3
function NetworkReportandDestroy {
    echo "Outputting Network Report to Desktop..."
    sleep 5

        $NetRepFull | Out-File -FilePath $DesktopPath\network_report.txt

    echo "Report Generated.. Grabbing IPv4 data!"
    sleep 3

        Select-String -Path "$DesktopPath\network_report.txt" -Pattern 'IPv4'

    sleep 2
    echo "IPv4 Data captured, deleting source file now."
    sleep 3

        rm $DesktopPath\network_report.txt

    sleep 3
    echo "Deleted!"
}

    # Stretch 1
function NetRep2Clip {
    Set-Clipboard -Value $NetRep2Mem | Get-Clipboard | Select-String -Pattern "IPv4"
}

    # Stretch 2
function pingpong {    
    ping 192.168.0.1
}

    # Stretch 3
function interweb {
            If (Test-Connection google.com -count 4 -quiet) {
          Write 'The host responded'
        }
}



# MAIN

<#
Task 1, 2, and 3
1 - Create a local file called network_report.txt that holds the contents of an ipconfig /all command.
2 - Use Select-String to search network_report.txt and return only the IP version 4 address.
3 - Remove the network_report.txt when you are finished searching it.
#>

NetworkReportandDestroy

    sleep 5




# Stretch Goal 1 - Instead of creating network_report.txt, use piping to store the output in memory and search it there.

echo "Now let's try that again, but commit it to memory this time!"

    sleep 3

echo "Working, stand by!"

    sleep 2

NetRep2Clip

    sleep 5

echo "Looks like that should do it.. Check your clipboard, hit your Windows key + V to see if it took!"

    sleep 5




# Stretch Goal 2 - Have your script test whether the network adapter is sending and receiving packets correctly.

echo "Now let's see if we can ping the Network adapter.."

    sleep 3

pingpong

    sleep 5 




# Stretch Goal 3 - Have your script test connectivity to the internet

echo "Now let's see if we're able to access the interwebs"

    sleep 2

interweb
    
    sleep 2

echo "Complete!"





# END