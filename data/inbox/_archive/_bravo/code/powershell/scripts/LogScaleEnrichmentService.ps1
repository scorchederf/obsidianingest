[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

#region "Functions"

enum LogType {
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

}
function logging {
    param (
        [LogType] $logtype,
        [string] $message,
        [string] $scriptname
    )
    try {
        $now = (Get-Date)
        $msg = $now.ToString('yyyy-MM-dd HH:mm:ss') + " " + $logtype.ToString().ToUpper().PadRight(10, " ") + "`t" + $message
        #write to log file based on date and script name
        $logfile = "C:\temp\" + $now.ToString("yyyyMMdd") + "-" + $scriptname + ".log"
        Add-Content -LiteralPath $logfile -Value $msg
        write-host $msg 
    }
    catch {
        Write-Host "An error occurred writing to the log file:"
        Write-Host $_
    }
}
function Get-BitwardenPassword {
    #CmdletBinding gives us advanced functions like -verbose or -debug
    [CmdletBinding()]
    Param (
        [Parameter(
            Mandatory = $true, 
            HelpMessage = "This is the name of the item we are wanting to retrieve the password for."
        )]
        [string]$itemName
    )
    # All functions should include BEGIN PROCESS END wrappers 
    #   https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_methods?view=powershell-7.2
    BEGIN {
        #The Begin block is an optional, preprocessing of the function that will only run once per call of the function. 
        #Use this block to setup the function by initializing objects such as variables, database connections, or arrays that will be used throughout the function.  
        #Any variables that are created in the Begin block will be accessible elsewhere in the function.

        #setting some local variables
        $now = Get-Date
        $cmd = "& 'C:\Program Files\BitwardenCLI\bw.exe'" 
    }
    PROCESS {
        #The Process block is used to specify the code that will continually execute on every object that might be passed to the function. 
        #A function can have a Process block without the other blocks, and a Process block is mandatory if a parameter is set to accept pipeline input.
        #This is where the magic happens

        #check environment variables
        $requiredEnvVariables = @("BW_CLIENTSECRET", "BW_CLIENTID", "BW_PASSWORD")
        foreach ($envVariable in $requiredEnvVariables) {
            try {
                $d = $null
                $d = (Get-ChildItem env:$envVariable -ErrorAction SilentlyContinue).Value.length 
                if ($d -le 0) {
                    throw "$envVariable has no data"
                }
            }
            catch {
                $msg = @{}
                $msg.Add("err", "$envVariable has no data. To set it use set-item -Path env:$envVariable -Value `"value here `"")
                #logging @loggingsplat -logtype NOTICE -message ($msg | ConvertTo-Json -Depth 10)
                write-host  ($msg | ConvertTo-Json -Depth 10 -Compress) 
            }
        }

        # LOGIN
        $params = " login --apikey"
        $response = Invoke-Expression -Command ($cmd + $params) -ErrorAction SilentlyContinue
        
        # GET SESSION KEY
        #$session = $env:BW_SESSION
        #if ($session.length -le 0) {
        $params = " unlock --passwordenv BW_PASSWORD"
        $sessionresponse = Invoke-Expression -Command ($cmd + $params) -ErrorAction SilentlyContinue
        $keys = $sessionresponse -match '(?<sessionkey>"(.*?)")'
        $sessionkey = $keys[0].replace('$ export BW_SESSION="', '').replace('"', "")
        $env:BW_SESSION = $sessionkey
        #} 
        # GET PASSWORD 
        $params = " get password $itemName"
        #$params = ' list items --session "' + $sessionkey + '"'
        $bwresponse = Invoke-Expression -Command ($cmd + $params) -ErrorAction SilentlyContinue
        return $bwresponse        
 
    }
    END {
        #Like the Begin block, the End block is called once per function call. It is optional; one-time post-processing. Think of this as a place to finalize the function. 
        #It is a good practice to have an End block even if it is left empty.
        #clean up resources, close database connections etc.
    }
}


#endregion

#init 
$scriptname = $PSCommandPath.split('\')[-1].split('.')[0]
logging -scriptname $scriptname -logtype info -message "Logscale Enrichment Service"

$domains = @("int.ucq.com.au", "lccq.org.au", "qld.bluecare.org.au", "uhc.uc.com.au"); 

$logscaleURL = "ucareqld.logscale.us-2.crowdstrike.com"
$logscaleRepo = "ucqv-overview"
$logscaleAPI = ""


#region "enrich security identifiers (SIDs) with onprem facts"
function Send-EnrichedSecurityIdentifiers() {
    $outcsv = "c:\temp\enrichSIDs.csv"
    $SIds = $null
    logging -scriptname $scriptname -logtype info -message "[enrichSIDs] start"  

    foreach ($domain in $domains) {
        $tmp = get-adgroup -filter * -server $domain -properties * | `
            Select-Object -Property @{Name = 'Domain'; Expression = { $domain } }, ObjectClass, DistinguishedName, SID, SamAccountName, { $_.Description.replace("`r", "").replace("`n", "") } 
        logging -scriptname $scriptname -logtype info -message "[enrichSIDs] $domain returned $($tmp.count) results"  
        $SIds += $tmp
    } 

    $orig = Import-Csv -Path $outcsv
    if ($SIds.count -lt $orig.count) {
        # dont upload if results are lower, lazy (could probably do a % difference in files blah blah)
        logging -scriptname $scriptname -logtype info -message "The enrichSIDs file contained less records [$($SIds.count)] than the original [$($orig.count)]. Will not upload incase we have incorrect results." 
    }
    else {
        logging -scriptname $scriptname -logtype info -message "[enrichSIDs] Starting file upload" 
        $SIDs | Export-Csv -Path $outcsv -append -NoTypeInformation 
        # -k stops ssl certificate error
        Invoke-Expression -Command "C:\git\cyber\curl.exe -k https://$logscaleURL/api/v1/repositories/$logscaleRepo/files -H `"Authorization: Bearer $logscaleAPI`" -F `"file=@$outcsv`""
        logging -scriptname $scriptname -logtype info -message "[enrichSIDs] File upload complete"
    }

    logging -scriptname $scriptname -logtype info -message "[enrichSIDs] end"  
}
Send-EnrichedSecurityIdentifiers
#endregion




#region enrich country data - https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv
