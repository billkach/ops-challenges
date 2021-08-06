# Script Name                           syseventtasker.ps1
# Author                                Bill Kachersky
# Date of last revision                 08/05/2021
# Description of purpose                PULL SYS EVENT LOGS FROM LAST 24 HRS

$Begin=Get-Date -Date '8/4/2021'
$End=Get-Date -Date '8/5/2021'

Get-EventLog -LogName System -After $Begin -Before $End | format-table -wrap | Out-File -FilePath .\last_24.txt

Get-EventLog -LogName System -EntryType Error | format-table -wrap | Out-File -filepath .\errors.txt

Get-EventLog -LogName System -InstanceId 16 | format-table -wrap

Get-EventLog -LogName System -Newest 20 | format-table -wrap

Get-EventLog -LogName System -Newest 500 | Group-Object -Property Source | format-table -auto -wrap