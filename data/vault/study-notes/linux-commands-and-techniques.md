---
title: Linux Commands and Techniques
aliases: []
tags:
- topic/linux-commands
- topic/techniques
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: linux-commands.md
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
os: linux
---

# Linux Commands and Techniques

## Overview
This note covers various Linux commands and techniques that can be used for reconnaissance, privilege escalation, and other security testing activities.

## Common Commands
- `sudo killall openvpn` - Kill all openvpn connections.
- `mkdir -p storage/local/something/something` - Create parent paths.
- `ls -lat /var/backups` - List files by date.
- `ls -li /var/backups` - Get inode number (unique identifier).
- `unzip filename.zip` - Unzip file.
- `gzip filename.gz` - Compress file.
- `find / -name "rockyou-30000.rule" 2>/dev/null` - Find specific file.
- `find /mnt/Finance/ -name *cred*` - Search for files containing 'cred'.
- `grep -rn /mnt/Finance/ -ie cred` - Search recursively for 'cred'.
- `netstat -tulp` - List listening ports.
- `cat * | grep -i passw*` - Look for passwords.
- `sudo -l` - Check if Sudo is available.
- `id` - Check user groups.
- `find / -group $groupname 2>/dev/null` - Find binaries within a group.
- `ls -la /usr/bin/bugtracker && file /usr/bin/bugtracker` - Check permissions and type of binary.
- `echo "/bin/sh" >> /tmp/cat; chmod +x /tmp/cat; export PATH=/tmp:$PATH; echo $PATH` - Modify PATH to execute a shell.
- `sudo mkdir /mnt/Finance && sudo mount -t cifs -o username=plaintext,password=Password123,domain=. //192.168.220.129/Finance /mnt/Finance` - Mount a CIFS share.
- `mount -t cifs //192.168.220.129/Finance /mnt/Finance -o credentials=/path/credentialfile.txt` - Mount a CIFS share with credentials file.
- `dd if=/dev/urandom of=certificateOfIncorporation.pdf bs=1M count=30` - Create a random file.
- `dd if=/dev/urandom of=reverse-shell.exe bs=1M count=10` - Create a reverse shell.
- `STDIN – 0` - Standard Input.
- `STDOUT – 1` - Standard Output.
- `STDERR – 2` - Standard Error.
- `find /etc/ -name shadow 2>/dev/null > results.txt` - Redirect output to file.
- `find /etc/ -name *.conf 2>/dev/null | grep systemd` - Use `|` to pipe output.
- `find /etc/ -name *.conf 2>/dev/null | grep systemd | wc -l` - Count results.
- `find /etc/ -name shadow 2>/dev/null` - Redirect error messages.
- `find /etc/ -name shadow 2> stderr.txt 1> stdout.txt` - Redirect stdout and stderr to different files.
- `find /etc/ -name passwd >> stdout.txt 2>/dev/null` - Append to stdout and stderr.
- `cat << EOF > stream.txt` - Redirect stdin stream to file.
- `find / -name *.log 2>/dev/null | wc -l` - Count log files.
- `more /etc/passwd` - Display file contents with `more`.
- `less /etc/passwd` - Display file contents with `less`.
- `head /etc/passwd` - Display first lines of file.
- `tail /etc/passwd` - Display last lines of file.
- `cat /etc/passwd | sort` - Sort file contents.
- `cat /etc/passwd | grep "/bin/bash"` - Search for specific text.
- `cat /etc/passwd | grep -v "false\|nologin"` - Exclude results.
- `cat /etc/passwd | grep -v "false\|nologin" | cut -d":" -f1` - Use `cut` to extract specific fields.
- `cat /etc/passwd | grep -v "false\|nologin" | tr ":" " "` - Replace characters.
- `cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | column -t` - Format output.
- `cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}'` - Use `awk` for complex operations.
- `cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}' | sed 's/bin/HTB/g'` - Use `sed` for text substitution.
- `cat /etc/passwd | grep -v "false\|nologin" | tr ":" " " | awk '{print $1, $NF}' | wc -l` - Count lines.
- `netstat -tunl | grep LISTEN | grep -v "tcp6" | grep -v "127.0.0" | wc -l` - Count services listening on all interfaces.

