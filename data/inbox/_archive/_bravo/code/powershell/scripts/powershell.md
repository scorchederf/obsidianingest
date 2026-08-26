

# * simple single line logging
```powershell
# Append the message to the log file
Add-Content -Path "C:\temp\test.log" -Value (Get-Date -Format "yyyy-MM-dd HH:mm:ss" + "`tThis is a custom log message.")
```
