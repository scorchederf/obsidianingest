---
title: Information Gathering - Web Edition
aliases: []
tags:
- topic/information-gathering
- topic/web
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 05-144-informationgathering-web-11-AutomatingRecon.pdf
related_tools:
- '[[aquatone]]'
- '[[burpsuite]]'
- '[[dirb]]'
- '[[ffuf]]'
- '[[gobuster]]'
- '[[hydra]]'
- '[[john]]'
- '[[nmap-1787746090]]'
- '[[nikto]]'
- '[[wpscan]]'
related_techniques:
- '[[crawling]]'
- '[[file-inclusion]]'
- '[[password-cracking]]'
- '[[sql-injection]]'
related_tactics:
- '[[active-infrastructure-identification]]'
- '[[passive-infrastructure-identification]]'
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

# Information Gathering - Web Edition

## Introduction
This module covers various techniques and tools for information gathering in web environments. It includes methods for discovering hidden directories, testing for SQL injection, and cracking passwords.

## Tools
The following tools are discussed in the module:

- **Aquatone**: A tool for generating screenshots and HTML reports of web applications.
- **Burpsuite**: A web application security testing tool that can be used for intercepting and modifying HTTP(S) traffic.
- **Dirb**: A web directory and file brute-forcing tool.
- **FFUF**: A fast fuzzer that can be used to test for directory and file existence.
- **Gobuster**: A tool for discovering hidden directories and files on web servers.
- **Hydra**: A network login cracker that supports many different services.
- **John the Ripper**: A password cracker that supports many different hash types.
- **Nmap**: A network scanning tool that can be used for service and version detection.
- **Nikto**: A web server scanner that checks for vulnerabilities and misconfigurations.
- **WPScan**: A tool for WordPress security audits and vulnerability scanning.

## Techniques
The module covers several techniques for information gathering, including:

- **Crawling**: Using tools like Gobuster and Dirb to discover hidden directories and files.
- **File Inclusion**: Testing for file inclusion vulnerabilities to gain access to sensitive files.
- **Password Cracking**: Using tools like John the Ripper to crack passwords.
- **SQL Injection**: Testing for SQL injection vulnerabilities to gain access to databases.

## Tactics
The module focuses on the following MITRE ATT&CK tactics:

- **Active Infrastructure Identification**: Using tools like Nmap and Nikto to identify active infrastructure.
- **Passive Infrastructure Identification**: Using techniques like crawling to identify hidden directories and files.

## References
- https://academy.hackthebox.com/module/144/section/3081

