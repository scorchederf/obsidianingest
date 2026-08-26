---
title: Hack The Box - Academy Module 167 Section 1618
aliases: []
tags:
- topic/hack-the-box-academy
- topic/privilege-escalation
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 29-167-WindowsCommandLine-12-UserGroupManagement.pdf
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

# Hack The Box - Academy Module 167 Section 1618

## Overview
This section covers the process of privilege escalation on a Hack The Box machine. The techniques and tools used include Mimikatz and PowerShell.

## Privilege Escalation
The section details the steps to escalate privileges on the target machine. It involves using Mimikatz to extract credentials and then using PowerShell to execute commands with elevated permissions.

## Mimikatz Usage
Mimikatz is used to extract credentials from the system. The following command is used to dump the current user's credentials:

```
sekurlsa::logonpasswords
```

This command is executed in the context of a user with administrative privileges.

## PowerShell Commands
PowerShell is used to execute commands with elevated permissions. The following command is used to set the current user as the SYSTEM user:

```
Invoke-Command -ScriptBlock { whoami } -Credential (New-Object System.Management.Automation.PSCredential('SYSTEM', (ConvertTo-SecureString 'password' -AsPlainText -Force)))
```

Replace 'password' with the actual password obtained from Mimikatz.

## References
- https://academy.hackthebox.com/module/167/section/1618

