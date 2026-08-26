---
title: Hack The Box - Academy Module 147 Section 1638
aliases: []
tags:
- topic/hack-the-box-academy
- topic/active-enumeration
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 10-147-passwordattacks-13-passthehash.pdf
related_tools:
- '[[nmap-1787746090]]'
- '[[nikto]]'
- '[[dirb]]'
- '[[wpscan]]'
- '[[sqlmap]]'
- '[[john]]'
related_techniques:
- '[[t1003]]'
- '[[t1008]]'
- '[[t1020]]'
related_tactics:
- '[[ta0003]]'
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

# Hack The Box - Academy Module 147 Section 1638

## Introduction
This section covers the techniques and tools used to enumerate and exploit a target system in the context of the Hack The Box Academy module 147, section 1638.

## Active Enumeration
The active enumeration phase involves using tools like `nmap` and `nikto` to gather information about the target system. The following commands are used:

```bash
nmap -sV -p- <target_ip>
nikto -h <target_ip>
```

These commands help in identifying open ports, services, and potential vulnerabilities.

## Directory Browsing
Directory browsing is used to find hidden directories and files. The `dirb` tool is used for this purpose:

```bash
dirb http://<target_ip>```

This command helps in discovering additional paths and directories that might contain sensitive information.

## Web Application Scanning
Web application scanning is performed using tools like `wpscan` and `sqlmap`. The following commands are used:

```bash
wpscan --url http://<target_ip>/wp-login.php
sqlmap -u http://<target_ip>/path/to/vulnerable/page```

These tools help in identifying and exploiting vulnerabilities in web applications.

## Password Cracking
Password cracking is a crucial part of the active enumeration phase. The `john` tool is used for this purpose:

```bash
john --wordlist=/path/to/wordlist <hash_file>
```

This command attempts to crack the hashes obtained from the target system.

## Techniques and Tactics
The techniques and tactics used in this module include:

- **T1003**: Establishes a connection to a remote host.
- **T1008**: Enumerates network shares and services.
- **T1020**: Exploits a web application vulnerability.

These techniques are part of the active enumeration and lateral movement tactics.

## References
- https://academy.hackthebox.com/module/147/section/1638

