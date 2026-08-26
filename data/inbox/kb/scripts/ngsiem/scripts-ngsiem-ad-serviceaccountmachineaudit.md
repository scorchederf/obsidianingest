---
aliases:
tags:
---
[[microsoft-activedirectory]] [[crowdstrike-ngsiem]]

Shows a list of endpoints that a service account /svc_/i has logged into

```
$ucq-repo-ad()

| windows.EventID = 4624        //A user successfully logged on to a computer. For information about the type of logon

| windows.EventData.TargetUserName = /svc_/i      // *svc*

| windows.EventData.WorkstationName != "-"

| groupBy([windows.EventData.TargetUserName], function=[

  count(windows.EventData.WorkstationName, distinct=true),

  collect(windows.EventData.WorkstationName, separator=",")

])

| drop(_count)
```