---
title: Hack The Box - Academy Module 23 Section 1493
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 20-23-FileInclusion-07-LFIFileUploads.pdf
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

# Hack The Box - Academy Module 23 Section 1493

## Introduction
This module covers the use of the `net use` command to establish network connections and map drives. The `net use` command is a powerful tool for network administrators and attackers to manage network connections and access shared resources.

## Syntax
The basic syntax for the `net use` command is as follows:

```cmd
net use [options] [\computeremote] [password] [/user:[user_name]]
```

Where:
- `options` can include various parameters such as `/add`, `/delete`, `/persistent:yes`, etc.
- `computer` is the name of the remote computer.
- `remote` is the shared resource path on the remote computer.
- `password` is the password for the remote resource.
- `user_name` is the username for the remote resource.

## Usage
The `net use` command can be used to:
- Map a network drive to a remote resource.
- Disconnect a network drive.
- List all current network connections.
- Set persistent connections that survive system restarts.

Example usage:

```cmd
net use Z: \192.168.1.10	est /user:Administrator password /persistent:yes
```

This command maps drive `Z:` to the shared resource `\192.168.1.10	est` on the remote computer `192.168.1.10` using the username `Administrator` and password `password`. The connection will be persistent and survive a system restart.

## Notes
It is important to use the `net use` command with caution, as it can be used to gain unauthorized access to network resources. Ensure that you have proper authorization before using this command in a network environment.

## References
- https://academy.hackthebox.com/module/23/section/1493

