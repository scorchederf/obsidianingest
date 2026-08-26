---
id: offsec labs
tags: [offsec, labs]
created: 2023-01-27
---
# offsec labs

backlinks: [[snippets-bash]]

sources:

---

## PEN-200: 7.1.7 DNS Enumeration

 Exercises

(To be performed on your own Kali machine - Reporting is required for these exercises)

1. Find the DNS servers for the megacorpone.com domain.
```shell
└─$ dig ns megacorp.com                     
; <<>> DiG 9.18.8-1-Debian <<>> ns megacorp.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 56985
;; flags: qr rd ad; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 0
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;megacorp.com.                  IN      NS

;; ANSWER SECTION:
megacorp.com.           0       IN      NS      ns1.mytrafficmanagement.com.
megacorp.com.           0       IN      NS      ns2.mytrafficmanagement.com.

;; Query time: 236 msec
;; SERVER: 172.17.224.1#53(172.17.224.1) (UDP)
;; WHEN: Sat Jan 28 08:14:36 AEST 2023
;; MSG SIZE  rcvd: 124


```

2. Write a small script to attempt a zone transfer from megacorpone.com using a higher-level scripting language such as Python, Perl, or Ruby.
3. Recreate the example above and use dnsrecon to attempt a zone transfer from megacorpone.com.

4. Now that you have proven your DNS prowess, let's see you put it to work on a real unknown network. The first step is to identify the lab's DNS server. The network on VM Group 1 is private and the domain name is currently unknown; however, you do know the lab's IP range, and that is plenty of information for this problem. Take an active approach to scan this IP range identify the host(s) listening on the DNS port, and then query those servers to find the true DNS server for the public domain. Then, identify the full domain name of the main DNS server. The flag is in a TXT record with the same name as the full domain name.

```
# used nmap instead
nmap -v -p 53 192.168.176.1-255 > vm1.nmap

#summary
Nmap scan report for dc.MAILMAN.com (192.168.176.149)
Host is up (0.24s latency).

PORT   STATE SERVICE
53/tcp open  domain

└─$ dnsrecon -d dc.MAILMAN.com                                   
[*] std: Performing General Enumeration against: dc.MAILMAN.com...
[-] DNSSEC is not configured for dc.MAILMAN.com
[*]      A dc.MAILMAN.com 192.168.176.149
[*]      TXT dc.MAILMAN.com OS{6d8a534b161a66160a55fc3159ddf8bb}
[*] Enumerating SRV Records
[+] 0 Records Found


```

5. You have figured out where the main DNS server is located. Now,once started VM Group 2, use your active recon techniques to interrogate this server and learn more about the domain. In doing so, you will learn that the DNS host you found is also the name server for a special subdomain. Going further, you will then learn about a single very special host (an A record) within this special subdomain. What is the only host known about by the DNS server on this additional subdomain? The flag is in a TXT record with the same name as the full domain name of this host.

```shell

#find the dns server
nmap -v -p 53 192.168.125.1-255 > vm2.nmap  

NAMESERVER=dc.MAILMAN.COM 192.168.125.149

#modify hosts file and add dc.mailman.com
192.168.125.149 dc.mailman.com

#dnsrecon did not show any other 

#dig directly by passing the ip address
└─$ dig axfr mailman.com @192.168.125.149 

; <<>> DiG 9.18.8-1-Debian <<>> axfr mailman.com @192.168.125.149
;; global options: +cmd
mailman.com.            3600    IN      SOA     dc.mailman.com. hostmaster.mailman.com. 158 900 600 86400 3600
mailman.com.            3600    IN      NS      dc.mailman.com.
_msdcs.mailman.com.     3600    IN      NS      dc.mailman.com.

#new nameserver discovered _msdcs.mailman.com

dig axfr _msdcs.mailman.com @192.168.125.149

; <<>> DiG 9.18.8-1-Debian <<>> axfr _msdcs.mailman.com @192.168.125.149
;; global options: +cmd
_msdcs.mailman.com.     3600    IN      SOA     dc.mailman.com. hostmaster.mailman.com. 47 900 600 86400 3600
_msdcs.mailman.com.     3600    IN      NS      dc.mailman.com.
608b67a2-2eca-4397-bfb4-0697e7f987fe._msdcs.mailman.com. 600 IN CNAME dc.mailman.com.
_kerberos._tcp.Default-First-Site-Name._sites.dc._msdcs.mailman.com. 600 IN SRV 0 100 88 dc.mailman.com.
_ldap._tcp.Default-First-Site-Name._sites.dc._msdcs.mailman.com. 600 IN SRV 0 100 389 dc.mailman.com.
_kerberos._tcp.dc._msdcs.mailman.com. 600 IN SRV 0 100 88 dc.mailman.com.
_ldap._tcp.dc._msdcs.mailman.com. 600 IN SRV    0 100 389 dc.mailman.com.
_ldap._tcp.be24abe3-dc4e-4070-a0ce-21a930a25f6e.domains._msdcs.mailman.com. 600 IN SRV 0 100 389 dc.mailman.com.
gc._msdcs.mailman.com.  3600    IN      TXT     "OS{5fd3cdcce59e5cffee026563c86ed999}"
_ldap._tcp.Default-First-Site-Name._sites.gc._msdcs.mailman.com. 600 IN SRV 0 100 3268 dc.mailman.com.
_ldap._tcp.gc._msdcs.mailman.com. 600 IN SRV    0 100 3268 dc.mailman.com.
_ldap._tcp.pdc._msdcs.mailman.com. 600 IN SRV   0 100 389 dc.mailman.com.
_msdcs.mailman.com.     3600    IN      SOA     dc.mailman.com. hostmaster.mailman.com. 47 900 600 86400 3600



#flag found OS{5fd3cdcce59e5cffee026563c86ed999}


```

6. You have recovered all the information you can about the target domain, but that might not be the only domain that the DNS server manages. Instead of approaching the recon from a domain name perspective, you should try approaching it from an IP perspective by doing a brute force search of the available IP range 192.168.x.0/24 on VM Group 3. What new domain do you discover using this approach?

```Answer```





 Exercises

(To be performed on your own Kali machine - Reporting is required for these exercises)

    Use Nmap to conduct a ping sweep of your target IP range and save the output to a file. Use grep to show machines that are online.
    Scan the IP addresses you found in exercise 1 for open webserver ports. Use Nmap to find the webserver and operating system versions.
    Use NSE scripts to scan the machines in the labs that are running the SMB service.
    Use Wireshark to capture a Nmap connect and UDP scan and compare it against the Netcat port scans. Are they the same or different?
    Use Wireshark to capture a Nmap SYN scan and compare it to a connect scan and identify the difference between them.

(To be performed with the Topic Exercises VMs under “Resources” - Reporting is not required for these exercises)

6. There is a service running on a high-level TCP port on the VM #1.. Find it, and you will find the flag together with it.

```shell
┌──(kali㉿kali)-[~]
└─$ sudo nmap -T4 -sS --open -p 1024-65535 $IP
[sudo] password for kali: 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-06 20:08 AEST
Stats: 0:00:20 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 28.28% done; ETC: 20:09 (0:00:51 remaining)
Stats: 0:00:31 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 45.64% done; ETC: 20:09 (0:00:36 remaining)
Stats: 0:00:54 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 62.84% done; ETC: 20:09 (0:00:31 remaining)
Stats: 0:01:40 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 65.77% done; ETC: 20:10 (0:00:52 remaining)
Stats: 0:01:44 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 65.97% done; ETC: 20:10 (0:00:53 remaining)
Nmap scan report for 192.168.143.52
Host is up (0.25s latency).
Not shown: 60968 closed tcp ports (reset), 3542 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE
2222/tcp  open  EtherNetIP-1
59811/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 155.66 seconds
                                                                                                                                                                                            
┌──(kali㉿kali)-[~]
└─$ nc -nv $IP -p 59811                  
no port[s] to connect to
                                                                                                                                                                                            
┌──(kali㉿kali)-[~]
└─$ nc -nv $IP 59811   
(UNKNOWN) [192.168.143.52] 59811 (?) open
You found me. Great job!
Here is your flag:
OS{376233bf8c2d418b0dbdf9f5ac06a711}






```

    The NMAP Scripting Engine (NSE) includes a ton of really useful scripts to assist in the active recon process for all sorts of things - not just the handful of services discussed in this module. For example, in the NMAP library there are over 100 NSE discovery scripts. For this challenge, you will need to use a new discovery script to help you enumerate the HTTP title of the default page of all the hosts with web servers on the VM Group 1. Even something as simple as scanning the web server titles can help you get all sorts of information about the target including the purpose of the website, software version information, and even help you find login pages. In this challenge, you need to find the host with a web server with the title 'Under Construction'. The flag is located on the index.html page of the web server matching this title.

```shell

nmap -T4 --script=http-title 192.168.1.1-254 

                                                                                                                                                                                         
┌──(kali㉿kali)-[~]
└─$ nmap -T4 --script=http-title --open 192.168.165.1-254 

Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-07 18:39 AEST
Stats: 0:00:02 elapsed; 0 hosts completed (0 up), 254 undergoing Ping Scan
Ping Scan Timing: About 9.45% done; ETC: 18:39 (0:00:19 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (0 up), 254 undergoing Ping Scan
Ping Scan Timing: About 75.49% done; ETC: 18:39 (0:00:02 remaining)
Stats: 0:00:09 elapsed; 0 hosts completed (0 up), 254 undergoing Ping Scan
Parallel DNS resolution of 13 hosts. Timing: About 0.00% done
Stats: 0:00:13 elapsed; 0 hosts completed (0 up), 254 undergoing Ping Scan
Parallel DNS resolution of 13 hosts. Timing: About 0.00% done
Nmap scan report for 192.168.165.6
Host is up (0.31s latency).
Not shown: 989 closed tcp ports (conn-refused), 9 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
|_http-title: Under Construction

Nmap scan report for 192.168.165.8
Host is up (0.31s latency).
Not shown: 985 closed tcp ports (conn-refused), 13 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE
22/tcp open  ssh
25/tcp open  smtp

Nmap scan report for 192.168.165.9
Host is up (0.30s latency).
Not shown: 990 closed tcp ports (conn-refused), 7 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE
135/tcp open  msrpc
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap scan report for 192.168.165.11
Host is up (0.31s latency).
Not shown: 974 closed tcp ports (conn-refused), 23 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE
135/tcp open  msrpc
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap scan report for 192.168.165.12
Host is up (0.31s latency).
Not shown: 983 closed tcp ports (conn-refused), 14 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE
135/tcp open  msrpc
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap scan report for 192.168.165.13
Host is up (0.31s latency).
Not shown: 987 closed tcp ports (conn-refused), 8 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE
22/tcp   open  ssh
139/tcp  open  netbios-ssn
443/tcp  open  https
|_http-title: Site doesn't have a title (text/html).
445/tcp  open  microsoft-ds
9999/tcp open  abyss

Nmap scan report for 192.168.165.14
Host is up (0.31s latency).
Not shown: 973 closed tcp ports (conn-refused), 22 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE
21/tcp  open  ftp
80/tcp  open  http
|_http-title: IIS Windows Server
135/tcp open  msrpc
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap scan report for 192.168.165.15
Host is up (0.31s latency).
Not shown: 984 closed tcp ports (conn-refused), 12 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
8080/tcp open  http-proxy
|_http-title: Dashboard [Jenkins]

Nmap scan report for 192.168.165.20
Host is up (0.31s latency).
Not shown: 985 closed tcp ports (conn-refused), 11 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
| http-title: LOGIN |Messaging Web Application
|_Requested resource was ./login.php
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap scan report for 192.168.165.21
Host is up (0.31s latency).
Not shown: 985 closed tcp ports (conn-refused), 13 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
|_http-title: Chicken monitoring site

Nmap scan report for 192.168.165.22
Host is up (0.30s latency).
Not shown: 983 closed tcp ports (conn-refused), 15 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE
22/tcp   open  ssh
3306/tcp open  mysql

Nmap scan report for 192.168.165.149
Host is up (0.31s latency).
Not shown: 977 closed tcp ports (conn-refused), 12 filtered tcp ports (no-response)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT     STATE SERVICE
53/tcp   open  domain
88/tcp   open  kerberos-sec
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
389/tcp  open  ldap
445/tcp  open  microsoft-ds
464/tcp  open  kpasswd5
593/tcp  open  http-rpc-epmap
636/tcp  open  ldapssl
3268/tcp open  globalcatLDAP
3269/tcp open  globalcatLDAPssl

Nmap scan report for 192.168.165.254
Host is up (0.31s latency).
Not shown: 996 filtered tcp ports (no-response), 3 closed tcp ports (conn-refused)
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE
53/tcp open  domain

Nmap done: 254 IP addresses (13 hosts up) scanned in 73.13 seconds


http://192.168.165.6/

OS{496d1137bf27b0b390b4928b6ccbc675}



```
## PEN-200: 7.3.4 SMB Enumeration


To be performed on your own Kali machine - Reporting is required for these exercises)

    Use Nmap to make a list of the SMB servers in the lab that are running Windows.
    Use NSE scripts to scan these systems for SMB vulnerabilities.
    Use nbtscan and enum4linux against these systems to identify the types of data you can obtain from different versions of Windows.

(To be performed with the Topic Exercises VMs under “Resources” - Reporting is not required for these exercises)

1. Server message block (SMB) is an extremely important service that can be used to determine a wealth of information about a server including its users. Use nmap to identify the lab machines listening on the smb port and then use enum4linux to enumerate those machines. In doing so, you will find a machine with the local user alfred. The flag is located in the comments of one of the SMB shares of the host that has the alfred user.

```shell




for i in $( cat smb.txt | awk -F " " '{print $2}' | uniq | grep -v "Nmap" | grep -v "Ports" | sort ); do; enum4linux $i >> /home/kali/Documents/git/bravo/offsec/pen200/7/enum3.txt; done;    

OS{b58f925410818dab1c972575b40d43db}




```








## PEN-200: 7.4.3 NFS Enumeration

(To be performed on your own Kali machine - Reporting is required for these exercises)

    Use Nmap to make a list of machines running NFS in the labs.
    Use NSE scripts to scan these systems and collect additional information about accessible shares.




