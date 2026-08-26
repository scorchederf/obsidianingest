# LOG 201m: Preparing, Parsing, and Analyzing Log Data using Falcon LogScale

~timestamps are graphical in nature only, it is epoch 
https://www.epochconverter.com/

## wildcard
method="P*" or method="D*ETE"
url=*

## events without a certain field
url!=*

## groupby
statuscode >= 500 | groupBy(url)
groupBy(field="method", function=count(as="_count"))
statuscode >= 500 | groupBy(url, function=count(as="Error count"))
groupBy([url, statuscode])


## count
method=GET | count()

## average
method=GET
| avg(responsesize)

## sort
"example.com" | groupBy(method) | sort()

## transformation functions
sizeInKb := responsesize / 1000

## string replacement
// The `replace` function can replace text in field based on regular expressions. Note that it supports capturing groups.replace("/products/(.*)", field=url, replacement="[\"category\"]=$1")

## groupby
can use additional functions by specificifying them in the function field
function[sum(), max, etc]

| groupby ([field1, field2],
    function=[
        collect(["field3", "field4"]),
        sum("field1", as=sum_field1),
        avg("field2", as=avg_field2)
    ]
)

![Alt text](_archive/_prebravo/tools/logscale/image-9.png)

| groupby(field=region, function=[
    groupby(product, function=[
        sum(sales, as=totalsales),
        sum(revenue, as=totalrevenue)
    ])
])



## collect
groupby(Application, function=collect([@collect.host, Application]))
![Alt text](_archive/_prebravo/tools/logscale/image-8.png)


## arithmetic expressions
eval(x=responsesize * 2 - 100.5)

## regex
regex("/products/.+/.+ HTTP/")
/\/products\/.+\/.+ HTTP\//i

## extracting fields
regex("/products/(?<category>.+)/(?<productId>.+) HTTP/")
regex("/products/(?<category>.+)/(?<productId>.+) HTTP/") | groupBy(category)

## timechart
statuscode >= 400 and url="/products/*"| timechart(series=statuscode)
timechart(span=30s)

// This example gets creates a time chart with the P90, P95, and P99.9 of// the response size.timechart(function=percentile(field=responsesize, percentiles=[90, 95, 99.9]))

## creating test events
use the createEvents function
createEvents("this is a sample event")

## ingestion
csv is already in the row/column format so compression is minimal 
json is in keyvalue pairs
plaintext compression is good but requires custom parser
xml is not recommended due to all the additional metadata

## event fields
@id             unique field
@timestamp      required
@timezone       zulu time (recommendation to )
#repo           this is the repo where the data is stored

## field types
@   Metadata Fields start with the “@” symbol and provide essential information about each event, such as the event’s timestamp, ID, and timezone. These default fields are automatically attached during ingestion
\#  Tag Fields start with the “#” symbol and define how events are stored and indexed. We can apply tag fields at parse-time during the ingestion process. We can also apply tag fields at the log shipper
    tag fields speed up queries

user fields are not prefixed with @ and \#

## createEvents()
```
createEvents(["report_id=1 issue_reported=Crash latitude=30.309724 month=Oct year=2022 longitude=-97.733665 issue_status=ARCHIVED","report_id=2 issue_reported=Crash latitude=30.309724 month=Oct year=2022 year=2022 longitude=-97.733665 issue_status=ARCHIVED","report_id=3 issue_reported=Crash latitude=30.309724 month=Jul year=2022 longitude=-97.733665 issue_status=ARCHIVED","report_id=4 issue_reported=Crash latitude=30.309724 month=Sep year=2022 longitude=-97.733665 issue_status=ARCHIVED","report_id=5 issue_reported=Crash latitude=30.309724 month=Jan year=2022 longitude=-97.733665 issue_status=ARCHIVED","report_id=6 issue_reported=Crash latitude=30.309724 month=Sep year=2022 longitude=-97.733665 issue_status=ARCHIVED","report_id=7 issue_reported=Crash latitude=30.309724 month=Oct year=2022 longitude=-97.733665 issue_status=ARCHIVED","report_id=8 issue_reported=Crash latitude=30.309724 month=Oct year=2023 longitude=-97.733665 issue_status=ARCHIVED","report_id=9 issue_reported=Crash latitude=30.309724 month=Feb longitude=-97.733665 issue_status=ARCHIVED","report_id=10 issue_reported=Crash latitude=30.309724 month=Jul longitude=-97.733665 issue_status=ARCHIVED","report_id=11 issue_reported=Crash latitude=30.309724 month=Jul longitude=-97.733665 issue_status=ARCHIVED","report_id=12 issue_reported=Crash latitude=30.309724 month=Dec longitude=-97.733665 issue_status=ARCHIVED","report_id=13 issue_reported=Crash latitude=30.309724 month=Aug longitude=-97.733665 issue_status=ARCHIVED","report_id=14 issue_reported=Crash latitude=30.309724 month=Feb longitude=-97.733665 issue_status=ARCHIVED","report_id=15 issue_reported=Crash latitude=30.309724 month=Aug longitude=-97.733665 issue_status=ARCHIVED","report_id=16 issue_reported=Crash latitude=30.309724 month=Feb longitude=-97.733665 issue_status=ARCHIVED","report_id=17 issue_reported=Crash latitude=30.309724 month=Feb longitude=-97.733665 issue_status=ARCHIVED","report_id=18 issue_reported=Crash latitude=30.309724 month=Jun longitude=-97.733665 issue_status=ARCHIVED","report_id=19 issue_reported=Crash latitude=30.309724 month=Oct year=2024 longitude=-97.733665 issue_status=ARCHIVED","report_id=20 issue_reported=Crash latitude=30.309724 month=Jan longitude=-97.733665 issue_status=ARCHIVED","report_id=21 issue_reported=Crash latitude=30.309724 month=Feb longitude=-97.733665 issue_status=ARCHIVED","report_id=22 issue_reported=Crash latitude=30.309724 month=Oct year=2024 longitude=-97.733665 issue_status=ARCHIVED","report_id=23 issue_reported=Crash latitude=30.309724 month=Oct year=2024 longitude=-97.733665 issue_status=ARCHIVED"])
| kvParse() 
| format(format="%s,%s", field=[latitude,longitude], as=location)
| groupBy([month])
```




## exporting packages
1. go to settings
2. create a package
3. export package

## importing packages
1. go to settings
2. go to installed
3. import package



## grouping by hour buckets
| Application="icloud-base"
| bucket(30m, field=Application, function=count())
| parseTimestamp(field=_bucket,format=millis)       //this converts the _bucket to a timestamp
//| inc := counterAsRate(_count)
| table(fields=[@timestamp, Application, _count])

## difference
| Application="icloud-base"
| bucket(buckets=10, field=[Application], function=count())
| parseTimestamp(field=_bucket,format=millis)       //this converts the _bucket to a timestamp
//| table(fields=[@timestamp, Application, _count])
//| sort(field=[@timestamp, _count])
| eval(difference = (_count/100))




# data sources
autosharding 
#humioBackfill is used to ingest non-current data
    if set to true then its a historical 










![Alt text](_archive/_prebravo/tools/logscale/image-6.png)
capturing group holds a copy of the string in memory *bad*
non-capturing group good
![Alt text](_archive/_prebravo/tools/logscale/image-7.png)

regex101.com
    - private instance
    - 
regexone.com







# filtering 
```
createEvents(["event_id=1 msg=warning speed=75 timestamp=2023-04-03T12:00:00Z location=Main St temperature=85 humidity=60 status=success","event_id=2 msg=error speed=90 timestamp=2023-04-03T13:00:00Z location=1st Ave temperature=95 humidity=95 status=failed","event_id=3 msg=info speed=60 timestamp=2023-04-04T10:00:00Z location=Main St temperature=80 humidity=40 status=success","event_id=4 msg=info speed=85 timestamp=2023-04-04T09:30:00Z location=2nd St temperature=91 humidity=98 status=failed","event_id=5 msg=error speed=100 timestamp=2023-04-04T10:45:00Z location=3rd St temperature=90 humidity=99 status=failed","event_id=6 msg=warning speed=50 timestamp=2023-04-03T08:00:00Z location=Main St temperature=75 humidity=30 status=success","event_id=7 msg=info speed=40 timestamp=2023-04-02T18:00:00Z location=4th St temperature=88 humidity=45 status=success","event_id=8 msg=info speed=95 timestamp=2023-04-04T11:15:00Z location=Main St temperature=92 humidity=97 status=failed"])|kvParse() | parseTimestamp(field=timestamp, as=@timestamp)|time:year(@timestamp)|time:dayOfMonth(@timestamp)|time:hour(@timestamp)|time:minute(@timestamp)|format(format="%s:%s", field=[_hour, _minute], as="time")

// Add your test query provided above below this line; ensrue that you prefix the command with a pipe `|` character, before the function.
//1. Find all events with the words "warning" or "error" in the msg. //Events: 1, 2, 5, 6
// | msg=warning or msg=error//2. Find events with a speed greater than 80. 
//Events: 2, 4, 5, 8
// | speed > 80
//3. Identify events that happened in the last 4 years.. //Events: 1, 2, 3, 4, 5, 6, 7, 8
// | _year > 2019
//4. Search for events where the location contains "Main". //Events 1, 3, 6, 8
// | location ="*Main*"
//5. Search for events with a temperature above 90 degrees and high humidity. Note the ambiguity of humidity;
// hint: pick a humidity threshold that you hypothesize to be high. //Events Vary
//| temperature >=90 humidity >=90

```





```

"AD_SERVER_DNS_Internet"
| bucket(span=1h, field=RuleName) 
| eval(
    prvtme=_bucket + (3600000 * 1), 
    previousTotal=_count,
    pk2=concat(field=[prvtme,RuleName])
)
| join(query={
        bucket(span=1h, field=RuleName) 
        | eval(
            pk1=concat(field=[_bucket,RuleName]),
            currentTotal=_count)
        },
        field=pk2,                  //pk in primary query
        key=pk1,                    //pk in sub query
        mode=left,
        include=[currentTotal,pk1, _bucket]
)
//| rename(field="pk1", as="pkCurrentHour")
//| rename(field="pk2", as="pkPreviousHour")
| parseTimestamp(field=prvtme,format=milliseconds)
| eval(difference=(currentTotal-previousTotal))
| eval(percent=((currentTotal/previousTotal)*100)-100)
| eval(rndpercent=round(percent))
//| table(fields=[])
| table(fields=[@timestamp, RuleName, currentTotal, previousTotal, difference, pk1, pk2, rndpercent])
| sort(field=@timestamp, reverse=false)

```



```

        Severity >= "0" and Severity <= "19"  | Severity := "Info" ;
        Severity >= "20" and Severity <= "39"  | Severity := "🟢 Low" ;
        Severity >= "40" and Severity <= "59"  | Severity := "🟡 Medium" ;
        Severity >= "60" and Severity <= "79"  | Severity := "🟠 High" ;
        Severity >= "80" and Severity <= "100"  | Severity := "🔴 Critical" ;


        

| eval(icon="")

| case {
        loglevel = "INFO"  | icon := "🔵";
        loglevel = NOTICE | icon := "🟢" ;
        loglevel = WARNING | icon := "🟠" ;
        * | icon := "👾"
}
```


time:year(field=@timestamp, as=year)

## regex get field
| #repo = "ucq-dns"
//| regex(field="fqdn", regex="(<country>[^,.]*)$")
| regex("(?<country>[^,.]*)$", field=fqdn) 
| in(field=country, values=["cn", "ru"])
| groupby(fqdn)






# rules being incorrectly formated, count per day
```
RuleName = /2023\/08\//i 
| time:dayOfMonth(field=@ingesttimestamp, as=dd)
| groupby(field=[dd, @collect.host, Type])
| sort(field=dd, order=desc)
```






# draft
```
#repo="ucq-palofirewall"
| top(field=[SourceIP], limit=50)
| join(query={
        #repo="unitingcare-queensland"      //falcon
        | table(fields=[LocalAddressIP4, ComputerName])
    },
    field=SourceIP,                  //pk in primary query
    key=LocalAddressIP4,                           //pk in sub query
    include=[LocalAddressIP4,ComputerName]
)
| table(fields=[LocalAddressIP4, ComputerName, SourceIP, _count])
```



## stage 2
```
#repo="unitingcare-queensland"
| groupBy(field=[LocalAddressIP4, ComputerName])
| join(repo="ucq-palofirewall", field=LocalAddressIP4, key=SourceIP, query={ top(field=[SourceIP], limit=50)}, include=[SourceIP, _count], mode=left)
| _count > 0
| ComputerName != ""
| sort(field=_count, order=desc)
```