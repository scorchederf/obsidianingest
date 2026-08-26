---
title: Linux Privilege Escalation
aliases: []
tags:
- topic/linux-privilege-escalation
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 25-51-LinuxPrivilegeEscalation-01-Introduction.pdf
related_tools:
- '[[enum4linux-ng]]'
- '[[crackmapexec]]'
- '[[donpapi]]'
- '[[evil-winrm]]'
- '[[ettercap]]'
- '[[eyewitness]]'
- '[[fierce]]'
- '[[ffuf]]'
- '[[fierce]]'
- '[[finalrecon]]'
related_techniques:
- '[[t1003]]'
- '[[t1020]]'
- '[[t1077]]'
- '[[t1110]]'
- '[[t1132]]'
- '[[t1555]]'
related_tactics:
- '[[ta0003]]'
- '[[ta0005]]'
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

# Linux Privilege Escalation

## Introduction
This module covers the techniques and tools used to escalate privileges on a Linux system. It includes methods such as password cracking, service enumeration, and privilege escalation techniques.

## Password Cracking
Password cracking is a common method for gaining higher privileges. Tools such as `crackmapexec`, `donpapi`, and `evil-winrm` can be used to crack passwords and gain access to the system.

## Service Enumeration
Service enumeration involves identifying and exploiting services running on the system. Tools like `enum4linux-ng` and `ettercap` can be used to discover and interact with services.

## Privilege Escalation Techniques
Various techniques for privilege escalation are discussed, including the use of `fierce` and `ffuf` for directory and file enumeration, and `eyewitness` for web server enumeration.

## Tools
The following tools are mentioned and used in the module:
- `enum4linux-ng`
- `crackmapexec`
- `donpapi`
- `evil-winrm`
- `ettercap`
- `eyewitness`
- `fierce`
- `ffuf`
- `finalrecon`

## References
- https://academy.hackthebox.com/module/51/section/466

