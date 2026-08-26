# sentinel


## exchange activity on account
```kql
let upn = "Lisa.Negrello@uccommunity.org.au";
let cutoff = ago(30d); // datetime 
OfficeActivity
| where TimeGenerated > cutoff 
| where UserId like upn
| extend Path_ = tostring(parse_json(Folders)[0].Path) 
| extend Subject_ = tostring(parse_json(Item).Subject)
| extend ExchangeObject = strcat("", strcat(Path_, Subject_))
| summarize by TimeGenerated, OfficeWorkload, RecordType, Operation, ExchangeObject, OfficeObjectId


```