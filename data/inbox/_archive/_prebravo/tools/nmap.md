---
id: tools-apache2
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-apache2

backlinks: [[]]

sources:

---

- Default settings
  - SYN or stealth scannign (sends SYN and awaits SYACK response, never sends a final ack)
  - to search for scripts ```shell ls -1 /usr/share/nmap/scripts/smb*```
- flags
    - -sT       starts a connect scan which waits for the connection to complete (and is therefore slower)
    - -sU       starts a udp scan
    - -oG       outputs in a grepable format
    - -O        OS fingerprinting
    - -sV       service banners (banners can be modified by sys admins to lie and scans can be slow)
    - -A        service enumeration scripts
    - --open    only show open ports
    - -t4       t0 (slow) to t5(insane mode), t4 is a good mix
    - --script=smb-os-discovery  located here /usr/share/nmap/scripts
- examples
  - tcp and udp scan ```shell sudo nmap -sS -sU 10.11.1.115```
  - network sweep (icmp echo, tcp syn 443, tcp ack 80, icmp timestamp) ```shell nmap -sn 10.11.1.1-254```
  - network sweep targeted at port 80 ```nmap -p 80 10.11.1.1-254 -oG web-sweep.txt```
    - ```shell grep open web-sweep.txt | cut -d" " -f2```
  - tcp connect scan, top 20 ports (/usr/share/nmap/nmap-services), os version detection, script scanning, traceroute with A ```shell nmap -sT -A -O --top-ports=20 10.11.1.1-254 -oG top-port-sweep.txt```
  - os fingerprinting ```shell sudo nmap -O 10.11.1.220```
  - banner grabbing or service enumeration ```shell nmap -sV -sT -A 10.11.1.220```
  - smb-os-discovery script attempts to connect to the SMB service on a target system and determine its operating system```shell nmap 10.11.1.220 --script=smb-os-discovery```
  - search and show only open ports but run fast ```shell sudo nmap -T4 -sS --open -p 1024-65535 $IP```
  - search for title pages on ip range ```shell nmap -T4 -sV --script=http-title --open 192.168.165.1-254```
  -  
