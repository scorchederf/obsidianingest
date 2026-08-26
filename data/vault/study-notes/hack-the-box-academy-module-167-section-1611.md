---
title: Hack The Box - Academy Module 167 Section 1611
aliases: []
tags:
- topic/hack-the-box-academy
- path/hack-the-box-academy-module-167-section-1611
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 29-167-WindowsCommandLine-07-EnvironmentVariables.pdf
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

# Hack The Box - Academy Module 167 Section 1611

## Overview
This module covers the process of gaining access to a vulnerable service and escalating privileges on a Hack The Box machine. The section focuses on identifying and exploiting a service misconfiguration to gain initial access and then moving laterally to gain higher privileges.

## Identifying the Vulnerability
The module starts by identifying a misconfigured service on the target machine. The service is running an outdated version of a web application that has known vulnerabilities. The instructor demonstrates how to use tools like `nmap` and `dirb` to identify the service and its version.

## Exploiting the Vulnerability
Once the service is identified, the module guides the user through the process of exploiting the vulnerability. This involves using a payload to gain initial access to the machine. The payload is a custom script that is designed to exploit the specific vulnerability in the service.

## Escalating Privileges
After gaining initial access, the module explains how to escalate privileges. This involves using tools like `mimikatz` to extract credentials and then using those credentials to gain higher privileges on the machine. The module also covers the use of `PowerShell` and `cmd` to execute commands and move laterally within the network.

## References
- https://academy.hackthebox.com/module/167/section/1611

