---
title: nmap
---

# nmap
- open ports only `nmap -p- $ip`
- tcp `sudo nmap -sV -sC -oA scans/alltcp -p- $ip`
- udp `sudo nmap -F -sU -oA scans/alludp -p- $ip` 
- vuln `sudo nmap --script vuln -v -oA scans/vuln $ip`
- quiet `sudo nmap -p50000 -sS -Pn -n --disable-arp-ping --packet-trace --source-port 53 $ip`
- flags
    - blocking ping probes `-Pn`