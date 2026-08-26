---
id: ssh
tags: [ssh, remote]
created: 2023-01-12 11:56
---
# ssh

backlinks: [[]]

sources:
- <https://matt.might.net/articles/ssh-hacks/>

---

Standard connection using $IP variable connecting to port 2222
```shell
export IP=192.168.1.2
ssh student@$IP -p 2222
```


Transfer file over ssh connection
If these are going to be large files, you may want to use the -C flag to enable compression.

```shell
cat file | ssh -e none remote-host 'cat > file'
```

ssh tunneling by adding the -L flag and setting the destination server ip as your intermeditary

```shell
    #-L local_port:destination_server_ip:remote_port
ssh  -L 8999:<ip address of server c>:9001 pnap@ssh.server.com
```
