---
title: JoomlaScan
aliases: []
tags:
- tool/joomlascan
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: JoomlaScan.md
related_tools:
- '[[python2.7]]'
- '[[urllib3]]'
- '[[certifi]]'
- '[[bs4]]'
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

# JoomlaScan

## Description
A free software to find the components installed in Joomla CMS, built out of the ashes of [Joomscan](https://github.com/OWASP/joomscan).

## Usage
```sh
python2.7 -m pip install urllib3
python2.7 -m pip install certifi
python2.7 -m pip install bs4
```

- standard scan
  - `python2.7 joomlascan.py -u http://dev.inlanefreight.local`

## References
- https://github.com/drego85/JoomlaScan

