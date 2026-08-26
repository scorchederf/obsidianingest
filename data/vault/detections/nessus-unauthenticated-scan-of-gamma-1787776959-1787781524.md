---
title: Nessus Unauthenticated Scan of Gamma
aliases: []
tags:
- detections/nessus
- tool/nessus
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
- '[[c-windows-win-ini]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: windows
---

# Nessus Unauthenticated Scan of Gamma

## Exercise Description
Follow the steps to create an unauthenticated scan of Gamma using Nessus. The scan should be performed on your own Kali and public lab machines. The exercise involves running the scan with Wireshark open to identify the steps the scanner performed and reviewing the scan results.

## Exercise on VM #1
Perform a Basic Network Scan of the victim machine on VM #1, which is running a server with several vulnerabilities. Configure the scan to assess all ports. Once the scan completes, review the results to identify a critical vulnerability that allows directory traversal and arbitrary file access. The scan was able to read the file `C:\Windows\win.ini` as a proof of concept. The contents of the file are as follows:

```plaintext
﻿; for 16-bit app support
[fonts]
[extensions]
[mci extensions]
[files]
[Mail]
MAPI=1
; OS{cc407ed31b68267e4058d8e9937a20e3}
```

Nessus stopped searching after one exploit was found. To report all known exploits, enable the 'Perform thorough tests' setting and re-scan.

## References
- https://github.com/offsec-labs/PEN-200/blob/main/8.2.5%20Nessus%20Vulnerability%20Scanning%20Unauthenticated%20scan.md

