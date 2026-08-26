---
aliases:
tags:
source:
  - https://github.com/SamJoan/droopescan
desc:
---
A plugin-based scanner that aids security researchers in identifying issues with several CMSs, mainly Drupal & Silverstripe.

- install
	- `sudo pip3 install droopescan`
- help
	- `droopescan -h`
- joomla scan
	- `droopescan scan joomla --url http://dev.inlanefreight.local/`
- drupal scan
	- `droopescan scan drupal -u http://drupal.inlanefreight.local`
- 


# output
```sh
[+] Possible version(s):                                                        
    3.8.10
    3.8.11
    3.8.11-rc
    3.8.12
    3.8.12-rc
    3.8.13
    3.8.7
    3.8.7-rc
    3.8.8
    3.8.8-rc
    3.8.9
    3.8.9-rc

[+] Possible interesting urls found:
    Detailed version information. - http://dev.inlanefreight.local/administrator/manifests/files/joomla.xml
    Login page. - http://dev.inlanefreight.local/administrator/
    License file. - http://dev.inlanefreight.local/LICENSE.txt
    Version attribute contains approx version - http://dev.inlanefreight.local/plugins/system/cache/cache.xml

[+] Scan finished (0:00:01.523369 elapsed)

```