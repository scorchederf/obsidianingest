

#repo=unitingcare-queensland

```
#repo=unitingcare-queensland    // crowdstrike
| groupby(#event_simpleName)
```

#   #event_simpleName
    - [ ] DnsRequest
        - DomainName
    - [x] PtyCreated
    - [ ] RansomwareOpenFile
        - tracks which processes are opening a high number of files at high velocity 
            - https://www.reddit.com/r/crowdstrike/comments/qmv4t8/event_simple_name_ransomewareopenfile/
        - TargetFileName
    - [x] RemoteBruteForceDetectInfo
    - [x] SensorTampering
    - [ ] SensitiveWmiQuery
    - [x] SuspiciousDnsRequest
    - [ ] UserAccountAddedToGroup
    - [ ] UserAccountCreated
        - very noisy - DEFAULTUSER1, ONESIGN.LOGIN
    - [ ] UserAccountDeleted
        - very noisy - DEFAULTUSER1, ONESIGN.LOGIN
    - [x] UserLogonFailed
    - [ ] WebScriptFileWritten





aip     agent ip represents the external ip address of the endpoint
aid     unique identifier for the device

# get aid from ip, computername, username
//  #event_simpleName = LocalIpAddressIP4                   | LocalAddressIP4 = 10.14.212.95 | selectLast([aid])                            //ipaddress     to aid
//  #kind = Secondary AND SecondaryEventType = aidmaster    | ComputerName = UCL-GW5HZH3 | selectLast([aid])                                //computername  to aid
//                                                            UserName = astein | groupby([aid, ComputerName])    






# mega activity TEST
https://ucareqld.logscale.us-2.crowdstrike.com/ucqv-overview/search?connect-points=false&end=1711589068180&live=false&query=%2F%2F%20TESTING%20FILE%20UPLOAD%20https%3A%2F%2Fmega.nz%2Ffilerequest%2FqQDd5Ch-1h4%0A%2F%2F%7C%20%22*mega.nz*%22%0A%2F%2F%7C%20DomainName%20%3D%20mega.nz%0A%2F%2F%7C%20fqdn%20%3D%20mega.nz%20%20%20%20%20%20%20%20%2F%2Fucq-dns%0A%0A%2F%2F%7C%20SessionId%20%3D%201%20%20%20%20%20%2F%2FProcessRollup2%0A%23repo%3Ducq-palofirewall%0A%7C%20SourceIP%20%3D%2010.14.212.95%0A%7C%20DestinationIP%3D31.216.144.5%0A%7C%20timechart(function%3Dsum(BytesSent))&start=1711588528180&tz=Australia%2FBrisbane&widgetType=time-chart