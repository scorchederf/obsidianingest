---
title: SSH Tunneling and Reverse Connections
aliases: []
tags:
- study-notes
- techniques
- t1003
- t1132
- t1555
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: mermaidjs.md
related_tools:
- '[[nmap-1787746090]]'
- '[[netcat]]'
- '[[socat]]'
- '[[mimikatz]]'
- '[[lazagne]]'
related_techniques:
- '[[t1003]]'
- '[[t1132]]'
- '[[t1555]]'
related_tactics:
- '[[ta0003]]'
related_services:
- '[[ssh]]'
- '[[mysql]]'
- '[[rdp]]'
related_os: []
related_notes: []
mitre_tactic: TA0003
mitre_technique: T1003, T1132, T1555
real_path: ''
port: ''
protocol: ''
os: ''
---

# SSH Tunneling and Reverse Connections

## SSH Tunneling
SSH tunneling is a method of securely forwarding network traffic over an encrypted SSH connection. It can be used to bypass firewalls and access internal networks or services that are not directly accessible from the internet.

Example 1:
```mermaid
flowchart LR
    subgraph Local_Machine
        A[You connect to
localhost:1234]
    end

    subgraph SSH_Tunnel
        T[Encrypted Tunnel]
    end

    subgraph Remote_Host[10.129.202.64]
        B[localhost:3306
MySQL Server]
    end

    A --> T --> B
```

Example 2:
```mermaid
flowchart LR
    subgraph Remote_Host[10.129.202.64]
        B[Connects to
localhost:9999]
    end

    subgraph SSH_Tunnel
        T[Encrypted Tunnel]
    end

    subgraph Local_Machine
        A[localhost:4444
e.g., listener]
    end

    B --> T --> A
```

Example 3:
```mermaid
flowchart LR
    subgraph Target_Network
        WIN[Windows Target]
        UBUNTU[Ubuntu Pivot
172.16.5.129]
    end

    subgraph Attacker
        ATTACK[Attack Host
127.0.0.1:8000]
    end

    WIN -- "Reverse HTTPS Payload
connects to 172.16.5.129:8080" --> UBUNTU
    UBUNTU -- "Port Forwarding
8080 → 127.0.0.1:8000" --> ATTACK
```

Example 4:
```mermaid
flowchart LR
    YOU[You
10.129.1.10]
    UBUNTU[Ubuntu
172.16.5.129]
    WIN[Windows
172.16.5.200]

    YOU -- "VPN / Route Exists" --> UBUNTU
    UBUNTU -- "Internal Network" --> WIN
    YOU -- "RDP connection TCP 3389" --> WIN
```

## Techniques and Tactics
These examples demonstrate techniques related to SSH tunneling and reverse connections, which are part of the MITRE ATT&CK framework.

- **T1003 - Exploitation of Remote Services**: This technique involves exploiting a remote service to gain access to a system. SSH tunneling can be used to bypass network restrictions and gain access to internal services.

- **T1132 - Reverse Shell**: A reverse shell is a type of shell connection where the attacker's shell is established on the target machine, and the connection is tunneled back to the attacker's machine. This is often used to maintain persistence and gain access to the target system.

- **T1555 - Reverse HTTPS**: This technique involves using HTTPS to establish a reverse shell or other types of connections. It can be used to bypass firewalls and other network security measures.

