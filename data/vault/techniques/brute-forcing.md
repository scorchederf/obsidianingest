---
title: Brute Forcing
aliases: []
tags:
- technique/t1110
- technique/t1003
- tool/hydra
- tool/medusa
category: techniques
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: bruteforcing.md
related_tools:
- '[[hydra]]'
- '[[medusa]]'
related_techniques:
- '[[t1110]]'
- '[[t1003]]'
related_tactics:
- '[[ta0003]]'
related_services: []
related_os: []
related_notes: []
mitre_tactic: TA0003
mitre_technique: T1110
real_path: ''
port: ''
protocol: ''
os: ''
---

# Brute Forcing

## Overview
Brute forcing is a technique used to gain unauthorized access to systems by attempting to guess or exhaustively try all possible combinations of usernames and passwords. This technique is often used to exploit weak or default credentials.

Two commonly used tools for brute forcing are `hydra` and `medusa`.

## Hydra
Hydra is a powerful network login cracker that supports a wide variety of services. It can perform brute force attacks on various protocols such as HTTP, FTP, SSH, Telnet, and more.

**Usage Example**:
```bash
hydra -L usernames.txt -P passwords.txt -vV -t 4 http_login
```

- `-L usernames.txt`: Specifies the file containing usernames.
- `-P passwords.txt`: Specifies the file containing passwords.
- `-vV`: Verbose mode with version information.
- `-t 4`: Specifies the number of threads to use.

## Medusa
Medusa is a network authentication cracker that supports a wide range of protocols. It can be used to brute force usernames and passwords for various services.

**Usage Example**:
```bash
medusa -h 192.168.1.100 -u users.txt -P passwords.txt -M ssh
```

- `-h 192.168.1.100`: Specifies the target host.
- `-u users.txt`: Specifies the file containing usernames.
- `-P passwords.txt`: Specifies the file containing passwords.
- `-M ssh`: Specifies the protocol to use (in this case, SSH).

## References
- assets/attachments/kb/htb/redteam/assets/techniques/bruteforcing/16-57-BruteForcing-12-Medusa.pdf

