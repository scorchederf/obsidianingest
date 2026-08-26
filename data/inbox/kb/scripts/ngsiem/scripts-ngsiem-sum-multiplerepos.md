---
aliases:
tags:
source:
desc:
---
# sum totals from multiple cases (could be repos)


```
| #Vendor=abnormal OR #repo = /mimecast/i
| case {
    #Vendor=abnormal | attackType := Vendor.messages.attackType | attackType := Vendor.attackType | attackType != /Spam/i | inc:=1;
    #repo = /mimecast/i | event.action = rej | inc:=1;
    #repo = /mimecast/i | Vendor.virusFound = /malware/i | inc:=1
}
| count(inc)
```