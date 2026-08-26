---
title: Hack The Box - Academy Module 18 Section 93
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 31-18-LinuxFundamentals-08-EditingFiles.pdf
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

# Hack The Box - Academy Module 18 Section 93

## Introduction
This section covers the basics of using the Metasploit Framework to perform a variety of tasks, including enumeration, exploitation, and post-exploitation activities. It is designed to provide a comprehensive overview of the Metasploit Framework and its capabilities.

## Metasploit Framework Basics
The Metasploit Framework is a powerful tool for penetration testers and security researchers. It provides a wide range of modules for various tasks, including exploitation, post-exploitation, and auxiliary modules for information gathering. The framework is designed to be modular and flexible, allowing users to create custom exploits and post-exploitation modules.

## Using Metasploit for Enumeration
Metasploit can be used for enumeration purposes, such as identifying open ports, services, and vulnerabilities. The `auxiliary/scanner` modules can be used for this purpose. For example, the `auxiliary/scanner/portscan/tcp` module can be used to scan a range of IP addresses for open ports.

## Exploitation with Metasploit
Metasploit provides a wide range of exploit modules that can be used to exploit vulnerabilities in target systems. To use an exploit module, you can use the `msfconsole` command-line interface. For example, to use the `exploit/multi/http/struts2_s2_045` module, you can run the following command:

```bash
use exploit/multi/http/struts2_s2_045
set RHOSTS <target_ip>
set RPORT 80
exploit
```

This will attempt to exploit the Struts2 S2-045 vulnerability on the target system.

## Post-Exploitation with Metasploit
After gaining access to a target system, Metasploit can be used for post-exploitation activities, such as maintaining access, gathering information, and cleaning up. The `post` modules can be used for these purposes. For example, the `post/multi/gather/credentials` module can be used to gather credentials from the target system.

## References
- https://academy.hackthebox.com/module/18/section/93

