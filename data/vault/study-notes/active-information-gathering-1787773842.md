---
title: active-information-gathering
aliases: []
tags:
- topic/active-information-gathering
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: notes.md
related_tools:
- '[[openssl]]'
- '[[mingw-w64]]'
related_techniques:
- '[[t1003]]'
- '[[t1059]]'
- '[[t1132]]'
related_tactics:
- '[[ta0003]]'
- '[[ta0005]]'
related_services:
- '[[ServiioService.exe]]'
- '[[Serviio]]'
related_os:
- '[[C:\Program Files\Serviio\bin\ServiioService.exe]]'
- '[[C:\Program Files\My Program\My Service\service.exe]]'
- '[[C:\Program Files\USBPcap\USBPcap.inf]]'
- '[[/etc/cron*]]'
- '[[etc-crontab]]'
- '[[/var/scripts/user_backups.sh]]'
- '[[etc-passwd]]'
- '[[S-1-1-0]]'
- '[[S-1-5-114]]'
- '[[S-1-5-32-544]]'
- '[[S-1-5-32-545]]'
- '[[S-1-5-4]]'
- '[[S-1-2-1]]'
- '[[S-1-5-11]]'
- '[[S-1-5-15]]'
- '[[S-1-5-113]]'
- '[[S-1-2-0]]'
- '[[S-1-5-64-10]]'
- '[[S-1-16-8192]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# active-information-gathering

## active-information-gathering
backlinks: [[snippets-bash]]

sources:
- <https://danielmiessler.com/study/vulnerability-database-resources/>

## Unquoted Service Paths
This technique involves exploiting unquoted service paths to escalate privileges. When a service path is unquoted, Windows will interpret the path incorrectly, allowing an attacker to place a malicious executable in a directory that corresponds to one of the interpreted paths. This can be used to run the malicious executable with the same privileges as the service, often the NT\SYSTEM account. The example provided shows how to replace the ServiioService.exe with a malicious executable named adduser.exe, which then adds a user to the administrators group and restarts the machine.

## Windows Kernel Vulnerabilities
Exploiting system-level software, such as drivers or the kernel, requires careful consideration of the target's operating system, version, and architecture. The example provided demonstrates how to identify the correct version and architecture of the USBPcap driver using `systeminfo` and `driverquery`. It then compiles a C code exploit using MinGW-w64 and executes it on the Windows victim machine to potentially escalate privileges.

## Linux Privileges
The example demonstrates how to exploit insecure file permissions on a Linux system. It shows how to modify a cron job script to add a reverse shell one-liner, and how to modify the /etc/passwd file to add a new superuser account. The steps include generating a password hash, appending it to the /etc/passwd file, and then switching to the new superuser account.

## Group Information
GROUP INFORMATION
-----------------

Group Name                                                    Type             SID          Attributes
============================================================= ================ ============ ==================================================
Everyone                                                      Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account and member of Administrators group Well-known group S-1-5-114    Group used for deny only
BUILTIN\Administrators                                        Alias            S-1-5-32-544 Group used for deny only
BUILTIN\Users                                                 Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\INTERACTIVE                                      Well-known group S-1-5-4      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                                                 Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users                              Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization                                Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account                                    Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
LOCAL                                                         Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication                              Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Mandatory Level                        Label            S-1-16-8192

## References
- https://danielmiessler.com/study/vulnerability-database-resources/
- https://www.mingw-w64.org/

