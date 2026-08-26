---
id: tips and tricks
tags: [tips, tricks]
created: 2023-01-16
---
# tips and tricks

backlinks: [[snippets-bash]]

sources:

- <https://superuser.com/questions/236930/how-to-clean-up-output-of-linux-script-command>

---

ippsec notes
- Remember to search all fields in ad - bloodhound doesn't get the info field 
- Remember to check different encodings when using strings
- strings -e l password-manager
- Foxyproxy Mozilla plugin for burpsuite
- Mogura ( whackamolee
- Can a user change another users password
- Add path to hosts file so you can reference it
- Smbclient - try no Params , then '' values for username: password, then random 'pleasesub'
- Dirbuster  check for file extensions as well because default ii's settings may be excluded
- when you first hit a machine, make sure you check what processes are currently running 
- use axel for fast downloads
- 




- Clean up the output of script or tee console

```shell
cat typescript | perl -pe 's/\e([^\[\]]|\[.*?[a-zA-Z]|\].*?\a)//g' | col -b > typescript-processed
```

- Provide a list that can be useful in automation (one entry per line)

```shell
ls -la
```

- start the apache2 service

```shell
sudo systemctl start apache2
```

- Verify a service is running

```shell
sudo ss -antlp | grep apache2
```

- Ensure a service starts at startup

```shell
sudo systemctl enable apache2
```

- to see all available services

```shell
systemctrl list-unit-files
```

- elevate terminal to root

```shell
sudo -i
```

- to list your sudo permissions

```shell
sudo -l
```

- to get a list of usernames from the /etc/passwd file (you can only split on 1 delimiter)

```shell
# cut -d delimiter=":" -f field=1
cut -d ":" -f 1 /etc/passwd
```

- awk is used for text processing and can use multiple delimiters

```shell
echo "hello::there::friend" | awk -F "::" '{print $1, $3}'
hello friend
```

- gzip a file (-d deflate)

```shell
gzip -d access-logs.tar.gz
```

- tarball (-x extract)

```shell
tar -xf access-logs.tar 
```



access-logs.tar.gz

scp -P 2222 student@$IP:access-logs.tar.gz /home/kali/Documents/git/bravo/offsec/pen200/3


#allows clipboard use
rdesktop -u student -p lab $WINIP -5 -K -r clipboard:CLIPBOARD





# LinuxAlice #MUST USE FIXED IP ADDRESS AND NOT LOCALHOST
python3 -m http.server --bind 192.168.119.175 9000


Windows binaries on kali
/usr/share/windows-binaries        



# powershell faster get-childitem
$files = robocopy "c:\dev\git\bravo" NULL *.txt /S /L /NDL /NP /NJH /NJS /NS /NC | ForEach-Object { $_.TrimStart() }; $files


# port numbers
are there any numbers in the port number that look familiar 2121 - maybe port 21? try netcat or an ftp client to connect
