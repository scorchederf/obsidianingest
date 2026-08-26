---
title: Aquatone
aliases: []
tags:
- tool/aquatone
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: aquatone.md
related_tools:
- '[[nmap]]'
- '[[masscan]]'
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

# Aquatone

## Description
Aquatone is a tool for visual inspection of websites across a large amount of hosts and is convenient for quickly gaining an overview of HTTP-based attack surface.

## Installation
- Original version is no longer in development, new fork done by shelld3v
- install via extraction
  - `cd opt; sudo wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip`
  - `sudo unzip aquatone_linux_amd64_1.7.0.zip`

## Usage
- Aquatone can make a report on hosts scanned with the [Nmap](https://nmap.org/) or [Masscan](https://github.com/robertdavidgraham/masscan) portscanner. Simply feed Aquatone the XML output and give it the `-nmap` flag to tell it to parse the input as Nmap/Masscan XML
  - `cat scan.xml | aquatone -nmap`
- execute using output from nmap
  - `cat web_discovery.xml | ./aquatone -nmap`

## References
- https://github.com/michenriksen/aquatone
- https://github.com/shelld3v/aquatone

