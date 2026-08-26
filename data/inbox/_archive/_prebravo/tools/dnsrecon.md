---
id: tools-dnsrecon
tags: ["kali", "tool", "dns", "secure"]
created: 2023-01-12 11:56
---
# tools-dnsrecon

backlinks: [[]]

sources:

---
```shell
#simple
└─$ dnsrecon -d dc.MAILMAN.com                                   
[*] std: Performing General Enumeration against: dc.MAILMAN.com...
[-] DNSSEC is not configured for dc.MAILMAN.com
[*]      A dc.MAILMAN.com 192.168.176.149
[*]      TXT dc.MAILMAN.com OS{6d8a534b161a66160a55fc3159ddf8bb}
[*] Enumerating SRV Records
[+] 0 Records Found


```



```shell
─$ dnsrecon -d megacorpone.com -t axfr
[*] Checking for Zone Transfer for megacorpone.com name servers
[*] Resolving SOA Record
[+]      SOA ns1.megacorpone.com 51.79.37.18
[*] Resolving NS Records
[*] NS Servers found:
[+]      NS ns3.megacorpone.com 66.70.207.180
[+]      NS ns1.megacorpone.com 51.79.37.18
[+]      NS ns2.megacorpone.com 51.222.39.63
[*] Removing any duplicate NS server IP Addresses...
[*]  
[*] Trying NS server 51.79.37.18
[+] 51.79.37.18 Has port 53 TCP Open
[-] Zone Transfer Failed (Zone transfer error: REFUSED)
[*]  
[*] Trying NS server 51.222.39.63
[+] 51.222.39.63 Has port 53 TCP Open
[+] Zone Transfer was successful!!
[*]      NS ns1.megacorpone.com 51.79.37.18
[*]      NS ns2.megacorpone.com 51.222.39.63
[*]      NS ns3.megacorpone.com 66.70.207.180
[*]      TXT Try Harder
[*]      TXT google-site-verification=U7B_b0HNeBtY4qYGQZNsEYXfCJ32hMNV3GtC0wWq5pA
[*]      MX @.megacorpone.com fb.mail.gandi.net 217.70.178.216
[*]      MX @.megacorpone.com fb.mail.gandi.net 217.70.178.215
[*]      MX @.megacorpone.com fb.mail.gandi.net 217.70.178.217
[*]      MX @.megacorpone.com spool.mail.gandi.net 217.70.178.1
[*]      A admin.megacorpone.com 51.222.169.208
[*]      A beta.megacorpone.com 51.222.169.209
[*]      A fs1.megacorpone.com 51.222.169.210
[*]      A intranet.megacorpone.com 51.222.169.211
[*]      A mail.megacorpone.com 51.222.169.212
[*]      A mail2.megacorpone.com 51.222.169.213
[*]      A ns1.megacorpone.com 51.79.37.18
[*]      A ns2.megacorpone.com 51.222.39.63
[*]      A ns3.megacorpone.com 66.70.207.180
[*]      A router.megacorpone.com 51.222.169.214
[*]      A siem.megacorpone.com 51.222.169.215
[*]      A snmp.megacorpone.com 51.222.169.216
[*]      A support.megacorpone.com 51.222.169.218
[*]      A syslog.megacorpone.com 51.222.169.217
[*]      A test.megacorpone.com 51.222.169.219
[*]      A vpn.megacorpone.com 51.222.169.220
[*]      A www.megacorpone.com 149.56.244.87
[*]      A www2.megacorpone.com 149.56.244.87
[*]  
[*] Trying NS server 66.70.207.180
[+] 66.70.207.180 Has port 53 TCP Open
[-] Zone Transfer Failed (Zone transfer error: REFUSED)




```