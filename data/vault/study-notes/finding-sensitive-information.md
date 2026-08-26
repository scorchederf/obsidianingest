---
title: Finding Sensitive Information
aliases: []
tags:
- topic/finding-sensitive-information
- topic/service-attacks
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 11-115-AttackingCommonServices-04-FindingSensitiveInformation.pdf
related_tools: []
related_techniques: []
related_tactics: []
related_services:
- '[[ftp]]'
- '[[email]]'
- '[[mssql]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Finding Sensitive Information

## Introduction
When attacking a service, we usually play a detective role, and we need to collect as much information as possible and carefully the details. Therefore, every single piece of information is essential.

## Finding Sensitive Information
Let us imagine we are in an engagement with a client, we are targeting email, FTP, databases, and storage, and our goal is to obtain Remote Code Execution (RCE) on any of these services. We started the enumeration and tried anonymous access to all services. FTP has anonymous access. We found an empty file within the FTP service, but with the name johnsmith. We tried the same against the email service, and we successfully logged in. With email access, searching emails containing the word password, we found many, but one of them contains John's credentials for the MSSQL database. We accessed the database and used the built-in functionality to execute commands and successfully got RCE on the database server. A misconfigured service let us access a piece of information that initially may look insignificant, but it opened the doors for us to discover more information and finally get remote code execution on the database server. This is the importance of paying attention to every piece of information, every detail, as we enumerate and attack common services.

## Sensitive Information
Sensitive information may include, but is not limited to: • Usernames. • Email Addresses. • Passwords. • DNS records. • IP Addresses. • Source code. • Configuration files. • PII.

## Common Services
This module will cover some common services where we can find interesting information and discover different methods and tools to use to automate our discovery process. These services include: • File Shares.

## References
- https://academy.hackthebox.com/

