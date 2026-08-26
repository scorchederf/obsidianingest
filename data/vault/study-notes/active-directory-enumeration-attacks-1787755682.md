---
title: Active Directory Enumeration & Attacks
aliases: []
tags:
- topic/active-directory-enumeration-attacks
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 13-143-AttackingActiveDirectory-02-ToolsOfTheTrade.pdf
related_tools:
- '[[enum4linux-ng]]'
- '[[nmap-1787746090]]'
- '[[responder]]'
- '[[BloodHound]]'
- '[[PowerView]]'
- '[[powershell]]'
related_techniques:
- '[[t1003]]'
- '[[t1089]]'
- '[[t1132]]'
related_tactics:
- '[[ta0005]]'
related_services:
- '[[ldap]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Active Directory Enumeration & Attacks

## Introduction
Active Directory (AD) is a critical component of many enterprise networks, providing centralized user and resource management. Enumerating AD can reveal valuable information about the network, including user accounts, groups, and permissions. This study note covers various techniques and tools for enumerating Active Directory.

## Tools and Techniques
Several tools and techniques are commonly used for AD enumeration. These include:

- **enum4linux-ng**: A tool for enumerating information from an Active Directory domain. It can be used to gather information such as domain controllers, users, and groups.

- **nmap**: A network scanning tool that can be used to discover services and hosts on a network. It can also be used to gather information about AD services.

- **responder**: A tool that can be used to capture and analyze network traffic, including Kerberos tickets and NTLM hashes.

- **BloodHound**: A graphing tool that visualizes the relationships between users, groups, and resources in an AD environment.

- **PowerView**: A PowerShell module that provides a set of cmdlets for enumerating AD information.

- **PowerShell**: The scripting language used to interact with AD and perform various enumeration tasks.

## Techniques
Several MITRE ATT&CK techniques are relevant to AD enumeration:

- **T1003**: Collection of credentials. This involves gathering credentials from various sources, including AD.

- **T1089**: Use of credentials. This involves using collected credentials to gain access to systems or services.

- **T1132**: Discovery of shared resources. This involves identifying shared resources in the network, which can be useful for lateral movement.

## Mitigation
Mitigating AD enumeration attacks involves implementing strong security practices, such as:

- Enforcing strong password policies.

- Implementing multi-factor authentication (MFA).

- Regularly updating and patching systems.

- Monitoring network traffic for unusual activity.

## References
- https://academy.hackthebox.com/module/143/section/1517

