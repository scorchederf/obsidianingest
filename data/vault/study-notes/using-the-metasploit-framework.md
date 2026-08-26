---
title: Using the Metasploit Framework
aliases: []
tags:
- topic/metasploit
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: 09-039-metasploit-08-Databases.pdf
related_tools:
- '[[metasploit]]'
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

# Using the Metasploit Framework

## Introduction
This section provides an overview of the Metasploit Framework, a powerful tool for penetration testing and ethical hacking. It covers the basics of using Metasploit to identify and exploit vulnerabilities in systems.

## Getting Started
To begin using Metasploit, you need to install it on your system. The installation process can vary depending on your operating system, but generally, you can download the latest version from the official Metasploit website or use package managers like `apt` or `brew`.

## Navigating the Metasploit Console
Once installed, you can start the Metasploit console by running the `msfconsole` command. The console provides a command-line interface for executing various tasks, such as searching for exploits, launching attacks, and post-exploitation activities.

## Using Search and Exploits
The `search` command allows you to search for exploits based on various criteria, such as the target operating system, the vulnerability type, or the name of the exploit. For example, to search for exploits targeting Windows systems, you can use the command: 

```bash
search windows
```

Once you have identified an exploit, you can use the `use` command to select it and configure its options. For instance, to use the `exploit/windows/smb/ms17_010_eternalblue` exploit, you would run:

```bash
use exploit/windows/smb/ms17_010_eternalblue
```

You can then set options such as the target IP address, username, and password.

## Launching Exploits
After configuring the exploit, you can launch it using the `run` command. For example, to launch the `exploit/windows/smb/ms17_010_eternalblue` exploit, you would run:

```bash
run
```

The Metasploit console will then attempt to exploit the target system and provide feedback on the success or failure of the operation.

## Post-Exploitation
If the exploit is successful, you can use the Metasploit post-exploitation modules to gain further access to the target system. These modules can be used to execute commands, upload and download files, and perform other tasks. For example, to execute a command on the target system, you can use the `shell` module:

```bash
use post/multi/gather/shell
set SESSION <session_id>
run
```

Replace `<session_id>` with the ID of the session you established during the exploitation.

## Conclusion
This guide provides a basic introduction to using the Metasploit Framework. For more detailed information and advanced usage, refer to the official Metasploit documentation and community resources.

## References
- https://academy.hackthebox.com/module/39/section/411

