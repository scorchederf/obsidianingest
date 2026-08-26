---
title: SQL Injection Fundamentals
aliases: []
tags:
- topic/sql-injection-fundamentals
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 17-33-SqlInjectionFundamentals-07-IntroToSqlIjections.pdf
related_tools: []
related_techniques:
- '[[file-inclusion]]'
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
SQL Injection is a common web application vulnerability that allows attackers to inject malicious SQL queries into a web application's input fields. This can lead to unauthorized access to sensitive data, data manipulation, and even complete control over the database.

## Types of SQL Injection
There are several types of SQL Injection, including:
- **Error-Based SQL Injection**: Exploits errors in the application to extract information from the database.
- **Union-Based SQL Injection**: Uses the `UNION` operator to combine the results of two or more SQL queries.
- **Boolean-Based SQL Injection**: Forces the application to return true or false to determine the validity of the injected SQL query.
- **Time-Based SQL Injection**: Forces the application to wait for a certain amount of time to determine the validity of the injected SQL query.

## Common Vulnerabilities
Common vulnerabilities that can lead to SQL Injection include:
- **Improper Input Validation**: Failing to validate user input can allow attackers to inject malicious SQL.
- **Inadequate Parameterization**: Using dynamic SQL queries without proper parameterization can expose the application to SQL Injection.
- **Lack of Proper Error Handling**: Failing to handle errors properly can provide attackers with information about the database structure.

## Detection and Prevention
To detect and prevent SQL Injection, consider the following strategies:
- **Input Validation**: Validate and sanitize all user inputs.
- **Parameterization**: Use parameterized queries to separate SQL code from data.
- **Error Handling**: Handle errors gracefully without exposing sensitive information.
- **Use of ORM**: Use Object-Relational Mapping (ORM) tools to abstract database interactions.

## Example of SQL Injection
Consider the following vulnerable query:
```sql
SELECT * FROM users WHERE username = 'admin' AND password = 'password';
``` 
An attacker could inject the following payload to bypass the password check:
```sql
' OR '1'='1
``` 
This would result in the query:
```sql
SELECT * FROM users WHERE username = 'admin' AND password = '' OR '1'='1';
``` 
Which would return all users, as the condition `1='1'` is always true.

## References
- https://academy.hackthebox.com/module/33/section/193

