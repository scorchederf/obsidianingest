---
title: Offsec Labs - Whois and Google Hacking Exercises
aliases: []
tags:
- study-notes/pen-testing
- pen-testing
- whois
- google-hacking
- netcraft
- social-media
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: lab.md
related_tools:
- '[[whois]]'
- '[[google]]'
- '[[netcraft]]'
- '[[social-searcher]]'
related_techniques:
- '[[t1039]]'
- '[[t1588]]'
related_tactics:
- '[[ta0003]]'
- '[[ta0005]]'
related_services:
- '[[apache]]'
- '[[Font Awesome Web Fonts]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Offsec Labs - Whois and Google Hacking Exercises

## Whois Enumeration
What is the first nameserver for offensive-security.com (the one with the lowest number and ends in -A)?

```shell
┌──(kali㉿kali)-[~]
└─$ whois offensive-security.com
...
Tech Email: 1224861dbf76da04cb0faff2ddb47834-14869841@contact.gandi.net
Name Server: NS-34-A.GANDI.NET      #answer
Name Server: NS-182-B.GANDI.NET
Name Server: NS-185-C.GANDI.NET
```

## Google Hacking
1. Who is the VP of Legal for MegaCorp One and what is their email address?

site:megacorpone.com legal
https://www.megacorpone.com/contact.html
mcarlow@megacorpone.com

2. Use Google dorks (either your own or any from the GHDB) to search www.megacorpone.com for interesting documents.

3. What is the email address of VP of Legal for Megacorpone.com?

site:megacorpone.com legal
https://www.megacorpone.com/contact.html
mcarlow@megacorpone.com

4. What other MegaCorp One employees can you identify that are not listed on www.megacorpone.com?

from:megacorpone.com
    https://twitter.com/realwilladler - William Adler 
    - trying wadler@megacorpone.com
    - William Adler - correct

## Netcraft
Exercises

1. Use Netcraft to determine what application server is running on www.megacorpone.com.
https://sitereport.netcraft.com/?url=http://www.megacorpone.com
Apache

2. What is the name of the Client-Side Scripting Framework that handles fonts?
https://sitereport.netcraft.com/?url=http://www.megacorpone.com
Font Awesome Web Fonts

## Social Media
Use any of the social media tools previously discussed to identify additional MegaCorp One employees. What is the full name of MegaCorp One's IT and Security Director?

https://www.social-searcher.com/search-users/?ntw=&q6=megacorpone
Alan Grofield IT and Security DirectorMegaCorpOne Henderson, Nevada, United States · IT and Security Director ·

## References
- https://www.megacorpone.com/contact.html
- https://sitereport.netcraft.com/?url=http://www.megacorpone.com
- https://www.social-searcher.com/search-users/?ntw=&q6=megacorpone

