---
title: Hack The Box - Academy Module 115 Section 1106
aliases: []
tags:
- topic/hack-the-box-academy
- path/hack-the-box-academy-module-115-section-1106
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 08-115-ShellsAndPayloads-03-ReverseShell.pdf
related_tools:
- '[[bettercap]]'
- '[[burpsuite]]'
- '[[dirb]]'
- '[[dnsenum]]'
- '[[nmap-1787746090]]'
- '[[nikto]]'
- '[[nuclei]]'
- '[[sqlmap]]'
- '[[wpscan]]'
related_techniques:
- '[[crawling]]'
- '[[file-inclusion]]'
- '[[password-cracking]]'
- '[[sql-injection]]'
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

# Hack The Box - Academy Module 115 Section 1106

## Overview
This section covers the techniques and tools used to enumerate and exploit a target on Hack The Box. The focus is on using bettercap, burpsuite, dirb, dnsenum, nmap, nikto, nuclei, sqlmap, and wpscan to gather information and identify vulnerabilities.

## Tools and Techniques
- **bettercap**: A powerful tool for network reconnaissance and exploitation.
- **burpsuite**: A web application security testing tool used for intercepting and manipulating HTTP(S) traffic.
- **dirb**: A web directory and file brute-forcing tool.
- **dnsenum**: A tool for enumerating subdomains and services from a given domain.
- **nmap**: A network exploration and security auditing tool.
- **nikto**: A web server scanner designed to find security vulnerabilities in web servers.
- **nuclei**: A fast and flexible open-source scanner for web applications.
- **sqlmap**: An open-source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws.
- **wpscan**: A tool for WordPress plugin and theme security auditing.

## Techniques
- **Crawling**: Using tools like bettercap, burpsuite, and nuclei to crawl the target website and identify potential vulnerabilities.
- **File Inclusion**: Exploiting file inclusion vulnerabilities to gain access to sensitive files.
- **Password Cracking**: Using tools like djohn and sqlmap to crack passwords.
- **SQL Injection**: Identifying and exploiting SQL injection vulnerabilities using sqlmap.

## Tactics
- **TA0003**: Active infrastructure identification, which involves identifying and enumerating the target's infrastructure.
- **TA0005**: Passive infrastructure identification, which involves gathering information about the target without directly interacting with it.

## Services
- **HTTP**: The Hypertext Transfer Protocol used for web traffic.
- **HTTPS**: The secure version of HTTP, used for encrypted web traffic.

## References
- https://academy.hackthebox.com/module/115/section/1106

