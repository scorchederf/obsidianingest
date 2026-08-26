---
aliases:
tags:
source:
desc: Splunk is a log analytics tool used to gather, analyze and visualize data.
---

- `https` port 8000
- The biggest focus of Splunk during an assessment would be weak or null authentication because admin access to Splunk gives us the ability to deploy custom applications that can be used to quickly compromise a Splunk server and possibly other hosts in the network depending on the way Splunk is set up
- default creds
	- `admin:changeme`
	- If the default credentials do not work, it is worth checking for common weak passwords such as `admin`, `Welcome`, `Welcome1`, `Password123`
- The Splunk Enterprise trial converts to a free version after 60 days, which doesn’t require authentication. It is not uncommon for system administrators to install a trial of Splunk to test it out, which is subsequently forgotten about. This will automatically convert to the free version that does not have any form of authentication, introducing a security hole in the environment. Some organizations may opt for the free version due to budget constraints, not fully understanding the implications of having no user/role management.


# discovery
- identifies itself on nmap scan
	- `sudo nmap -sV 10.129.201.50`
		```sh
		Starting Nmap 7.80 ( https://nmap.org ) at 2021-09-22 08:43 EDT
		Nmap scan report for 10.129.201.50
		Host is up (0.11s latency).
		Not shown: 991 closed ports
		PORT     STATE SERVICE       VERSION
		80/tcp   open  http          Microsoft IIS httpd 10.0
		135/tcp  open  msrpc         Microsoft Windows RPC
		139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
		445/tcp  open  microsoft-ds?
		3389/tcp open  ms-wbt-server Microsoft Terminal Services
		5357/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
		8000/tcp open  ssl/http      Splunkd httpd
		8080/tcp open  http          Indy httpd 17.3.33.2830 (Paessler PRTG bandwidth monitor)
		8089/tcp open  ssl/http      Splunkd httpd
		Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
		
		Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
		Nmap done: 1 IP address (1 host up) scanned in 39.22 seconds	  
		```
	- 


# enumerate



# attack

- gain remote code execution on Splunk by creating a custom application to run Python, Batch, Bash, or PowerShell scripts
	- [[reverse_shell_splunk]]
- If the compromised Splunk host is a deployment server, it will likely be possible to achieve RCE on any hosts with Universal Forwarders installed on them. To push a reverse shell out to other hosts, the application must be placed in the `$SPLUNK_HOME/etc/deployment-apps` directory on the compromised host



# exploits

