[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

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
        $session = $env:BW_SESSION
        if ($session.length -le 0) {
            $params =  " unlock --passwordenv BW_PASSWORD"
            $sessionresponse = Invoke-Expression -Command ($cmd + $params) -ErrorAction SilentlyContinue
            $keys = $sessionresponse -match '(?<sessionkey>"(.*?)")'
            $sessionkey = $keys[0].replace('$ export BW_SESSION="', '').replace('"', "")
            $env:BW_SESSION=$sessionkey
        } 

        <#

        #write-host($sessionkey)
        #>

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

function get-credential($u,$d){

    $p = Read-BitwardenPassword -itemName $u  
    $sp = ConvertTo-SecureString -String $p -AsPlainText -Force
    $du = ($d + "\" + $u + "prd").replace("-", "_")
    write-host $du,$p -ForegroundColor Red
    $pc = New-Object -TypeName PSCredential -ArgumentList $du, $sp
    write-host $pc

    #$pc = [PsCredential]::New($u,$p)
    return $pc
}

function send-Email() {
    
    param(
        [parameter(Mandatory = $true)]
        $subject,
        [parameter(Mandatory = $true)]
        $body,
        [parameter(Mandatory = $true)]
        $logFilePath,
        [parameter(Mandatory = $true)]
        $userid,
        [parameter(Mandatory = $true)]
        $received
    )

    $params = @{
        Message = @{
            Subject      = $subject
            Body         = @{
                ContentType = "Text"
                Content     = $body
            }
            ToRecipients = @(
                @{
                    EmailAddress = @{
                        Address = $received
                    }
                }
            )
            Attachments  = @(
                @{
                    "@odata.type" = "#microsoft.graph.fileAttachment"
                    Name          = ($logFilePath -split '\\')[-1]
                    ContentBytes  = $([convert]::ToBase64String((Get-Content $logFilePath -Encoding byte)))
                }
            )
        }
    }
    Send-MgUserMail -UserId $userId -BodyParameter $params

	
}

function get-usersdata() {

    $clientid = ""
    $tenantid = ""
    $clientsecret = "" # the client secret that need to change every 6 months. 
    $body = @{
        Grant_Type    = "client_credentials"
        Scope         = "https://graph.microsoft.com/.default"
        Client_Id     = $clientid
        Client_Secret = $clientsecret
    }
    $connection = Invoke-RestMethod -Uri https://login.microsoftonline.com/$TenantID/oauth2/v2.0/token -Method POST -Body $body
    $token = ConvertTo-SecureString $connection.access_token -AsPlainText -Force
    Connect-MgGraph -AccessToken $token
    # get all users with last sign in date etc
    # you can change adjust the filter accordingly. 
    $allusers = get-mguser -filter "OnPremisesSyncEnabled eq true" -all -ErrorAction Stop -Property @(
        'UserPrincipalName'
        'AccountEnabled'
        'SignInActivity'
        'CreatedDateTime'
        'DisplayName'
        'JobTitle'
        'OfficeLocation'
        'Mail'
        'OnPremisesSyncEnabled'
        'OnPremisesImmutableId'
        'OnPremisesDistinguishedName'
        'OnPremisesLastSyncDateTime'
        'SignInSessionsValidFromDateTime'
        'RefreshTokensValidFromDateTime'
        'OnPremisesDomainName'
        'id'     ) | Select-Object @(
        'UserPrincipalName'
        'AccountEnabled'
        'CreatedDateTime'
        'DisplayName'
        'Mail'
        'OnPremisesSyncEnabled'
        'OnPremisesImmutableId'
        'OnPremisesDomainName'
        'OnPremisesDistinguishedName'
        'OnPremisesLastSyncDateTime'
        'SignInSessionsValidFromDateTime'
        'RefreshTokensValidFromDateTime'
        'id'
        @{n = 'LastSignInDateTime'; e = { [datetime]$_.SignInActivity.LastSignInDateTime } }
        @{n = 'lastNonInteractiveSignInDateTime'; e = { [datetime]$_.SignInActivity.lastNonInteractiveSignInDateTime } }
    )
    return $allusers
}



# $users = get-usersdata
<#
$bc  = get-credential -u "svc-bc-cyberauto" -d  "bluecare"
$int = get-credential -u "svc_int_cyberauto" -d "int"
$ucc = get-credential -u "svc-ucc-cyberauto" -d "lccq"               #lccq.org.au
$uhc = get-credential -u "svc-uhc-cyberauto" -d "uhc"


    {
    UHC.UC.COM.AU { $v_domainname="UHC" }
    LCCQ.ORG.AU { $v_domainname="LCCQ" }
    uc.com.au  { $v_domainname="UC" }
    INT.UCQ.COM.AU { $v_domainname="INT" }
    EXT.UCQ.COM.AU { $v_domainname="EXT" }
    10.20.1.25 {$v_domainname="BLUECARE" }
    }

 #>

function edit-adattributes($server,$filter,$aadUser){
    switch ($server.ToLower()) {
        "int.ucq.com.au" {
            $d = Get-ADUser -Server $server -Identity $filter -Credential $int
            [System.ConsoleColor]$clr = 'Magenta'      
        }
        "lccq.org.au" {
            $d = Get-ADUser -Server $server -Filter {EmailAddress -like $filter} -Credential $ucc
            [System.ConsoleColor]$clr = 'Yellow' 
        }
        "qld.bluecare.org.au" {
            $d = Get-ADUser -Server $server -Filter {EmailAddress -like $filter} -Credential $bc
            [System.ConsoleColor]$clr = 'Blue' 
        }
        "uhc.uc.com.au" {
            $d = Get-ADUser -Server $server -Filter {EmailAddress -like $filter} -Credential $uhc
            [System.ConsoleColor]$clr = 'Green' 
        }
    } 
    if ($null -eq $d) {
        #wasnt found
        write-host "not found" -ForegroundColor Red
    } else {
        #found
        $msg = "server:{0} `t| sam:{1} `t| att5:[{3}] `t| att6:[{5}] `t| att9:[{7}]" `
            -f $server, $d.SamAccountName, `
            $d.extensionAttribute5, $user.LastSignInDateTime, `
            $d.extensionAttribute6, $user.lastNonInteractiveSignInDateTime, `
            $d.extensionAttribute9, $(Get-Date)
        write-host $msg -ForegroundColor $clr


        $Confirm = Read-Host -Prompt "Are you sure you want to update the user (Y/N)"
        if ($confirm -eq 'y') {
          write-host "updating"
        } else {
          Write-Host "cancelled"
        }

    }


    #write-host $user.OnPremisesDomainName.ToLower().PadLeft($leftPad), " - ", $d.SamAccountName.PadLeft($leftPad), " - ", $d.extensionAttribute5, " - ", $d.extensionAttribute6, " - ", $d.extensionAttribute9 -ForegroundColor Blue
    #$user = Get-ADUser @params





}

# -and $_.OnPremisesDomainName.ToLower() -eq "int.ucq.com.au"
$filteredUsers = $users | Where-Object {$_.OnPremisesDomainName -ne $null -and $_.DisplayName -like "Adam Stein*" } #| where-object {}
foreach ($user in ($filteredUsers)) {
    #write-host $user.UserPrincipalName

    switch ($user.OnPremisesDomainName.ToLower()) {
        "int.ucq.com.au" {
            $filter = ($user.UserPrincipalName).Split("@")[0]
            $server = "int.ucq.com.au"
            edit-adattributes -server $server -filter $filter -aadUser $user
        }
        "lccq.org.au" {
            $filter = ($user.UserPrincipalName)
            $server = "lccq.org.au"
            edit-adattributes -server $server -filter $filter -aadUser $user
        }
        "qld.bluecare.org.au" {
            $filter = ($user.UserPrincipalName)
            $server = "qld.bluecare.org.au"
            edit-adattributes -server $server -filter $filter -aadUser $user
        }
        "uhc.uc.com.au" {
                $filter = ($user.UserPrincipalName)
                $server = "uhc.uc.com.au"
                edit-adattributes -server $server -filter $filter -aadUser $user
        }
        default {
            Write-Host ($user.UserPrincipalName) -ForegroundColor Red
        }
    }
    # start-sleep -Milliseconds 100

}








            #   get the user based on OnPremisesDistinguishedName and then 
            #       set extensionAttribute4 for last login interactive,                 $user.LastSignInDateTime
            #       set OnPremisesDistinguishedName5 for last login noninteractive      $($user.lastNonInteractiveSignInDateTime)
            #       set extensionAttribute6 for the time it stamped.                    $currentdatetime
            
            
            #set-aduser -server $user.OnPremisesDomainName -Replace @{
            #    extensionAttribute5=$($user.LastSignInDateTime); 
            #    extensionAttribute6=$($user.lastNonInteractiveSignInDateTime); 
            #    extensionAttribute9=$currentdatetime
            #} -erroraction Stop -verbose -whatif 