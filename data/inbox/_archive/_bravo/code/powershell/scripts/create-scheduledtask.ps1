#region CREDS
$pass   = "=&%y)z#^30'Sd4#,R3B7Jj"
$acc    = "SVC_INT_CYBERTSK_PRD@int.ucq.com.au"
#endregion

#glob
$python     = "C:\Program Files\Python311\python.exe"
$powershell = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
$repo       = "C:\secops\git\cyber\scheduledtasks"

#local
$taskName           = "Cyber - AzureKeyVault Ping (ps)"
$taskDescription    = "This task checks if the azurekeyvault is accessible for the SVC_INT_CYBERTSK_PRD@int.ucq.com.au account"
$scriptName         = "azurekeyvault.ps1"
$trigger            = New-ScheduledTaskTrigger -Daily -At 7:40am


#-----------------------------------------------------------------
#DO NOT MODIFY BELOW
$argument   = ""
$action     = ""
switch ([IO.Path]::GetExtension($scriptName).ToLower()) {
    ".ps1" {
        $argument = "-ExecutionPolicy Bypass -command '$repo\$scriptName'"
        $action   = New-ScheduledTaskAction -Execute $powershell -Argument $argument
        break;
    }
    ".py" {
        $argument = 'INSERT PY COMMAND HERE "$repo\$scriptName"'
        $action   = New-ScheduledTaskAction -Execute $python -Argument $argument
        break;
    }
}

Register-ScheduledTask `
    -TaskName $taskName `
    -Description $taskDescription `
    -Action $action `
    -Trigger $trigger `
    -User $acc `
    -Password $pass











<#

$scriptPath         = $repo + 



$action             = New-ScheduledTaskAction -Execute $powershell -Argument $argument




$scriptName = "[ADAM] Test"
$description = "Test script for falcon deployment"
$argument = '-ExecutionPolicy Bypass -command "C:\git\cyber\team\adam\sendmail.ps1"'
$Trigger = 
$Action = 

#$Principal = New-ScheduledTaskPrincipal -UserId "INT\SVC_INT_CYBERTSK_PRD" -RunLevel Highest -LogonType ServiceAccount
#$principal = New-ScheduledTaskPrincipal -UserId "NT AUTHORITY\Interactive" -LogonType Interactive
$principal = New-ScheduledTaskPrincipal -UserId "INT\SVC_INT_CYBERTSK_PRD" -LogonType ServiceAccount


Register-ScheduledTask `
    -TaskName $scriptName `
    -Action $Action `
    -Trigger $Trigger `
    -Principal $Principal






#>