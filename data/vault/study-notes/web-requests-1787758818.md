---
title: Web Requests
aliases: []
tags:
- study-notes
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 31-26-WebRequests-05-HttpMethodsAndCodes.pdf
related_tools:
- '[[burpsuite]]'
related_techniques:
- '[[web-attacks]]'
related_tactics:
- '[[ta0005]]'
related_services:
- '[[http]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Web Requests

## Introduction
Web requests are a fundamental part of web application security testing. They are used to interact with web applications and can be used to identify vulnerabilities, test authentication mechanisms, and more. This study note covers the basics of making web requests using Burp Suite, a popular tool in the cybersecurity field.

## Using Burp Suite for Web Requests
Burp Suite is a powerful tool for web application security testing. It provides a range of features for intercepting, modifying, and analyzing HTTP(S) traffic. Here are some key steps to make web requests using Burp Suite:

1. **Intercept Requests**
   - Open Burp Suite and navigate to the `Proxy` tab.
   - Configure the proxy settings to route traffic through Burp Suite.
   - Make a web request to the target application.
   - Burp Suite will intercept the request and display it in the `Intercept` tab.

2. **Analyze Requests**
   - In the `Intercept` tab, you can view the request details, including headers, payloads, and more.
   - Use the `Intruder` module to test different payloads and identify potential vulnerabilities.
   - Use the `Repeater` module to manually test specific requests.

3. **Modify Requests**
   - In the `Intercept` tab, you can modify the request headers, payloads, and other parameters.
   - Use the `Proxy` tab to send the modified request to the target application.

4. **Save Requests**
   - Use the `History` tab to save and manage intercepted requests for future analysis.

## References
- https://academy.hackthebox.com/module/35/section/221

