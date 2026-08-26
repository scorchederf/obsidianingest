---
title: Hack The Box - Academy Module 33 Section 792
aliases: []
tags:
- topic/hack-the-box-academy
- topic/web-attacks
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 17-33-SqlInjectionFundamentals-13-ReadingFiles.pdf
related_tools:
- '[[gobuster]]'
- '[[hydra]]'
- '[[nmap-1787746090]]'
- '[[curl]]'
- '[[dirb]]'
related_techniques:
- '[[web-attacks]]'
related_tactics:
- '[[reconnaissance]]'
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

# Hack The Box - Academy Module 33 Section 792

## Introduction
This module covers web application security and the techniques used to identify and exploit vulnerabilities in web applications. The focus is on using tools like `gobuster`, `hydra`, and `nmap` to discover and test web services.

## Tools and Techniques
The following tools and techniques are discussed in the module:

- **gobuster**: A directory and file brute-forcing tool. It can be used to discover hidden directories and files on a web server.

- **hydra**: A network login cracker that can be used to brute-force login credentials.

- **nmap**: A network scanning tool that can be used to discover open ports and services.

- **curl**: A command-line tool for transferring data with URLs. It can be used to test web services and download files.

- **dirb**: A directory and file brute-forcing tool similar to `gobuster`.

## Example Commands
The module provides the following example commands for using the tools mentioned:

- **gobuster**
  ```bash
  gobuster dir -u http://target.com -w /path/to/wordlist.txt
  ```

- **hydra**
  ```bash
  hydra -L usernames.txt -P passwords.txt http://target.com http-get-form /login:username:password
  ```

- **nmap**
  ```bash
  nmap -sV -p 80,443 target.com
  ```

- **curl**
  ```bash
  curl -X POST -d 'username=admin&password=admin' http://target.com/login
  ```

- **dirb**
  ```bash
  dirb http://target.com /path/to/wordlist.txt
  ```

## References
- https://academy.hackthebox.com/module/33/section/792

