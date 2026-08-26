---
title: Using the Metasploit Framework
aliases: []
tags:
- topic/metasploit
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: 09-039-metasploit-09-Plugins.pdf
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
This section introduces the Metasploit Framework and its usage in cybersecurity. It covers the basics of setting up and using Metasploit for ethical hacking purposes.

## Setting Up Metasploit
1. Install Metasploit on your system.
2. Start the Metasploit console.
3. Use the `search` command to find modules.
4. Use the `use` command to select a module.
5. Configure the module parameters using the `set` command.
6. Run the module using the `run` command.

## Using Metasploit Modules
Metasploit modules are categorized into various types such as exploits, auxiliary, and post. Each module can be used for different purposes like exploiting vulnerabilities, gathering information, and post-exploitation tasks.

Example: Using the `exploit/multi/http/brute` module for HTTP brute-forcing.

## Post-Exploitation
After gaining access, use Metasploit's post-exploitation modules to maintain access, gather information, and clean up traces.

Example: Using the `post/multi/gather/credentials` module to gather credentials.

## Advanced Usage
Explore advanced features like multi-threading, payload customization, and module chaining.

Example: Using the `multi/handler` module to set up a reverse shell handler.

## References
- https://academy.hackthebox.com/module/39/section/413

