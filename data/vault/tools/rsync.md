---
title: rsync
aliases: []
tags:
- tool/rsync
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: rsync.md
related_tools:
- '[[rsync]]'
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

# rsync

## Usage
- list directories `rsync --list-only $ip::`
- list files in public dir `rsync --list-only $ip::public`
- get file `rsync $ip::public/flag.txt flag.txt`

