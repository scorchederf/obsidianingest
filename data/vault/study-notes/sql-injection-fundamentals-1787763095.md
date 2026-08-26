---
title: SQL Injection Fundamentals
aliases: []
tags:
- topic/sql-injection-fundamentals
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 17-33-SqlInjectionFundamentals-15-MitigatingSQLInjection.pdf
related_tools: []
related_techniques:
- '[[t1003-003]]'
related_tactics:
- '[[ta0005]]'
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

# SQL Injection Fundamentals

## Introduction
SQL Injection is a common web application vulnerability that allows attackers to inject malicious SQL queries into a web application's input fields, leading to unauthorized access to the database. This technique is part of the MITRE ATT&CK framework under the tactic TA0005, which covers data from web and API endpoints.

## Types of SQL Injection
There are several types of SQL Injection, including:
- Error-Based SQL Injection
- Union-Based SQL Injection
- Blind SQL Injection
- Time-Based SQL Injection

## Detection
Detecting SQL Injection vulnerabilities involves monitoring for unusual patterns in the database logs, analyzing the application's error messages, and using automated tools like SQLMap to test for vulnerabilities.

## Mitigation
Mitigating SQL Injection risks includes:
- Using parameterized queries
- Implementing input validation
- Employing a web application firewall (WAF)
- Regularly updating and patching the application and database

## References
- https://academy.hackthebox.com/module/33/section/794

