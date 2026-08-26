---
title: 'Falcon 302: Advanced Threat Hunting with Falcon'
aliases: []
tags:
- study-notes/hunting
- tool/crowdstrike-falcon
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: crowdstrike-falcon-training-302.md
related_tools:
- '[[CrowdStrike Falcon]]'
related_techniques:
- '[[T1003.004 - Command and Scripting Interpreter - PowerShell]]'
- '[[T1059.004 - Execute Commands]]'
related_tactics:
- '[[TA0003 - Defense Evasion]]'
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

# Falcon 302: Advanced Threat Hunting with Falcon

## Introduction
Class will begin at 5 minutes past the hour! 

1. Sign into CrowdStrike University first: https://crowdstrike.litmos.com/course/5313033
2. Sign into CloudShare Second: https://use.cloudshare.com/Class/bwvsl?passphrase=LogantheTiredTurtle
3. Be sure to remember which email address you use.
4. If/when the pop-up shows in the browser for the clipboard > Click allow on the browser pop-up
5. No VM’s found is expected on first login
6. I’ll give you the Falcon Encounter code after the setup demo

stephen.ferguson@crowdstrike.com

## Hunting Queries
Case insensitive `ParentBaseFileName=/cmd\.exe/i`

Exactly `^cmd\.exe`
- `^` starts with

Powershell hunt can show the score based on execution, downloading, hidden

Here is the breakdown of the “interesting score” is when something is found vs not found:
- PowerShell Hunt Report
- Score = Varies = Sum of all the columns, kind of like an “interesting” score
- Exec = 0 or 4 = Execution seen in CommandLine
- Dwnld = 0 or 4 = Download seen in CommandLine
- Encode = 0 or 5 = Is there encoding found in the CommandLine syntax
- ExecPol = 0 or 1 = Execution Policy syntax seen
- NonI = 0 or 1 = Non-Interactive
- NoProf = 0 or 1 = No Profile seen in syntax
- Hidden = 0 or 1 = Is the CommandLine showing Hidden switches
- Domain = 0 or 3 = Is there a Domain seen in the syntax
- VM = 0 or 3 = Virtual Machine commands seen in syntax such as Hypervisor
- Prxy = 0 or 4 = Proxy commands seen in syntax
- Obf1 = 0 or 4 = Obfuscation seen
- Obf2 = 0 or 4 = Obfuscation seen

## Hunting Queries (continued)
```hcl
#event_simpleName=ProcessRollup2
| aid=?aid
| ImageFileName=/(?<FileName>[^\/|\\]*)$
| FileName = /^(net|nmap|ipconfig|whoami|quser|ping|netstat|tasklist|hostname|at)\.exe$/i
| table([aid, UserName, ParentBaseFileName, ImageFileName, CommandLine], limit=1000)
```

Verify hash
Investigate user

External prevalence is against all CrowdStrike clients
Internal prevalence is against our environment

Aid = Agent identifier
ContextProcessId = 
TargetProcessId =

## Additional Resources
Infragard - https://www.infragard.org/
NCFTA - https://www.ncfta.net/
Interpol – https://www.interpol.int/en
NCIJTF – https://www.fbi.gov/investigate/cyber/national-cyber-investigative-joint-task-force
Cyber Threat Alliance - https://www.cyberthreatalliance.org/
CISA - https://www.cisa.gov/
Dept of State OSAC - https://www.state.gov/overseas-security-advisory-council/
STIX - https://makingsecuritymeasurable.mitre.org/docs/stix-intro-handout.pdf

## Day 4
Treeid is the way to map an event

? Can we follow the id to get a full process

? Can we block domains in custom IOA's ?

Support Reference: https://supportportal.crowdstrike.com/s/article/ka16T000000wxxHQAQ

52.86.45.171

Capstone

RemoteAddressIP4=52.86.45.171

```hcl
#event_simpleName=ProcessRollup2
| join(query={RemoteAddressIP4=52.86.45.171}, field=[TargetProcessId], key=[ContextProcessId])
| groupBy([UserName, ComputerName, @timestamp])
| sort(@timestamp, order=asc)
```

Endpoints impacted in this attack:
- INITECH-WRK134
- INITECH-WRK144
- INITECH-WRK132
- INITECH-WRK139
- INITECH-WEBIIS
- INITECH-AD
- INITECH-EXCHANG
- INITECH-FILE1
- INITECH-FILE2 (no malicious activity but accessed during this time)
- INITECH-WRK137 (no malicious activity but accessed during this time)

Actor IP addresses and/or domains:
- 52.86.45.171
- 10.3.0.80
- 3.228.237.193

Adversary identification based on TTPs/IOCs/IOAs observed:
- EMISSARY PANDA
- Gains access to the machine using a malicious HTA which downloads and executes Hyperbro, Sysupdate.exe also helpful to ID them

Compromised user accounts:
- milton.waddams
- leonard.katzman

9b59882.exe - Able Desktop / Hyperbro
- MD5 Hash: e346480dee921d101311e5b1026bf9ed
- SHA256 Hash: 07f87f7b3313acd772f77d35d11fc12d3eb7ca1a2cd7e5cef810f9fb657694a0
- VirusTotal Link: https://www.virustotal.com/gui/file/07f87f7b3313acd772f77d35d11fc12d3eb7ca1a2cd7e5cef810f9fb657694a0

Ckatz64.exe - MimiKatz
- MD5 Hash: 491bd07773b80cd07e9705900c63d51b
- SHA256 Hash: fedd3df503d4c985954dd90954e6cd1ce7739598d977f733db27e6e39c21cd52
- VirusTotal link: https://www.virustotal.com/gui/file/fedd3df503d4c985954dd90954e6cd1ce7739598d977f733db27e6e39c21cd52
- Hybrid Analysis: https://www.hybrid-analysis.com/sample/fedd3df503d4c985954dd90954e6cd1ce7739598d977f733db27e6e39c21cd52

Sysupdate.exe - Bronze Union
- MD5 Hash: c8d83840b96f5a186e7bb6320e998f72
- SHA256 Hash: 938f32822c1a6b1140ac0af60a06ae39011464de37c511921d8a7d9c6a69c9df
- VirusTotal link: https://www.virustotal.com/gui/file/938f32822c1a6b1140ac0af60a06ae39011464de37c511921d8a7d9c6a69c9df
- Hybrid Analysis: https://www.hybrid-analysis.com/sample/938f32822c1a6b1140ac0af60a06ae39011464de37c511921d8a7d9c6a69c9df

Sysupdate-938.exe - Bronze Union
- MD5 Hash: C8d83840b96f5a186e7bb6320e998f72
- SHA256 Hash: 938f32822c1a6b1140ac0af60a06ae39011464de37c511921d8a7d9c6a69c9df
- VirusTotal link: https://www.virustotal.com/gui/file/938f32822c1a6b1140ac0af60a06ae39011464de37c511921d8a7d9c6a69c9df/detection
- Hybrid Analysis: https://www.hybrid-analysis.com/sample/938f32822c1a6b1140ac0af60a06ae390114

## References
- https://crowdstrike.litmos.com/course/5313033
- https://use.cloudshare.com/Class/bwvsl?passphrase=LogantheTiredTurtle
- https://library.humio.com/data-analysis/functions-table.html
- https://library.humio.com/data-analysis/functions-groupby.html
- https://library.humio.com/data-analysis/dashboards-parameters.html#dashboards-parameters-example-regex
- https://library.humio.com/data-analysis/dashboards-parameters.html#dashboards-parameters-example-case-insensitive
- https://www.crowdstrike.com/cybersecurity-101/threat-hunting/
- https://falcon.crowdstrike.com/documentation/category/y907ff6d/hunting-queries
- https://www.crowdstrike.com/cybersecurity-101/endpoint-security/endpoint-detection-and-response-edr/
- https://supportportal.crowdstrike.com/s/article/How-long-will-Historical-Data-be-available-to-view-in-my-Falcon-console
- https://www.crowdstrike.com/cybersecurity-101/incident-response/
- https://www.crowdstrike.com/cybersecurity-101/indicators-of-compromise/
- https://www.infragard.org/
- https://www.ncfta.net/
- https://www.interpol.int/en
- https://www.fbi.gov/investigate/cyber/national-cyber-investigative-joint-task-force
- https://www.cyberthreatalliance.org/
- https://www.cisa.gov/
- https://www.state.gov/overseas-security-advisory-council/
- https://makingsecuritymeasurable.mitre.org/docs/stix-intro-handout.pdf
- https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/
- https://learn.microsoft.com/en-us/windows/win32/sync/mutex-objects?redirectedfrom=MSDN
- https://www.sans.org/blog/looking-at-mutex-objects-for-malware-discovery-indicators-of-compromise/
- https://www.crowdstrike.com/blog/sunspot-malware-technical-analysis/
- https://learn.microsoft.com/en-us/windows/win32/secauthz/enabling-and-disabling-privileges-in-c--
- https://www.programmingalgorithms.com/algorithm/elf-hash/cpp/
- https://www.crowdstrike.com/blog/what-is-a-hunting-lead/
- https://pentestlab.blog/2020/01/21/persistence-wmi-event-subscription/
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mstsc
- https://supportportal.crowdstrike.com/s/article/ka16T000000wxxHQAQ

