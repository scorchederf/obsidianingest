---
id: tools-apache2
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-burpsuite

backlinks: [[]]

sources:

---

FoxyProxy Basic 


- ensure certificate is unique
  - Proxy > Options > Proxy Listeners in BurpSuite and click Regenerate CA certificate
  - close and restart
  - browse to http://burp to get link for certificate, then import via firefox settings - view certificate
  - 
- intruder is used for brute forcing
- repeater 

```shell
# start the service
sudo systemctrl start apache2

# watch traffic on the apache2 access log
sudo watch -n 5 cat /var/log/apache2/access.log

```
