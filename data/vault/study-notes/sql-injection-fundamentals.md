---
title: SQL Injection Fundamentals
aliases: []
tags:
- topic/sql-injection
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: 17-33-SqlInjectionFundamentals-03-TypesOfDatabases.pdf
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

# SQL Injection Fundamentals

## Introduction
SQL Injection is a common web application vulnerability that allows an attacker to inject and execute malicious SQL statements through an application's input fields. This can lead to data theft, unauthorized access, and other serious security issues.

## Types of SQL Injection
There are several types of SQL injection, including:
- Error-Based SQL Injection
- Union-Based SQL Injection
- Blind SQL Injection
- Time-Based SQL Injection

## Detection
Detecting SQL Injection vulnerabilities involves monitoring for unusual patterns in logs, using automated tools, and performing manual testing. Common signs include slow response times, unexpected errors, and unexpected data in responses.

## Mitigation
Mitigating SQL Injection risks includes using parameterized queries, input validation, and employing web application firewalls (WAFs). Regular security audits and updates are also crucial.

## References
- https://academy.hackthebox.com/module/33/section/182

