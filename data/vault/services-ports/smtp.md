---
title: smtp
aliases: []
tags:
- study-notes/enumeration
- study-notes/protocol
- study-notes/brute-force
- study-notes/phishing
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: smtp.md
related_tools:
- '[[host]]'
- '[[dig]]'
- '[[nmap]]'
- '[[telnet]]'
- '[[smtp-user-enum]]'
- '[[o365spray]]'
- '[[mailsniper]]'
- '[[credking]]'
- '[[hydra]]'
- '[[swaks]]'
related_techniques:
- '[[t1008]]'
- '[[t1110]]'
related_tactics:
- '[[ta0003]]'
related_services:
- '[[smtp]]'
- '[[pop3]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: 25, 143, 110, 465, 587, 993, 995
protocol: tcp
os: ''
---

# smtp

## Enumeration
- host
  - `host -t MX $domainname`
  - get ip address `host -t A mail1.$domainname.`
- dig `dig mx $domainname | grep

## References
- https://github.com/pentestmonkey/smtp-user-enum
- https://github.com/0xZDH/o365spray
- https://github.com/dafthack/MailSniper
- https://github.com/ustayready/CredKing

