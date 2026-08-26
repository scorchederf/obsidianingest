---
title: Hack The Box - Academy Module 33 Section 191
aliases: []
tags:
- topic/hack-the-box-academy
- path/hack-the-box-academy-module-33-section-191
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 17-33-SqlInjectionFundamentals-05-QueryResults.pdf
related_tools: []
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

# Hack The Box - Academy Module 33 Section 191

## Overview
This section covers the use of `nmap` for network scanning and enumeration. It provides a step-by-step guide on how to use `nmap` to identify open ports and services on a target machine.

## Nmap Usage
The following commands are provided for using `nmap` to scan a target IP address for open ports and services:

```bash
nmap -sS -sV -O 192.168.1.100
```

- `-sS` performs a TCP SYN scan.
- `-sV` enables service version detection.
- `-O` enables OS detection.

This command will provide detailed information about the open ports, services, and operating system of the target machine.

## Example Output
The output from the `nmap` command might look like this:

```plaintext
Nmap scan report for 192.168.1.100
Host is up (0.00032s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
```

This output indicates that the target machine has SSH and HTTP services running on ports 22 and 80, respectively.

## References
- https://academy.hackthebox.com/module/33/section/191

