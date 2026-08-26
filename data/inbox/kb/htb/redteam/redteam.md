
# IF YOU GET STUCK
- do you have a username or a password?
    - have you tried logging into every service?
    - have you tried every account (including administrator/root) with the other passwords (password reuse)



# Additional Resources
- [Payloads all the things](https://swisskyrepo.github.io/PayloadsAllTheThings/)
- 

# Operating systems
- [linux commands](kb/htb/redteam/assets/techniques/linux-commands.md)
- [windows commands](kb/htb/redteam/assets/techniques/win-commands.md)


# Reconnnaissance
Exploring the target and identifying potential vulnerabilities
 - [nmap](kb/htb/redteam/assets/tools/nmap.md)

# Resource development
Developing C2 infrastructure, malware or other resources to support attack
- [seclists](kb/htb/redteam/assets/techniques/seclists.md)
- [transfers](kb/htb/redteam/assets/techniques/transfers.md)

# Initial Access
Gaining an initial foot hold on a target system

- [21 ftp](kb/htb/redteam/assets/services/ftp.md)
    - anonymous login 
    - bruteforcing 
- [22 ssh](kb/htb/redteam/assets/services/ssh.md)
- [25,143,110,465,587,993,995 smtp](kb/htb/redteam/assets/services/smtp.md)
- [53 udp/tcp dns](kb/htb/redteam/assets/services/dns.md)
- [80,443 http/s](kb/htb/redteam/assets/services/http.md)
    - [sql injection](kb/htb/redteam/assets/techniques/sqlinjection.md)
    - [api](kb/htb/redteam/assets/services/httpapi.md)
    - [cross site scripting](kb/htb/redteam/assets/techniques/xss.md)
    - [file inclusion](kb/htb/redteam/assets/techniques/file-inclusions.md)
    - [file uploads](kb/htb/redteam/assets/techniques/file-uploads.md)
    - [javascript injection](kb/htb/redteam/assets/techniques/javascript-injection.md)
    - [web attacks](kb/htb/redteam/assets/techniques/web-attacks.md)
- [139,445 smb](kb/htb/redteam/assets/services/smb.md)
- [873 rsync](kb/htb/redteam/assets/services/rsync.md)
- [1433,2433(hidden) sqlserver](kb/htb/redteam/assets/services/mssql.md)
- [3306 mysql](kb/htb/redteam/assets/services/mysql.md)
- [3389 rdp](kb/htb/redteam/assets/services/rdp.md)
- [5432 postgresql](kb/htb/redteam/assets/services/postgresql.md)
- [5985,5986 winrm](kb/htb/redteam/assets/services/winrm.md)
- [6379 redis](kb/htb/redteam/assets/services/redis.md)
- [27017 mongodb](kb/htb/redteam/assets/services/mongodb.md)



# Execution
Running malware on an infected system

# Persistence
Protecting the attackers foothold against restarts, etc

# Privilige escalation
Gaining high level permissions on an infected machine.

# Defense Evasion
Defending against antivirus and other security solutions

# Credential Access
Stealing password, api keys, ssh keys, etc
- [password cracking](kb/htb/redteam/assets/techniques/passwordcracking.md)
- [linux credential hunting](kb/htb/redteam/assets/techniques/linux-credhunting.md)
- [attacking wifi](kb/htb/redteam/assets/techniques/attacking-wifi.md)
- 
  
# Discovery
Exploring an infected network from the inside

# Lateral movement
Moving from one system to another with a network
- [lateral movement basics](kb/htb/redteam/assets/techniques/lateral-movement.md)
- 


# Collection
Collecting sensitive and useful data from compromised systems

# Command and control
Communicating between malware and its operator

# Exfiltration
Moving data out of the infected network

# Impact
Attacking system confidentiality, integrity or availablity

# Scripts
- [powershell](kb/htb/redteam/assets/scripts/powershell.md)


# Tools
- [excel](kb/htb/redteam/assets/tools/excel.md)
- [mermaidjs](kb/htb/redteam/assets/tools/mermaidjs.md)
- [sqlmap](kb/htb/redteam/assets/tools/sqlmap.md)
- 


# Resources
- [cyber security checklist](kb/htb/redteam/assets/resources/cyberchecklist.md)