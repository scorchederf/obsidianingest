---
title: Windows Version and Ping
aliases: []
tags:
- os/windows
- tool/ping
- tool/get-wmiobject
category: os
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: win-commands.md
related_tools:
- '[[ping.exe]]'
- '[[Get-WmiObject]]'
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
os: windows
---

# Windows Version and Ping

## Ping Command
```powershell
ping.exe -t ucq-cyber-p001 |Foreach{"{0} - {1}" -f (Get-Date),$_}
```

## Get Windows Version
```powershell
Get-WmiObject -Class win32_OperatingSystem | select Version,BuildNumber
```

