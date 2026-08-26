---
title: SQLMap Essentials
aliases: []
tags:
- study-notes/sqlmap-essentials
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: 18-58-SQLMap-01-SQLMapOverview.pdf
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
SQLMap is a powerful open-source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. With more than 10000 parameters, SQLMap supports a wide range of databases, including MySQL, PostgreSQL, Oracle, Microsoft SQL Server, IBM DB2, and SQLite.

## Installation
To install SQLMap, you can use pip, the Python package installer. Run the following command in your terminal:

```bash
pip install sqlmap
```

Alternatively, you can download the latest version from the official GitHub repository and install it manually.

## Basic Usage
SQLMap can be used to test for SQL injection vulnerabilities and to exploit them. Here are some basic commands to get started:

```bash
sqlmap -u 'http://example.com/vulnerable-page' --level=5 --risk=3
```

This command will test the target URL for SQL injection vulnerabilities, with a higher level of detection and a higher risk of false positives.

You can also specify the database type and other parameters, such as the target database name and the username and password for authentication.

## Advanced Options
SQLMap offers a wide range of advanced options to customize the scanning process. Some of the key options include:

- `--dbs`: Lists all the databases on the target server.
- `--tables`: Lists all the tables in a specific database.
- `--dump`: Dumps the contents of a specific table or column.
- `--batch`: Runs SQLMap in batch mode, which is useful for automated testing.
- `--technique`: Specifies the injection technique to use, such as `E` for error-based, `U` for union, etc.

For more detailed information, you can refer to the official SQLMap documentation.

## References
- https://academy.hackthebox.com/module/58/section/509

