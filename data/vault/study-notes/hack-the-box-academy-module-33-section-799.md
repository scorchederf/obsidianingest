---
title: Hack The Box - Academy Module 33 Section 799
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 17-33-SqlInjectionFundamentals-09-UsingComments.pdf
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

# Hack The Box - Academy Module 33 Section 799

## Overview
This module covers the basics of web application security and how to perform a web application penetration test. It includes an overview of common web application vulnerabilities and how to exploit them.

## Common Web Application Vulnerabilities
- SQL Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Broken Authentication
- Insecure Direct Object References (IDOR)
- Security Misconfiguration
- Insufficient Logging and Monitoring
- Unvalidated Redirects and Forwards
- Sensitive Data Exposure
- Missing Function Level Access Control
- Using Components with Known Vulnerabilities

## Exploiting SQL Injection
To exploit SQL Injection, you can use tools like sqlmap or manually craft SQL queries. Here is an example of a SQL injection payload:

```
' OR '1'='1
```

This payload can be used to bypass authentication or retrieve sensitive information from the database.

## Exploiting Cross-Site Scripting (XSS)
To exploit XSS, you can inject malicious scripts into web pages. For example, you can use a reflected XSS payload to steal session cookies. Here is an example of a reflected XSS payload:

```
<img src=x onerror=alert(document.domain)>
```

This payload will trigger an alert box with the domain name when the page is loaded.

## Exploiting Broken Authentication
Broken authentication can be exploited by performing brute force attacks or session hijacking. Here is an example of a brute force attack using a tool like Hydra:

```
hydra -l username -P password.txt http-post-form '/login.php:username=^USER^&password=^PASS^:Incorrect username or password'
```

This command attempts to log in with all usernames and passwords from a file.

## Exploiting Insecure Direct Object References (IDOR)
IDOR can be exploited by manipulating URLs to access sensitive data. For example, you can use a tool like Burp Suite to intercept and modify HTTP requests. Here is an example of an IDOR payload:

```
http://example.com/api/users/12345
```

By changing the user ID, you can access data that should be restricted.

## References
- https://academy.hackthebox.com/module/33/section/799

