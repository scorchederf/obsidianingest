---
title: hydra
aliases: []
tags:
- tool/hydra
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: hydra.md
related_tools:
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

# hydra

## Usage
- `hydra -L users.list -P passwords.list ftp://$ip:2121 -vv -I -t 40 -f -u`

## Flags
- `-f`      stop at first hit
- `-t 40`   increase threads (may cause breaking)
- `-u`      loop around users, not passwords (effective! implied with -x)

