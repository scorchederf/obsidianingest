---
title: Hack The Box - Academy Module 23 Section 1492
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 20-23-FileInclusion-04-PHPFilters.pdf
related_tools:
- '[[ffuf]]'
- '[[nmap-1787746090]]'
- '[[nikto]]'
related_techniques:
- '[[crawling]]'
- '[[brute-forcing]]'
related_tactics:
- '[[passive-enumeration]]'
- '[[active-enumeration]]'
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

# Hack The Box - Academy Module 23 Section 1492

## Overview
This section covers the process of enumerating a target machine on Hack The Box using various tools and techniques. The main focus is on using `ffuf` for brute-forcing, `nmap` for service enumeration, and `nikto` for web application scanning.

## Brute-Forcing with ffuf
The `ffuf` tool is used to perform brute-forcing on the target. The following command is used to brute-force directories and files:

```
ffuf -w wordlist.txt -u http://<target>/FUZZ
```

Replace `wordlist.txt` with the appropriate wordlist and `<target>` with the target IP or domain.

## Service Enumeration with nmap
The `nmap` tool is used to enumerate services running on the target machine. The following command is used to perform a comprehensive service scan:

```
nmap -A -p- <target>
```

This command performs an aggressive scan on all ports, providing detailed information about the services running.

## Web Application Scanning with nikto
The `nikto` tool is used to scan the web application for vulnerabilities. The following command is used to perform a scan:

```
nikto -h http://<target>
```

Replace `<target>` with the target IP or domain. This command scans the web application for known vulnerabilities and misconfigurations.

## Crawling with ffuf
The `ffuf` tool is also used for crawling the target to find additional directories and files. The following command is used to crawl the target:

```
ffuf -u http://<target>/FUZZ -c -w wordlist.txt
```

This command crawls the target, looking for additional resources and checking for common HTTP status codes.

## References
- https://academy.hackthebox.com/module/23/section/1492

