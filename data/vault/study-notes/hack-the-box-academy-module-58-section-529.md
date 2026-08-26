---
title: Hack The Box - Academy Module 58 Section 529
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 18-58-SQLMap-08-AdvancedDatabaseEnumeration.pdf
related_tools:
- '[[gobuster]]'
- '[[dirb]]'
- '[[nmap-1787746090]]'
- '[[nikto]]'
- '[[wpscan]]'
- '[[sqlmap]]'
- '[[john]]'
related_techniques:
- '[[t1003]]'
- '[[t1020]]'
- '[[t1132]]'
related_tactics:
- '[[ta0003]]'
- '[[ta0005]]'
related_services:
- '[[http]]'
- '[[https]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Hack The Box - Academy Module 58 Section 529

## Overview
This module covers various techniques and tools used in web application penetration testing. The focus is on identifying and exploiting vulnerabilities in web applications.

## Tools and Techniques
The following tools and techniques are discussed in the module:

- **gobuster**: A directory and file brute-forcing tool.
- **dirb**: A directory brute-forcing tool.
- **nmap**: A network scanning tool.
- **nikto**: A web server scanner.
- **wpscan**: A WordPress security scanner.
- **sqlmap**: A tool for detecting and exploiting SQL injection vulnerabilities.
- **john**: A password cracker.

Techniques covered include:

- **T1003**: Data from Local System.
- **T1020**: Security Software Identification.
- **T1132**: Security Software Discovery.

## Usage
The module provides practical examples and commands for using the above tools. For instance, the following command is used with gobuster to brute-force directories:

```
gobuster dir -u http://target.com -w /path/to/wordlist.txt
```

Similarly, the following command is used with nmap to perform a basic scan:

```
nmap -sV target.com
```

These commands are intended to be run in a Linux environment.

## References
- https://academy.hackthebox.com/module/58/section/529

