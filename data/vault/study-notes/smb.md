---
title: smb
aliases: []
tags:
- study-notes
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: smb.md
related_tools:
- '[[nmap]]'
- '[[smbmap]]'
- '[[smbclient]]'
- '[[enum4linux]]'
- '[[crackmapexec]]'
- '[[responder]]'
- '[[rpcclient]]'
- '[[impacket-psexec]]'
- '[[hydra]]'
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

# smb

## Mounting VHD via SMB Share
- `mkdir smbmount`
- `mount -t cifs \\$ip/david -o user=david smbmount`

## Nmap Enumeration
- `sudo nmap $ip -sV -sC -p139,445`

## smbmap
- `smbmap -H $ip`
- `smbmap -u david -p gRzX7YbeTcDG7 -H $ip`
- `smbmap -H $ip -u anonymous -R`

## smbclient
- `smbclient -N -L \\$ip`
- `smbclient -L \\$ip/$sharename`
- `smbclient -N -L \\$ip/$sharename`
- `smbclient -U administrator \\$ip/ADMIN$`
- `smbclient -U david \\$ip/david`
- `smbclient -U

## References
- https://www.willhackforsushi.com/sec504/SMB-Access-from-Linux.pdf

