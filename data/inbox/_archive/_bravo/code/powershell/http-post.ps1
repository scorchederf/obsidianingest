$env:HostIP = (
    Get-NetIPConfiguration |
    Where-Object {
        $_.IPv4DefaultGateway -ne $null -and
        $_.NetAdapter.Status -ne "Disconnected"
    }
).IPv4Address.IPAddress
netsh trace start capture=yes IPv4.Address=$env:HostIP tracefile=c:\temp\pscapture.etl
################################################




$url = "https://auth-qa.bluecare.online/oauth/token"
$postParams = @{
    grant_type='client_credentials';
    client_id = '';
    client_secret = '';
    audience = 'https://api-qa.bluecare.online/billing';
}
$response = Invoke-WebRequest -Uri $url -Method POST -Body $postParams -Verbose
write-host $response



#############################################
# stop the trace 
netsh trace stop

