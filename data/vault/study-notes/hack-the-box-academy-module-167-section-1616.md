---
title: Hack The Box - Academy Module 167 Section 1616
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 29-167-WindowsCommandLine-10-CMDvsPowerShell.pdf
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

# Hack The Box - Academy Module 167 Section 1616

## Introduction
This module covers the process of gaining access to a target machine through a SQL injection vulnerability. The objective is to exploit a SQL injection vulnerability to gain a reverse shell and further access to the system.

## Identifying the Vulnerability
The first step is to identify the SQL injection vulnerability. This can be done by sending crafted payloads to the target application and observing the responses. Common techniques include using SQL injection payloads to extract information from the database or to manipulate the application's behavior.

## Exploiting the SQL Injection
Once the vulnerability is identified, the next step is to exploit it. This involves crafting and sending SQL injection payloads to the target application. The goal is to gain control over the database or the application, which can lead to further exploitation.

## Gaining a Reverse Shell
After gaining control over the database or the application, the next step is to gain a reverse shell. This can be done by using tools such as `msfvenom` to generate a payload that will establish a reverse shell connection to the attacker's machine.

## Post-Exploitation
Once a reverse shell is established, the attacker can further explore the target machine. This may involve executing commands, uploading and running additional payloads, or using tools such as `meterpreter` to gain deeper access to the system.

## References
- https://academy.hackthebox.com/module/167/section/1616

