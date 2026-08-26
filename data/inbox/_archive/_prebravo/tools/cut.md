---
id: tools-cut
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-cut

backlinks: [[]]

sources:

---
*** CUT ONLY ACCEPTS 1 CHAR FIELD DELIMITER - AWK ALLOWS MULTIPLE ***

Cut is used to extract a section of text from a line and output it to the standard output.

- -f field number
- -d field delimiter

```shell
echo "I hack binaries,web apps,mobile apps, and just about anything else"| cut -f 2 -d ","
web apps

# get the usernames out of the /etc/passwd file
cut -d ":" -f 1 /etc/passwd
geoclue
Debian-snmp
sslh
ntpsec
redsocks
rwhod
```