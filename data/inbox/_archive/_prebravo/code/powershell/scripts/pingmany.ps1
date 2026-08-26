# List of server names or IP addresses to ping
$serverList = @("server1", "192.168.1.1", "server2", "10.0.0.1")
# Function to ping the servers and display the results
function Ping-Servers {
    param (
        [string[]]$servers
    )

    foreach ($server in $servers) {
        $pingResult = Test-Connection -ComputerName $server -Count 1 -ErrorAction SilentlyContinue
        if ($pingResult) {
            Write-Host "Ping succeeded: $server"
        } else {
            Write-Host "Ping failed: $server"
        }
    }
}
# Call the function with the server list
Ping-Servers -servers $serverList



