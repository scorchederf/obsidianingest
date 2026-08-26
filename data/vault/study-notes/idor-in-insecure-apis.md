---
title: IDOR in Insecure APIs
aliases: []
tags:
- study-notes/idor
- technique/t1190
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 23-134-WebAttacks-10-IDORinInsecureAPIs.pdf
related_tools:
- '[[burpsuite]]'
related_techniques:
- '[[t1190]]'
related_tactics:
- '[[ta0005]]'
related_services: []
related_os: []
related_notes: []
mitre_tactic: TA0005
mitre_technique: T1190
real_path: ''
port: ''
protocol: ''
os: ''
---

# IDOR in Insecure APIs

## Introduction to IDOR in Insecure APIs
IDOR (Insecure Direct Object References) vulnerabilities can be exploited to access resources or functions that are out of the user's intended access. Unlike traditional IDOR vulnerabilities that involve accessing files or resources, this scenario focuses on exploiting IDOR vulnerabilities in function calls and APIs. Exploiting such vulnerabilities can allow attackers to perform actions on behalf of other users, such as changing their profiles, resetting passwords, or even buying items using their payment information.

## Identifying Insecure APIs
The Employee Manager web application was used as an example to demonstrate the identification of IDOR vulnerabilities in APIs. The Edit Profile page was tested for IDOR vulnerabilities. The PUT request to the /profile/api.php/profile/1 API endpoint was intercepted using Burp, revealing the JSON parameters sent with the request. The parameters included 'uid', 'uuid', and 'role', with the 'role' parameter set to 'employee'. This suggests that the application sets user access privileges on the client-side, which could be manipulated to gain more privileges.

## Exploiting Insecure APIs
Several attempts were made to exploit the identified IDOR vulnerabilities in the APIs. These attempts included changing the 'uid' to another user's 'uid', changing another user's details, creating new users, and changing the 'role' to a more privileged role (e.g., admin). However, the application appeared to have some form of access control in place, preventing these actions. The 'role' parameter was checked against the 'role' cookie, and the application returned errors for unauthorized actions.

## Testing for IDOR Information Disclosure
The next step was to test the API for IDOR Information Disclosure vulnerabilities. The goal was to read other users' details using GET requests. If the API was vulnerable, it could potentially leak other users' details, which could be used to complete IDOR attacks on function calls.

## References
- https://academy.hackthebox.com/module/134/section/1201

