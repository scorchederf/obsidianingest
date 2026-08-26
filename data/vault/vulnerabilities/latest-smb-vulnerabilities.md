---
title: Latest SMB Vulnerabilities
aliases: []
tags:
- vulnerabilities/CVE-2020-0796
- technique/t1059
- technique/t1132
- attack-methodologies/lateral-movement
category: vulnerabilities
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 11-115-AttackingCommonServices-08-LatestSMBVulnerabilities.pdf
related_tools: []
related_techniques:
- '[[T1059.004]]'
- '[[t1132]]'
related_tactics:
- '[[ta0005]]'
related_services:
- '[[smb-1787747781]]'
related_os: []
related_notes: []
mitre_tactic: TA0005
mitre_technique: T1059.004, T1132
real_path: ''
port: ''
protocol: ''
os: ''
---

# Latest SMB Vulnerabilities

## Overview
One recent significant vulnerability that affected the SMB protocol was called SMBGhost with the CVE-2020-0796. This vulnerability consisted of a compression mechanism of the version SMB v3.1.1, which made Windows 10 versions 1903 and 1909 vulnerable to an unauthenticated attacker. The vulnerability allowed the attacker to gain remote code execution (RCE) on the target system.

## Concept of the Attack
The concept of the attack is an integer overflow vulnerability in a function of an SMB driver that allows system commands to be overwritten while accessing memory. An integer overflow results from a CPU attempting to generate a number that is greater than the value that can be stored in the allocated memory space. Arithmetic operations can always return unexpected values, resulting in an error. An example of an integer overflow can occur when a programmer does not allow a negative number to occur. In this case, an integer overflow occurs when a variable performs an operation that results in a negative number, and the variable is returned as a positive integer. This vulnerability occurred because, at the time, the function lacked bounds checks to handle the size of the data sent in the process of SMB session negotiation.

## Initiation of the Attack
1. The client sends a request manipulated by the attacker to the SMB server.
2. The sent compressed packets are processed according to the negotiated protocol responses.
3. This process is performed with the system's privileges or at least with the privileges of an administrator.
4. The local process is used as the destination, which should process these compressed packets.
This is when the cycle starts all over again, but this time to gain remote access to the target system.

## Trigger Remote Code Execution
1. The sources used in the second cycle are from the previous process.
2. In this process, the integer overflow occurs by replacing the overwritten buffer with the attacker's instructions and forcing the CPU to execute those instructions.
3. The same privileges of the SMB server are used.
4. The remote attacker system is used as the destination, in this case, granting access to the local system.

## References
- https://academy.hackthebox.com/

