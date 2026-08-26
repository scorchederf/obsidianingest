Users added to active directory
```
//Create a daily summary of Azure Active Directory group additions 
let daterange=7d; 
AuditLogs 
| where TimeGenerated > ago (daterange) 
| where OperationName == "Add member to group" 
| extend Type = tostring(TargetResources[0].type) 
| where Type == "User" 
| extend GroupName = tostring(parse_json(tostring(parse_json(tostring(TargetResources[0].modifiedProperties))[1].newValue))) 
| extend UserAdded = tostring(TargetResources[0].userPrincipalName) 
| where isnotempty(UserAdded) 
| summarize GroupAdditions=make_set(UserAdded) by GroupName, startofday(TimeGenerated) 
| sort by GroupName asc, TimeGenerated desc
```
Show sign in logs for user
```
let daterange = ago(1d); 
SigninLogs 
| where TimeGenerated > daterange 
| where UserPrincipalName contains "adam.stein" 
| project TimeGenerated, Identity, AppDisplayName, ResultType, ResultDescription
```
Count of all tables
```
union withsource=sourceTable * 
| project sourceTable 
| summarize count() by sourceTable
```
Office activity by workload
```
OfficeActivity 
| summarize dcount(TimeGenerated) by OfficeWorkload
```
Search for clicks originating from outlook
```
let dateRange = ago(14d);   //LENGTH OF TIME TO SEARCH IN LOGS (d or h) 
let urlSearch = "microsoft";   //THE URL TO SEARCH FOR (CAN BE PARTIAL) 
DeviceEvents 
| where TimeGenerated > dateRange and ActionType == "BrowserLaunchedToOpenUrl" and isnotempty(RemoteUrl) 
| where InitiatingProcessFileName =~ "outlook.exe"  
  or InitiatingProcessFileName =~ "runtimebroker.exe" //RuntimeBroker.exe opens links for all apps from the Windows store  
| where RemoteUrl contains urlSearch 
| project TimeGenerated, UserPrincipalName = InitiatingProcessAccountUpn, DeviceName, RemoteUrl, InitiatingProcessFileName
```
OneDrive download activity
```
let daterange = ago(10d); 
let upn = "adam.stein@premiers.qld.gov.au"; 
OfficeActivity 
| where TimeGenerated > daterange 
| where UserId == upn 
| where Operation == "FileDownloaded"       //onedrive files downloaded
```
Search for hash
```
let _timeBin = 1h; 
let _daterange = ago(10d); 
let _hash = "8627c192f7c23f2ad709d6798f58e7d8690908e7"; 
DeviceFileEvents 
| where TimeGenerated > _daterange 
| where MD5 contains _hash or SHA1 contains _hash or SHA256 contains _hash
```
Sign in activity
```
let daterange = ago(500m);  
let upns = dynamic(['adam.stein@ucareqld.com.au', 'edward.mccabe@ucareqld.com.au']); 
 SigninLogs  
| where TimeGenerated > daterange  
| where UserPrincipalName in(upns) 
| project TimeGenerated, UserPrincipalName, ClientAppUsed, AppDisplayName, Country = LocationDetails.countryOrRegion, State = LocationDetails.state, City = LocationDetails.city,  
DeviceName = DeviceDetail.displayName, StatusAdditionalDetails = Status.additionalDetails, RiskDetail, RiskLevelDuringSignIn, UserType
```
Office Mail Forwarding
```
OfficeActivity
  | where (Operation =~ "Set-Mailbox" and Parameters contains 'ForwardingSmtpAddress') 
  or (Operation in~ ('New-InboxRule','Set-InboxRule') and (Parameters contains 'ForwardTo' or Parameters contains 'RedirectTo'))
  | extend parsed=parse_json(Parameters)
  | extend fwdingDestination_initial = (iif(Operation=~"Set-Mailbox", tostring(parsed[1].Value), tostring(parsed[2].Value)))
  | where isnotempty(fwdingDestination_initial)
  | extend fwdingDestination = iff(fwdingDestination_initial has "smtp", (split(fwdingDestination_initial,":")[1]), fwdingDestination_initial )
  | parse fwdingDestination with * '@' ForwardedtoDomain 
  | parse UserId with *'@' UserDomain
  | extend subDomain = ((split(strcat(tostring(split(UserDomain, '.')[-2]),'.',tostring(split(UserDomain, '.')[-1])), '.') [0]))
  | where ForwardedtoDomain !contains subDomain
  | extend Result = iff( ForwardedtoDomain != UserDomain ,"Mailbox rule created to forward to External Domain", "Forward rule for Internal domain")
  | extend ClientIPAddress = case( ClientIP has ".", tostring(split(ClientIP,":")[0]), ClientIP has "[", tostring(trim_start(@'[[]',tostring(split(ClientIP,"]")[0]))), ClientIP )
  | extend Port = case(
  ClientIP has ".", (split(ClientIP,":")[1]),
  ClientIP has "[", tostring(split(ClientIP,"]:")[1]),
  ClientIP
  )
  | project TimeGenerated, UserId, UserDomain, subDomain, Operation, ForwardedtoDomain, ClientIPAddress, Result, Port, OriginatingServer, OfficeObjectId, fwdingDestination
  | extend timestamp = TimeGenerated, AccountCustomEntity = UserId, IPCustomEntity = ClientIPAddress, HostCustomEntity = OriginatingServer
```
Self service password resets
```
let daterange=30d; 
let tBin = 1d;
AuditLogs 
| where TimeGenerated > ago (daterange) 
| where LoggedByService == "Self-service Password Management"
| extend UserPrincipalName = tostring(InitiatedBy.user.userPrincipalName) 
| project
    TimeGenerated,
    OperationName,
    UserPrincipalName,
    Result,
    ResultDescription,
    ActivityDisplayName
| order by TimeGenerated
```
Date filter
```
OfficeActivity
| where TimeGenerated between (datetime('2022-11-09 00:00') .. datetime('2022-11-10 00:00'))
```

