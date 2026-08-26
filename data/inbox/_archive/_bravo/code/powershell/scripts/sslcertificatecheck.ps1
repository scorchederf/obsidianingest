

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

#region "DO NOT DELETE - import common functions, init logging"
Import-Module C:\git\cyber\scheduledtasks\inc.ps1
$scriptname = $PSCommandPath.split('\')[-1].split('.')[0]
logging -scriptname $scriptname -logtype info -message "script initialised"
#endregion

function get-data(){
    foreach ($domain in $domains) {
        $counter = 0
        do {
            $target = "https://crt.sh/?q=" + $domain + "&output=json"
            try{
                $data += Invoke-RestMethod $target
                $irmok = $true
                logging -scriptname $scriptname -logtype info -message "retrieved data for $domain"
            }catch {
                $irmok = $false
                logging -scriptname $scriptname -logtype info -message "failed to retrieve data for $domain, attempt $counter"
                $counter += 1
            }
            start-sleep -Seconds 1
        } until ($counter -eq 5 -or $irmok -eq $true)
    }
    $data | ConvertTo-Json >> $tempfile       #save it so we can read it back
}

function get-html($collection) {
    $output = $null
    $collection | Sort-Object -Property "not_after" | ForEach-Object {
        $expires = Get-Date($_.not_after); 
        $diff = New-TimeSpan -End $expires  -Start (Get-Date);
        $msg = [string]::Format("<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>`n", $_.common_name, $diff.Days, $expires.ToLongDateString()); 
        $output += $msg 
    }
    return $output
}


$domains = Get-Content "C:\git\cyber\data\domain_db.txt"
$exclusions = Get-Content -Path "C:\git\cyber\data\domain_db_exclude.txt"
$tempfile =  "c:\temp\certcheckraw1.json"

$warn = @()
$expired =  @()
$active =  @()

#load up all our data
get-data
$data = $null
$data = (Get-Content $tempfile | ConvertFrom-Json)

$groups = $data | select-object common_name, entry_timestamp, not_after | Group-Object common_name

foreach ($group in $groups) {
    $latest = $null   
    $latest = $group.Group | Sort-Object -Property "not_after" -Descending | Select-Object -First 1
    $expires = Get-Date($latest.not_after); 
    $diff = New-TimeSpan -End $expires  -Start (Get-Date);
    $msglog = [string]::Format("{0},{1},{2}", $latest.common_name, $diff.Days, $expires.ToString("u"))
    if ($diff.Days -in 1..30) {         #expires in the next 30 days
        logging -scriptname $scriptname -logtype info -message "EXPIRING,$msglog"
        $warn += $latest
    } elseif ($diff.Days -le 0) {
        logging -scriptname $scriptname -logtype info -message "EXPIRED,$msglog"
        $expired += $latest
    } else {
        logging -scriptname $scriptname -logtype info -message "ACTIVE,$msglog"
        $active += $latest
    }
}

#build notification email
$table = "<table BORDER=1 CELLSPACING=0 CELLPADDING=5 style='border-collapse: collapse;'><tr><th>domain</th><th>days</th><th>expires on</th></tr>{0}</table>"
$warnhtml =     "<h5>Expiring soon</h5>"    + [string]::Format($table, (get-html -collection $warn))
$activehtml =   "<h5>Active</h5>"           + [string]::Format($table, (get-html -collection $active))
$expiredhtml =  "<!--<h5>Expired</h5>"      + [string]::Format($table, (get-html -collection $expired)) + "-->"


$html = $null
$html =  "<h5>" + $groups.count + " domains checked from " + $env:computername + "</h5>"
$html += $warnhtml + $activehtml + $expiredhtml

Send-MailMessage `
    -From "cyber@ucareqld.com.au" `
    -To  "adam.stein@ucareqld.com.au" `
    -Subject "SSL Cert Search - Revision" `
    -BodyAsHtml $html `
    -Encoding utf32 `
    -SmtpServer $smtp

#delete the data file
#remove-item -Path 