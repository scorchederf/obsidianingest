---
title: Using the Metasploit Framework
aliases: []
tags:
- topic/metasploit
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 09-039-metasploit-12-WritingAndImportingModules.pdf
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
This module covers the basics of using the Metasploit Framework. Metasploit is a powerful tool for penetration testing and ethical hacking, providing a wide range of exploits and post-exploitation modules.

## Installation
To install Metasploit, follow the official documentation or use package managers like `apt` for Linux or `brew` for macOS. Ensure you have Ruby installed as Metasploit is written in Ruby.

## Starting Metasploit
Open a terminal and start Metasploit by running `msfconsole`. This command opens the Metasploit console, where you can interact with the framework.

## Using Modules
Metasploit modules are categorized into different types such as exploits, payloads, and post-exploitation. To use a module, you can search for it using the `search` command or browse the modules in the `auxiliary` and `exploit` directories.

## Running an Exploit
To run an exploit, first, find a suitable module using the `search` command. For example, to find a web application exploit, you might run `search web`. Once you have selected a module, you can run it with the `use` command followed by the module name. For instance, `use auxiliary/exploit/http/nessus_login`.

After selecting the module, you can set options using the `set` command. For example, `set RHOSTS 192.168.1.100` to set the target IP address. Finally, run the exploit with the `run` command.

## Post-Exploitation
Post-exploitation modules can be run to gain further access or gather information. For example, to get a shell, you might use the `shell` module. To execute a command, use the `cmd` module. These modules can be run using the `use` and `run` commands as described above.

## Payloads
Payloads are used to deliver a payload to the target system. Common payloads include reverse shells, bind shells, and meterpreter sessions. To use a payload, you can set the `PAYLOAD` option and then run the exploit. For example, `set PAYLOAD linux/x86/meterpreter/reverse_tcp` to set a Linux reverse shell payload.

## Exploiting Vulnerabilities
Metasploit can be used to exploit known vulnerabilities. For example, to exploit a vulnerability in a web application, you might use the `http/nessus_login` module. Ensure you have the necessary permissions and that the target is vulnerable to the chosen exploit.

## Conclusion
Metasploit is a versatile tool for ethical hackers and penetration testers. By mastering its usage, you can effectively test the security of systems and networks. Always ensure you have permission to test and use Metasploit responsibly.

## References
- https://academy.hackthebox.com/module/39/section/417

