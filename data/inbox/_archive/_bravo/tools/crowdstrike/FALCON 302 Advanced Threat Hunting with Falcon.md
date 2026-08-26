# FALCON 302: Advanced Threat Hunting with Falcon

Class will begin at 5 minutes past the hour!
1. Sign into CrowdStrike University first:    https://crowdstrike.litmos.com/course/5313033
2. Sign into CloudShare Second:   https://use.cloudshare.com/Class/bwvsl?passphrase=LogantheTiredTurtle
3. Be sure to remember which email address you use.
4. If/when the pop-up shows in the browser for the clipboard > Click allow on the browser pop-up
5. No VM’s found is expected on first login
6. I’ll give you the Falcon Encounter code after the setup demo

stephen.ferguson@crowdstrike.com

---
Day 1

- case insensitive `ParentBaseFileName=/cmd\.exe/i`
- exactly `^cmd\.exe`
    - `^` starts with

- chat notes
```
table()                                            - https://library.humio.com/data-analysis/functions-table.html
groupBy()                                        - https://library.humio.com/data-analysis/functions-groupby.html
Parameters                                     - https://library.humio.com/data-analysis/dashboards-parameters.html#dashboards-parameters-example-regex
Case-Insensitive Parameter               - https://library.humio.com/data-analysis/dashboards-parameters.html#dashboards-parameters-example-case-insensitive

```

```
#event_simpleName=ProcessRollup2
| aid=?aid
| ImageFileName=/(?<FileName>[^\\/|\\\\]*)$/
| FileName = /^(net|nmap|ipconfig|whoami|quser|ping|netstat|tasklist|hostname|at)\.exe$/i
| table([aid, UserName, ParentBaseFileName, ImageFileName, CommandLine], limit=1000)
```

**powershell hunt** can show the score based on execution, downloading, hidden
```
Here is the breakdown of the “interesting score” is when something is found vs not found:
PowerShell Hunt Report
Score   = Varies = Sum of all the columns, kind of like an “interesting” score 
Exec       = 0 or 4 = Execution seen in CommandLine
Dwnld     = 0 or 4 = Download seen in CommandLine
Encode    = 0 or 5 = Is there encoding found in the CommandLine syntax
ExecPol   = 0 or 1 = Execution Policy syntax seen
NonI        = 0 or 1 = Non-Interactive
NoProf    = 0 or 1 = No Profile seen in syntax
Hidden    = 0 or 1 = Is the CommandLine showing Hidden switches
Domain   = 0 or 3 = Is there a Domain seen in the syntax
VM          = 0 or 3 = Virtual Machine commands seen in syntax such as Hypervisor
Prxy        = 0 or 4 = Proxy commands seen in syntax
Obf1       = 0 or 4 = Obfuscation seen
Obf2       = 0 or 4 = Obfuscation seen

```

https://www.crowdstrike.com/cybersecurity-101/threat-hunting/
https://falcon.crowdstrike.com/documentation/category/y907ff6d/hunting-queries 
EDR - https://www.crowdstrike.com/cybersecurity-101/endpoint-security/endpoint-detection-and-response-edr/
A good reference link for data retention: https://supportportal.crowdstrike.com/s/article/How-long-will-Historical-Data-be-available-to-view-in-my-Falcon-console
Incident Response (IR): Plan & Process:  https://www.crowdstrike.com/cybersecurity-101/incident-response/
https://www.crowdstrike.com/cybersecurity-101/indicators-of-compromise/



```
#event_simpleName = ProcessRollup2
//#event_simpleName = ScheduledTaskRegistered
//| groupBy([UserName], function=collect([ComputerName], separator=","))
/*
Accounts beginning with S-1-5-90-0 (account names DWM-x) are generated on the fly by the Desktop Window Manager component for its system services.
Accounts beginning with S-1-5-96-0 (account names UMFD-x) are generated on the fly by the User Mode Driver Framework component for its system services. */
//| !in(field=UserName, values=["DWM-*", "*$", "UMFD-*"])
| UserName = SVC-YNN
// /schtasks\.exe/i//| table([aid, UserName, ParentBaseFileName, ImageFileName, CommandLine], limit=1000)
//| groupBy([CommandLine])
//| CommandLine = "schtasks  /create /sc ONCE /st 00:00 /tn \"Device Management\" /tr C:\\Temp\\revshell.exe"| FileName=/RAR\.exe/i
//| groupBy([CommandLine])| CommandLine = /intel/i


```

verify hash
investigate user

external prevelence is against all crowdstrike clients
internal prevelence is against our environment

aid = agent identifier
ContextProcessId = 
TargetProcessId = 



```
Infragard - https://www.infragard.org/
NCFTA - https://www.ncfta.net/
Interpol – https://www.interpol.int/en
NCIJTF – https://www.fbi.gov/investigate/cyber/national-cyber-investigative-joint-task-force
Cyber Threat Alliance - https://www.cyberthreatalliance.org/
CISA - https://www.cisa.gov/
Dept of State OSAC - https://www.state.gov/overseas-security-advisory-council/
STIX - https://makingsecuritymeasurable.mitre.org/docs/stix-intro-handout.pdf

```



"Be a student of your environment"


"When threathunting, finding nothing is ok. There may not be anything there!"


https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/


MUTEX Objects - https://learn.microsoft.com/en-us/windows/win32/sync/mutex-objects?redirectedfrom=MSDN
Looking at Mutex Ojects for Malware Discovery & Indicators of Compromise - https://www.sans.org/blog/looking-at-mutex-objects-for-malware-discovery-indicators-of-compromise/

https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/


SeDebugPrivileges - https://learn.microsoft.com/en-us/windows/win32/secauthz/enabling-and-disabling-privileges-in-c--
ElfHash - https://www.programmingalgorithms.com/algorithm/elf-hash/cpp/


```
#repo=base_sensor #event_simpleName=CommandHistory cid="*"  
| in(aid, values=["a0945be5fa2c408ca5afe848288f410f"], ignoreCase=true) 
| case {    ApplicationName != *        
| ApplicationName := "--";    *;} 
| CommandHistory := splitString(CommandHistory, by="¶") 
| commandHistory := concatArray(CommandHistory, separator="\n") 
| timestamp := formatTime("%FT%TZ", field=timestamp) 
| applicationName := rename(ApplicationName) 
| commandCount := rename(CommandCount) 
| table([@timestamp, timestamp, applicationName, commandCount, commandHistory, aid, cid], limit=20000) 
| sort(@timestamp, order=desc, limit=20000)


```


groupby = frequency analysis


headfirst books use the same techniques



is winrar installed by default on a windows machine? Does the user have elevated privs?
lsass keyword
c:\temp\stuff       destination folder
-scul UTF-16 little-endian encoding, why?
-imon1      show results in monitor 1 why?


Here is a nice explanation of hunting leads also:  https://www.crowdstrike.com/blog/what-is-a-hunting-lead/

show command lines from network connections

join data is stored in temp lookup table


1.42k work score

**cmd + slash = selected line comment**

by default joins are INNER LEFT

108 work score, **Higher, further, faster, baby. - Capt. Marvel**


https://www.crowdstrike.com/cybersecurity-101/machine-learning-cybersecurity/
https://www.crowdstrike.com/blog/how-crowdstrike-achieves-fast-machine-learning-model-training-with-tensorflow-and-rust/


```
ComputerName=REYNHOLM-WRK137 #event_simpleName=Wmi*

//groupBy([#event_simpleName]) 
| #event_simpleName = NetworkConnectIP4
| cidr(RemoteAddressIP4, subnet=["10.1.0.0/8","127.0.0.1"]) 
//|groupBy([RemoteAddressIP4])
//| join({#event_simpleName=ProcessRollup2}, field=[ContextProcessId], key=TargetProcessId, include=[FileName, CommandLine,ComputerName], mode=left)
| join({#event_simpleName=ProcessRollup2 FileName!=dsregcmd.exe}, field=[ContextProcessId],key=TargetProcessId, include=[FileName, CommandLine], mode=left)
|groupBy([ComputerName], function=collect([FileName]))
//|groupBy([ComputerName,FileName, CommandLine])
```

https://pentestlab.blog/2020/01/21/persistence-wmi-event-subscription/

```
#event_simpleName=NetworkConnectIP4
RemoteAddressIP4=/^(10\.|192\.168\.|172\.1[6-9]\.|172\.2[09]\.|172\.3[0-1]\.)/
| join({#event_simpleName=ProcessRollup2 FileName!=dsregcmd.exe}, field=
[ContextProcessId],key=TargetProcessId, include=[FileName, CommandLine])
|groupBy([ComputerName], function=collect([FileName]))

```

#event_simpleName = AgentOnline


How long will historical data be available:
https://supportportal.crowdstrike.com/s/article/How-long-will-Historical-Data-be-available-to-view-in-my-Falcon-console



aid is unique to machine and install. everytime the agent is uninstalled/reinstalled we loose historical data


OMG OMG OMG!


https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/



```
cidr()           - https://library.humio.com/data-analysis/functions-cidr.html
in()             - https://library.humio.com/data-analysis/functions-in.html
join()           - https://library.humio.com/data-analysis/functions-join.html
Persistence - WMI Event Subscription:  https://pentestlab.blog/2020/01/21/persistence-wmi-event-subscription/
mstsc.exe reference:      https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mstsc

```


| !cidr(field=DestinationIP, subnet=["10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"])  



---
day 4



treeid is the way to map a event

?can we follow the id to get a full process


? can we block domains in custom IOA's ?



Support Reference:  https://supportportal.crowdstrike.com/s/article/ka16T000000wxxHQAQ



52.86.45.171

capstone


RemoteAddressIP4=52.86.45.171





event_simpleName=ProcessRollup2
| join(query={RemoteAddressIP4=52.86.45.171}, field=[TargetProcessId], key=[ContextProcessId])
| groupBy([UserName, ComputerName, @timestamp])
| sort(@timestamp, order=asc)



-


Stephen Ferguson "Ferg"  to  Everyone 14:56
#event_simpleName=AgentOnline LocalIP=?IP
| groupBy([ComputerName,LocalIP], function=[])

Stephen Ferguson "Ferg"  to  Everyone 15:11
endpoints impacted in this attack
-        INITECH-WRK134
-        INITECH-WRK144
-        INITECH-WRK132
-        INITECH-WRK139
-        INITECH-WEBIIS
-        INITECH-AD
-        INITECH-EXCHANG
-        INITECH-FILE1
-        INITECH-FILE2            (no malicious activity but accessed during this time)
INITECH-WRK137       (no malicious activity but accessed during this time)
Actor IP addresses and/or domains 
-        52.86.45.171
-        10.3.0.80   
-        3.228.237.193
Adversary identification based on TTPs/IOCs/IOAs observed 
    - EMISSARY PANDA 
-        Gains access to the machine using a malicious HTA which downloads and executes Hyperbro, 
Sysupdate.exe also helpful to ID them
Compromised user accounts
-        milton.waddams
-        leonard.katzman
9b59882.exe - Able Desktop / Hyperbro 
- MD5 Hash: e346480dee921d101311e5b1026bf9ed
- SHA256 Hash: 07f87f7b3313acd772f77d35d11fc12d3eb7ca1a2cd7e5cef810f9fb657694a0
- VirusTotal Link:  https://www.virustotal.com/gui/file/07f87f7b3313acd772f77d35d11fc12d3eb7ca1a2cd7e5cef810f9fb657694a0
 
Ckatz64.exe - MimiKatz            
- MD5 Hash:  491bd07773b80cd07e9705900c63d51b
                                    - SHA256 Hash: fedd3df503d4c985954dd90954e6cd1ce7739598d977f733db27e6e39c21cd52
                                    - VirusTotal link: https://www.virustotal.com/gui/file/fedd3df503d4c985954dd90954e6cd1ce7739598d977f733db27e6e39c21cd52
- Hybrid Analysis: https://www.hybrid-analysis.com/sample/fedd3df503d4c985954dd90954e6cd1ce7739598d977f733db27e6e39c21cd52
Sysupdate.exe - Bronze Union  
- MD5 Hash:              c8d83840b96f5a186e7bb6320e998f72
                                    - SHA256 Hash:        938f32822c1a6b1140ac0af60a06ae39011464de37c511921d8a7d9c6a69c9df
                                    - VirusTotal link: https://www.virustotal.com/gui/file/938f32822c1a6b1140ac0af60a06ae39011464de37c511921d8a7d9c6a69c9df
- Hybrid Analysis: https://www.hybrid-analysis.com/sample/938f32822c1a6b1140ac0af60a06ae39011464de37c511921d8a7d9c6a69c9df
 
Sysupdate-938.exe - Bronze Union            
- MD5 Hash:  C8d83840b96f5a186e7bb6320e998f72
                                    - SHA256 Hash:938f32822c1a6b1140ac0af60a06ae39011464de37c511921d8a7d9c6a69c9df
                                    - VirusTotal link:        https://www.virustotal.com/gui/file/938f32822c1a6b1140ac0af60a06ae39011464de37c511921d8a7d9c6a69c9df/detection
- Hybrid Analysis: https://www.hybrid-analysis.com/sample/938f32822c1a6b1140ac0af60a06ae39011464de37c511921d8a7d9c6a69c9df

Sysupdate-770.exe - Bronze Union
- MD5 Hash:  Ef41da16fdedcc450d0cc6ca708a9222
                                    - SHA256 Hash:  0777fa4832ecf164029e23d0125b4fdc87e2f46ffc4e1badd6a45cf5be721660
                                    - VirusTotal Link:  https://www.virustotal.com/gui/file/0777fa4832ecf164029e23d0125b4fdc87e2f46ffc4e1badd6a45cf5be721660
- Hybrid Analysis: https://www.hybrid-analysis.com/sample/006569f0a7e501e58fe15a4323eedc08f9865239131b28dc5f95f750b4767b38/5fcdd3b90bc9111ac32acd9b
kwpsinvfy.exe - WPS Office Module
- MD5 Hash:  48bc44a21a7a52a9d0d22050bae0e3e5
                                    - SHA256 Hash: 0d180ba0d1f450ea814372da06a0f6ca35ee91a74ec49b3bdf9e3bc68342b9ae
                                    - VirusTotal Link:  https://www.virustotal.com/gui/file/0d180ba0d1f450ea814372da06a0f6ca35ee91a74ec49b3bdf9e3bc68342b9ae/details
                                    - Hybrid Analysis: https://www.hybrid-analysis.com/sample/0d180ba0d1f450ea814372da06a0f6ca35ee91a74ec49b3bdf9e3bc68342b9ae?environmentId=120
2023SwinglineCatalog.exe - Payload for beacon from email
- MD5 Hash:  ce45134235707fc02d7e6cb3564e9f6b
                                    - SHA256 Hash: 41e55c1e3cbd95af63045f46ccd7d7d23e6da1d3690f05fa62ac5b13ee867af2




saved queries from environment

events/network
```
#event_simpleName=NetworkConnectIP4 RemoteAddressIP4=52.86.45.171| join(query={#event_simpleName=ProcessRollup2}, field=[ContextProcessId], key=TargetProcessId, include=[FileName], mode=left)|groupBy([ComputerName, FileName, UserName])
```

Find SwinglineCatalog.exe and make URL for Indicator Graph for Output

```
// Returning events for Process Executions of 2023SwinglineCatalog.exe Case-Insensitive 
//#event_simpleName=ProcessRollup2| FileName=/SwinglineCatalog\.exe/i OR OriginalFilename=/SwinglineCatalog.exe\.exe/i // Formatting that time so we can read it //|time := formatTime("%Y/%m/%d %H:%M:%S", field=@timestamp, locale=en_US, timezone=Z)// Grouping by Hash with a distinct count and renaming it inline and collecting various fields //| groupBy([SHA256HashData], function=([collect([time, FileName, OriginalFilename, FileVersion, ComputerName, UserName, CompanyName]), count(aid, distinct=true, as=EndpointCount)]))// Indicator Graph; uncomment correct cloud //| rootURL  := "https://falcon.crowdstrike.com/"//rootURL  := "https://falcon.laggar.gcw.crowdstrike.com/"//rootURL  := "https://falcon.eu-1.crowdstrike.com/"//rootURL  := "https://falcon.us-2.crowdstrike.com/"// Rebuilding the URL https://library.humio.com/data-analysis/functions-format.html#query-function-format-format-format // | colon := "%3A" | tick  := "%27" | plus  := "%2B"| format("[Indicator Graph](%sintelligence/graph?indicators=hash%s%s%s%s)", field=["rootURL", "colon", "tick", "SHA256HashData", "tick"], as="Indicator Graph")//Dropping the extra fields used to build the URL https://library.humio.com/data-analysis/functions-drop.html //| drop([colon, plus, rootURL, tick])
```

hosts with ips
```
#event_simpleName=AgentOnline|rename(field="ComputerName", as="RemoteHostConnected")
```

Indicator/Remote Access Graph with execution time - Ferg
```
// Returning events for Process Execution with Network connections and URL links//#event_simpleName=ProcessRollup2 FileName=?ConnectExe  | join({#event_simpleName=NetworkConnectIP4}, field=[TargetProcessId], key=[ContextProcessId], include=[RemoteAddressIP4])| join({$"Host with IPs"()}, field=[RemoteAddressIP4], key=[LocalAddressIP4], include=[RemoteHostConnected, ContextTimeStamp])// Formatting that time so we can read it //| ContextTimeStamp:=ContextTimeStamp*1000| time:=formatTime(format="%m/%d/%Y %H:%M:%S", field=ContextTimeStamp, timezone="Zulu")// Grouping by Hash with a distinct count and renaming it inline and collecting various fields ////| groupBy([SHA256HashData], function=([collect([time, RemoteAddressIP4, RemoteHostConnected, FileName, OriginalFilename, FileVersion, ClientComputerName, UserName, ComputerName]), count(aid, distinct=true, as=EndpointCount)]))| table([SHA256HashData, time, FileName, OriginalFilename, FileVersion, ClientComputerName, UserName, ComputerName, RemoteAddressIP4, RemoteHostConnected], limit=20000)// Indicator Graph; uncomment correct cloud //| rootURL  := "https://falcon.crowdstrike.com/"//rootURL  := "https://falcon.laggar.gcw.crowdstrike.com/"//rootURL  := "https://falcon.eu-1.crowdstrike.com/"//rootURL  := "https://falcon.us-2.crowdstrike.com/"// Rebuilding the URL https://library.humio.com/data-analysis/functions-format.html#query-function-format-format-format // | colon := "%3A" | tick  := "%27" | plus  := "%2B" | cont := "%2C"| format("[Indicator Graph](%sintelligence/graph?indicators=ip%s%s%s%s%shash%s%s%s%s)", field=["rootURL","colon","tick","RemoteAddressIP4","tick", "cont","colon","tick","SHA256HashData","tick"], as="Indicator Graph")| format("[Remote Access Graph](%s/investigate/remote-access-graph?timeRange=last30Days&userName=%s)", field=["rootURL","UserName"], as="Remote Access Graph")//Dropping the extra fields used to build the URL https://library.humio.com/data-analysis/functions-drop.html //| drop([colon, plus, rootURL, tick, cont])

```

Process Execution with Network connections and URL links
```
// Returning events for Process Execution with Network connections and URL links//#event_simpleName=ProcessRollup2 FileName=?ConnectExe  | join({#event_simpleName=NetworkConnectIP4}, field=[TargetProcessId], key=[ContextProcessId], include=[RemoteAddressIP4])| join({$"Host with IPs"()}, field=[RemoteAddressIP4], key=[LocalAddressIP4], include=[RemoteHostConnected])// Formatting that time so we can read it //|time := formatTime("%Y/%m/%d %H:%M:%S", field=@timestamp, locale=en_US, timezone=Z)// Grouping by Hash with a distinct count and renaming it inline and collecting various fields ////| groupBy([SHA256HashData], function=([collect([time, RemoteAddressIP4, RemoteHostConnected, FileName, OriginalFilename, FileVersion, ClientComputerName, UserName, ComputerName]), count(aid, distinct=true, as=EndpointCount)]))| table([SHA256HashData, time, RemoteAddressIP4, RemoteHostConnected, FileName, OriginalFilename, FileVersion, ClientComputerName, UserName, ComputerName], limit=20000)// Indicator Graph; uncomment correct cloud //| rootURL  := "https://falcon.crowdstrike.com/"//rootURL  := "https://falcon.laggar.gcw.crowdstrike.com/"//rootURL  := "https://falcon.eu-1.crowdstrike.com/"//rootURL  := "https://falcon.us-2.crowdstrike.com/"// Rebuilding the URL https://library.humio.com/data-analysis/functions-format.html#query-function-format-format-format // | colon := "%3A" | tick  := "%27" | plus  := "%2B" | cont := "%2C"| format("[Indicator Graph](%sintelligence/graph?indicators=ip%s%s%s%s%shash%s%s%s%s)", field=["rootURL","colon","tick","RemoteAddressIP4","tick", "cont","colon","tick","SHA256HashData","tick"], as="Indicator Graph")| format("[Remote Access Graph](%s/investigate/remote-access-graph?timeRange=last30Days&userName=%s)", field=["rootURL","UserName"], as="Remote Access Graph")//Dropping the extra fields used to build the URL https://library.humio.com/data-analysis/functions-drop.html //| drop([colon, plus, rootURL, tick, cont])

```

Quick Internal IP Lookup
```
#event_simpleName=AgentOnline LocalIP=?IP| groupBy([ComputerName,LocalIP], function= [])

```

Showing the RemoteIPs associated with the Remote Hosts

```
// Returning events for Process Executions of mstsc.exe Case-Insensitive //#event_simpleName=ProcessRollup2 FileName=/^mstsc\.exe/i  | join({#event_simpleName=NetworkConnectIP4}, field=[TargetProcessId], key=[ContextProcessId], include=[RemoteAddressIP4], mode=left)| join({$"Host with IPs"()}, field=[RemoteAddressIP4], key=[LocalAddressIP4], include=[RemoteHostConnected], mode=left)// Formatting that time so we can read it //|time := formatTime("%Y/%m/%d %H:%M:%S", field=@timestamp, locale=en_US, timezone=Z)// Grouping by Hash with a distinct count and renaming it inline and collecting various fields //| groupBy([SHA256HashData], function=([collect([time, RemoteAddressIP4, RemoteHostConnected, FileName, OriginalFilename, FileVersion, ClientComputerName, UserName, ComputerName]), count(aid, distinct=true, as=EndpointCount)]))// Indicator Graph; uncomment correct cloud //| rootURL  := "https://falcon.crowdstrike.com/"//rootURL  := "https://falcon.laggar.gcw.crowdstrike.com/"//rootURL  := "https://falcon.eu-1.crowdstrike.com/"//rootURL  := "https://falcon.us-2.crowdstrike.com/"// Rebuilding the URL https://library.humio.com/data-analysis/functions-format.html#query-function-format-format-format // | colon := "%3A" | tick  := "%27" | plus  := "%2B"| format("[Indicator Graph](%sintelligence/graph?indicators=hash%s%s%s%s)", field=["rootURL", "colon", "tick", "SHA256HashData", "tick"], as="Indicator Graph")//Dropping the extra fields used to build the URL https://library.humio.com/data-analysis/functions-drop.html //| drop([colon, plus, rootURL, tick])

```

3.2
```
#event_simpleName=NetworkConnectIP4 RemoteAddressIP4=/^(10\.|192\.168\.|172\.1[6-9]\.|172\.2[09]\.|172\.3[0-1]\.|127\.)/ | join({#event_simpleName=ProcessRollup2}, field=[ContextProcessId], key=TargetProcessId, include=[FileName, CommandLine], mode=left)|groupBy([ComputerName],function=collect([FileName]))
```

Fergs big Query
```s
#repo=unitingcare-queensland
// Returning events for Process Execution with Network connections and URL links//
#event_simpleName=ProcessRollup2
| join({#event_simpleName=NetworkConnectIP4}, field=[TargetProcessId], key=[ContextProcessId], include=[RemoteAddressIP4])
| join({#event_simpleName=AgentOnline|rename(field="ComputerName", as="RemoteHostConnected")}, field=[RemoteAddressIP4], key=[LocalAddressIP4], include=[RemoteHostConnected, ContextTimeStamp], mode=left)
// Formatting that time so we can read it //
| ContextTimeStamp:=ContextTimeStamp*1000| time:=formatTime(format="%m/%d/%Y %H:%M:%S", field=ContextTimeStamp, timezone="Zulu")
//Checking for Detections
| case{        
        TreeId = *          | EventDetails:= "Detections Found";        
        *                   | EventDetails:= "No Detections Found";        
}
// Tabling our output //
| table([aid, TargetProcessId,SHA256HashData, time, FileName, OriginalFilename, FileVersion, ClientComputerName, UserName, ComputerName, LocalAddressIP4, RemoteAddressIP4, RemoteHostConnected, EventDetails], sortby=EventDetails,limit=20000, order=asc)
// Indicator Graph; uncomment correct cloud //
//| rootURL  := "https://falcon.crowdstrike.com/"
//rootURL  := "https://falcon.laggar.gcw.crowdstrike.com/"
//rootURL  := "https://falcon.eu-1.crowdstrike.com/"
| rootURL  := "https://falcon.us-2.crowdstrike.com/"
// Rebuilding the URL https://library.humio.com/data-analysis/functions-format.html#query-function-format-format-format // 
| colon := "%3A" | semicolon := "%3B" | tick  := "%27" | plus  := "%2B" | cont := "%2C"| format("[Process Tree View](%s/graphs/process-explorer/tree?id=pid:%s:%s)", field=["rootURL","aid", "TargetProcessId"], as="Process Tree View")
| format("[Indicator Graph](%sintelligence/graph?indicators=ip%s%s%s%s%shash%s%s%s%s)", field=["rootURL","colon","tick","RemoteAddressIP4","tick", "cont","colon","tick","SHA256HashData","tick"], as="Indicator Graph")
| format("[Remote Access Graph](%s/investigate/remote-access-graph?timeRange=last30Days&userName=%s)", field=["rootURL","UserName"], as="Remote Access Graph")
| format("[IP Address Report](%s/investigate/dashboards/ip-search?destip=%s&isLive=false&sharedTime=true&sourceip=%s&start=1y)", field=["rootURL","RemoteAddressIP4", "LocalAddressIP4"], as="IP Address Report")
//Dropping the extra fields used to build the URL https://library.humio.com/data-analysis/functions-drop.html //
| drop([colon, semicolon, plus, rootURL, tick, cont])

```

ips to hostnames - ferg
```
/*What are the computernames for those Internal IPs ReferencesTimeFormat Function - https://library.humio.com/data-analysis/functions-formattime.html#table_javatimeformatIN Function         - https://library.humio.com/data-analysis/functions-in.htmlgroupBy Function    - https://library.humio.com/data-analysis/functions-groupby.html*/#event_simpleName=AgentOnline| in(field="LocalIP", values=[10.2.1.137,10.2.1.116,10.2.1.124,10.2.1.120,10.2.1.4,10.2.1.26,10.2.1.25,10.2.1.5])| ContextTimeStamp:=ContextTimeStamp*1000| ContextTimeStamp:=formatTime(format="%m/%d/%Y %H:%M:%S", field=ContextTimeStamp, timezone="CST")| groupBy([ComputerName,LocalIP], function=collect([ContextTimeStamp]))
```

mimikatz
```
regex(?Detection, field=DetectName, flags=i)| rename(field="TreeId", as="Detection Tree Id")| groupBy([ComputerName], function=collect([CommandLine, ParentProcessId, TargetProcessId, SHA256String, Severity, "Detection Tree Id", FalconHostLink]))
```

task1-1-nitin

```
#event_simpleName = ProcessRollup2 FileName=*.exe UserName!="DWM*" UserName!="UMFD*" UserName!="*$"|groupBy([UserName, ComputerName, FileName, CommandLine])|sort([_count])
```

winrar
```
#event_simpleName=ProcessRollup2 FileName=/.*rar\.exe.*/i| table([@timestamp, ComputerName, UserName, FileName, FilePath])
```

wmi-persistance
```
ComputerName=REYNHOLM-WRK137 WMI-Persistence| "#event_simpleName" = ScriptControlDetectInfo

```

failed logins
```
// Make UserNames all lowercase.| lower(UserName, as=UserName)// Make working with events easier and setting auth status| case {     #event_simpleName=UserLogonFailed2       | authStatus:="F" ;     #event_simpleName=UserLogon       | authStatus:="S" ;  }// Run a series that makes sure everything is in order and starts with a failure and ends with a success within timeframe. // Change your timeframes here within maxpause and maxduration. | groupBy([UserName, aip], function=series(authStatus, separator="", endmatch={authStatus=S}, maxpause=15min, maxduration=15min, memlimit=1024), limit=max)| authStatus=/F*S/i| failedLoginCount:=length("authStatus")-1
```

sus user
```
timeChart(series=UserName, span=1h)
```

fergalicious
```
#repo=base_sensor cid="*" | in(#event_simpleName, values=[ProcessRollup2, SyntheticProcessRollup2]) | in(aid, values=["0e05b927e42346848b12caa677140742"], ignoreCase=true) | commandLine := rename(CommandLine) | commandLine =~ wildcard(*, ignoreCase=true) | match("falcon/investigate/recon_apps.csv", field=FileName, include=[FileName]) | filename := rename(FileName) | filename=~wildcard("cmd.exe", ignoreCase=true) | !in(filename, values=[NONE], ignoreCase=true) | !in(commandLine, values=[NONE], ignoreCase=true) | event_platform match {    "Win" => username := UserName;    * => username := UserPrincipal;} | timestamp := formatTime("%FT%TZ", field=timestamp) | ContextTimeStamp := parseTimestamp(field=ContextTimeStamp, format=seconds) | contextTimestamp := formatTime("%FT%TZ", field=ContextTimeStamp) | ProcessStartTime := parseTimestamp(field=ProcessStartTime, format=seconds) | processStartTime := formatTime("%FT%TZ", field=ProcessStartTime) | computerName := rename(ComputerName) | parentProcessId := rename(ParentProcessId) | rawProcessId := rename(RawProcessId) | targetProcessId := rename(TargetProcessId) | table([timestamp, contextTimestamp, processStartTime, computerName, username, parentProcessId, rawProcessId, targetProcessId, filename, commandLine, aid, cid], limit=20000) | sort(processStartTime, type=any, order=desc, limit=20000) 
```

host with ips
```
#event_simpleName=NetworkConnectIP4|rename(field="ComputerName", as="RemoteHostConnected")
```

Indicator G and Remote Access G
```
// Returning events for Process Execution with Network connections and URL links//#event_simpleName=ProcessRollup2 FileName=?ConnectExe  | join({#event_simpleName=NetworkConnectIP4}, field=[TargetProcessId], key=[ContextProcessId], include=[RemoteAddressIP4])| join({$"Host with IPs"()}, field=[RemoteAddressIP4], key=[LocalAddressIP4], include=[RemoteHostConnected])// Formatting that time so we can read it //|time := formatTime("%Y/%m/%d %H:%M:%S", field=@timestamp, locale=en_US, timezone=Z)// Grouping by Hash with a distinct count and renaming it inline and collecting various fields ////| groupBy([SHA256HashData], function=([collect([time, RemoteAddressIP4, RemoteHostConnected, FileName, OriginalFilename, FileVersion, ClientComputerName, UserName, ComputerName]), count(aid, distinct=true, as=EndpointCount)]))| table([SHA256HashData, time, RemoteAddressIP4, RemoteHostConnected, FileName, OriginalFilename, FileVersion, ClientComputerName, UserName, ComputerName], limit=20000)// Indicator Graph; uncomment correct cloud //| rootURL  := "https://falcon.crowdstrike.com/"//rootURL  := "https://falcon.laggar.gcw.crowdstrike.com/"//rootURL  := "https://falcon.eu-1.crowdstrike.com/"//rootURL  := "https://falcon.us-2.crowdstrike.com/"// Rebuilding the URL https://library.humio.com/data-analysis/functions-format.html#query-function-format-format-format // | colon := "%3A" | tick  := "%27" | plus  := "%2B" | cont := "%2C"| format("[Indicator Graph](%sintelligence/graph?indicators=ip%s%s%s%s%shash%s%s%s%s)", field=["rootURL","colon","tick","RemoteAddressIP4","tick", "cont","colon","tick","SHA256HashData","tick"], as="Indicator Graph")| format("[Remote Access Graph](%s/investigate/remote-access-graph?timeRange=last30Days&userName=%s)", field=["rootURL","UserName"], as="Remote Access Graph")//Dropping the extra fields used to build the URL https://library.humio.com/data-analysis/functions-drop.html //| drop([colon, plus, rootURL, tick, cont])
```

Process Executions of c.exe with Indicator Graph Link
```
// Returning events for Process Executions of c.exe Case-Insensitive //#event_simpleName=ProcessRollup2| FileName=/^c\.exe/i OR OriginalFilename=/^c\.exe/i// Grouping by Hash with a distinct count and renaming it inline and collecting various fields //| groupBy([SHA256HashData], function=([collect([FileName, OriginalFilename, FileVersion, CompanyName]), count(aid, distinct=true, as=EndpointCount)]))// Indicator Graph; uncomment correct cloud //| rootURL  := "https://falcon.crowdstrike.com/"//rootURL  := "https://falcon.laggar.gcw.crowdstrike.com/"//rootURL  := "https://falcon.eu-1.crowdstrike.com/"//rootURL  := "https://falcon.us-2.crowdstrike.com/"// Rebuilding the URL https://library.humio.com/data-analysis/functions-format.html#query-function-format-format-format // | colon := "%3A" | tick  := "%27" | plus  := "%2B"| format("[Indicator Graph](%sintelligence/graph?indicators=hash%s%s%s%s)", field=["rootURL", "colon", "tick", "SHA256HashData", "tick"], as="Indicator Graph")//Dropping the extra fields used to build the URL https://library.humio.com/data-analysis/functions-drop.html //| drop([colon, plus, rootURL, tick])
```



