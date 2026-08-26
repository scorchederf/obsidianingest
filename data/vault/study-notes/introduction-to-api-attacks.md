---
title: Introduction to API Attacks
aliases: []
tags:
- study-notes
- api-attacks
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 00-268-APIAttacks-01-IntroductionToAPIAttacks.pdf
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

# Introduction to API Attacks

## Introduction to API Attacks
Application Programming Interfaces (APIs) are foundational to modern software development, with web APIs being the most prevalent. They enable seamless communication and data exchange across diverse systems over the internet, serving as crucial bridges to facilitate integration and collaboration among different software applications.

At their essence, APIs consist of defined rules and protocols that dictate how disparate systems interact. They specify data formats, requirements, delineate access methods for resources, and define expected response structures. APIs are broadly categorized as public, accessible to external parties, or private, restricted to specific organizations or groups of systems.

API Building Styles

Web APIs can be built using various architectural styles, including REST, SOAP, GraphQL, and gRPC, each with its own strengths and use cases:

- **Representational State Transfer (REST)** is the most popular API style. It uses a stateless approach where clients make requests to resources on a server using standard HTTP methods (GET, POST, PUT, DELETE). RESTful APIs are stateless, meaning each request contains all necessary information for the server to process it, and responses are typically serialized as JSON or XML.

- **Simple Object Access Protocol (SOAP)** uses XML for message exchange between systems. SOAP APIs are standardized and offer comprehensive features for security, transactions, and error handling, but are generally more complex to implement and use than RESTful APIs.

- **GraphQL** is an alternative style that provides a more flexible and efficient way to fetch and update data. Instead of returning a fixed set of fields for each resource, GraphQL allows clients to specify exactly what data they need, reducing over-fetching and under-fetching of data. It uses a single endpoint and a strongly-typed query language to retrieve data.

- **gRPC** is a newer style that uses Protocol Buffers for message serialization, providing a high-performance, efficient way to communicate between systems. gRPC APIs can be developed in a variety of programming languages and are particularly useful for microservices and distributed systems.

In this module, our focus will be on attacks against a RESTful web API. However, the vulnerabilities demonstrated may also exist in other API styles.

## OWASP API Security Top 10
The OWASP API Security Top 10 is a list of the most critical security risks that can affect APIs. The following are the top 10 security risks identified by OWASP:

1. **Broken Object Level Authorization** - The API allows authenticated users to access data they are not authorized to view.

2. **Broken Authentication** - The authentication mechanisms of the API can be bypassed or circumvented, allowing unauthorized users to access the API.

3. **Broken Object Property Level Authorization** - The API reveals sensitive data to authorized users that they should not access or permits them to modify sensitive properties.

4. **Unrestricted Resource Consumption** - The API does not limit the amount of resources users can consume, potentially leading to denial of service.

5. **Broken Function Level Authorization** - The API allows unauthorized users to perform authorized operations.

6. **Unrestricted Access to Sensitive Business Flows** - The API exposes sensitive business flows, leading to potential financial losses and other damages.

7. **Server Side Request Forgery (SSRF)** - The API does not validate requests adequately, allowing attackers to send malicious requests to internal resources.

8. **Security Misconfiguration** - The API suffers from security misconfigurations, including vulnerabilities that lead to injection attacks.

9. **Improper Inventory Management** - The API does not properly and securely manage version inventory.

10. **Unsafe Consumption of APIs** - The API consumes another API unsafely, leading to potential security risks.

## References
- https://academy.hackthebox.com/

