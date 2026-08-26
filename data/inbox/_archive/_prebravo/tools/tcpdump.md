---
id: tools-tcpdump
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-tcpdump

backlinks: [[]]

sources:

---

## tcpdump

Tcpdump is a text-based network sniffer that is streamlined, powerful, and flexible despite the lack of a graphical interface. It is by far the most commonly-used command-line packet analyzer and can be found on most Unix and Linux operating systems, but local user permissions determine the ability to capture network traffic.

Tcpdump can both capture traffic from the network and read existing capture files. 

```shell
# read an existing pcap 
sudo tcpdump -r password_cracking_filtered.pcap
```

- filter using awk

```shell
sudo tcpdump -n -r password_cracking_filtered.pcap | awk -F" " '{print $5}' | sort | uniq -c | head
```

- -X output hex and ascii

```shell
sudo tcpdump -nX -r password_cracking_filtered.pcap
```

- specific port

```shell
sudo tcpdump -n port 81 -r password_cracking_filtered.pcap
```

- source host and destination host

```shell
sudo tcpdump -n src host 172.16.40.10 dst host 192.168.1.1 -r password_cracking_filtered.pcap
```

- -w test.pcap = save to file
- -i eth0 | any = specify interface or any
- -D list all interfaces (eg tcpdump -D)
-  


#google on port 443  
tcpdump -A dst www.google.com and port 443  

#extract user agent from http request header  
sudo tcpdump -nn -A -s1500 -l | grep "User-Agent:"  

#get requests  
sudo tcpdump -s 0 -A -vv 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420'  

#post requests  
sudo tcpdump -s 0 -A -vv 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x504f5354'  



#extract http passwords in POST requests  
sudo tcpdump -s 0 -A -n -l | egrep -i "POST /|pwd=|passwd=|password=|Host:"  
#http request urls  
sudo tcpdump -s 0 -v -n -l | egrep -i "POST /|GET /|Host:"  
#cookie capture  
sudo tcpdump -nn -A -s0 -l | egrep -i 'Set-Cookie|Host:|Cookie:'  
#ftp creds  
sudo tcpdump -nn -v port ftp or ftp-data 



##TCP FLAGS##

Unskilled Attackers Pester Real Security Folks
==============================================
                     TCPDUMP FLAGS
Unskilled =  URG  =  (Not Displayed in Flag Field, Displayed elsewhere) 
Attackers =  ACK  =  (Not Displayed in Flag Field, Displayed elsewhere)
Pester    =  PSH  =  [P] (Push Data)
Real      =  RST  =  [R] (Reset Connection)
Security  =  SYN  =  [S] (Start Connection)
Folks     =  FIN  =  [F] (Finish Connection)
          SYN-ACK =  [S.] (SynAcK Packet)
                     [.] (No Flag Set)

##USAGE##
Basic communication // see the basics without many options
# tcpdump -nS

Basic communication (very verbose) // see a good amount of traffic, with verbosity and no name help
# tcpdump -nnvvS

A deeper look at the traffic // adds -X for payload but doesn’t grab any more of the packet
# tcpdump -nnvvXS

Heavy packet viewing // the final “s” increases the snaplength, grabbing the whole packet
# tcpdump -nnvvXSs 1514

host // look for traffic based on IP address (also works with hostname if you’re not using -n) 
# tcpdump host 1.2.3.4

src, dst // find traffic from only a source or destination (eliminates one side of a host conversation) 
# tcpdump src 2.3.4.5 
# tcpdump dst 3.4.5.6

net // capture an entire network using CIDR notation 
# tcpdump net 1.2.3.0/24

proto // works for tcp, udp, and icmp. Note that you don’t have to type proto 
# tcpdump icmp

port // see only traffic to or from a certain port 
# tcpdump port 3389

src, dst port // filter based on the source or destination port 
# tcpdump src port 1025 # tcpdump dst port 389

src/dst, port, protocol // combine all three 
# tcpdump src port 1025 and tcp 
# tcpdump udp and src port 53

You also have the option to filter by a range of ports instead of declaring them individually, and to only see packets that are above or below a certain size.

Port Ranges // see traffic to any port in a range 
tcpdump portrange 21-23

Packet Size Filter // only see packets below or above a certain size (in bytes) 
tcpdump less 32 
tcpdump greater 128
[ You can use the symbols for less than, greater than, and less than or equal / greater than or equal signs as well. ]

// filtering for size using symbols 
tcpdump > 32 
tcpdump <= 128

[ Note: Only the PSH, RST, SYN, and FIN flags are displayed in tcpdump‘s flag field output. URGs and ACKs are displayed, but they are shown elsewhere in the output rather than in the flags field ]

Keep in mind the reasons these filters work. The filters above find these various packets because tcp[13] looks at offset 13 in the TCP header, the number represents the location within the byte, and the !=0 means that the flag in question is set to 1, i.e. it’s on.

Show all URG packets:
# tcpdump 'tcp[13] & 32 != 0'

Show all ACK packets:
# tcpdump 'tcp[13] & 16 != 0'

Show all PSH packets:
# tcpdump 'tcp[13] & 8 != 0'

Show all RST packets:
# tcpdump 'tcp[13] & 4 != 0'

Show all SYN packets:
# tcpdump 'tcp[13] & 2 != 0'

Show all FIN packets:
# tcpdump 'tcp[13] & 1 != 0'

Show all SYN-ACK packets:
# tcpdump 'tcp[13] = 18'

Show icmp echo request and reply
#tcpdump -n icmp and 'icmp[0] != 8 and icmp[0] != 0'

Show all IP packets with a non-zero TOS field (one byte TOS field is at offset 1 in IP header):
# tcpdump -v -n ip and ip[1]!=0

Show all IP packets with TTL less than some value (on byte TTL field is at offset 8 in IP header):
# tcpdump -v ip and 'ip[8]<2'

Show TCP SYN packets:
# tcpdump -n tcp and port 80 and 'tcp[tcpflags] & tcp-syn == tcp-syn'
# tcpdump tcp and port 80 and 'tcp[tcpflags] == tcp-syn'
# tcpdump -i <interface> "tcp[tcpflags] & (tcp-syn) != 0"

Show TCP ACK packets:
# tcpdump -i <interface> "tcp[tcpflags] & (tcp-ack) != 0"

Show TCP SYN/ACK packets (typically, responses from servers):
# tcpdump -n tcp and 'tcp[tcpflags] & (tcp-syn|tcp-ack) == (tcp-syn|tcp-ack)'
# tcpdump -n tcp and 'tcp[tcpflags] & tcp-syn == tcp-syn' and 'tcp[tcpflags] & tcp-ack == tcp-ack'
# tcpdump -i <interface> "tcp[tcpflags] & (tcp-syn|tcp-ack) != 0"

Show TCP FIN packets:
# tcpdump -i <interface> "tcp[tcpflags] & (tcp-fin) != 0"

Show ARP Packets with MAC address
# tcpdump -vv -e -nn ether proto 0x0806

Show packets of a specified length (IP packet length (16 bits) is located at offset 2 in IP header):
# tcpdump -l icmp and '(ip[2:2]>50)' -w - |tcpdump -r - -v ip and '(ip[2:2]<60)'

More Details: 
http://danielmiessler.com/study/tcpdump/



https://hackertarget.com/tcpdump-examples/ 

sudo tcpdump -i eth0 -nn -s0 -v port 80
-i : Select interface that the capture is to take place on, this will often be an ethernet card or wireless adapter but could also be a vlan or something more unusual. Not always required if there is only one network adapter.
-nn : A single (n) will not resolve hostnames. A double (nn) will not resolve hostnames or ports. This is handy for not only viewing the IP / port numbers but also when capturing a large amount of data, as the name resolution will slow down the capture.
-s0 : Snap length, is the size of the packet to capture. -s0 will set the size to unlimited - use this if you want to capture all the traffic. Needed if you want to pull binaries / files from network traffic.
-v : Verbose, using (-v) or (-vv) increases the amount of detail shown in the output, often showing more protocol specific information.
port 80 : this is a common port filter to capture only traffic on port 80, that is of course usually HTTP.


