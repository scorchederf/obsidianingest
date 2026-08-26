---
title: DNS Subdomain Takeover
aliases: []
tags:
- technique/t1003
- technique/t1132
- attack/lateral-movement
category: techniques
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: 11-115-AttackingCommonServices-14-LatestDNSVulnerabilities.pdf
related_tools:
- '[[aquatone]]'
- '[[droopescan]]'
- '[[fierce]]'
- '[[finalrecon]]'
- '[[gobuster]]'
- '[[ffuf]]'
- '[[lazagne]]'
related_techniques:
- '[[t1003-003]]'
- '[[t1132-001]]'
related_tactics:
- '[[ta0005]]'
related_services:
- '[[dns]]'
related_os: []
related_notes: []
mitre_tactic: TA0005
mitre_technique: T1003.003
real_path: ''
port: ''
protocol: ''
os: ''
---

# DNS Subdomain Takeover

## Introduction
Latest DNS Vulnerabilities
We can find thousands of subdomains and domains on the web. Often they point to no longer active third-party service providers such as AWS, GitHub, and others. At best, they display an error message as confirmation of a deactivated third-party service. Large corporations are also affected time and again. Companies often cancel services from third-party providers but forget to delete the associated DNS records. This is because no additional costs are incurred for a DNS entry. Many well-known bug bounty platforms, such as HackerOne, already explicitly list Subdomain Takeover as a bounty category. With a simple search, we can find several tools, for example, that automate the discovery of vulnerable subdomains or help create Proof of Concepts (PoC) that can then be submitted to the bug bounty program of our choice or the affected company. RedHuntLabs did a study on this in 2020, and they found that over 400,000 subdomains out of 220 million were vulnerable to subdomain takeover. 62% of them belonged to the e-commerce sector.

## The Concept of Attacks
The concept of subdomain takeover involves making a DNS change to a subdomain that is no longer used by the company. By doing so, we can become the owner of that particular subdomain and manage it as we choose. The existing subdomain no longer points to a third-party provider and is therefore no longer occupied. Pretty much anyone can register this subdomain as their own. Visiting this subdomain and the presence of the CNAME record in the company's DNS leads, in most cases, to things working as expected. However, the design and function of this subdomain are now in the hands of the attacker. Subdomain takeover can be used not only for phishing but also for many other attacks. These include, for example, stealing cookies, cross-site request forgery (CSRF), abusing CORS, and defeating content security policy (CSP). We can see some examples of subdomain takeovers on the HackerOne website, which have earned the bug bounty hunters considerable payouts.

## Initiation of Subdomain Takeover
Step 1: The source, in this case, is the subdomain name that is no longer used by the company that we discovered.
Step 2: The source and its DNS servers. Since this subdomain is in the list, the DNS server considers the subdomain as trustworthy and forwards the visitor.
Step 3: The destination here is the person who requests the IP address of the subdomain where they want to be forwarded via the network.

## References
- https://academy.hackthebox.com/

