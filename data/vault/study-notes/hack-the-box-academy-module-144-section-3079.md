---
title: Hack The Box - Academy Module 144 Section 3079
aliases: []
tags:
- topic/hack-the-box-academy
- tool/
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 05-144-informationgathering-web-10-CreepyCrawlies.pdf
related_tools:
- '[[john]]'
- '[[hydra]]'
- '[[gobuster]]'
- '[[fierce]]'
- '[[dirb]]'
- '[[nmap-1787746090]]'
- '[[nmap-1787746090]]'
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

# Hack The Box - Academy Module 144 Section 3079

## Overview
This section of the Hack The Box Academy Module 144 focuses on password cracking and enumeration techniques. The instructor demonstrates the use of various tools and techniques to gain access to a target system.

## Password Cracking
The instructor uses the `john` tool for password cracking. The steps include:

1. **Identifying the Hash Type**: Determine the hash type of the password.
2. **Using Wordlists**: Utilize wordlists to crack the password.
3. **Brute-forcing**: Employ brute-forcing techniques if necessary.

Example command: `john --wordlist=/path/to/wordlist hash.txt`

The instructor also mentions the use of `hydra` for password cracking, particularly for SSH and FTP services.

## Web Enumeration
The instructor uses `gobuster` and `fierce` for web enumeration. These tools are used to discover hidden directories and files on the target server.

Example commands:

- `gobuster dir -u http://target.com -w /path/to/directory-wordlist`
- `fierce -u http://target.com -w /path/to/directory-wordlist`

The instructor also mentions the use of `dirb` for similar purposes.

## Network Scanning
The instructor uses `nmap` for network scanning. The steps include:

1. **Basic Scan**: Perform a basic scan to identify open ports and services.
2. **Detailed Scan**: Use more detailed options to gather more information about the target.

Example commands:

- `nmap -sS -O target.com`
- `nmap -sV -p- target.com`

The instructor also mentions the use of `nmap` for service version detection and OS detection.

## References
- https://academy.hackthebox.com/module/144/section/3079

