# powershell



## * simple single line logging
```powershell
# Append the message to the log file
Add-Content -Path "C:\temp\test.log" -Value (Get-Date -Format "yyyy-MM-dd HH:mm:ss" + "`tThis is a custom log message.")
```


## quick unique line count csv
```powershell
 (import-csv .\20250507_A_cyber-crowdstrike-compromisedpassworduser.csv | select-object -Property ObjectSID ).count
```

## create a simple url safe api key

```powershell
$bytes = New-Object Byte[] 32; [System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes); $apiKey = [Convert]::ToBase64String($bytes).Replace('+', '-').Replace('/', '_').TrimEnd('='); $apiKey

```
