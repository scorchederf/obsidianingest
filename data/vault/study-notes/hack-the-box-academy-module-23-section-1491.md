---
title: Hack The Box - Academy Module 23 Section 1491
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 20-23-FileInclusion-03-BasicBypasses.pdf
related_tools:
- '[[gobuster]]'
- '[[ffuf]]'
- '[[dirb]]'
- '[[fierce]]'
- '[[gobuster]]'
- '[[ffuf]]'
- '[[dirb]]'
- '[[fierce]]'
related_techniques:
- '[[file-inclusion]]'
- '[[crawling]]'
- '[[file-inclusion]]'
- '[[crawling]]'
- '[[file-inclusion]]'
- '[[crawling]]'
- '[[file-inclusion]]'
- '[[crawling]]'
related_tactics:
- '[[t1003]]'
- '[[t1003]]'
- '[[t1003]]'
- '[[t1003]]'
- '[[t1003]]'
- '[[t1003]]'
- '[[t1003]]'
- '[[t1003]]'
related_services:
- '[[http]]'
- '[[http]]'
- '[[http]]'
- '[[http]]'
- '[[http]]'
- '[[http]]'
- '[[http]]'
- '[[http]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Hack The Box - Academy Module 23 Section 1491

## Overview
This module covers techniques for web application enumeration and exploitation, focusing on file inclusion and crawling. The techniques involve using tools like gobuster, ffuf, dirb, and fierce to identify and exploit vulnerabilities in web applications.

## Tools and Techniques
The following tools and techniques are discussed in the module:

- **gobuster**: A tool for directory and file brute-forcing.
- **ffuf**: A tool for fast fuzzing of HTTP(S) endpoints.
- **dirb**: A web server directory brute-forcing tool.
- **fierce**: A tool for discovering hidden hosts and services.

These tools are used to identify and exploit file inclusion vulnerabilities and to crawl web applications for potential targets.

## Examples
The module provides examples of using these tools to enumerate and exploit file inclusion vulnerabilities in web applications. For instance, the following command is used to brute-force directories and files using gobuster:

```bash
$ gobuster dir -u http://target.com -w /path/to/wordlist.txt
```

Similarly, the following command is used with ffuf to fuzz HTTP(S) endpoints:

```bash
$ ffuf -u http://target.com/FUZZ -w /path/to/wordlist.txt
```

These commands are used to identify potential targets and vulnerabilities in the web application.

## References
- https://academy.hackthebox.com/module/23/section/1491

