#USAGE
<#

#region "DO NOT DELETE - import common functions, init logging"
Import-Module C:\secops\git\cyber\common\inc.ps1 -Force
$scriptname = $PSCommandPath.split('\')[-1].split('.')[0]
$hostname = $env:computername
logging -hostname $hostname -scriptname $scriptname -logtype DEBUG -message "script executing"
#endregion

#>
enum LogType {
    DEBUG       = 10
    NOTICE      = 15            # notice is used for success message
    INFO        = 20
    WARNING     = 30
    ERROR       = 40
    CRITICAL    = 50

}

#global smtp server for use
$smtp = "mail.uchealth.com.au"
$logpath = "c:\temp"

function logging {
    param (
        [string] $hostname,
        [string] $scriptname,
        [LogType] $logtype,
        [string] $message
    )
    try {
        $timestamp = [datetime]::UtcNow.ToString("yyyy-MM-ddTHH:mm:ssZ")
        $msg = $timestamp + " " + $hostname + " " + $scriptname + " LOG - " + $logtype + " - " + $message
        $now = Get-Date
        #write to log file based on date and script name
        $logfile = $logpath + "\" + $now.ToString("yyyyMMdd") + "-" + $scriptname + ".log"
        Add-Content -LiteralPath $logfile -Value $msg
        write-host $msg 
    }
    catch {
        Write-Host "An error occurred writing to the log file:"
        Write-Host $_
    }
}
