
- vars
    - `export ip=10.10.23.3 && echo $ip`
    - `export hn=target.htb && echo $hn`
    - `export dn=target.htb && echo $dn`

- recon
    - scan
        - tcp `sudo nmap -sV -sC -oA scans/alltcp -p- $ip`
        - udp `sudo nmap -F -sU -oA scans/alludp -p- $ip` 
        - vuln `sudo nmap --script vuln -v -oA scans/vuln $ip`
        - quiet `sudo nmap -p50000 -sS -Pn -n --disable-arp-ping --packet-trace --source-port 53 $ip`
    - results
        - dns
            - hostname
                - `sudo echo "$ip $hn" >> /etc/hosts` !! check
            - domains
                - `gobuster dns -d $dn -w /usr/share/wordlists/seclists/Discovery/DNS/dns-Jhaddix.txt -o scans/domains.gobuster`
            - subdomains 
                - `ffuf -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u -o scans/subdomains.ffuf http://FUZZ.$hostname/`

        - os
        - ports
            - 20/21 ftp
            - 23 ssh
            - 80/443

- ports
    - 21        ftp
        - anonymous
            - `ftp $ip` username anonymous password anonymous
        - brute force
            - `hydra -l b.smith -P passwords.txt ftp://$ip`
    - 22        ssh
        - `ssh -l username -p PORT $ip`
        - 
        - brute force
            - `hydra -L username.txt -P password.txt -u -f ssh://$ip:PORT -t 4`
    - 80/443    http
        - scan
            - fuzz virtual hosts `ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://$hn:PORT/ -H 'Host: FUZZ.$hn' -t 100 -o scans/vhosts.ffuf`
            - fuzz directories `ffuf -w /usr/share/SecLists/Discovery/Web-Content/combined_directories.txt -u http://$ip:PORT/FUZZ -recursion -t 100 -o scans/dir.ffuf`
            - fuzz extensions `ffuf -w /opt/useful/SecLists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://$hn:PORT/indexFUZZ -H 'Host:$hn' -t 100 -o scans/fileext.ffuf`
            - fuzz pages `ffuf -w /usr/share/SecLists/Discovery/Web-Content/combined_directories.txt -u http://$ip:PORT/blog/FUZZ.php -t 100 -o scans/pages.ffuf`
                - get `ffuf -w /usr/share/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://hn:PORT/admin/admin.php?FUZZ=key -t 100 -o scans/get.ffuf`
                - post `ffuf -w /usr/share/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://hn:PORT/admin/admin.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -t 100 -o scans/post.ffuf`
        - brute force
            - basic auth `hydra -C /usr/share/SecLists/Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt $ip -s PORT http-get /`
            - known password `hydra -L /usr/share/SecLists/Usernames/Names/names.txt -p amormio -u -f $ip -s PORT http-get /`
            - usernames and rockyou `hydra -L /usr/share/SecLists/Usernames/Names/names.txt -P /opt/useful/SecLists/Passwords/Leaked-Databases/rockyou.txt -u -f $ip -s PORT http-get /`
            - webform `sudo hydra -P /usr/share/wordlists/rockyou.txt -l admin -f $ip -s PORT http-post-form "/login.php:username=^USER^&password=^PASS^:F=<form name='login'"`


- linux
    - list all listening ports `netstat -antp | grep -i list`