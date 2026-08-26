---
title: Password Attacks
aliases: []
tags:
- topic/password-attacks
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 10-147-passwordattacks-02-credentialstorage.pdf
related_tools: []
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

# Password Attacks

## Introduction
Password attacks are a common method used by attackers to gain unauthorized access to systems, networks, and applications. This study note covers various techniques and methods used in password attacks, including brute-forcing, dictionary attacks, and credential stuffing.

## Brute-Forcing
Brute-forcing involves trying every possible combination of characters to guess a password. This can be done using tools like Hydra or Medusa. The process can be time-consuming and resource-intensive, but it can be effective against weak or default passwords.

## Dictionary Attacks
Dictionary attacks use a list of common or frequently used passwords to try and gain access. These attacks are faster than brute-forcing and can be automated using tools like Hashcat or John the Ripper. They are effective against weak passwords that are not complex.

## Credential Stuffing
Credential stuffing involves using stolen credentials from one source (e.g., a data breach) to try and gain access to another system. This attack is often automated and can be successful if the same or similar credentials are used across multiple systems. Tools like Burp Suite can be used to automate this process.

## Mitigation Strategies
To mitigate password attacks, organizations should implement strong password policies, use multi-factor authentication (MFA), and regularly update and patch systems. Additionally, using password managers can help users create and manage strong, unique passwords.

## References
- https://academy.hackthebox.com/module/147/section/1313

