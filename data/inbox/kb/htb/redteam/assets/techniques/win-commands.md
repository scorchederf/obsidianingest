
- ping with timestamp `ping.exe -t ucq-cyber-p001 |Foreach{"{0} - {1}" -f (Get-Date),$_}`


- get windows version `Get-WmiObject -Class win32_OperatingSystem | select Version,BuildNumber`
- 