---
title: Hack The Box - Academy Module 103 Section 974
aliases: []
tags:
- topic/hack-the-box-academy
- topic/web-attacks
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 19-103-CrossSiteScripting-04-DomXSS.pdf
related_tools:
- '[[ffuf]]'
- '[[nmap-1787746090]]'
related_techniques:
- '[[T1210]]'
- '[[T1184]]'
related_tactics:
- '[[ta0003]]'
- '[[ta0005]]'
related_services:
- '[[http]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Hack The Box - Academy Module 103 Section 974

## Introduction
In this section, we will explore the techniques and tools used to enumerate and exploit web applications. The focus will be on using `ffuf` and `nmap` to identify and exploit web vulnerabilities.

## Using ffuf for Brute-forcing
To start, we will use `ffuf` to brute-force directories and files on the target web application. The command to use `ffuf` is as follows:

```bash
ffuf -u http://<target>/FUZZ -w /path/to/wordlist.txt -e .php,.html
```

This command will send requests to the target URL, replacing `FUZZ` with each word from the wordlist, and append the extensions specified in the wordlist.

## Using nmap for Service Enumeration
Next, we will use `nmap` to enumerate services running on the target. The command to use `nmap` is as follows:

```bash
nmap -sV -p 80 <target>
```

This command will perform a service version scan on port 80, which is commonly used for HTTP services.

## Identifying Vulnerabilities
After enumerating the services, we will look for potential vulnerabilities. Common techniques include checking for directory traversal, file inclusion, and other common web application vulnerabilities.

## Exploiting Vulnerabilities
Once vulnerabilities are identified, we can exploit them using various techniques. For example, if a directory traversal vulnerability is found, we can use the `ffuf` command to exploit it.

```bash
ffuf -u http://<target>/FUZZ/../../../../etc/passwd -w /path/to/wordlist.txt -e .php,.html
```

This command will attempt to access the `/etc/passwd` file by traversing directories.

## References
- https://academy.hackthebox.com/module/103/section/974

