---
title: Hack The Box - Academy Module 35 Section 219
aliases: []
tags:
- topic/hack-the-box-academy
- topic/web-attacks
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 31-26-WebRequests-01-HyperTextTransferProtocol.pdf
related_tools:
- '[[ffuf]]'
- '[[nmap-1787746090]]'
related_techniques:
- '[[t1184]]'
- '[[t1190]]'
related_tactics:
- '[[ta0003]]'
- '[[ta0005]]'
related_services:
- '[[http]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Hack The Box - Academy Module 35 Section 219

## Introduction
This section covers the use of `ffuf` and `nmap` for web application enumeration and testing. It is part of the Hack the Box Academy module 35, section 219.

## Using ffuf for Enumeration
The `ffuf` tool is used to perform a quick and dirty enumeration of the web application. The following command is provided as an example:
```
ffuf -u http://<target>/FUZZ -w /path/to/wordlist.txt -e .php
```
This command will enumerate the target web application by sending requests to URLs that match the pattern `http://<target>/FUZZ` and using a wordlist of PHP file extensions.

## Using nmap for Service Discovery
The `nmap` tool is used to discover open services on the target system. The following command is provided as an example:
```
nmap -sV -p- <target>
```
This command will perform a service discovery scan on the target system, scanning all ports and identifying the services running on each port.

## Identifying Web Application Vulnerabilities
The section discusses the identification of potential vulnerabilities in the web application using the tools mentioned. It covers techniques such as path traversal and file inclusion, which are part of the MITRE ATT&CK techniques T1184 and T1190 respectively.

## References
- https://academy.hackthebox.com/module/35/section/219

