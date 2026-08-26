---
title: ftp
aliases: []
tags:
- study-notes/ftp
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: ftp.md
related_tools:
- '[[medusa]]'
- '[[hydra]]'
related_techniques: []
related_tactics: []
related_services:
- '[[ftp]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: '2121'
protocol: tcp
os: ''
---

# ftp

## Authentication Techniques
- try anonymous:anonymous authentication `ftp ftp://anonymous@$ip`
- brute forcing
    - medusa (slow)
        - `medusa -h $ip -U users.list -P passwords.list -M ftp -n 2121`
    - hydra
        - `hydra -L users.list -P passwords.list ftp://$ip:2121 -vv -I -t 40 -f -u`
        - `-f`      stop at first hit
        - `-t 40`   increase threads (may cause breaking)
        - `-u`      loop around users, not passwords (effective! implied with -x`

## Commands
- download all `mget *.*`

