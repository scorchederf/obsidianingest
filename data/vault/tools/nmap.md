---
title: nmap
aliases: []
tags:
- tool/nmap
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: nmap.md
related_tools:
- '[[nmap]]'
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

# nmap

## Description
- output all formats are saved to directory
  `-oA scan\nmap`
- search for webhosts based on input list
  - `nmap -p 80,443,8000,8180,8888,10000 --open -oA scan\web_discovery -iL hosts.txt`
- run vulnerability scan against host
  - `nmap -sV --script vuln -oA scan\nmap-vuln $ip`
- run Vulners NSE Script
  - provides a significantly more detailed information on potentially applicable CVEs
  - `it will send traffic out to the internet to get the information`
  - `nmap -sV -p- --script vulners -oA scan\nmap-vulners $ip`

## Full commands examples
```
# Ping scan
nmap -sP 192.168.0.0/24

# Quick scan
nmap -T4 -F 192.168.1.1 -vvv

# Quick scan plus (more info but more aggressive)
nmap -sV -T4 -O -F –version-light 192.168.1.1 -vvv

# TCP Syn and UDP Scan (requires root)
nmap -sS -sU -PN -p T:80,T:445,U:161 192.168.1.1

# Soft nmap
nmap -v -Pn -n -T4 -sT -sV --version-intensity=5 --reason 192.168.1.1

# Full nmap
nmap -v -Pn -n -T4 -sT -p- --reason 192.168.1.1

# Dedicated nmap
nmap -v -Pn -n -T4 -sV --version-intensity=5 -sT -p T:ports_found --reason <IP>
```

## Target specification
```
nmap 192.168.1.1
nmap 192.168.1.1-10
nmap 192.168.1.0/24
nmap google.com
nmap 192.168.1.0/24 --exclude192.168.1.1
nmap -iL targets.txt
```

## Scan techniques
```
# TCP SYN port scan (default, root needed)
nmap -sS 192.168.1.1

# TCP CONNECT port scan (default without root privilege)
# Require full connection so it is slower 
nmap -sT 192.168.1.1

# UDP port scan
nmap -sU 192.168.1.1

nmap -sA 192.168.1.1
nmap -sW 192.168.1.1
nmap -sN 192.168.1.1

# Ping scan
nmap -sP 192.168.0.0/24
```

## Host discovery
```
# No scan, only list targets (get hostnames)
nmap -sL 192.168.1.1

# Disable port scanning, only host discovery
nmap -sn 192.168.1.1

# Disable host discovery, only port scanning, can be usefull if firewall deny PING
nmap -Pn 192.168.1.1

# Disable DNS resolution
nmap 192.168.1.1 -n
```

## Services, ports and OS (fingerprinting
```
nmap -p 20 192.168.1.1
nmap -p 20-100 192.168.1.1
nmap -p U:53,T:25-100 192.168.1.1
nmap -p http,https 192.168.1.1

# All ports
nmap -p- 192.168.1.1

# Fast port scan (100 more common ports)
nmap 192.168.1.1 -F

# Top X ports
nmap 192.168.1.1 --top-ports 2000

# Try to get service version
nmap 192.168.1.1 -sV

# 0-9
nmap 192.168.1.1 -sV --version-intensity 3

# Light mode but faster
nmap 192.168.1.1 -sV --version-light

# Equivalent to version-intensity 9. Harder
nmap 192.168.1.1 -sV --version-all

# Aggressive mode (OS Detection, version, script, traceroute)
nmap 192.168.1.1 -A

# OS Detection using TCP/IP
nmap 192.168.1.1 -O 

# Disable OS dection if at least one open and one closed port are not found
nmap 192.168.1.1 -O --osscan-limit

# OS Scan guess more aggressive
nmap 192.168.1.1 -O --osscan-guess

# Set the maximum number x of OS detection tries against a target 
nmap 192.168.1.1 -O --max-os-tries 2
```

## NSE Scripts
```
# Default script scanning, considered safe
nmap 192.168.1.1 -sC
nmap 192.168.1.1 --script default

nmap 192.168.1.1 --script=xxx
nmap 192.168.1.1 --script=xxx --script-args xx=xx

# Scan default, but remove intrusive scripts
nmap 192.168.1.1 --script “not intrusive

## References
- https://nmap.org/

