---
title: Hack The Box - Academy Module 115 Section 1105
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 08-115-ShellsAndPayloads-03-BindShell.pdf
related_tools:
- '[[bettercap]]'
- '[[burpsuite]]'
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

# Hack The Box - Academy Module 115 Section 1105

## Overview
This section covers the use of `bettercap` and `burpsuite` for web application security testing.

## BetterCap Usage
BetterCap is a powerful tool for network and web application security testing. It can be used to perform various tasks such as network scanning, packet injection, and web application testing.

Example commands:

```bash
bettercap -i eth0 -t http://192.168.1.100
```

This command starts BetterCap on the `eth0` interface and targets the web application at `http://192.168.1.100`.

## Burp Suite Usage
Burp Suite is a web application security testing platform. It can be used to intercept and manipulate HTTP(S) traffic, perform automated and manual testing, and analyze vulnerabilities.

Example commands:

1. Start Burp Suite:

```bash
burpsuite
```

2. Configure Burp Suite to intercept traffic:

- Open Burp Suite and go to `Proxy` > `Options`.
- Configure the `Listen Address` and `Listen Port`.
- Ensure the Burp Suite proxy is set as the default proxy in the browser settings.

## References
- https://academy.hackthebox.com/module/115/section/1105

