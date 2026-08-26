---
title: Hack-the-Box Academy Module 103 - Section 1008
aliases: []
tags:
- topic/hack-the-box-academy
- topic/module-103
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: passwords.txt
related_tools:
- '[[dirbuster]]'
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

# Hack-the-Box Academy Module 103 - Section 1008

## Overview
This section covers the use of the `dirbuster` tool to enumerate directories on a target system. The goal is to identify hidden directories and files that may contain sensitive information.

## Tool Usage
The `dirbuster` tool is used to perform directory brute-forcing. The following command is used to run the tool against a target URL:

```
python3 dirbuster.py -u http://target.com -w /path/to/directory/list.txt
```

Where `http://target.com` is the target URL and `/path/to/directory/list.txt` is a file containing a list of directories to test.

## Example
Here is an example of a command used to enumerate directories on a target system:

```
python3 dirbuster.py -u http://192.168.1.100 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
```

This command will test the directories listed in `directory-list-2.3-medium.txt` against the target system at `http://192.168.1.100`.

