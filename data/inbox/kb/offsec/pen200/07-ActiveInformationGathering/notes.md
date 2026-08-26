---
id: activeinformationgathering
tags: [bash, cheatsheet]
created: 2023-01-26
---
# active-information-gathering

backlinks: [[snippets-bash]]

sources:
- <https://github.com/danielmiessler/SecLists>
  

---

- DNS Enumeration
  - you may need to modify the /etc/resolve.conf file to add a nameserver OR /etc/hosts to add a host address
  - find dns server on network ```shell nmap -v -p 53 192.168.176.1-255 > vm1.nmap```
  - forward lookup (hostname -> ip address) 
    - ```shell for ip in $( cat /usr/share/seclists/Discovery/DNS/namelist.txt ); do host $ip.megacorpone.com | grep -v "not found"; done```
    - ```shell nslookup <hostname>```
    - ```shell nslookup <hostname> <nameserver>```
  - reverse lookup (ip address -> hostname) 
    - ```shell for ip in $( seq 1 255 ); do; host 192.168.176.$ip; done; | grep -v "not found"```
    - ```shell nslookup <ipaddress>```
  - dns zone transfers 
    - ```shell ./dns.axfr.sh megacorpone.com```
    - ```shell dnsrecon -d megacorpone.com -t axfr```
    - ```shell dig -domain megacorpone.com @dc.mailman.com```
- Port scanning
  - netcat
    - TCP scaning using Connect (3way handshake - SYN - SYNACK - ACK)
      - ```shell nc -nvv -w 1 -z 10.11.1.220 3388-3390 ```
    - UDP scanning (prone to false positives)
      - ```shell nc -nv -u -z -w 1 10.11.1.115 160-162```
  - nmap
    - default scan (top 1000 ports) ```shell nmap 10.11.1.220```
    - all ports ```shell nmap -p 1-65535 10.11.1.220```
    - default scan (tcp and udp) ```shell sudo nmap -sS -sU 10.11.1.115 ```
    - network sweep ```shell nmap -sn 10.11.1.1-254```
- Server Messaging Block (SMB) enumeration
  - nbtscan ```shell sudo nbtscan -r 10.11.1.0/24 ```  TODO TODO 
  - nmap 
    - ```shell nmap -v -p 139,445 -oG smb.txt 10.11.1.1-254 ```
    - smb nse os discovery and enumeration ```shell nmap -v -p 139, 445 --script=smb-os-discovery 10.11.1.227```
    - to check for smb vulnerablities (unsafe=1 will crash systems) ```shell nmap -v -p 139,445 --script=smb-vuln-ms08-067 --script-args=unsafe=1 10.11.1.5```
    - run enum4linux on all smb shares in range ```shell for i in $( nmap -v -p 139, 445 --script=smb-os-discovery 10.11.1.227 | awk -F " " '{print $2}' | uniq | grep -v "Nmap" | grep -v "Ports" | sort ); do; enum4linux $i >> /home/kali/Documents/git/bravo/offsec/pen200/7/enum3.txt; done;```    
- Network File System (NFS) enumeration
  - PortMapper and RPCbind run on TCP 111. RPCbind maps RPC services to the ports on which they listen. RPC processes notify rpcbind when they start, registering the ports they are listening on the and RPC program numbers they expect to serve. The client system them contacts rpcbind on the server with a particular RPC program number. The rpcbind service then redirects the client to the proper prot number (often tcp 2049) so it can communicate withe the service
  - nmap
    - ```shell nmap -v -p 111 10.11.1.1-254 ```
    - nse script like rpcinfo ```shell nmap -sV -p 111 --script=rpcinfo 10.11.1.1-254```
      - run all the nfs scripts against the target ```shell nmap -p 111 --script=nsf* 10.11.1.72```
      - if you get an nfs-showmount hit ```shell mkdir home && sudo mount -o nolock 10.11.1.72:/home ~/home/ && cd home && ls```
- SMTP enumeration
  - if prompted with VRFY you can iterate users ```shell nc -nv 10.11.1.217 25```
- Simple Network Management Protocol (SNMP)
  -  simple udp stateless protocol susceptible to ip spoofing and replay attacks. No encryption so creds can be intercepted
  -  scan for snmp ports ```shell sudo nmap -sU --open -p 161 10.11.1.1-254 -oG open-snmp.txt ```
  -  can brute force using onesixtyone ```shell onesixtyone -c community.lst -i ips.lst ```
  -  can specify the community string ```shell snmpwalk -c public -v1 -t 10 10.11.1.14```
  -  enumerate windows processes ```shell snmpwalk -c public -v1 10.11.1.73 1.3.6.1.2.1.25.4.2.1.2```
  -  enumerate open tcp ports ```shell snmpwalk -c public -v1 10.11.1.14 1.3.6.1.2.1.6.13.1.3```
  -  enumerate installed software ```shell snmpwalk -c public -v1 10.11.1.50 1.3.6.1.2.1.25.6.3.1.2 ```







- permission denied trying to access file
  - we can see that its owner has a UUID of 1014, and also read (r), write (w), and execute (x) permissions on it. What can we do with this information? Since we have complete access to our Kali machine, we can try to add a local user to it using the adduser command, change its UUID to 1014, su to that user, and then try accessing the file again. The new user has a UUID of 1001, which is not really what we need. We can change it to 1014 using sed and confirm the change took place. The -i option is used to replace the file in-place and the -e option executes a script. In this case, that happens to be 's/1001/1014/g', which will globally replace the UUID in the /etc/passwd 