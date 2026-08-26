---
title: hashcat
aliases: []
tags:
- tool/hashcat
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: hashcat.md
related_tools:
- '[[hashcat]]'
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

# hashcat

## Usage
- build a mutated list of passwords
  - `hashcat password.list -r custom.rule --stdout | sort -u > mut_password.list`

