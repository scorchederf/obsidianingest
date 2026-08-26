---
title: Hack The Box - Academy Module 136 Section 1289
aliases: []
tags:
- topic/hack-the-box-academy
- topic/web-attacks
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 21-136-FileUploadAttacks-06-WhitelistFilters.pdf
related_tools:
- '[[ffuf]]'
- '[[nmap-1787746090]]'
- '[[gobuster]]'
- '[[nikto]]'
- '[[wpscan]]'
- '[[sqlmap]]'
- '[[dirb]]'
- '[[wpscan]]'
- '[[nuclei]]'
related_techniques:
- '[[t1210]]'
- '[[t1184]]'
- '[[t1132]]'
- '[[t1089]]'
- '[[t1555]]'
related_tactics:
- '[[ta0005]]'
- '[[ta0003]]'
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

# Hack The Box - Academy Module 136 Section 1289

## Introduction
This section covers the use of various tools and techniques to perform web application penetration testing. The main focus is on identifying and exploiting vulnerabilities in web applications.

## Tools and Techniques
The following tools and techniques are discussed in this section:

- **ffuf**: A fast fuzzer that can be used to discover hidden directories and files.
- **nmap**: A network scanning tool that can be used to identify open ports and services.
- **gobuster**: A directory and file enumeration tool that can be used to discover hidden directories and files.
- **nikto**: A web server scanner that can be used to identify security vulnerabilities in web applications.
- **wpscan**: A WordPress scanner that can be used to identify vulnerabilities in WordPress installations.
- **sqlmap**: A tool that automates the process of detecting and exploiting SQL injection vulnerabilities.
- **dirb**: A directory and file enumeration tool that can be used to discover hidden directories and files.
- **nuclei**: A modern HTTP reconnaissance and scanning tool that can be used to identify security vulnerabilities in web applications.

These tools are used in conjunction with techniques such as T1210 (Data from Local System), T1184 (Valid Accounts), T1132 (Brute Force), T1089 (Phishing), and T1555 (Exploitation for Privilege Escalation).

## Example Commands
The following example commands are provided to demonstrate the use of the tools mentioned:

- **ffuf**: `ffuf -u http://target.com/FUZZ -w /path/to/wordlist.txt`
- **nmap**: `nmap -sV -p- target.com`
- **gobuster**: `gobuster dir -u http://target.com -w /path/to/wordlist.txt`
- **nikto**: `nikto -h http://target.com`
- **wpscan**: `wpscan --url http://target.com`
- **sqlmap**: `sqlmap -u http://target.com/vulnerable_page.php --dbs`
- **dirb**: `dirb http://target.com /path/to/wordlist.txt`
- **nuclei**: `nuclei -l /path/to/targets.txt`

These commands can be used to identify and exploit vulnerabilities in web applications.

## References
- https://academy.hackthebox.com/module/136/section/1289

