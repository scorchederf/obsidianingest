---
title: Hack The Box - Academy Module 18 Section 79
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: 31-18-LinuxFundamentals-09-FileDescriptorsAndRedirects.pdf
related_tools:
- '[[john]]'
- '[[hydra]]'
- '[[masscan]]'
- '[[gobuster]]'
- '[[fierce]]'
- '[[nmap-1787746090]]'
- '[[curl]]'
- '[[dig]]'
- '[[ettercap]]'
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

# Hack The Box - Academy Module 18 Section 79

## Overview
This module covers various techniques and tools used in ethical hacking, focusing on password cracking, enumeration, and network scanning. The content includes practical exercises and explanations of how to use tools like John the Ripper, Hydra, Masscan, and Nmap.

## Password Cracking
The module introduces the use of John the Ripper for password cracking. It covers the following steps:

1. Install John the Ripper using `sudo apt-get install john`.
2. Use the `john` command to crack a password hash. For example, `john --wordlist=/path/to/wordlist /path/to/hash`.
3. Use Hydra for password cracking. For example, `hydra -L /path/to/usernames -P /path/to/passwords -t 4 -vV httplogin`.

## Network Scanning
The module covers network scanning using tools like Masscan and Nmap. It explains how to perform a quick scan using Masscan and a detailed scan using Nmap. For example, `masscan -p1-65535 192.168.1.1/24` and `nmap -sS -sV -O 192.168.1.1`.

## Service Enumeration
The module discusses the use of tools like Nmap, Nmap scripts, and other enumeration tools to identify open services and their versions. It covers techniques such as using `nmap -sV` to identify service versions and `nmap --script vuln` to find potential vulnerabilities.

## DNS Enumeration
The module explains how to use tools like `dig` and `nmap` for DNS enumeration. It covers techniques such as using `dig` to resolve domain names and `nmap` to discover subdomains and open ports.

## Web Enumeration
The module covers web enumeration techniques using tools like `gobuster` and `fierce`. It explains how to use `gobuster` to discover hidden directories and files and `fierce` to find subdomains and open ports.

## Reverse Engineering
The module touches on basic reverse engineering techniques, such as using `nmap` to identify services and `curl` to interact with web services. It covers examples like using `curl` to fetch web content and `nmap` to scan for open ports.

## References
- https://academy.hackthebox.com/module/18/section/79

