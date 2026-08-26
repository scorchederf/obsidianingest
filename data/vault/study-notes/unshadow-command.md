---
title: unshadow Command
aliases: []
tags:
- study-notes/credential-access
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: una.txt
related_tools:
- '[[unshadow]]'
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

# unshadow Command

## Description
The `unshadow` command is a tool used in forensic analysis and password cracking. It is designed to merge the `/etc/passwd` and `/etc/shadow` files from Unix/Linux systems to create a single file that can be used for password cracking or analysis.

## Usage
Usage: `unshadow PASSWORD-FILE SHADOW-FILE`

- `PASSWORD-FILE`: The file containing the `/etc/passwd` entries.
- `SHADOW-FILE`: The file containing the `/etc/shadow` entries.

## References
- https://www.forensicswiki.org/wiki/Unshadow

