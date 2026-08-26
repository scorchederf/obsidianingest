---
title: Cross-Site Scripting (XSS)
aliases: []
tags:
- study-notes/cross-site-scripting-xss
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 19-103-CrossSiteScripting-09-XSSPrevention.pdf
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

# Cross-Site Scripting (XSS)

## Introduction
Cross-Site Scripting (XSS) is a type of security vulnerability typically found in web applications. XSS enables attackers to inject client-side scripts into web pages viewed by other users. A successful XSS attack can lead to a loss of privacy and data, and can even be used to take control of how users interact with the affected website.

## Types of XSS
XSS can be categorized into three types:

1. **Reflected XSS (Type 1)**: The payload is reflected in the URL or form and is executed when the user visits the page. This type is also known as Non-Persistent XSS.

2. **Stored XSS (Type 2)**: The payload is stored on the server and is executed whenever the user visits the page. This type is also known as Persistent XSS.

3. **DOM-based XSS (Type 3)**: The payload is executed by manipulating the Document Object Model (DOM) of the web page. This type does not involve server-side processing.

## Exploitation Techniques
To exploit XSS vulnerabilities, attackers can use various techniques such as:

- **Injection of Malicious Scripts**: Injecting scripts that perform actions like stealing cookies, redirecting users, or executing arbitrary code.

- **Clickjacking**: Using XSS to trick users into clicking on a hidden frame that performs an action on the parent page.

- **Session Hijacking**: Stealing session tokens or cookies to impersonate a user.

## Detection and Mitigation
To detect and mitigate XSS vulnerabilities, organizations can use the following methods:

- **Input Validation**: Validate and sanitize user inputs to prevent malicious scripts from being executed.

- **Output Encoding**: Encode output data to ensure that any special characters are properly escaped.

- **Content Security Policy (CSP)**: Implement CSP to restrict the sources of executable content, thereby preventing XSS attacks.

- **Use of Anti-XSS Libraries**: Utilize libraries and frameworks that provide built-in protection against XSS.

## References
- https://academy.hackthebox.com/module/103/section/1009

