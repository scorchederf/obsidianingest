---
title: Linux Fundamentals
aliases: []
tags:
- topic/linux-fundamentals
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 31-18-LinuxFundamentals-05-GettingHelp.pdf
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

# Linux Fundamentals

## Introduction to Linux
Linux is a Unix-like operating system that is widely used in servers, desktops, and embedded systems. It is known for its stability, security, and flexibility. This module covers the basics of Linux, including file systems, permissions, and common commands.

## File Systems
Linux uses a hierarchical file system structure. The root directory is represented by "/". Common directories include:
- "/bin": Essential command binaries
- "/boot": Boot loader configuration files
- "/dev": Device files
- "/etc": Configuration files
- "/home": User home directories
- "/lib": Libraries
- "/media": Mount points for removable media
- "/mnt": Temporary mount points
- "/opt": Optional packages
- "/root": Home directory for the root user
- "/sbin": System binaries
- "/tmp": Temporary files
- "/usr": User utilities and libraries
- "/var": Variable data, such as logs and spool files

## Permissions
Linux permissions are managed using the chmod, chown, and chgrp commands. The basic permission modes are read (r), write (w), and execute (x). Ownership can be changed using chown and chgrp. For example, to change the owner of a file, use `chown user:group filename`.

## Common Commands
Here are some essential Linux commands:
- `ls`: List directory contents
- `cd`: Change directory
- `pwd`: Print working directory
- `mkdir`: Make directories
- `rm`: Remove files or directories
- `cp`: Copy files or directories
- `mv`: Move or rename files or directories
- `cat`: Concatenate and print files
- `grep`: Search for patterns in files
- `chmod`: Change file permissions
- `chown`: Change file owner
- `chgrp`: Change file group
- `nano`: Text editor
- `vim`: Text editor

