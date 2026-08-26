---
title: Passive and Active Enumeration Techniques
aliases: []
tags:
- study-notes/dns-enumeration-and-spoofing
- study-notes/http-s
- study-notes/http-api
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: cheatsheet-144-metasploit.md
related_tools:
- '[[curl]]'
- '[[dig]]'
- '[[nslookup]]'
- '[[theharvester]]'
- '[[waybackurls]]'
- '[[aquatone]]'
- '[[gobuster]]'
- '[[ffuf]]'
- '[[ZAP]]'
related_techniques:
- '[[DNS Enumeration]]'
- '[[Passive Subdomain Enumeration]]'
- '[[Passive Infrastructure Identification]]'
- '[[Active Infrastructure Identification]]'
- '[[Active Subdomain Enumeration]]'
- '[[Virtual Hosts]]'
- '[[Crawling]]'
related_tactics:
- '[[reconnaissance]]'
related_services:
- '[[http]]'
- '[[https]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Passive and Active Enumeration Techniques

## WHOIS Lookup
```bash
export TARGET="domain.tld"
whois $TARGET
```

This command performs a WHOIS lookup for the target domain.

## DNS Enumeration
```bash
nslookup $TARGET
nslookup -query=A $TARGET
dig $TARGET @<nameserver/IP>
dig a $TARGET @<nameserver/IP>
nslookup -query=PTR <IP>
dig -x <IP> @<nameserver/IP>
nslookup -query=ANY $TARGET
dig any $TARGET @<nameserver/IP>
nslookup -query=TXT $TARGET
dig txt $TARGET @<nameserver/IP>
nslookup -query=MX $TARGET
dig mx $TARGET @<nameserver/IP>
```

These commands are used to gather DNS records for the target domain.

## Passive Subdomain Enumeration
```bash
curl -s https://sonar.omnisint.io/subdomains/{domain} | jq -r '.[]' | sort -u
curl -s https://sonar.omnisint.io/tlds/{domain} | jq -r '.[]' | sort -u
curl -s https://sonar.omnisint.io/all/{domain} | jq -r '.[]' | sort -u
curl -s https://sonar.omnisint.io/reverse/{ip} | jq -r '.[]' | sort -u
curl -s https://sonar.omnisint.io/reverse/{ip}/{mask} | jq -r '.[]' | sort -u
curl -s "https://crt.sh/?q=${TARGET}&output=json" | jq -r '.[] | ".name_value\n\.common_name"' | sort -u
cat sources.txt | while read source; do theHarvester -d "${TARGET}" -b $source -f "${source}-${TARGET}";done
```

These commands and tools are used to enumerate subdomains and other information.

## Passive Infrastructure Identification
```bash
Netcraft: https://www.netcraft.com/
WayBackMachine: http://web.archive.org/
WayBackURLs: https://github.com/tomnomnom/waybackurls
waybackurls -dates https://$TARGET > waybackurls.txt
```

These resources and commands are used to identify historical infrastructure.

## Active Infrastructure Identification
```bash
curl -I "http://${TARGET}"
whatweb -a https://www.facebook.com -v
Wappalyzer: https://www.wappalyzer.com/
wafw00f -v https://$TARGET
Aquatone: https://github.com/michenriksen/aquatone
cat subdomain.list | aquatone -out ./aquatone -screenshot-timeout 1000
```

These commands and tools are used to identify active infrastructure.

## Active Subdomain Enumeration
```bash
HackerTarget: https://hackertarget.com/zone-transfer/
SecLists: https://github.com/danielmiessler/SecLists
nslookup -type=any -query=AXFR $TARGET nameserver.target.domain
gobuster dns -q -r "${NS}" -d "${TARGET}" -w "${WORDLIST}" -p ./patterns.txt -o "gobuster_${TARGET}.txt"
```

These commands and tools are used to enumerate subdomains.

## Virtual Hosts
```bash
curl -s http://192.168.10.10 -H "Host: randomtarget.com"
cat ./vhosts.list | while read vhost;do echo "\n********\nFUZZING: ${vhost}\n********";curl -s -I http://<IP address> -H "HOST: ${vhost}.target.domain" | grep "Content-Length: " ;done
ffuf -w ./vhosts -u http://<IP address> -H "HOST: FUZZ.target.domain" -fs 612
```

These commands are used to fuzz for possible virtual hosts.

## Crawling
```bash
ZAP: https://www.zaproxy.org/
ffuf -recursion -recursion-depth 1 -u http://192.168.10.10/FUZZ -w /opt/useful/SecLists/Discovery/Web-Content/raft-small-directories-lowercase.txt
ffuf -w ./folders.txt:FOLDERS,./wordlist.txt:WORDLIST,./extensions.txt:EXTENSIONS -u http://www.target.domain/FOLDERS/WORDLISTEXTENSIONS
```

These tools and commands are used to crawl the target web server.

## References
- https://www.virustotal.com/gui/home/url
- https://censys.io/
- https://crt.sh/
- https://www.netcraft.com/
- http://web.archive.org/
- https://github.com/tomnomnom/waybackurls
- https://github.com/michenriksen/aquatone
- https://hackertarget.com/zone-transfer/
- https://github.com/danielmiessler/SecLists
- https://www.zaproxy.org/

