---
title: File Search Commands
aliases: []
tags:
- study-notes
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: linux.md
related_tools:
- '[[locate]]'
- '[[find]]'
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

# File Search Commands

## File Search Commands
- search for a file
  - `locate`
    - `locate tomcat_flag.txt 2>/dev/null`
    - database doesn't exist `sudo updatedb; locate tomcat_flag 2>/dev/null`
  - `find`
    - `sudo find / -type f -name "tomcat_flag.txt" 2>/dev/null`
    - `find / -type f -name "tomcat_flag.txt" 2>/dev/null`

