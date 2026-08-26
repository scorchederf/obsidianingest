---
title: Hack The Box - Academy Module 158 Section 1426
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 12-158-pivoting-02-dynamicportforwarding.pdf
related_tools:
- '[[john]]'
- '[[hydra]]'
- '[[nmap-1787746090]]'
- '[[curl]]'
- '[[gobuster]]'
- '[[dirb]]'
- '[[nikto]]'
- '[[wpscan]]'
- '[[sqlmap]]'
- '[[w3af]]'
- '[[wpscan]]'
- '[[nmap-1787746090]]'
- '[[curl]]'
- '[[gobuster]]'
- '[[dirb]]'
- '[[nikto]]'
- '[[wpscan]]'
- '[[sqlmap]]'
- '[[w3af]]'
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

# Hack The Box - Academy Module 158 Section 1426

## Overview
This module covers the process of enumerating and exploiting a target machine in a simulated environment. The main techniques used include network scanning, service enumeration, and web application attacks.

## Network Scanning
The module starts with a basic network scan using `nmap` to identify open ports and services on the target machine.

```bash
nmap -sS -O 192.168.1.100
```

This command performs a SYN scan and OS detection to gather information about the target.

## Service Enumeration
After identifying open ports, the module suggests using `curl` to interact with web services and `gobuster` and `dirb` for directory and file enumeration.

```bash
curl http://192.168.1.100/
gobuster dir -u http://192.168.1.100 -w /usr/share/wordlists/dirb/common.txt
dirb http://192.168.1.100 /usr/share/wordlists/dirb/common.txt
```

These commands are used to test for web services and enumerate directories and files.

## Web Application Attacks
The module then focuses on attacking web applications using tools like `nikto`, `wpscan`, and `sqlmap`.

```bash
nikto -h http://192.168.1.100
wpscan --url http://192.168.1.100
sqlmap -u http://192.168.1.100/vulnerabilities.txt
```

These tools are used to identify and exploit vulnerabilities in the web application.

## Post-Exploitation
Finally, the module covers post-exploitation activities such as privilege escalation and lateral movement. It suggests using `john` and `hydra` for password cracking.

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt 192.168.1.100.hash
hydra -L users.txt -P passwords.txt 192.168.1.100 ssh
```

These commands are used to crack passwords and attempt SSH login brute-forcing.

## References
- https://academy.hackthebox.com/module/158/section/1426

