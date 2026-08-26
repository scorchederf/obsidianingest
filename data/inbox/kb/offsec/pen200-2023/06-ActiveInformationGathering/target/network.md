	
	
# 192.168.207.12
	135/tcp open  msrpc         Microsoft Windows RPC
	139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
	445/tcp open  microsoft-ds?
	Host script results:
			|_clock-skew: 2s
			| smb2-security-mode: 
			|   311: 
			|_    Message signing enabled but not required
			| smb2-time: 
			|   date: 2023-04-25T06:17:58
			|_  start_date: N/A
	Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	
	
# 192.168.207.6
	22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
			| ssh-hostkey: 
			|   3072 565711b5dcf113d35088b8aba983e229 (RSA)
			|   256 4f1df255cb40e076b4369019a2baf044 (ECDSA)
			|_  256 6746b39726a9e3a84deb20b39b8d7a32 (ED25519)
	80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
			|_http-server-header: Apache/2.4.41 (Ubuntu)
			|_http-title: Under Construction
	
	
# 192.168.207.8
	22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
			| ssh-hostkey: 
			|   3072 8e08fb846956cf344b2d82a530b95e72 (RSA)
			|   256 af8d4ed710626b0fdc82f770e4fbebb6 (ECDSA)
			|_  256 8a00939f561a0ba2d3b0c85901ad8fff (ED25519)
	25/tcp open  smtp    Postfix smtpd
			| ssl-cert: Subject: commonName=mail
			| Subject Alternative Name: DNS:mail
			| Not valid before: 2021-12-02T15:18:58
			|_Not valid after:  2031-11-30T15:18:58
			|_ssl-date: TLS randomness does not represent time
			|_smtp-commands: mail, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, CHUNKING
	
	
# 192.168.207.9
	135/tcp open  msrpc         Microsoft Windows RPC
	139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
	445/tcp open  microsoft-ds?
	Host script results:
			|_clock-skew: 3s
			| smb2-time: 
			|   date: 2023-04-25T06:21:37
			|_  start_date: N/A
			| smb2-security-mode: 
			|   311: 
			|_    Message signing enabled but not required
	
	
# 192.168.207.11
	135/tcp open  msrpc         Microsoft Windows RPC
	139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
	445/tcp open  microsoft-ds?
	Host script results:
			|_clock-skew: 3s
			| smb2-time: 
			|   date: 2023-04-25T06:21:36
			|_  start_date: N/A
			| smb2-security-mode: 
			|   311: 
			|_    Message signing enabled but not required
			| clock-skew: 
			|   3s: 
			|     192.168.207.11
			|_    192.168.207.9
	Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
