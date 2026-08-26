---
title: Hack The Box - Academy Module 103 Section 967
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 19-103-CrossSiteScripting-02-StoredXSS.pdf
related_tools:
- '[[bettercap]]'
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

# Hack The Box - Academy Module 103 Section 967

## Overview
This section covers the use of the `bettercap` tool for network reconnaissance and enumeration. It provides a practical example of how to use `bettercap` to gather information about the network and hosts.

## Using BetterCap
BetterCap is a powerful network reconnaissance tool that can be used to perform various tasks such as scanning for open ports, identifying services, and gathering information about network hosts. The following steps demonstrate how to use BetterCap to gather information about the network.

1. **Installation**: Ensure that `bettercap` is installed on your system. You can install it via package managers or from source.

2. **Running BetterCap**: Start `bettercap` by running the following command:

```bash
bettercap
```

3. **Scanning for Open Ports**: Use the `scan` command to scan for open ports on the network. For example:

```bash
bettercap> scan
```

4. **Identifying Services**: Once you have identified the open ports, use the `service` command to identify the services running on those ports. For example:

```bash
bettercap> service
```

5. **Gathering Information**: Use the `info` command to gather detailed information about the hosts on the network. For example:

```bash
bettercap> info
```

6. **Saving Output**: You can save the output of the `bettercap` commands to a file for further analysis. For example:

```bash
bettercap> save output.txt
```

## References
- https://academy.hackthebox.com/module/103/section/967

