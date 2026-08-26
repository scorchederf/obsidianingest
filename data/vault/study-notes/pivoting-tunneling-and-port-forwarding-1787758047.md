---
title: Pivoting, Tunneling, and Port Forwarding
aliases: []
tags:
- topic/pivoting
- topic/tunneling
- topic/port-forwarding
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 12-158-pivoting-01-introduction.pdf
related_tools:
- '[[ettercap]]'
- '[[evil-winrm]]'
- '[[burpsuite]]'
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

# Pivoting, Tunneling, and Port Forwarding

## Introduction
Pivoting, tunneling, and port forwarding are techniques used in cybersecurity to extend the reach of an attacker's network or to bypass network restrictions. These techniques are often used in penetration testing and ethical hacking to gain access to internal networks or to tunnel traffic through a compromised host.

## Pivoting
Pivoting involves using a compromised host to gain access to other networks that the attacker would not normally have access to. This can be achieved by setting up a reverse SSH tunnel or by using tools like `ettercap` to manipulate network traffic.

### Example
```bash
ssh -R 2222:localhost:22 user@compromised_host
```
This command sets up a reverse SSH tunnel, allowing the attacker to connect to the local machine from the compromised host on port 2222.

## Tunneling
Tunneling involves creating a secure connection between two points to forward traffic. This can be used to bypass network restrictions or to access internal services from an external network. Tools like `evil-winrm` and `burpsuite` can be used for tunneling.

### Example with evil-winrm
```bash
evil-winrm -i 10.10.10.10 -u user -p password
```
This command connects to a Windows machine using `evil-winrm`, allowing the attacker to execute commands on the remote machine.

## Port Forwarding
Port forwarding involves redirecting traffic from one port to another. This can be used to expose services on a local machine to the internet or to forward traffic from a remote machine to a local machine. Tools like `ettercap` can be used for port forwarding.

### Example with ettercap
```bash
ettercap -T -q -M ARP /10.10.10.10/ /10.10.10.11/
```
This command uses `ettercap` to perform ARP poisoning between two hosts, allowing the attacker to intercept and manipulate traffic between them.

