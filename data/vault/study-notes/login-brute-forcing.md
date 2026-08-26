---
title: Login Brute Forcing
aliases: []
tags:
- study-notes
- tool/hydra
- tool/crackmapexec
- technique/t1003
- attack-methodologies/lateral-movement
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: 16-57-BruteForcing-08-PersonalizedWordlists.pdf
related_tools:
- '[[hydra]]'
- '[[crackmapexec]]'
related_techniques:
- '[[t1003]]'
related_tactics: []
related_services: []
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: T1003
real_path: ''
port: ''
protocol: ''
os: ''
---

# Login Brute Forcing

## Overview
This study note covers the technique of login brute forcing, which is a common method used by attackers to gain unauthorized access to systems by attempting to guess or crack user credentials. This technique is part of the MITRE ATT&CK framework under T1003, which involves the use of brute force or dictionary attacks to obtain user credentials.

## Tools Used
The following tools are commonly used for login brute forcing:

- **Hydra**: A network login cracker that supports many different services. It can be used to brute force usernames and passwords for various protocols such as SSH, FTP, HTTP, and more.

- **CrackMapExec**: A tool that can be used to perform brute force attacks against network services like SMB, LDAP, and others. It can also be used to enumerate users and groups on Windows domain controllers.

## Techniques
The technique of login brute forcing involves the following steps:

1. **Identify the Target**: Determine the service or protocol that needs to be brute forced, such as SSH, FTP, or SMB.
2. **Gather Credentials**: Use tools like `hydra` or `crackmapexec` to attempt to brute force the credentials. These tools can use wordlists or dictionaries to try different combinations of usernames and passwords.
3. **Monitor for Success**: Keep an eye on the output to see if any successful login attempts are made. This can be done by monitoring the console output or using logging mechanisms.

## Example Commands
Here are some example commands for using `hydra` and `crackmapexec` for brute forcing:

- **Hydra Example**:
```
hydra -L usernames.txt -P passwords.txt -V -t 4 ssh://192.168.1.100
```

- **CrackMapExec Example**:
```
crackmapexec smb 192.168.1.100 -u usernames.txt -p passwords.txt
```

These commands attempt to brute force the SSH service and SMB service, respectively, using the provided usernames and passwords.

## References
- https://academy.hackthebox.com/module/57/section/512

