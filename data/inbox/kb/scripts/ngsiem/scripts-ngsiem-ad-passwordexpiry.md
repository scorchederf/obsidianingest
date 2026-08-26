---
aliases:
tags:
---
[[microsoft-activedirectory]] [[crowdstrike-ngsiem]]
# Shows users who have had their password expiry disabled or enabled

```
$ucq-repo-ad()

| windows.EventID = 5136                      //5136:   A directory service object was modified https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=5136

| windows.EventData.AttributeValue = 66048    //66048:  Password Doesn't Expire https://jackstromberg.com/2013/01/useraccountcontrol-attributeflag-values/

| case {

    //https://jackstromberg.com/2013/01/useraccountcontrol-attributeflag-values/

    windows.EventData.OperationType = %%14674 | windows.EventData.OperationTypeString := "added"; // Value Added – new value added ('%%14674')

    windows.EventData.OperationType = %%14675 | windows.EventData.OperationTypeString := "deleted"; // Value Deleted – value deleted ('%%14675', typically “Value Deleted” is a part of change operation).

    * | windows.EventData.OperationTypeString = "unknown";

}

| groupBy([@timestamp, windows.EventData.DSName, windows.EventData.ObjectDN, windows.EventData.SubjectDomainName, windows.EventData.SubjectUserName, windows.EventData.OperationTypeString])

| drop([_count])
```

