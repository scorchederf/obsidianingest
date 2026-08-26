---
title: Hack The Box - Academy Module 143 Section 1264
aliases: []
tags:
- topic/hack-the-box-academy
- topic/active-enumeration
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 13-143-AttackingActiveDirectory-04-ExternalReconandEnumerationPrinciples.pdf
related_tools:
- '[[nmap-1787746090]]'
- '[[nikto]]'
- '[[dirb]]'
- '[[wpscan]]'
- '[[sqlmap]]'
related_techniques:
- '[[T1046]]'
- '[[T1588]]'
- '[[T1595]]'
related_tactics:
- '[[ta0003]]'
- '[[ta0005]]'
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

# Hack The Box - Academy Module 143 Section 1264

## Introduction
This section covers the basics of active enumeration techniques and tools used to identify and exploit vulnerabilities in web applications. The focus is on using tools like nmap, nikto, dirb, wpscan, and sqlmap to gather information and identify potential targets.

## Active Enumeration Techniques
Active enumeration involves actively probing the target system to gather information. This can include scanning for open ports, identifying services, and testing for vulnerabilities. The techniques covered include:
- **T1046 - Network Scanning**: Using tools like nmap to scan for open ports and services.
- **T1588 - Service Scan**: Using tools like nmap to identify services running on the target.
- **T1595 - Network Service Scanning**: Using tools like nmap to scan for network services and their versions.

## Tools and Commands
The following tools and commands are used in the module to perform active enumeration:
- **nmap**: 
  ```bash
  nmap -sV -p- <target>
  ```
  This command scans all ports on the target and identifies the services running on each port.
- **nikto**: 
  ```bash
  nikto -h <target>
  ```
  This command scans the target for common web server misconfigurations and vulnerabilities.
- **dirb**: 
  ```bash
  dirb <target> /path/to/directory
  ```
  This command scans the target for directories and files.
- **wpscan**: 
  ```bash
  wpscan --url <target>
  ```
  This command scans the target for WordPress vulnerabilities.
- **sqlmap**: 
  ```bash
  sqlmap -u <target>
  ```
  This command is used to test for SQL injection vulnerabilities.

## References
- https://academy.hackthebox.com/module/143/section/1264

