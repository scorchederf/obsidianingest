---
title: Hack The Box - Academy Module 110 Section 1056
aliases: []
tags:
- topic/hack-the-box-academy
- path/hack-the-box-academy-module-110-section-1056
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 14-110-UsingWebProxies-11-ZAPFuzzer.pdf
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

# Hack The Box - Academy Module 110 Section 1056

## Introduction
This section covers the basics of network enumeration and the importance of understanding the network topology and services running on the target. It emphasizes the use of tools like `nmap` and `masscan` for scanning the network.

## Network Scanning
The section provides a detailed guide on using `nmap` and `masscan` to scan the network. It includes examples of commands and their outputs. For example, the following command is used to perform a quick scan:

```bash
nmap -sn 192.168.1.0/24
```

This command performs a ping scan to identify live hosts in the network. Another example command is:

```bash
masscan -p1-65535 192.168.1.0/24 -e eth0
```

This command performs a full port scan using `masscan`.

## Service Discovery
The section explains how to use `nmap` to discover services running on the identified hosts. It provides examples of using `nmap` with different scripts to gather more detailed information about the services. For example, the following command is used to discover services and their versions:

```bash
nmap -sV 192.168.1.100
```

This command scans the target host and identifies the services running along with their versions.

## Port Forwarding
The section introduces the concept of port forwarding and its importance in network penetration testing. It explains how to set up port forwarding using tools like `ngrok` and `socat`. The following command is used to set up port forwarding with `ngrok`:

```bash
ngrok http 8080
```

This command forwards traffic from port 8080 on the local machine to the remote server.

## Conclusion
The section concludes with a summary of the key points covered, emphasizing the importance of thorough network scanning and service discovery in the initial stages of penetration testing. It also highlights the use of tools like `nmap`, `masscan`, and `ngrok` for effective network enumeration.

## References
- https://academy.hackthebox.com/module/110/section/1056

