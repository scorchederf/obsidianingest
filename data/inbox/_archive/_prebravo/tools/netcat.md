---
id: tools-apache2
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-apache2

backlinks: [[]]

sources:

---

- flags
    - -w 5  connection timeout
    - -z    send zero data mode




Send binary from Kali to Windows
```shell

#windows listens for connecction and writes the output to binary.exe
c:\Tools\practical_tools\nc.exe -nlvp 4455 > c:\Users\offsec\Desktop\binary.exe
listening on [any] 4455 ...


#kali sends binary 
nc -w 3 10.11.0.22 4455 < binary.exe




```