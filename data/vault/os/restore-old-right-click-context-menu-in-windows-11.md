---
title: Restore Old Right Click Context Menu in Windows 11
aliases: []
tags:
- os/windows
- path
category: os
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: microsoft-windows-tweaks.md
related_tools: []
related_techniques: []
related_tactics: []
related_services: []
related_os:
- '[[HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32
port: ''
protocol: ''
os: windows
---

# Restore Old Right Click Context Menu in Windows 11

## Command
```bash
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve
```

