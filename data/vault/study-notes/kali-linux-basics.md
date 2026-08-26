---
title: Kali Linux Basics
aliases: []
tags:
- tool/kali
- os/linux
- topic/system-commands
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: notes.md
related_tools:
- '[[kali-creds]]'
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

# Kali Linux Basics

## Password Change
Change the default password using the `passwd` command.

```shell
passwd
# follow instructions and exec
kali-creds
kali-creds                                                                 
 * Verifying that you are running this binary as 'kali'.                                                                 
 * Confirming that you changed your password.                                                                 
Awesome. You updated your password. Make sure you also update the password for 'root'.                                                                 
Great job. Here is your flag:                                                                 
OS{c271be138a57b9b1bc22301306cd2b7d}
Press any key to continue...
```

The kali system uses the following directories:

- `/bin` - basic programs (ls, cd, cat, etc.)
- `/sbin` - system programs (fdisk, mkfs, sysctl, etc)
- `/etc` - configuration files
- `/tmp` - temporary files (typically deleted on boot)
- `/usr/bin` - applications (apt, ncat, nmap, etc.)
- `/usr/share` - application support and data files

## Man Pages
Using the `man` command allows you to see the help manual. If you cannot access the `man` command, you can use `apropos` which does the same as `man -k`.

```shell
man -k password
# or
man -k "user password"
# or can use regex
man -k "^passw"
```

The `which` command searches through the directories that are defined in the `$PATH` environment variable for a given file name.

```shell
echo $PATH
/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/home/kali/.dotnet/tools
which sbd
/usr/bin/sbd
```

The `locate` command is the quickest way to find the locations of files and directories in Kali. You may need to manually update it.

```shell
# update the database
sudo updatedb
# search for sbd.exe file, I know its here somewhere
locate sbd.exe
/usr/share/windows-resources/sbd/sbd.exe
```

## Directory Management
Creating directories can be expedited by using the `-p` flag.

```shell
mkdir -p test/{recon, exploit, report}
ls -1 test/
exploit
recon
report
```

## Service Management
Manage services using `systemctl`.

```shell
# list all services
sudo systemctl list-unit-files
# start a service
sudo systemctl start ssh
# stop a service
sudo systemctl stop ssh
# make a service start at boot
sudo systemctl enable ssh
```

## Socket Investigation
Investigate sockets using the `ss` command.

```shell
# show all listening and non-listening ports, exact numbers, show process using socket
sudo ss -antlp | grep sshd
LISTEN 0      128          0.0.0.0:22        0.0.0.0:*    users:("sshd",pid=16104,fd=3)
LISTEN 0      128             [::]:22           [::]:*    users:("sshd",pid=16104,fd=4)
```

## Package Management
Manage packages using `apt` and `dpkg`.

```shell
# update the list of packages
sudo apt update
# upgrade all packages or just one
sudo apt upgrade
sudo apt upgrade metasploit-framework
# is package available in the Kali Linux repos
apt-cache search pure-ftpd
# show a package
apt show resource-agents
# install a package
sudo apt install pure-ftpd
# completely remove a package (--purge removes all saved settings etc)
sudo apt remove pure-ftpd
```

Install a package from a `.deb` file using `dpkg`.

```shell
# install a package from .deb file 
sudo dpkg -i man-db_2.7.0.2-5_amd64.deb
```

