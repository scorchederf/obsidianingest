---
title: Pivoting, Tunneling, and Port Forwarding
aliases: []
tags:
- study-notes
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 12-158-PivotingTunnelingPortForwarding-01-Introduction.pdf
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
This section covers the concepts of pivoting, tunneling, and port forwarding, which are essential techniques for network penetration testing and ethical hacking.

## Pivoting
Pivoting is the process of using a compromised host to gain access to other hosts on a network. This can be achieved through various methods, including DNS pivoting, IP address pivoting, and using a compromised host as a pivot point.

## Tunneling
Tunneling involves creating a secure connection between two points over an insecure network. This can be done using tools like `ettercap` and `evil-winrm` to establish a reverse shell or tunneling connection.

## Port Forwarding
Port forwarding is the process of redirecting traffic from one port to another. This can be useful for redirecting traffic from a local machine to a remote machine or vice versa. Tools like `burpsuite` can be used to set up port forwarding and tunneling.

## Tools and Commands
Here are some tools and commands that can be used for pivoting, tunneling, and port forwarding:

- **ettercap**
  - `ettercap -T -M ARP /192.168.1.0/24 /192.168.1.1/`
- **evil-winrm**
  - `evil-winrm -i 192.168.1.100 -u administrator -p password`
- **burpsuite**
  - `burpsuite -proxy-listen 127.0.0.1:8080`

These commands can be used to set up and manage tunnels and port forwarding.

