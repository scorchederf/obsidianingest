---
title: Footprinting
aliases: []
tags:
- study-notes
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 04-112-footprinting-03-domaininformation.pdf
related_tools:
- '[[ettercap]]'
- '[[burpsuite]]'
- '[[eyewitness]]'
- '[[feroxbuster]]'
- '[[ffuf]]'
related_techniques:
- '[[crawling]]'
- '[[dns-enumeration]]'
- '[[file-inclusion]]'
- '[[web-attacks]]'
related_tactics:
- '[[ta0003]]'
- '[[ta0005]]'
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

# Footprinting

## Introduction
This study note covers the techniques and tools used for footprinting, which is the process of gathering information about a target system or network. Footprinting is a crucial first step in many penetration testing engagements, as it helps to gather intelligence about the target's infrastructure, services, and potential vulnerabilities.

## Tools
Several tools are commonly used for footprinting, including:

- **Ettercap**: A network protocol analyzer and man-in-the-middle attack tool that can be used to intercept and manipulate network traffic.
- **Burpsuite**: A web application security testing tool that can be used to intercept and manipulate HTTP(S) traffic.
- **EyeWitness**: A tool that generates visual reports of web applications by taking screenshots and generating HTML files.
- **Feroxbuster**: A fast HTTP(S) scanner that can be used to discover hidden directories and files on a web server.
- **FFUF**: A fast fuzzer that can be used to discover hidden directories and files on a web server.

## Techniques
The following techniques are commonly used during the footprinting phase:

- **Crawling**: Using tools like Burpsuite and Feroxbuster to crawl the target's web application and discover hidden directories and files.
- **DNS Enumeration**: Using tools like DNSEnum to gather information about the target's domain and subdomains.
- **File Inclusion**: Using tools like Ettercap and Burpsuite to exploit file inclusion vulnerabilities in web applications.
- **Web Attacks**: Using tools like EyeWitness to generate visual reports of web applications and identify potential vulnerabilities.

## Example Commands
Here are some example commands that can be used during the footprinting phase:

- **Burpsuite**:
  ```bash
  burpsuite
  ```

- **Feroxbuster**:
  ```bash
  feroxbuster -u http://target.com -w wordlist.txt
  ```

- **FFUF**:
  ```bash
  ffuf -u http://target.com/FUZZ -w wordlist.txt
  ```

## References
- https://academy.hackthebox.com/module/112/section/1061

