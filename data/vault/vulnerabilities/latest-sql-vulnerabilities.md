---
title: Latest SQL Vulnerabilities
aliases: []
tags:
- vulnerabilities/sql
- tool/enum4linux-ng
- technique/t1003-003
- technique/t1132-001
category: vulnerabilities
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 11-115-AttackingCommonServices-10-LatestSQLVulnerabilities.pdf
related_tools:
- '[[enum4linux-ng]]'
related_techniques:
- '[[t1003-003]]'
- '[[t1132-001]]'
related_tactics: []
related_services:
- '[[mssql]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: T1003.003, T1132.001
real_path: ''
port: ''
protocol: ''
os: ''
---

# Latest SQL Vulnerabilities

## Concept of the Attack
We will focus on the undocumented MSSQL server function called xp_dirtree for this vulnerability. This function is used to view the contents of a specific folder (local or remote). Furthermore, this function provides some additional parameters that can be specified. These include the depth, how far the function should go in the folder, and the actual target folder.

## Concept of Attacks
1. The source here is the user input, which specifies the function and the folder shared in the network.
2. The process should ensure that all contents of the specified folder are displayed to the user.
3. The execution of system commands on the MSSQL server requires elevated privileges with which the service executes the commands.
4. The SMB service is used as the destination to which the specified information is forwarded. This is when the cycle starts all over again, but this time to obtain the NTLMv2 hash of the MSSQL service user.

## Steal The Hash
5. Here, the SMB service receives the information about the specified order through the previous process of the MSSQL service.
6. The data is then processed, and the specified folder is queried for the contents.
7. The associated authentication hash is used accordingly since the MSSQL running user queries the service.
8. In this case, the destination for the authentication and query is the host we control and the shared folder on the network.
Finally, the hash is intercepted by tools like Responder, WireShark, or TCPDump and displayed to us, which we can try to use for our purposes.

## References
- https://academy.hackthebox.com/

