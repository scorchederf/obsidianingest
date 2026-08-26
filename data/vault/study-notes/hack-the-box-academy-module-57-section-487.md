---
title: Hack The Box - Academy Module 57 Section 487
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 16-57-BruteForcing-04-UsernameBruteForce.pdf
related_tools:
- '[[gobuster]]'
- '[[ffuf]]'
- '[[dirb]]'
- '[[nmap-1787746090]]'
- '[[curl]]'
- '[[enum4linux-ng]]'
- '[[dnsenum]]'
- '[[bloodhound]]'
- '[[evil-winrm]]'
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

# Hack The Box - Academy Module 57 Section 487

## Introduction
This module covers the basics of web enumeration and information gathering techniques. The goal is to identify and exploit vulnerabilities in a web application.

## Web Enumeration Tools
The following tools are used for web enumeration:

- **Gobuster**: A directory and subdomain enumeration tool.
- **FFUF**: A fast fuzzer for web enumeration.
- **Dirb**: A directory brute-forcing tool.
- **Nmap**: A network scanning tool.
- **Curl**: A command-line tool for transferring data with URLs.
- **Enum4linux-ng**: A tool for enumerating Windows domain information.
- **DNSenum**: A tool for DNS enumeration.
- **Bloodhound**: A tool for Active Directory enumeration.
- **Evil-WinRM**: A tool for executing commands on Windows systems via WinRM.

## Example Commands
Here are some example commands used in the module:

- **Gobuster**
  ```bash
  gobuster dir -u http://target -w /path/to/directory-wordlist.txt
  ```

- **FFUF**
  ```bash
  ffuf -u http://target/FUZZ -w /path/to/wordlist.txt
  ```

- **Dirb**
  ```bash
  dirb http://target
  ```

- **Nmap**
  ```bash
  nmap -sC -sV -O target
  ```

- **Curl**
  ```bash
  curl -I http://target
  ```

- **Enum4linux-ng**
  ```bash
  enum4linux-ng -a target
  ```

- **DNSenum**
  ```bash
  dnsenum target
  ```

- **Bloodhound**
  ```bash
  bloodhound -d target.com
  ```

- **Evil-WinRM**
  ```bash
  evil-winrm -i target -u user -p password
  ```

## References
- https://academy.hackthebox.com/module/57/section/487

