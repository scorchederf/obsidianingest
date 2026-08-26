---
title: Hack The Box - Academy Module 136 Section 1261
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 21-136-FileUploadAttacks-03-UploadExploitation.pdf
related_tools:
- '[[bettercap]]'
- '[[burpsuite]]'
related_techniques:
- '[[brute-forcing]]'
related_tactics:
- '[[passive-enumeration]]'
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

# Hack The Box - Academy Module 136 Section 1261

## Overview
This section covers the use of bettercap and Burp Suite for brute-forcing and enumeration purposes.

## BetterCap Usage
BetterCap is a powerful tool for network reconnaissance and testing. It can be used to perform various network attacks, including brute-forcing. The following command can be used to perform a brute-force attack on a target using BetterCap:

```
bettercap --target <target_ip> --http-bruter <username_file> <password_file>
```

Replace `<target_ip>`, `<username_file>`, and `<password_file>` with the appropriate values.

## Burp Suite Usage
Burp Suite is a web application security testing tool that can be used to perform various security tests, including brute-forcing. The following steps can be followed to use Burp Suite for brute-forcing:

1. Start Burp Suite and configure the proxy settings to intercept traffic.
2. Use the Intruder tool in Burp Suite to set up a brute-force attack. Select the target application and the payload type.
3. Set the payload values and launch the attack.

## References
- https://academy.hackthebox.com/module/136/section/1261

