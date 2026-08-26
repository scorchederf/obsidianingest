---
title: EyeWitness
aliases: []
tags:
- tool/eyewitness
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: eyewitness.md
related_tools:
- '[[eyewitness]]'
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

# EyeWitness

## Description
EyeWitness is a tool used to capture screenshots from a list of URLs. It also provides server header information and identifies default credentials if known. The tool is powered by Chromium for better reliability and easier installation.

## Installation
- Installation via `sudo`:
  - `sudo apt install eyewitness`
  - Navigate to the `Python/setup` directory and execute `setup.sh`

## Usage
- Options:
  - `eyewitness -h`
- Execute using output from `nmap`:
  - `eyewitness --web -x web_discovery.xml -d inlanefreight_eyewitness`

## References
- https://github.com/RedSiege/EyeWitness

