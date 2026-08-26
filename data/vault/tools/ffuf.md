---
title: ffuf
aliases: []
tags:
- tool/ffuf
- tool/curl
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: Attacking_Web_Applications_With_Ffuf_Module_Cheat_Sheet.pdf
related_tools:
- '[[ffuf]]'
- '[[curl]]'
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

# ffuf

## Description
Ffuf is a tool used for directory and file brute-forcing. It can be used to find hidden directories, files, and parameters in web applications.

## Usage
```bash
ffuf -h
```

```bash
ffuf -w wordlist.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ Directory
```

```bash
ffuf -w wordlist.txt:FUZZ -u http://SERVER_IP:PORT/indexFUZZ Extension
```

```bash
ffuf -w wordlist.txt:FUZZ -u http://SERVER_IP:PORT/blog/FUZZ.php Page
```

```bash
ffuf -w wordlist.txt:FUZZ -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v Recursive
```

```bash
ffuf -w wordlist.txt:FUZZ -u https://FUZZ.hackthebox.eu/ Sub-domain
```

```bash
ffuf -w wordlist.txt:FUZZ -u http://academy.htb:PORT/ -H 'Host: FUZZ.academy.htb' -fs xxx VHost
```

```bash
ffuf -w wordlist.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php?FUZZ=key -fs xxx Parameter
```

```bash
ffuf -w wordlist.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx Parameter - POST
```

```bash
ffuf -w ids.txt:FUZZ -u http://admin.academy.htb:PORT/admin/admin.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx Value Fuzzing
```

## Wordlists
```plaintext
/opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
```

```plaintext
/opt/useful/SecLists/Discovery/Web-Content/web-extensions.txt
```

```plaintext
/opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
```

```plaintext
/opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt
```

```bash
sudo sh -c 'echo "SERVER_IP academy.htb" >> /etc/hosts' Add DNS entry
```

```bash
for i in $(seq 1 1000); do echo $i >> ids.txt; done Create Sequence Wordlist
```

