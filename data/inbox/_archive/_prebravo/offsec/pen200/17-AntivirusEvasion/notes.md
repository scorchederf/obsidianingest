---
id: activeinformationgathering
tags: [bash, cheatsheet]
created: 2023-01-26
---
# active-information-gathering

backlinks: [[snippets-bash]]

sources:
- <https://danielmiessler.com/study/vulnerability-database-resources/>

- Antivirus evasion
  - designed to prevent, detect and remove malicious software and can contain firewalls, website scanners etc
  - detection methods
    - signature based detection is based on a continous sequence of bytes within malware
      - bypass by changing or obfuscating contents in order to break the identifying byte sequence (or signature)
    - Heuristic-Based Detection is a detection method that relies on various rules and algorithms to determine whether or not an action is considered malicious. This is often achieved by stepping through the instruction set of a binary file or by attempting to decompile and then analyze the source code. The idea is to look for various patterns and program calls (as opposed to simple byte sequences) that are considered malicious.
    - Behavior-Based Detection dynamically analyzes the behavior of a binary file. This is often achieved by executing the file in question in an emulated environment, such as a small virtual machine, and looking for behaviors or actions that are considered malicious.
  - bypassing antivirus
    - on disk evasion
      - packers generate an executable that is not only smaller, but is also functionally equivalent with a completely new binary structure
        - [UPX is a free, secure, portable, extendable, high-performance executable packer for several executable formats](https://upx.github.io/)
      - obfuscators reorganize and mutate code in a way that makes it difficult to reverse engineer.This includes replacing instructions with semantically equivalent ones, inserting irrelevant instructions or "dead code",3 splitting or reordering functions
      - "Crypter" software cryptographically alters executable code, adding a decrypting stub that restores the original code upon execution. This decryption happens in-memory, leaving only the encrypted code on-disk. Encryption has become foundational in modern malware as one of the most effective AV evasion techniques.
      - software protectors. Highly effective antivirus evasion requires a combination of all of the previous techniques in addition to other advanced ones, including anti-reversing, anti-debugging, virtual machine emulation detection, and so on. In most cases, software protectors were designed for legitimate purposes but can also be used to bypass AV detection.
        - [Enigma Protector is a powerful system designed for comprehensive protection of executable files](https://www.enigmaprotector.com/en/home.html)
    - in memory evasion
      - In-Memory Injections, also known as PE Injection is a popular technique used to bypass antivirus products. Rather than obfuscating a malicious binary, creating new sections, or changing existing permissions, this technique instead focuses on the manipulation of volatile memory. One of the main benefits of this technique is that it does not write any files to disk, which is one the main areas of focus for most antivirus products.
        - Remote Process Memory Injection. This technique attempts to inject the payload into another valid PE that is not malicious. The most common method of doing this is by leveraging a set of Windows APIs.3 First, we would use the OpenProcess4 function to obtain a valid HANDLE5 to a target process that we have permissions to access. After obtaining the HANDLE, we would allocate memory in the context of that process by calling a Windows API such as VirtualAllocEx.6 Once the memory has been allocated in the remote process, we would copy the malicious payload to the newly allocated memory using WriteProcessMemory.7 After the payload has been successfully copied, it is usually executed in memory in a separate thread using the CreateRemoteThread8 API.
          - powershell can be used to do a lot of the heavy lifting
        - Reflective DLL Injection. Unlike regular DLL injection, which implies loading a malicious DLL from disk using the LoadLibrary9 API, this technique attempts to load a DLL stored by the attacker in the process memory. The main challenge of implementing this technique is that LoadLibrary does not support loading a DLL from memory. Furthermore, the Windows operating system does not expose any APIs that can handle this either. Attackers who choose to use this technique must write their own version of the API that does not rely on a disk-based DLL.
        - Process Hollowing. When using process hollowing to bypass antivirus software, attackers first launch a non-malicious process in a suspended state. Once launched, the image of the process is removed from memory and replaced with a malicious executable image. Finally, the process is then resumed and malicious code is executed instead of the legitimate process.
        - Inline hooking. As the name suggests, this technique involves modifying memory and introducing a hook (instructions that redirect the code execution) into a function to point the execution flow to our malicious code. Upon executing our malicious code, the flow will return back to the modified function and resume execution, appearing as if only the original code had executed.
    - [Shellter](https://www.shellterproject.com/) is a dynamic shellcode injection tool and one of the most popular free tools capable of bypassing antivirus software. 
    - [Veil](https://github.com/Veil-Framework/Veil) Veil is a tool designed to generate metasploit payloads that bypass common anti-virus solutions.
      - 