---
title: Network Scan Results
aliases: []
tags:
- detection/nmap
category: detections
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: network.md
related_tools:
- '[[nmap-1787746090]]'
related_techniques: []
related_tactics: []
related_services:
- '[[ssh]]'
- '[[http]]'
- '[[smtp]]'
- '[[msrpc]]'
- '[[netbios-ssn]]'
- '[[microsoft-ds]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Network Scan Results

## Network Scan Summary
The network scan results include the following open ports and services on the hosts 192.168.207.12, 192.168.207.6, 192.168.207.8, 192.168.207.9, and 192.168.207.11.

- **192.168.207.12**
  - 135/tcp: msrpc
  - 139/tcp: netbios-ssn
  - 445/tcp: microsoft-ds

- **192.168.207.6**
  - 22/tcp: ssh (OpenSSH 8.2p1 Ubuntu 4ubuntu0.3)
  - 80/tcp: http (Apache httpd 2.4.41)

- **192.168.207.8**
  - 22/tcp: ssh (OpenSSH 8.2p1 Ubuntu 4ubuntu0.2)
  - 25/tcp: smtp (Postfix smtpd)

- **192.168.207.9**
  - 135/tcp: msrpc
  - 139/tcp: netbios-ssn
  - 445/tcp: microsoft-ds

- **192.168.207.11**
  - 135/tcp: msrpc
  - 139/tcp: netbios-ssn
  - 445/tcp: microsoft-ds

## Service Details
Service detection results for the hosts include the following details:

- **192.168.207.12**
  - SMB2 security mode: Message signing enabled but not required
  - Clock skew: 2s

- **192.168.207.6**
  - SSH hostkey: RSA, ECDSA, ED25519
  - HTTP server header: Apache/2.4.41 (Ubuntu)
  - HTTP title: Under Construction
  - SSL certificate: Subject: commonName=mail, Subject Alternative Name: DNS:mail, Not valid before: 2021-12-02T15:18:58, Not valid after: 2031-11-30T15:18:58
  - SMTP commands: mail, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING

- **192.168.207.8**
  - SSH hostkey: RSA, ECDSA, ED25519
  - SMTP commands: mail, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING

- **192.168.207.9**
  - SMB2 security mode: Message signing enabled but not required
  - Clock skew: 3s
  - SMB2 time: date: 2023-04-25T06:21:37, start_date: N/A
  - Clock skew: 3s (192.168.207.11)
  - Clock skew: 3s (192.168.207.9)

