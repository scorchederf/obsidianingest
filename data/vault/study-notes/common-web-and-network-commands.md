---
title: Common Web and Network Commands
aliases: []
tags:
- study-notes
- tools
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: cheatsheet-17.md
related_tools:
- '[[curl]]'
- '[[tree]]'
- '[[wp_scan]]'
- '[[msfconsole]]'
- '[[html2text]]'
- '[[grep]]'
- '[[jq]]'
- '[[man]]'
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

# Common Web and Network Commands

## Commands
```
- `tree -L 1`
  Lists contents of current directory

- `curl -s -X GET <url>`
  Makes a GET request to a webserver and receives HTML source code of requested web page

- `curl -I -X GET <url>`
  Prints the response header of the GET request from the requested web page

- `curl -X POST -d <data> <url>`
  Sends a POST request with data to specific webserver

- `wp_scan -u <url> -e a`
  Scans specific WordPress application to enumerate plugins

- `wp_scan -u <url> -e u`
  Scans specific WordPress application to enumerate users

- `msfconsole`
  Starts Metasploit Framework

- `html2text`
  Converts redirected HTML output or files to easily readable output

- `grep <pattern>`
  Filters specific pattern in files or redirected output

- `jq`
  Transforms JSON input and streams of JSON entities

- `man <tool>`
  Man provides you with the manpage of the specific tool
```

