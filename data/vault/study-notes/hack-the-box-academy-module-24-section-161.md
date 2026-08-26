---
title: Hack The Box - Academy Module 24 Section 161
aliases: []
tags:
- topic/hack-the-box-academy
- path/hack-the-box-academy-module-24-section-161
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 07-024-filetransfers-05-MiscellaneousFileTransferMethods.pdf
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

# Hack The Box - Academy Module 24 Section 161

## Introduction
This section covers the basics of using the Metasploit Framework to perform a SQL injection attack. It is part of the Hack The Box Academy module 24, section 161.

## SQL Injection Fundamentals
SQL injection is a technique used to exploit vulnerabilities in web applications to manipulate the underlying SQL database. It allows attackers to execute arbitrary SQL commands, leading to data theft, unauthorized access, and other malicious activities.

## Metasploit Framework
The Metasploit Framework is a powerful tool for penetration testing and vulnerability research. It includes a wide range of modules for various types of attacks, including SQL injection.

## Performing the Attack
To perform the SQL injection attack, follow these steps:

1. Identify a vulnerable parameter in the web application.
2. Craft a payload that will be injected into the SQL query.
3. Send the payload to the web application and observe the response.
4. Analyze the response to determine if the payload was successful.

## Example Payload
Example payload: `1' OR '1'='1`

## Mitigation
To mitigate SQL injection attacks, web application developers should:

1. Use parameterized queries or prepared statements.
2. Sanitize user inputs.
3. Implement input validation.
4. Use a web application firewall (WAF).

## References
- https://academy.hackthebox.com/module/24/section/161

