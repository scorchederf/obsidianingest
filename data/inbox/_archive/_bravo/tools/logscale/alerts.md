# pingsweep

```ts
/* 
Apply SIaaS_UCQ_Reconnaissance - Ping Sweep Detected on events on events which are detected by the Local system
    and when the domain is one of the following UCQ
    and when the event(s) were detected by one or more of Firewall
    and when the IP protocol is one of the following ICMP.icmp_ip
    and NOT when either the source or destination IP is one of the following 122.165.153.143, 203.23.20.50, 203.23.21.150
and when any of these BB:CategoryDefinition: Firewall or ACL Accept, BB:CategoryDefinition: Firewall or ACL Denies with the same source IP more than 99 times, across more than 99 destination IP within 1 minutes
*/
#repo = ucq-palofirewall
| in(field=domain, values=["UCQ*"])
| in(field=Protocol, values=["icmp"])
| Application = "ping"
| !in(field=SourceIP,       values=["122.165.153.143", "203.23.20.50", " 203.23.21.150", 
    "10.14.111.80",     //   UCQ-SCOM1-P001.INT.UCQ.COM.AU
    "10.14.12.66",      //   UCQ-MSPMD1-P003.INT.UCQ.COM.AU
    "10.14.121.141",    //   UCQ-SWIPAM-P001.INT.UCQ.COM.AU
    "10.14.121.79",     //   UCQ-SOLARW-P001.INT.UCQ.COM.AU
    "10.14.121.48",     //   UCQ-SOLARW-P002.INT.UCQ.COM.AU
    "10.15.112.75",     //   UCQ-SCOM2-P001.INT.UCQ.COM.AU
    "10.14.12.66",      //   UCQ-MSPMD1-P003.INT.UCQ.COM.AU
    "10.14.111.81"      //   UCQ-SCOM1-P002.INT.UCQ.COM.AU
    ])
| !in(field=DestinationIP,  values=["122.165.153.143", "203.23.20.50", " 203.23.21.150"])
| bucket(field=[SourceIP], function=count(DestinationIP), span=60s)
| parseTimestamp(field=_bucket,format=millis, as=mills)
| formatTime(format="%c", as="readabledate", field=mills, timezone="Australia/Brisbane")
| _count > 99
| table(fields=[readabledate, SourceIP, _count])


```