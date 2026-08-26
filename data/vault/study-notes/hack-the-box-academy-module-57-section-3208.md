---
title: Hack The Box - Academy Module 57 Section 3208
aliases: []
tags:
- topic/hack-the-box-academy
- topic/penetration-testing
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 16-57-BruteForcing-11-LoginForms.pdf
related_tools:
- '[[nmap-1787746090]]'
- '[[netcat]]'
- '[[net]]'
- '[[netsh]]'
- '[[netstat]]'
- '[[ping]]'
- '[[whoami]]'
- '[[net use]]'
- '[[certutil]]'
- '[[powershell]]'
- '[[mimikatz]]'
related_techniques:
- '[[t1003]]'
- '[[t1059]]'
- '[[t1132]]'
related_tactics:
- '[[ta0005]]'
- '[[ta0003]]'
related_services:
- '[[ftp]]'
- '[[smb-1787747781]]'
related_os:
- '[[C:\Windows\System32\net.exe]]'
- '[[C:\Windows\System32\netsh.exe]]'
- '[[C:\Windows\System32\netstat.exe]]'
- '[[C:\Windows\System32\ping.exe]]'
- '[[C:\Windows\System32\whoami.exe]]'
- '[[c-windows-system32-net-exe]]'
- '[[C:\Windows\System32\net use.exe]]'
- '[[C:\Windows\System32\certutil.exe]]'
- '[[C:\Windows\System32\powershell.exe]]'
- '[[C:\Windows\System32\mimikatz.exe]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Hack The Box - Academy Module 57 Section 3208

## Introduction
This module covers the basics of penetration testing, including enumeration, privilege escalation, and lateral movement techniques. The focus is on using various tools and techniques to gain access to a target system and move laterally within a network.

## Enumeration
The module starts with enumeration techniques to gather information about the target system. Key tools and commands used include:

- **nmap**: For scanning the network and identifying open ports and services.
- **netcat (netcat.exe)**: For establishing a connection and transferring data.
- **netsh**: For configuring network interfaces and services.
- **netstat**: For displaying network connections, routing tables, interface statistics, etc.
- **ping**: For testing network connectivity.
- **whoami**: For displaying the current user context.
- **net use**: For mapping network drives.
- **certutil**: For downloading and executing files over HTTPS.
- **powershell**: For executing PowerShell commands.
- **mimikatz**: For credential dumping.

## Privilege Escalation
The module then covers techniques for privilege escalation, including:

- **T1003 - Pass-the-Hash**: Using the `net use` command to map a network drive and gain access to the target system.
- **T1059 - Command and Scripting Interpreter**: Using `certutil` to download and execute a payload.
- **T1132 - Run as Service**: Using `mimikatz` to dump credentials and escalate privileges.

## Lateral Movement
Finally, the module discusses techniques for moving laterally within the network, including:

- **T1003 - Pass-the-Hash**: Using the `net use` command to map a network drive and gain access to the target system.
- **T1059 - Command and Scripting Interpreter**: Using `certutil` to download and execute a payload.

## References
- https://academy.hackthebox.com/module/57/section/3208

