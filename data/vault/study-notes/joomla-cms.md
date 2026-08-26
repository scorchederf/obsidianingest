---
title: Joomla CMS
aliases: []
tags:
- topic/joomla
- tool/curl
- tool/python
- tool/joomlascan
- tool/droopescan
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: joomla.md
related_tools:
- '[[curl]]'
- '[[python]]'
- '[[joomlascan]]'
- '[[droopescan]]'
related_techniques:
- '[[t1008]]'
- '[[t1110]]'
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

# Joomla CMS

## Description
Joomla is a free and open-source content management system (CMS) used to build and manage websites. It’s similar in purpose to WordPress or Drupal.

Joomla collects some anonymous usage statistics such as the breakdown of Joomla, PHP, and database versions and server operating systems in use on Joomla installations. This data can be queried via their public API.

## Enumeration
- Check the page source
  - `curl -s http://dev.inlanefreight.local/ | grep Joomla`
- Check `/robots.txt`
  - `curl -s http://dev.inlanefreight.local/robots.txt | grep Joomla`
- Look for `/readme.txt`
  - `curl -s http://dev.inlanefreight.local/README.txt | head -n 5`
- May be able to fingerprint the version from JavaScript files in the `media/system/js/` directory or by browsing to `administrator/manifests/files/joomla.xml`
  - `curl -s http://dev.inlanefreight.local/administrator/manifests/files/joomla.xml | xmllint --format -`
- Get approximate version via `/plugins/system/cache/cache.xml`
  - `curl -s http://dev.inlanefreight.local/plugins/system/cache/cache.xml`
- Use tools like [[droopescan]] and [[JoomlaScan]]

## Attack
- Brute force
  - [joomla-bruteforce](https://github.com/ajnik/joomla-bruteforce)
  - `curl https://raw.githubusercontent.com/ajnik/joomla-bruteforce/refs/heads/master/joomla-brute.py -o joomla-brute.py`
  - `chmod +x joomla-brute.py`
  - `sudo python3 joomla-brute.py -u http://app.inlanefreight.local -w /usr/share/wordlists/rockyou.txt -usr

## References
- https://www.joomla.org/
- https://developer.joomla.org/about/stats.html
- https://developer.joomla.org/about/stats/api.html
- https://github.com/ajnik/joomla-bruteforce
- https://github.com/dpgg101/CVE-2019-10945

