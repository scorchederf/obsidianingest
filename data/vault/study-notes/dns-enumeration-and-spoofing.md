---
title: DNS Enumeration and Spoofing
aliases: []
tags:
- study-notes/dns
- tool/nmap
- tool/dig
- tool/fierce
- tool/gobuster
- tool/subfinder
- tool/subbrute
- tool/ettercap
- tool/bettercap
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: dns.md
related_tools:
- '[[nmap]]'
- '[[dig]]'
- '[[fierce]]'
- '[[gobuster]]'
- '[[subfinder]]'
- '[[subbrute]]'
- '[[ettercap]]'
- '[[bettercap]]'
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

# DNS Enumeration and Spoofing

## DNS Enumeration
- [viewdns.info](https://viewdns.info/)

- `nmap -p53 -Pn -sV -sC $ip`

- `dig AXFR @ns1.inlanefreight.htb inlanefreight.htb`

- [fierce](https://github.com/mschwager/fierce)
    - install `python -m pip install fierce`

- `sudo echo "$ip $hn" >> /etc/hosts` !! check

- `gobuster dns -d $dn -w /usr/share/wordlists/seclists/Discovery/DNS/dns-Jhaddix.txt -o scans/domains.gobuster`

- subdomains
    - fuff
        - `ffuf -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u -o scans/subdomains.ffuf http://FUZZ.$hostname/`
    - [subfinder](https://github.com/projectdiscovery/subfinder)
        - `/subfinder -d inlanefreight.com -v`
    - [subbrute](https://github.com/TheRook/subbrute.git)
        - install `git clone https://github.com/TheRook/subbrute.git >> /dev/null 2>&1`
        - set resolvers `echo "ns1.inlanefreight.com" > ./resolvers.txt`
        - exec `./subbrute inlanefreight.com -s ./names.txt -r ./resolvers.txt`
        - `python3 subbrute.py inlanefreight.htb -s /usr/share/seclists/Discovery/DNS/namelist.txt -r resolvers.txt`
        - `dig axfr hr.inlanefreight.htb @inlanefreight.htb | grep "TXT"`

- [can-i-take-over-xyz](https://github.com/EdOverflow/can-i-take-over-xyz)

## DNS Spoofing
- [ettercap](https://www.ettercap-project.org/)
    - modify `cat /etc/ettercap/etter.dns` to add in target domain and ip address
        - `inlanefreight.com      A   192.168.225.110`
        - `*.inlanefreight.com    A   192.168.225.110`
    - start ettercap and scan for live hosts `Hosts > Scan for Hosts`
    - Once completed, add the target IP address (e.g., 192.168.152.129) to Target1 and add a default gateway IP (e.g., 192.168.152.2) to Target2
    - active dns_spoof `Plugins > Manage Plugins`
    - if successful user is sent to controlled page

- [bettercap](https://www.bettercap.org/)

## References
- https://github.com/mschwager/fierce
- https://github.com/TheRook/subbrute.git
- https://github.com/EdOverflow/can-i-take-over-xyz
- https://www.ettercap-project.org/
- https://www.bettercap.org/

