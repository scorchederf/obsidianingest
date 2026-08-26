---
title: Hack The Box - Academy Module 35 Section 220
aliases: []
tags:
- topic/hack-the-box-academy
- topic/web-attacks
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 31-26-WebRequests-03-HttpRequestsAndResponses.pdf
related_tools:
- '[[ffuf]]'
- '[[nmap-1787746090]]'
related_techniques:
- '[[t1003]]'
- '[[t1077]]'
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

# Hack The Box - Academy Module 35 Section 220

## Introduction
This section covers the use of `ffuf` and `nmap` to perform web application enumeration and information gathering.

## Using ffuf
The `ffuf` tool is used to perform brute-forcing and directory enumeration. The following command is provided:

```
ffuf -w wordlist.txt -u http://<target>/FUZZ
```

This command will brute-force the URLs using the `wordlist.txt` file.

## Using nmap
The `nmap` tool is used to perform service and port scanning. The following command is provided:

```
nmap -sC -sV -p- <target>
```

This command will perform a comprehensive scan of the target, including service version detection and port scanning.

## Techniques and Tactics
The techniques and tactics covered in this section include:
- **T1003**: Reconnaissance - Information Gathering
- **T1077**: Discovery - Service Detection

These techniques are part of the MITRE ATT&CK framework.

## References
- https://academy.hackthebox.com/module/35/section/220

