---
title: Hack The Box - Academy Module 167 Section 1609
aliases: []
tags:
- topic/hack-the-box-academy
- topic/privilege-escalation
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 29-167-WindowsCommandLine-03-SystemNavigation.pdf
related_tools:
- '[[mimikatz]]'
- '[[powershell]]'
related_techniques:
- '[[t1003]]'
- '[[t1059]]'
related_tactics:
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

# Hack The Box - Academy Module 167 Section 1609

## Overview
This section of the Hack The Box - Academy covers techniques for privilege escalation, focusing on the use of Mimikatz and PowerShell.

## Mimikatz Usage
Mimikatz is a powerful tool for privilege escalation. The section explains how to use Mimikatz to extract credentials from memory. Key commands include:

```powershell
sekurlsa::logonpasswords
```

This command lists all the credentials stored in the memory of the current machine.

## PowerShell Commands
PowerShell is used to gather information and perform actions on the system. The section provides examples of how to use PowerShell to find and exploit misconfigurations. Key commands include:

```powershell
Get-NetFirewallRule
```

This command lists all the firewall rules on the system, which can be useful for identifying potential misconfigurations.

## References
- https://academy.hackthebox.com/module/167/section/1609

