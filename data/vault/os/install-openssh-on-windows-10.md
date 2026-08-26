---
title: Install OpenSSH on Windows 10
aliases: []
tags:
- os/windows
- tool/openssh
category: os
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: ssh.md
related_tools:
- '[[openssh]]'
related_techniques: []
related_tactics: []
related_services:
- '[[sshd]]'
related_os:
- '[[Add-WindowsCapability]]'
- '[[Start-Service]]'
- '[[Set-Service]]'
- '[[Get-NetFirewallRule]]'
- '[[New-NetFirewallRule]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: windows
---

# Install OpenSSH on Windows 10

## Install OpenSSH on Windows 10
```powershell
# Install the OpenSSH Client
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Install the OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Start the sshd service
Start-Service sshd

# OPTIONAL but recommended:
Set-Service -Name sshd -StartupType 'Automatic'

# Confirm the Firewall rule is configured. It should be created automatically by setup. Run the following to verify
if (!(Get-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -ErrorAction SilentlyContinue | Select-Object Name, Enabled)) {
    Write-Output 'Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it...'
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
} else {
    Write-Output 'Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists.'
}
```

