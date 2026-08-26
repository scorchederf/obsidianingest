---
title: Hack The Box - Academy Module 110 Section 1052
aliases: []
tags:
- topic/hack-the-box-academy
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 14-110-UsingWebProxies-08-EncodingDecoding.pdf
related_tools:
- '[[nmap-1787746090]]'
- '[[netcat]]'
- '[[net]]'
- '[[ping]]'
- '[[whoami]]'
- '[[net user]]'
- '[[net localgroup]]'
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

# Hack The Box - Academy Module 110 Section 1052

## Introduction
In this section, we will be covering the basics of network scanning and enumeration using tools like nmap, netcat, and net. This will help us to understand the network topology and identify potential targets.

## Network Scanning with Nmap
First, we will use nmap to scan the network and identify all the active hosts. The command used is as follows:

```
$ nmap -sn 192.168.1.0/24
```
This command performs a ping scan on the specified subnet and lists all the active hosts.

## Port Scanning with Nmap
Next, we will perform a detailed port scan on the identified hosts using nmap. The command used is as follows:

```
$ nmap -p- 192.168.1.10
```
This command scans all the ports on the host 192.168.1.10 and lists the open ports.

## Using Netcat for Network Communication
Netcat can be used for various network communication tasks. For example, to open a listening port on a target machine, we can use the following command:

```
$ nc -lvp 4444
```
This command listens on port 4444 and waits for incoming connections.

## Using Net for Network Enumeration
Net is a powerful tool for network enumeration. We can use it to list all the users on a domain or a specific machine. The command to list all users on the domain is as follows:

```
$ net user
```
To list users on a specific machine, we can use the following command:

```
$ net user \192.168.1.10
```
This command lists all the users on the machine 192.168.1.10.

## Using Ping to Test Connectivity
Ping can be used to test the connectivity to a host. The command used is as follows:

```
$ ping 192.168.1.10
```
This command sends a ping to the host 192.168.1.10 and checks if it is reachable.

## Using Whoami to Check Current User
Whoami can be used to check the current user's credentials. The command used is as follows:

```
$ whoami
```
This command displays the current user's credentials.

## Using Net User to List Users
Net user can be used to list all the users on a domain or a specific machine. The command used is as follows:

```
$ net user
```
This command lists all the users on the domain.

## Using Net Localgroup to List Local Groups
Net localgroup can be used to list all the local groups on a machine. The command used is as follows:

```
$ net localgroup
```
This command lists all the local groups on the machine.

## References
- https://academy.hackthebox.com/module/110/section/1052

