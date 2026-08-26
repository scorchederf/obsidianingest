# Checking to see if we can hit the Falcon and LogScale cloud endpoints...
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12    # Set TLS if needed
$check = @("https://ts01-gyr-maverick.cloudsink.net","https://ucareqld.ingest.logscale.us-2.crowdstrike.com")
Write-Host ""
Write-host "Checking access to Falcon and LogScale..."
Write-Host ""
Foreach ($site in $check)
{
    $HTTP_Request = [System.Net.WebRequest]::Create($site)
    $HTTP_Response = $HTTP_Request.GetResponse()
    $HTTP_Status = [int]$HTTP_Response.StatusCode
    If ($HTTP_Status -eq 200) 
    {
        Write-Host "[*] $site is reachable"
    }
    Else 
    {
            Write-Host "[!] $site not accessible from this host"

            $smtp = "mail.uchealth.com.au"
            Send-MailMessage `
                -To "cyber@ucareqld.com.au" `
                -From "cyber@ucareqld.com.au" `
                -Subject "[ALERT] UCC-DHCP-P004 cant hit $site" -SmtpServer $smtp

    }
    If ($HTTP_Response -eq $null) { } 
    Else 
    { 
        $HTTP_Response.Close() 
    }
}









if (![string]::IsNullOrEmpty($Bcc.ToString())) {
    $optionalSplat.Add("Bcc", $Bcc)
}