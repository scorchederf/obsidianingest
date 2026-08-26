---
id: tools-host
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-apache2

backlinks: [[]]

sources:

---

host command in Linux system is used for DNS (Domain Name System) lookup operations.

if command returns (NXDOMAIN) it means the hostname does not exist


```shell
#a records
host www.megacorpone.com
www.megacorpone.com has address 38.100.193.76

#mx records
host -t mx megacorpone.com

#txt records
host -t txt megacorpone.com


```