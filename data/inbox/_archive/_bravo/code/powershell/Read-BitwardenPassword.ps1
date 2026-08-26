
<#
.SYNOPSIS
Returns the password using the BitWarden CLI


.DESCRIPTION
Checks for the required Bitwarden environment variables, then 
    logs in, 
    initiates a new session and,
    uses that session key to retreive the password for the itemname passed to the function

.PARAMETER itemName
The name of the item we want to retrieve from BitWarden

.EXAMPLE
Read-BitwardenPassword -itemName "BobsSuperSecretPassword"

.NOTES
General notes

open cmd as user
    runas /user:int\service-account c:\windows\system32\cmd.exe

set env vars
    [System.Environment]::SetEnvironmentVariable('BW_CLIENTSECRET',	'VALUE', 'User')
    [System.Environment]::SetEnvironmentVariable('BW_CLIENTID',		'VALUE', 'User')
    #	To avoid the password being stored in history, capture via read-host
    $ps = read-host
    [System.Environment]::SetEnvironmentVariable('BW_PASSWORD',		$ps, 'User')










#>
function Read-BitwardenPassword{
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
        $cmd = "& 'C:\temp\bwtest\bw.exe'" 
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
        $params =  " unlock --passwordenv BW_PASSWORD"
        $sessionresponse = Invoke-Expression -Command ($cmd + $params) -ErrorAction SilentlyContinue
        $keys = $sessionresponse -match '(?<sessionkey>"(.*?)")'
        $sessionkey = $keys[0].replace('$ export BW_SESSION="', '').replace('"', "")
        
        # GET PASSWORD 
        $params = " get password $key --session $sessionkey"
        $bwresponse = Invoke-Expression -Command ($cmd + $params) -ErrorAction SilentlyContinue
        write-host $bwresponse        

    }
    END {
        #Like the Begin block, the End block is called once per function call. It is optional; one-time post-processing. Think of this as a place to finalize the function. 
        #It is a good practice to have an End block even if it is left empty.
        #clean up resources, close database connections etc.
    }
}

Read-BitwardenPassword -itemName ""