---
title: Login Brute Forcing
aliases: []
tags:
- study-notes/login-brute-forcing
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 16-57-BruteForcing-06-DetermineLoginParameters.pdf
related_tools:
- '[[crackmapexec]]'
- '[[get-240token]]'
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

# Login Brute Forcing

## Introduction
This study note covers the technique of login brute forcing, which involves attempting to gain unauthorized access to a system by systematically trying different passwords.

## Tools
The following tools are discussed in the study note:

- **crackmapexec**: A tool used for brute forcing and auditing of network shares, services, and protocols.
- **get-240token**: A tool used to retrieve tokens for authentication purposes.

## Crackmapexec
Crackmapexec is a versatile tool that can be used for various purposes, including brute forcing. Here is an example of how to use it for brute forcing a service:

```bash
\crackmapexec smb <target_ip> -u <username> -p <password>
```

This command attempts to brute force the password for the specified username on the SMB service of the target IP.

## Get-240token
The `get-240token` tool is used to retrieve tokens for authentication. This is particularly useful when dealing with services that require token-based authentication. Here is an example of how to use it:

```bash
\get-240token <target_url>
```

This command retrieves a token from the specified URL, which can then be used for further authentication.

## References
- https://academy.hackthebox.com/module/57/section/504

