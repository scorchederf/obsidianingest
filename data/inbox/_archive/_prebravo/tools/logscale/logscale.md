


# search for *.ru and *.cn domain names being requested
```
in(fqdn,values=["*.ru", "*.cn"])
| groupby(field=[fqdn,srcipaddress,protocol])
```


# limit number of results using sort
```
in(fqdn,values=["*.ru", "*.cn"])
| groupby(field=[fqdn,resolvedhostname], function=count()) | sort(field=_count, limit=20)
```

# get a count of all the repos
```
groupby(field=#repo)
```

# time chart of count of records in repos for every 5 minutes
```
timeChart(span=15m, function=count(), series=#repo)
```

# custom output using case
```
astein OR adm_astein
| case { 	
	#repo = ucq-palofirewall | format("%s from %s:%s to %s:%s",field=[Type,SourceIP,SourcePort, DestinationIP, DestinationPort],as=output) ; 
	#repo = ucq-ad | splitString(field=@rawstring, by = "\n") | format("eventid=%s | action=%s", field=[#windows.EventID , _splitstring[0]], as=output);
    "BOOO NOT HANDLED"
}
| table([@timestamp, #repo, output])
```

# worldmap 
tick the live view to refresh results automatically
```
#repo = "ucq-palofirewall"
| worldMap(ip=DestinationIP)
```


```

```
