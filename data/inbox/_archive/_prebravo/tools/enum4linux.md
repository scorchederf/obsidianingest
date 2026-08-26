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
  - -U      only show usernames

```shell
# start the service
sudo systemctrl start apache2

# watch traffic on the apache2 access log
sudo watch -n 5 cat /var/log/apache2/access.log

```
