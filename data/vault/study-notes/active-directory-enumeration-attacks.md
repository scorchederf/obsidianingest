---
title: Active Directory Enumeration & Attacks
aliases: []
tags:
- topic/active-directory
- tool/mimikatz
- tool/enum4linux-ng
- tool/dnsenum
- technique/t1003
- technique/t1008
- technique/t1020
- technique/t1132
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: 13-143-AttackingActiveDirectory-03-Scenario.pdf
related_tools:
- '[[mimikatz]]'
- '[[enum4linux-ng]]'
- '[[dnsenum]]'
related_techniques:
- '[[t1003-003]]'
- '[[t1008]]'
- '[[t1020]]'
- '[[t1132]]'
related_tactics:
- '[[ta0003]]'
related_services: []
related_os: []
related_notes: []
mitre_tactic: TA0003
mitre_technique: T1003.003, T1008, T1020, T1132
real_path: ''
port: ''
protocol: ''
os: ''
---

# Active Directory Enumeration & Attacks

## Introduction
Active Directory (AD) enumeration and attacks are crucial for understanding how to both defend against and exploit AD environments. This study note covers various techniques and tools used for enumerating and attacking AD.

## Tools
- **Mimikatz**: A powerful tool for post-exploitation that can extract credentials, Kerberos tickets, and more.
- **Enum4Linux-ng**: A tool for enumerating services and shares on Windows machines.
- **Dnsenum**: A tool for DNS enumeration to gather information about AD domains and hosts.

## Techniques
- **T1003.003**: Credential Dumping
- **T1008**: Discovery of Domain Members
- **T1020**: Discovery of Domain Trust Relationships
- **T1132**: Discovery of Domain Users, Groups, and Computers

## Example Commands
- **Mimikatz**: `mimikatz # sekurlsa::logonpasswords`
- **Enum4Linux-ng**: `enum4linux-ng -a <target_ip>`
- **Dnsenum**: `dnsenum --dns <target_dns_server>`

## References
- https://academy.hackthebox.com/module/143/section/1263

