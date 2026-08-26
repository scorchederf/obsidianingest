---
title: Latest FTP Vulnerabilities
aliases: []
tags:
- study-notes
- technique/t1003
- technique/password-cracking
- technique/file-inclusion
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 11-115-AttackingCommonServices-06-LatestFTPVulnerabilities.pdf
related_tools:
- '[[curl]]'
related_techniques:
- '[[t1003]]'
- '[[t1003-003]]'
related_tactics: []
related_services:
- '[[ftp]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Latest FTP Vulnerabilities

## Concept of the Attack
In discussing the latest vulnerabilities, we will focus on the CoreFTP before build 727 vulnerability assigned CVE-2022-22836. This vulnerability is for an FTP service that does not correctly process the HTTP PUT request and leads to an authenticated directory/ arbitrary file write vulnerability. This vulnerability allows us to write files outside the directory to which the service has access.

## CoreFTP Exploitation
The exploit for this attack is relatively straightforward based on a single cURL command. The command is as follows:

```
curl -k -X PUT -H "Host: <IP>" --basic -u <username>:<password> --data-binary "PoC."
```

This command creates a raw HTTP PUT request with basic auth, the path for the file (https://<IP>/../../../../../whoops), and its content (--data-binary "PoC."). Additionally, we specify the header (-H "Host: <IP>") with the IP address of our target system.

## Directory Traversal
1. The user specifies the type of HTTP request with the file's content, including escaping characters to break out of the restricted area.
2. The changed type of HTTP request, file contents, and path entered by the user are taken over and processed by the process.
3. The application checks whether the user is authorized to be in the specified path. Since the restrictions only apply to a specific folder, all permissions granted to it are bypassed as it breaks out of that folder using the directory traversal.
4. The destination is another process that has the task of writing the specified contents of the user on the local system.

## Arbitrary File Write
1. The same information that the user entered is used as the source. In this case, the filename (whoops) and the contents (--data-binary "PoC.").
2. The process takes the specified information and proceeds to write the desired content to the specified file.
3. Since all restrictions were bypassed during the directory traversal vulnerability, the service approves writing the contents to the specified file.
4. The filename specified by the user (whoops) with the desired content ("PoC.") now serves as the destination on the local system.

## Interacting with Common Services
Protocol Specific Attacks
- FTP
- SMB
- SQL Databases
- RDP
- DNS
- SMTP

## References
- https://academy.hackthebox.com/

