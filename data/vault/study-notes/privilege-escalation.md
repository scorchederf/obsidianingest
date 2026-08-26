---
title: Privilege Escalation
aliases: []
tags:
- attack/privilege-escalation
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: microsoft-windows-privilegeescalation.md
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

# Privilege Escalation

## Privilege Information
```cmd
whoami /priv
```

```plaintext
Privilege Name                Description                          State
============================= ==================================== ========
SeShutdownPrivilege           Shut down the system                 Disabled
SeChangeNotifyPrivilege       Bypass traverse checking             Disabled
SeUndockPrivilege             Remove computer from docking station Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set       Disabled
SeTimeZonePrivilege           Change the time zone                 Disabled
```

- `SeShutdownPrivilege`
  - Although it says “Disabled”, we can still use this privilege because this only means that the privilege is "disabled" in our current session, which is due to us not currently shutting down our machine.

