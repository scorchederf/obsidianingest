---
title: Hack The Box - Academy Module 144 Section 1251
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 05-144-informationgathering-web-03-dns.pdf
related_tools:
- '[[gobuster]]'
- '[[nmap-1787746090]]'
- '[[nikto]]'
- '[[dirb]]'
- '[[wpscan]]'
- '[[sqlmap]]'
- '[[john]]'
- '[[hashcat]]'
related_techniques:
- '[[t1003]]'
- '[[t1089]]'
- '[[t1132]]'
related_tactics:
- '[[ta0003]]'
- '[[ta0005]]'
related_services:
- '[[http]]'
- '[[https]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Hack The Box - Academy Module 144 Section 1251

## Overview
This module covers the process of enumerating and exploiting a vulnerable web application on a Hack The Box machine. The focus is on using tools like `gobuster`, `nmap`, `nikto`, `dirb`, `wpscan`, `sqlmap`, `john`, and `hashcat` to identify and exploit vulnerabilities.

## Tools and Techniques
The module covers the following tools and techniques:

- `gobuster` - A directory and file brute-forcing tool.
- `nmap` - A network scanning tool.
- `nikto` - A web server scanner.
- `dirb` - A directory brute-forcing tool.
- `wpscan` - A WordPress security scanner.
- `sqlmap` - A tool for automating SQL injection attacks.
- `john` - A password cracker.
- `hashcat` - A password cracker.

The techniques covered include:

- T1003 - Security Account Manager (SAM) database access.
- T1089 - SQL injection.
- T1132 - Pass-the-hash.

## Steps
1. **Initial Enumeration**
   - Use `nmap` to scan the target machine for open ports and services.
   - Use `gobuster` and `dirb` to enumerate directories and files.
   - Use `nikto` to scan for vulnerabilities in the web server.
2. **Web Application Enumeration**
   - Use `wpscan` to scan for WordPress vulnerabilities.
   - Use `sqlmap` to test for SQL injection vulnerabilities.
3. **Password Cracking**
   - Use `john` and `hashcat` to crack passwords.
4. **Exploitation**
   - Use the identified vulnerabilities to gain access to the system.

## References
- https://academy.hackthebox.com/module/144/section/1251

