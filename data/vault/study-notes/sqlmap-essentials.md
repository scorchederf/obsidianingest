---
title: SQLMap Essentials
aliases: []
tags:
- topic/sqlmap
- topic/penetration-testing
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: 18-58-SQLMap-02-GettingStartedwithSQLMap.pdf
related_tools:
- '[[sqlmap]]'
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

# SQLMap Essentials

## Introduction
SQLMap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. With more than 10000 tested settings, SQLMap supports a wide range of databases, allowing pen-testers to execute sophisticated SQL injection attacks and take over of database servers.

## Basic Usage
To use SQLMap, you can run it from the command line with the following syntax:

```
sqlmap -u <URL> --data=<POST data> --cookie=<cookie> --user-agent=<user-agent>
```

For example, to test a URL for SQL injection vulnerabilities, you can use:

```
sqlmap -u 'http://example.com/vulnerable_page' --level=5 --risk=3
```

This command will perform a thorough test with a high risk level, which may cause more damage to the database but also provide more detailed information.

## Common Options
Here are some common options you can use with SQLMap:

- `--level=<level>`: Set the level of tests to perform. The higher the level, the more tests will be run, but the more time it will take.
- `--risk=<risk>`: Set the risk level of the tests. The higher the risk, the more aggressive the tests will be.
- `--dbs`: List all databases on the target server.
- `--tables`: List all tables in a specific database.
- `--dump=<table_name>`: Dump all records from a specific table.
- `--batch`: Run SQLMap in batch mode, which will not ask for user input.

## Advanced Techniques
SQLMap supports various advanced techniques to bypass WAFs and other security measures. Some of these techniques include:

- `--tamper=<tamper_file>`: Use tamper scripts to modify the payload and bypass WAFs.
- `--technique=<technique>`: Use specific techniques to exploit the SQL injection flaw, such as `BEAST`, `BYPASS`, `COOKIE`, etc.
- `--batch`: Run SQLMap in batch mode, which will not ask for user input.

## References
- https://academy.hackthebox.com/module/58/section/694

