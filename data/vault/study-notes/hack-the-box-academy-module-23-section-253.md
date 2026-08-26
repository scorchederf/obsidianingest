---
title: Hack The Box - Academy Module 23 Section 253
aliases: []
tags:
- topic/hack-the-box-academy
- tool/enum4linux-ng
- tool/enum4linux
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 20-23-FileInclusion-05-PHPWrappers.pdf
related_tools:
- '[[enum4linux-ng]]'
- '[[enum4linux]]'
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

# Hack The Box - Academy Module 23 Section 253

## Description
This module covers the use of `enum4linux-ng` and `enum4linux` tools for enumerating information from a Windows domain. The goal is to gather information about the domain, such as users, groups, and shares.

## Tools Used
- `enum4linux-ng`
- `enum4linux`

## Usage
The tools are used to gather information about the domain by running commands against the target machine. For example, the following command can be used to gather information about the domain:

```bash
enum4linux-ng <target>
```

This will provide information about the domain, including users, groups, and shares.

## Output
The output from `enum4linux-ng` and `enum4linux` will include information such as:
- Domain name
- Users
- Groups
- Shares
- NetBIOS name
- Workgroup
- Domain controller
- Domain controllers
- DNS servers

## References
- https://academy.hackthebox.com/module/23/section/253

