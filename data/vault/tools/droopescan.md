---
title: Droopescan
aliases: []
tags:
- tool/droopescan
- tool/python
- tool/plugin-based
- tool/cms-scanner
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: droopescan.md
related_tools:
- '[[droopescan]]'
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

# Droopescan

## Description
A plugin-based scanner that aids security researchers in identifying issues with several CMSs, mainly Drupal & Silverstripe.

## Installation
- `sudo pip3 install droopescan`

## Usage
- `droopescan -h`

- Joomla scan
  - `droopescan scan joomla --url http://dev.inlanefreight.local/`

- Drupal scan
  - `droopescan scan drupal -u http://drupal.inlanefreight.local`

## Output
```sh
[+] Possible version(s): 
    3.8.10
    3.8.11
    3.8.11-rc
    3.8.12
    3.8.12-rc
    3.8.13
    3.8.7
    3.8.7-rc
    3.8.8
    3.8.8-rc
    3.8.9
    3.8.9-rc

[+] Possible interesting urls found:
    Detailed version information. - http://dev.inlanefreight.local/administrator/manifests/files/joomla.xml
    Login page. - http://dev.inlanefreight.local/administrator/
    License file. - http://dev.inlanefreight.local/LICENSE.txt
    Version attribute contains approx version - http://dev.inlanefreight.local/plugins/system/cache/cache.xml

[+] Scan finished (0:00:01.523369 elapsed)
```

## References
- https://github.com/SamJoan/droopescan

