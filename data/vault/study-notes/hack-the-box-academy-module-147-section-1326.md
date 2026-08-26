---
title: Hack The Box - Academy Module 147 Section 1326
aliases: []
tags:
- topic/hack-the-box-academy
- topic/web-attacks
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 10-147-passwordattacks-09-AttackingActiveDirectoryAndNTDS.dit.pdf
related_tools:
- '[[ffuf]]'
- '[[nikto]]'
- '[[wpscan]]'
related_techniques:
- '[[web-attacks]]'
related_tactics:
- '[[passive-enumeration]]'
- '[[active-enumeration]]'
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

# Hack The Box - Academy Module 147 Section 1326

## Introduction
This section covers the use of web application scanning tools to identify vulnerabilities in a web application. The tools discussed include ffuf, Nikto, and wpscan.

## Web Application Scanning Tools
The following tools are used to scan web applications for vulnerabilities:

- **ffuf**: A fast fuzzer that can be used to find directories and files on a web server.

- **Nikto**: A web server scanner that performs comprehensive tests against web servers to identify vulnerabilities and misconfigurations.

- **wpscan**: A tool for WordPress site and plugin security auditing.

## Usage of ffuf
To use ffuf, you can run the following command to scan a web application for directories and files:

```bash
ffuf -u http://target.com/FUZZ -w /path/to/wordlist.txt
```

This command will scan the target web application for directories and files using the provided wordlist.

## Usage of Nikto
To use Nikto, you can run the following command to scan a web server for vulnerabilities:

```bash
nikto -h http://target.com
```

This command will perform a comprehensive scan of the target web server and report any vulnerabilities found.

## Usage of wpscan
To use wpscan, you can run the following command to scan a WordPress site for vulnerabilities:

```bash
wpscan --url http://target.com --enumerate v
```

This command will scan the target WordPress site for vulnerabilities and enumerate plugins.

## References
- https://academy.hackthebox.com/module/147/section/1326

