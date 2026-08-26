---
title: powershell
---

# one liners
-  check recursively for files with size gt zero
    - `get-childitem -Recurse -File -Filter *.txt  | % {if($_.Length -gt 0) { write-host $_.FullName}}`
- check security event log for users who are failing event 4625
    - `$a = get-winevent @{logname='Security'; id=4625}; foreach ($b in $a) { write-host $b.properties[5].value }`
- get content tail
    - `Get-Content $filepath -tail 10`
- get environment variables
    - `Get-ChildItem -Path Env:`
    - `Get-ChildItem -Path Env:<name>`
    - `[System.Environment]::GetEnvironmentVariables()`
    - `remove-item env:<name>`  #!destructive
- version
    - `$PSVersionTable.PSVersion`