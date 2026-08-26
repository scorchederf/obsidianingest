---
title: http api
aliases: []
tags:
- study-notes/api
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: httpapi.md
related_tools:
- '[[curl]]'
- '[[jq]]'
- '[[ffuf]]'
related_techniques:
- '[[t1008]]'
- '[[t1110]]'
- '[[t1190]]'
related_tactics:
- '[[ta0003]]'
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

# http api

## API Types
- Representational State Transfer (REST) is the most popular API style. It uses a client-server model where clients make requests to resources on a server using standard HTTP methods (GET, POST, PUT, DELETE). RESTful APIs are stateless, meaning each request contains all necessary information for the server to process it, and responses are typically serialized as JSON or XML.
- Simple Object Access Protocol (SOAP) uses XML for message exchange between systems. SOAP APIs are highly standardized and offer comprehensive features for security, transactions, and error handling, but they are generally more complex to implement and use than RESTful APIs.
- GraphQL is an alternative style that provides a more flexible and efficient way to fetch and update data. Instead of returning a fixed set of fields for each resource, GraphQL allows clients to specify exactly what data they need, reducing over-fetching and under-fetching of data. GraphQL APIs use a single endpoint and a strongly-typed query language to retrieve data.
- gRPC is a newer style that uses Protocol Buffers for message serialization, providing a high-performance, efficient way to communicate between systems. gRPC APIs can be developed in a variety of programming languages and are particularly useful for microservices and distributed systems.

## Broken Object Level Authorization
- Its authorization checks (implemented at the source-code level) fail to correctly ensure that an authenticated user has sufficient permissions or privileges to request and view specific data or perform certain operations.

## Broken Object Property Level Authorization
- This category of vulnerabilities encompasses two subclasses:
  - Excessive Data Exposure: Reveals sensitive data to authorized users that they are not supposed to access.
  - Mass Assignment: Permits authorized users to manipulate sensitive object properties beyond their authorized scope, including modifying, adding, or deleting values.

## Unrestricted Resource Consumption
- Resources such as network bandwidth, CPU, memory, and storage can be consumed without proper authorization.
  - Example: `curl -O http://94.237.51.179:51135/SupplierCompaniesCertificatesOfIncorporations/reverse-shell.exe`

## Attack Vectors
- Authenticating with JWT and Swagger
  - `curl -X 'POST' 'http://'$rhost'/api/v1/authentication/suppliers/sign-in' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{

