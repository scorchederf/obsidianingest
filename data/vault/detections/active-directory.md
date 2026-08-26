---
title: Active Directory
aliases: []
tags:
- detection/nessus
- detection/windows
category: detections
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: microsoft-activedirectory.md
related_tools: []
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

# Active Directory

## Event Monitoring Configuration
```yaml
      - name: Application
        onlyEventIDs: [1518, 1511, 1000, 1001, 1002, 95, 1022, 1033]
      - name: Security
        excludeEventIDs: [4689, 4688, 5156, 5158, 5446, 5447, 4658, 5058, 5061, 600, 4656, 4661]
      - name: System
        onlyEventIDs: [7022, 7023, 7024, 7026, 7031, 7032, 7034, 6, 7045, 7000, 19, 1, 13, 12]
```

## Remote Desktop Port
```powershell
reg query "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp"
```

- To find out which port is used for RDP, run the following command:
  - `reg query "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp"`

## Remote Desktop Connection
```powershell
mstsc /v:10.1.2.3
mstsc /v:server01.domain.local
```

- To establish a Remote Desktop connection, use the following commands:
  - `mstsc /v:10.1.2.3`
  - `mstsc /v:server01.domain.local`

## Account Comparison
```powershell
$user1 = 'adm_alice'
$user2 = 'adm_bob'

$u1Groups = (Get-ADUser $user1 -Properties MemberOf).MemberOf
$u2Groups = (Get-ADUser $user2 -Properties MemberOf).MemberOf

Compare-Object $u1Groups $u2Groups -IncludeEqual
```

- To compare the groups of two user accounts, use the following PowerShell script:
  - `Compare-Object $u1Groups $u2Groups -IncludeEqual`

## References
- references to the provided material

