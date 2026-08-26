---
title: Service Misconfigurations
aliases: []
tags:
- topic/service-misconfigurations
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 11-115-AttackingCommonServices-03-ServiceMisconfigurations.pdf
related_tools: []
related_techniques: []
related_tactics: []
related_services:
- '[[ftp]]'
- '[[smb-1787747781]]'
- '[[SQL Databases]]'
- '[[rdp]]'
- '[[dns]]'
- '[[smtp]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Service Misconfigurations

## Introduction
Misconfigurations usually happen when a system administrator, technical support, or developer does not correctly configure the framework of an application, website, desktop, or server leading to dangerous open pathways for unauthorized users. Let's explore the most typical misconfigurations of common services.

## Authentication
In previous years (though we still see this sometimes during assessments), it was widespread for services to include default credentials (username and password). This presents a security issue because many administrators leave the default credentials unchanged. Nowadays, most software asks users to set up credentials upon installation, which is better than default credentials. However, it is important to note that we will still find vendors using default credentials, especially on older applications. Even when the service does not have a set of default credentials, an administrator may use weak passwords or no passwords when setting up services with the idea that they will change the password once the service is set up and running. As administrators, we need to define password policies that apply to software tested or installed in our environment. Administrators should be required to comply with a minimum password complexity to avoid user and password combinations such as: admin:admin, admin:password, admin:<blank>, root:12345678, administrator:Password. Once we grab the service banner, the next step should be to identify possible default credentials. If there are no default credentials, we can try the weak username and password combinations listed above.

## Anonymous Authentication
Another misconfiguration that can exist in common services is anonymous authentication. The service can be configured to allow anonymous access, which can pose a security risk. This means that anyone can access the service without proper authentication.

## Preventing Misconfigurations
Once we have figured out our environment, the most straightforward strategy to control risk is to lock down the most critical infrastructure and only allow desired behavior. Any communication that is not required by the program should be disabled. This may include the following: Admin interfaces should be disabled, debugging is turned off, disable the use of default usernames and passwords, set up the server to prevent unauthorized access, directory listing, and other issues. Run scans and audits regularly to help discover future misconfigurations or missing fixes. The OWASP Top 10 provides a section on how to secure the installation processes: A repeatable hardening process makes it fast and easy to deploy another environment that is appropriately locked down. Development, QA, and production environments should all be configured identically, with different credentials used in each environment. In addition, this process should be automated to minimize the effort required to set up a new secure environment. A minimal platform without unnecessary features, components, documentation, and samples. Remove or do not install unnecessary features and frameworks.

## Protocol Specific Attacks
The following sections provide an overview of attacks on common services: FTP, SMB, SQL Databases, RDP, DNS, and SMTP.

## References
- https://academy.hackthebox.com/

