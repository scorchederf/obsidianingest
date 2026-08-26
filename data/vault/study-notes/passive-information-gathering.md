---
title: Passive Information Gathering
aliases: []
tags:
- topic/passive-information-gathering
- tool/theHarvester
- tool/recon-ng
- tool/google-hacking-database
- tool/netcraft
- tool/github
- tool/ssllabs
- tool/pastebin
- tool/haveibeenpwned
- tool/socialsearcher
- tool/twofi
- tool/linkedin2username
- tool/rockyou
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: notes.md
related_tools:
- '[[theharvester]]'
- '[[recon-ng]]'
- '[[google-hacking-database]]'
- '[[netcraft]]'
- '[[github]]'
- '[[ssllabs]]'
- '[[pastebin]]'
- '[[haveibeenpwned]]'
- '[[socialsearcher]]'
- '[[twofi]]'
- '[[linkedin2username]]'
- '[[rockyou]]'
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

# Passive Information Gathering

## Website Reconnaissance
- Website: https://www.megacorpone.com
  - `about.html` reveals emails and Twitter accounts
  - Emails: `initiallastname@megacorpone.com`
  - CEO: `joe@megacorpone.com` uses a different format
  - TheHarvester
  - Look for social media platforms
  - Recon-ng: `modules discovery/info_disclosure/interesting_files`
  - `robots.txt`

## Whois Lookup
- `whois megacorpone.com`
  - Registrant names and roles
  - Addresses
  - Name servers
  - `whois 149.56.244.87` if known
  - Reverse whois if IP addresses are known

## Google Hacking Database
- `site:megacorpone.com`
  - Index of / for open directories
  - `https://www.megacorpone.com/assets`
  - `https://www.megacorpone.com/old-site`
  - Other sites
  - `site:megacorpone.com filetype:txt`
  - `https://www.megacorpone.com/robots.txt`
  - `site:megacorpone.com ext:php`
  - Search for programming languages used on the server

## Netcraft
- [Site reports matching *.megacorpone.com](https://searchdns.netcraft.com/?host=*.megacorpone.com)
  - [Site report for http://www.megacorpone.com](https://sitereport.netcraft.com/?url=http://www.megacorpone.com)

## Recon-ng
- `modules recon/domains-hosts/google_site_web`
  - `modules recon/hosts-hosts/resolve`
  - `modules discovery/info_disclosure/interesting_files`

## Open Source Code
- [GitHub (manual)](https://github.com/megacorpone)
  - Search `filename:users`
  - `xampp.users` exists and contains creds
  - `trivera:$apr1$A0vSKwao$GV3sgGAj53j.c3GkS4oUC0`
  - [Gitleaks #todo](https://github.com/zricethezav/gitleaks)
  - [Gitrob #todo](https://github.com/zricethezav/gitleaks)
  - [Showdan #todo](https://www.shodan.io/)
  - [Security Headers](https://securityheaders.com/)
  - [SSL Server Test](https://www.ssllabs.com/ssltest/)
  - [Pastebin](https://pastebin.com/)
  - Exposed credentials, IP addresses, etc.

## User Information Gathering
- [TheHarvester](https://github.com/laramies/theHarvester)
  - `theHarvester -d www.megacorpone.com -b all > theHarvester.megacorpone`

## Password Dumps
- [RockYou](https://en.wikipedia.org/wiki/RockYou#Data_breach)
  - [HaveIBeenPwned](https://haveibeenpwned.com/PwnedWebsites)

## Social Media
- [SocialSearcher](https://www.social-searcher.com/)
  - Twitter: [Twofi1](https://digi.ninja/projects/twofi.php)
  - LinkedIn: [LinkedIn2Username](https://github.com/initstring/linkedin2username)
  - Stack Overflow

## OSINT Framework
- [OSINT Framework](https://osintframework.com/)

## Maltego
- [Maltego](https://www.maltego.com/)

## References
- https://www.megacorpone.com
- https://www.exploit-db.com/google-hacking-database
- https://github.com/lanmaster53/recon-ng
- https://github.com/zricethezav/gitleaks
- https://www.shodan.io/
- https://securityheaders.com/
- https://www.ssllabs.com/ssltest/
- https://pastebin.com/
- https://haveibeenpwned.com/PwnedWebsites
- https://www.social-searcher.com/
- https://digi.ninja/projects/twofi.php
- https://github.com/initstring/linkedin2username

