

function capture{
    while ($true) {
        $ipaddress = "10.14.121.61"
        $hostname = hostname; $dir = "D:\captures\"
        $filename = $dir +  (Get-Date).ToString("yyyyMMddHHmm") + "-" + $hostname + "-Capture.etl"
        netsh trace start capture=yes IPv4.Address=$ipaddress tracefile=$filename
        Start-Sleep 60 #capture 60 seconds of traffic
        netsh trace stop
        Get-ChildItem -Path $filename | Compress-Archive -DestinationPath $dir\$hostname.zip -CompressionLevel Optimal -Update
        Remove-Item $filename.replace(".etl", ".cab") #cleanup
        Remove-Item $filename #cleanup
        [int]$NumSeconds = (New-TimeSpan -End (get-date -Minute 15 -Second 0).AddHours(1)).TotalSeconds
        write-host "sleeping for $NumSeconds seconds"
        start-sleep -Seconds $NumSeconds #sleep until the next hour
    }
}

function convert-files{
    Get-ChildItem "C:\temp" -Filter *.etl | 
    Foreach-Object { write-host $_.FullName
        #https://github.com/microsoft/etl2pcapng/releases
        c:\temp\etl2pcapng.exe $_.FullName $_.FullName.replace(".etl", ".pcap")
    }
}

#capture
convert-files