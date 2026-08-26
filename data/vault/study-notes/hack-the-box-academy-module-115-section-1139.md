---
title: Hack The Box - Academy Module 115 Section 1139
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: 08-115-ShellsAndPayloads-14-TheLiveEngagement.pdf
related_tools:
- '[[john]]'
- '[[hydra]]'
- '[[lazagne]]'
- '[[impacket]]'
- '[[kerbrute]]'
- '[[keytabextract]]'
- '[[lief]]'
- '[[linenum]]'
- '[[liffy]]'
- '[[lfifreak]]'
- '[[lfisuite]]'
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

# Hack The Box - Academy Module 115 Section 1139

## Overview
This section covers various techniques and tools used in ethical hacking, focusing on password cracking, credential harvesting, and Kerberos attacks. The content is part of the Hack The Box Academy module 115.

## Password Cracking
- **John the Ripper (john)**: A password cracking tool that can be used to crack hashes. It supports various hash types and can be used in a variety of scenarios.
- **Hydra (hydra)**: A network login cracker that can be used to perform brute-force attacks on various protocols and services.

## Credential Harvesting
- **Lazagne (lazagne)**: A password recovery tool that can extract passwords from various applications and services. It supports a wide range of applications and can be used to gather credentials from memory and registry.

## Kerberos Attacks
- **Impacket (impacket)**: A Python library that can be used to perform various Kerberos attacks, such as Kerberos Golden Ticket attacks. It includes tools like `wmiexec` and `psexec` for executing commands on remote machines.
- **Kerbrute (kerbrute)**: A tool that can be used to perform Kerberos brute-force attacks. It can be used to crack Kerberos TGTs (Ticket Granting Tickets) and gain access to the network.

## Keytab Extraction
- **Keytab Extract (keytabextract)**: A tool that can be used to extract keytabs from the system. Keytabs are used in Kerberos authentication and can be used to gain access to the network.

## Binary Analysis
- **Lief (lief)**: A library for parsing and modifying binary files. It can be used to analyze and manipulate executable files, which can be useful in understanding the behavior of malware or other binaries.

## Line Numbering
- **Linenum (linenum)**: A tool that can be used to add line numbers to text files. This can be useful for debugging or analyzing large text files.

## File Analysis
- **Liffy (liffy)**: A tool that can be used to analyze and extract information from various file formats. It can be used to extract passwords, credentials, and other sensitive information from files.

## File Inclusion
- **Lfi Freak (lfifreak)**: A tool that can be used to perform Local File Inclusion (LFI) attacks. LFI attacks can be used to read files from the server, which can be useful for gathering information or extracting sensitive data.

## File Inclusion Suite
- **Lfi Suite (lfisuite)**: A suite of tools that can be used to perform various file inclusion attacks. It includes tools like `lfi-finder` and `lfi-tester` for identifying and exploiting LFI vulnerabilities.

## References
- https://academy.hackthebox.com/module/115/section/1139

