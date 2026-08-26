---
title: Hack The Box - Academy Module 115 Section 1132
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 08-115-ShellsAndPayloads-06-Metasploit.pdf
related_tools:
- '[[nmap-1787746090]]'
- '[[netcat]]'
- '[[net]]'
- '[[netsh]]'
- '[[netstat]]'
- '[[ping]]'
- '[[powershell]]'
- '[[whoami]]'
related_techniques:
- '[[t1003]]'
- '[[t1089]]'
related_tactics:
- '[[ta0005]]'
related_services:
- '[[net]]'
- '[[netstat]]'
- '[[ping]]'
- '[[powershell]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Hack The Box - Academy Module 115 Section 1132

## Description
In this section, you will learn how to use Nmap to perform a network scan and identify open ports. Additionally, you will learn how to use Netcat, Net, Netsh, Netstat, Ping, PowerShell, and Whoami to gather information about the target system.

## Network Scan with Nmap
To perform a network scan, you can use the following command:

```
$ nmap -sS -O 192.168.1.1
```

This command will perform a SYN scan and attempt to determine the operating system of the target.

## Gathering Information with Net, Netsh, Netstat, Ping, PowerShell, and Whoami
You can use the following commands to gather information about the target system:

- Net:
```
$ net user
```

- Netsh:
```
$ netsh interface show interface
```

- Netstat:
```
$ netstat -an
```

- Ping:
```
$ ping 192.168.1.1
```

- PowerShell:
```
$ powershell -command whoami
```

- Whoami:
```
$ whoami
```

These commands will provide information about users, network interfaces, open ports, and the current user.

## Techniques and Tactics
The techniques used in this section include:

- T1003: Establishing a Reverse Shell
- T1089: Valid Accounts

The tactic associated with this section is:

- TA0005: Defense Evasion

## References
- https://academy.hackthebox.com/module/115/section/1132

