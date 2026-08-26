---
title: postgresql
aliases: []
tags:
- study-notes
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: postgresql.md
related_tools: []
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

# postgresql

## Connection
- connect `psql -U christine -h machine.htb -p 5432`

## Database Management
- list databases `\list`
- change db `\connect secrets`
- list tables `\dt`

## Query Execution
- select `SELECT * FROM flag;`      CASE SENSITIVE

## Mitigations
- [pg_escape_string](https://www.php.net/manual/en/function.pg-escape-string.php) `$escaped = pg_escape_string($data);`

## References
- https://www.php.net/manual/en/function.pg-escape-string.php

