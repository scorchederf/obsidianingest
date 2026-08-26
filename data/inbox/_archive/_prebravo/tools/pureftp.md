---
id: tools-apache2
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-apache2

backlinks: [[]]

sources:

---


Install
```shell sudo apt update && sudo apt install pure-ftpd```

#create users for using this bash function
```shell
kali@kali:~$ cat ./setup-ftp.sh
#!/bin/bash

sudo groupadd ftpgroup
sudo useradd -g ftpgroup -d /dev/null -s /etc ftpuser
sudo pure-pw useradd offsec -u ftpuser -d /ftphome
sudo pure-pw mkdb
cd /etc/pure-ftpd/auth/
sudo ln -s ../conf/PureDB 60pdb
sudo mkdir -p /ftphome
sudo chown -R ftpuser:ftpgroup /ftphome/
sudo systemctl restart pure-ftpd
```

#make it executable
```shell chmod +x setup-ftp.sh```


# execute
```shell
kali@kali:~$ sudo ./setup-ftp.sh
Password:
Enter it again:
Restarting ftp server
```


Change a users passwor
```shell

sudo pure-pw passwd billyt
Password: *********
Enter it again: *******
 

# Then update the password database.

pure-pw mkdb
```



PureDB /etc/pureftpd.pdb




sudo touch /etc/pure-ftpd/pureftpd.passwd

systemctl stop pure-ftpd; systemctl start pure-ftpd


