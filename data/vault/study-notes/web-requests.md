---
title: Web Requests
aliases: []
tags:
- study-notes
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 31-26-WebRequests-02-HyperTextTransferProtocolSecure.pdf
related_tools:
- '[[curl]]'
- '[[ffuf]]'
- '[[fierce]]'
- '[[dirb]]'
related_techniques:
- '[[web-attacks]]'
related_tactics:
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

# Web Requests

## Introduction
This study note covers the use of various tools for web requests and enumeration. The focus is on using `curl`, `ffuf`, `fierce`, and `dirb` to perform web requests and gather information.

## curl
The `curl` tool is used to transfer data from or to a server. It is a command-line tool that supports various protocols, including HTTP, HTTPS, FTP, and more. It can be used to send HTTP requests and retrieve data from web servers.

**Example Usage:***
```
curl -X GET http://example.com
```

**Example Command:***
```
curl -X POST -d 'username=admin&password=admin' http://example.com/login
```

**Example Command with Headers:***
```
curl -H 'Content-Type: application/json' -d '{

## References
- https://academy.hackthebox.com/module/35/section/228

