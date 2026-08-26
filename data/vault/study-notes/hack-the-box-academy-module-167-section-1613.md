---
title: Hack The Box - Academy Module 167 Section 1613
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 29-167-WindowsCommandLine-09-WorkingWithScheduledTasks.pdf
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

# Hack The Box - Academy Module 167 Section 1613

## Introduction
This section covers the process of identifying and exploiting a vulnerability in a web application. The goal is to gain access to the system and escalate privileges.

## Identifying the Vulnerability
The vulnerability is a SQL injection flaw in the search functionality of the web application. The search parameter can be manipulated to execute arbitrary SQL queries.

## Exploiting the Vulnerability
To exploit the SQL injection, the following steps are taken:

1. Craft a payload to extract the database version and schema information.
2. Use the extracted information to craft more sophisticated payloads.
3. Gain access to the database and escalate privileges.

## Privilege Escalation
Once the database is compromised, the next step is to escalate privileges. This involves:

1. Identifying the user with administrative privileges.
2. Using the compromised credentials to log in and gain full control over the system.

## References
- https://academy.hackthebox.com/module/167/section/1613

