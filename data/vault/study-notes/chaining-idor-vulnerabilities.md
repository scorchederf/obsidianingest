---
title: Chaining IDOR Vulnerabilities
aliases: []
tags:
- study-notes
- techniques/t1003-003
- techniques/t1020
- techniques/t1132-001
- techniques/t1555-004
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 23-134-WebAttacks-11-ChainingIDORVulnerabilities.pdf
related_tools:
- '[[burpsuite]]'
- '[[ettercap]]'
- '[[eyewitness]]'
- '[[fierce]]'
- '[[ffuf]]'
- '[[fierce]]'
- '[[finalrecon]]'
- '[[get-240token]]'
related_techniques:
- '[[t1003-003]]'
- '[[t1020]]'
- '[[t1132-001]]'
- '[[t1555-004]]'
related_tactics:
- '[[ta0005]]'
related_services:
- '[[API]]'
related_os: []
related_notes: []
mitre_tactic: TA0005
mitre_technique: T1003.003, T1020, T1132.001, T1555.004
real_path: ''
port: ''
protocol: ''
os: ''
---

# Chaining IDOR Vulnerabilities

## Introduction to Web Attacks
This section covers the basics of web attacks, including HTTP Verb Tampering, Insecure Direct Object References (IDOR), and XML External Entity (XXE) Injection.

## Chaining IDOR Vulnerabilities
1. **IDOR Information Disclosure**: The initial vulnerability is an IDOR Information Disclosure, where the API endpoint returns the details of the requested user. This can be exploited to retrieve details of other users by changing the `uid` parameter in the GET request.

2. **Modifying Other Users' Details**: By intercepting the request when updating the profile, the role can be changed to `web_admin`, allowing the user to modify other users' details and create/delete users.

3. **Mass Assignment**: With the `web_admin` role, the user can perform mass assignments to change specific fields for all users, such as placing XSS payloads in their profiles or changing their email to a specified email.

## Example Exploitation
1. **Exploiting IDOR Information Disclosure**: Sending a GET request with a different `uid` to retrieve the details of another user.

2. **Exploiting IDOR Insecure Function Calls**: Changing the role to `web_admin` and using it to modify other users' details or create new users.

3. **Mass Assignment**: Writing a script to change all users' emails to a specified email.

## Questions
The section concludes with a question to change the admin's email to 'flag@idor.htb' and retrieve the flag on the 'edit profile' page.

## References
- https://academy.hackthebox.com/module/134/section/1200

