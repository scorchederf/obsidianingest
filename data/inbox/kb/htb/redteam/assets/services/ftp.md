---
title: ftp
---

# ftp

- techniques
    - try anonymous:anonymous authentication `ftp ftp://anonymous@$ip`
    - brute forcing
        - medusa (slow)
            - `medusa -h $ip -U users.list -P passwords.list -M ftp -n 2121`
        - hydra
            - `hydra -L users.list -P passwords.list ftp://$ip:2121 -vv -I -t 40 -f -u`
            - `-f`      stop at first hit
            - `-t 40`   increase threads (may cause breaking)
            - `-u`      loop around users, not passwords (effective! implied with -x)


- commands
    - download all `mget *.*`



