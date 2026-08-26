---
title: hydra
---

# hydra


- usage
    - `hydra -L users.list -P passwords.list ftp://$ip:2121 -vv -I -t 40 -f -u`

- flags
    - `-f`      stop at first hit
    - `-t 40`   increase threads (may cause breaking)
    - `-u`      loop around users, not passwords (effective! implied with -x)