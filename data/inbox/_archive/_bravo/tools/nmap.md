# nmap


https://nmap.org/book/host-discovery-strategies.html


## using predefined lists
`sudo -sn -oA nmap/tnet -iL hosts.lst | grep for | cut -d" " -f5`

## multiple ip addresses
` sudo nmap -sn -oA tnet <target1> <target2> <target3> | grep for | cut -d" " -f5`

## scan range
`sudo nmap -sn -oA tnet 10.129.2.18-20| grep for | cut -d" " -f5`

## scan top 10 ports
`sudo nmap <target> --top-ports=10 `

### tracing packets
`sudo nmap <target> -p 21 --packet-trace -Pn -n --disable-arp-ping`
```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-15 15:39 CEST
SENT (0.0429s) TCP 10.10.14.2:63090 > 10.129.2.28:21 S ttl=56 id=57322 iplen=44  seq=1699105818 win=1024 <mss 1460>
RCVD (0.0573s) TCP 10.129.2.28:21 > 10.10.14.2:63090 RA ttl=64 id=0 iplen=40  seq=0 win=0
```
SENT (0.0429s) TCP 10.10.14.2:63090 > 10.129.2.28:21 **S** ttl=56 id=57322 iplen=44  seq=1699105818 win=1024 <mss 1460>
S indicates that a TCP packet with a SYN flag has been sent to the target

RCVD (0.0573s) TCP 10.129.2.28:21 > 10.10.14.2:63090 **RA** ttl=64 id=0 iplen=40  seq=0 win=0
RA indicates that a TCP packet with a RST and ACK flag (RA) was returned

## tcp connect scan (is slower)
uses the three way handshake to determine if a port is open or closed, its the most accurate way to determine if port is open or not and is the most stealthy. 

`sudo nmap 10.129.2.28 -p 443 --packet-trace --disable-arp-ping -Pn -n --reason -sT `

## states returned by a scan
- open              = is actively accepting tcp, udp or sctp associations
- closed            = there is no application listening on the other side
- filtered          = nmap cannot determine if the port is open because packet filtering is preventing probes from reaching the port
- unfiltered        = port is accessible but unable to determine if it is closed or open
- open|filtered     = nmap is unable to determine if port is open or filtered
- closed|filtered   = namap is unable to determine if port is closed or filtered

## aggressive scan
- `sudo nmap <target> -p 80 -A`

## nmap scripting engine (NSE)

| Category  | Description                                                                                                                             |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------|
| auth      | Determination of authentication credentials.                                                                                            |
| broadcast | Scripts, which are used for host discovery by broadcasting and the discovered hosts, can be automatically added to the remaining scans. |
| brute     | Executes scripts that try to log in to the respective service by brute-forcing with credentials.                                        |
| default   | Default scripts executed by using the -sC option.                                                                                       |
| discovery | Evaluation of accessible services.                                                                                                      |
| dos       | These scripts are used to check services for denial of service vulnerabilities and are used less as it harms the services.              |
| exploit   | This category of scripts tries to exploit known vulnerabilities for the scanned port.                                                   |
| external  | Scripts that use external services for further processing.                                                                              |
| fuzzer    | This uses scripts to identify vulnerabilities and unexpected packet handling by sending different fields, which can take much time.     |
| intrusive | Intrusive scripts that could negatively affect the target system.                                                                       |
| malware   | Checks if some malware infects the target system.                                                                                       |
| safe      | Defensive scripts that do not perform intrusive and destructive access.                                                                 |
| version   | Extension for service detection.                                                                                                        |
| vuln      | Identification of specific vulnerabilities.                                                                                             |

- `sudo nmap <target> -sV --script vuln`



## ttl can identify the operating system
https://ostechnix.com/identify-operating-system-ttl-ping/
| Device / OS    | Version               | Protocol     | TTL |
|----------------|-----------------------|--------------|-----|
| AIX            | TCP                   | 60           |
| AIX            | UDP                   | 30           |
| Android        | 3.2.1                 | TCP and ICMP | 64  |
| Android        | 5.1.1                 | TCP and ICMP | 64  |
| AIX            | 3.2, 4.1              | ICMP         | 255 |
| BSDI           | BSD/OS 3.1 and 4.0    | ICMP         | 255 |
| Compa          | Tru64 v5.0            | ICMP         | 64  |
| Cisco          | ICMP                  | 254          |
| DEC Pathworks  | V5                    | TCP and UDP  | 30  |
| Foundry        | ICMP                  | 64           |
| FreeBSD        | 2.1R                  | TCP and UDP  | 64  |
| FreeBSD        | 3.4, 4.0              | ICMP         | 255 |
| FreeBSD        | 5                     | ICMP         | 64  |
| HP-UX          | 9.0x                  | TCP and UDP  | 30  |
| HP-UX          | 10.01                 | TCP and UDP  | 64  |
| HP-UX          | 10.2                  | ICMP         | 255 |
| HP-UX          | 11                    | ICMP         | 255 |
| HP-UX          | 11                    | TCP          | 64  |
| Irix           | 5.3                   | TCP and UDP  | 60  |
| Irix           | 6.x                   | TCP and UDP  | 60  |
| Irix           | 6.5.3, 6.5.8          | ICMP         | 255 |
| juniper        | ICMP                  | 64           |
| MPE/IX (HP)    | ICMP                  | 200          |
| Linux          | 2.0.x kernel          | ICMP         | 64  |
| Linux          | 2.2.14 kernel         | ICMP         | 255 |
| Linux          | 2.4 kernel            | ICMP         | 255 |
| Linux          | Red Hat 9             | ICMP and TCP | 64  |
| MacOS/MacTCP   | 2.0.x                 | TCP and UDP  | 60  |
| MacOS/MacTCP   | X (10.5.6)            | ICMP/TCP/UDP | 64  |
| NetBSD         | ICMP                  | 255          |
| Netgear FVG318 | ICMP and UDP          | 64           |
| OpenBSD        | 2.6 &amp; 2.7         | ICMP         | 255 |
| OpenVMS        | 07.01.2002            | ICMP         | 255 |
| OS/2           | TCP/IP 3.0            | 64           |
| OSF/1          | V3.2A                 | TCP          | 60  |
| OSF/1          | V3.2A                 | UDP          | 30  |
| Solaris        | 2.5.1, 2.6, 2.7, 2.8  | ICMP         | 255 |
| Solaris        | 2.8                   | TCP          | 64  |
| Stratus        | TCP_OS                | ICMP         | 255 |
| Stratus        | TCP_OS (14.2-)        | TCP and UDP  | 30  |
| Stratus        | TCP_OS (14.3+)        | TCP and UDP  | 64  |
| Stratus        | STCP                  | ICMP/TCP/UDP | 60  |
| SunOS          | 4.1.3/4.1.4           | TCP and UDP  | 60  |
| SunOS          | 5.7                   | ICMP and TCP | 255 |
| Ultrix         | V4.1/V4.2A            | TCP          | 60  |
| Ultrix         | V4.1/V4.2A            | UDP          | 30  |
| Ultrix         | V4.2 – 4.5            | ICMP         | 255 |
| VMS/Multinet   | TCP and UDP           | 64           |
| VMS/TCPware    | TCP                   | 60           |
| VMS/TCPware    | UDP                   | 64           |
| VMS/Wollongong | 1.1.1.1               | TCP          | 128 |
| VMS/Wollongong | 1.1.1.1               | UDP          | 30  |
| VMS/UCX        | TCP and UDP           | 128          |
| Windows        | for Workgroups        | TCP and UDP  | 32  |
| Windows        | 95                    | TCP and UDP  | 32  |
| Windows        | 98                    | ICMP         | 32  |
| Windows        | 98, 98 SE             | ICMP         | 128 |
| Windows        | 98                    | TCP          | 128 |
| Windows        | NT 3.51               | TCP and UDP  | 32  |
| Windows        | NT 4.0                | TCP and UDP  | 128 |
| Windows        | NT 4.0 SP5-           | 32           |
| Windows        | NT 4.0 SP6+           | 128          |
| Windows        | NT 4 WRKS SP 3, SP 6a | ICMP         | 128 |
| Windows        | NT 4 Server SP4       | ICMP         | 128 |
| Windows        | ME                    | ICMP         | 128 |
| Windows        | 2000 pro              | ICMP/TCP/UDP | 128 |
| Windows        | 2000 family           | ICMP         | 128 |
| Windows        | Server 2003           | 128          |
| Windows        | XP                    | ICMP/TCP/UDP | 128 |
| Windows        | Vista                 | ICMP/TCP/UDP | 128 |
| Windows        | 7                     | ICMP/TCP/UDP | 128 |
| Windows        | Server 2008           | ICMP/TCP/UDP | 128 |
| Windows        | 10                    | ICMP/TCP/UDP | 128 |
