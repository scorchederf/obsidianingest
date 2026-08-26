---
title: Using Web Proxies
aliases: []
tags:
- topic/web-proxies
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 14-110-UsingWebProxies-12-BurpScanner.pdf
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

# Using Web Proxies

## Introduction
Web proxies can be used to route HTTP requests through a third-party server, providing anonymity and bypassing certain network restrictions. This technique is useful for ethical hackers and penetration testers to access restricted resources or test web applications from a different geographical location.

## Types of Web Proxies
Web proxies can be categorized into several types, including:
- **Forward Proxies**: Used to route requests from a client to a server, often used for caching and filtering.
- **Reverse Proxies**: Used to route requests from a server to a client, often used for load balancing and security.
- **Anonymous Proxies**: Used to hide the client's IP address from the server.
- **Transparent Proxies**: Used to intercept and modify traffic without the client's knowledge.

## Using Web Proxies
To use web proxies, you can configure your browser or use specific tools. Here are some common methods:
- **Browser Configuration**: Most modern browsers allow you to set a proxy server in the settings.
- **Command Line Tools**: Tools like `curl` and `wget` can be configured to use a proxy server.
- **Proxy Chains**: A tool that allows you to chain multiple proxies to increase anonymity.
- **Proxy Services**: Online services that provide proxy servers for a fee or free of charge.

## Example
Here is an example of using the `curl` command with a proxy server:
```
$ curl -x http://proxy.example.com:8080 http://example.com
```
This command routes the request to `example.com` through the proxy server `http://proxy.example.com:8080`.

## References
- https://academy.hackthebox.com/module/110/section/1084

