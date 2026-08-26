---
id: kali.md
tags: [offsec, kali, pen-200]
created: 2023-01-13 11:56
---
# PEN-200: 3 Command line fun

backlinks:
- [[offsec/pen200/3/lab]]

sources:

---


## environment variables

These variables are a form of global storage for various settings inherited by any applications that are run during that terminal session

```shell
# list all environment variables
env
SHELL=/bin/bash
...
PWD=/home/kali
XDG_SESSION_DESKTOP=lightdm-xsession
LOGNAME=kali
XDG_SESSION_TYPE=x11


# $PATH is a colon-separated list of directory paths that Bash will search through whenever a command is run without a full path
echo $PATH
/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/home/kali/.dotnet/tools

#current terminal users username
echo $USER

#present working directory
echo $PWD

#home directory
echo $HOME

# ASSIGN ENVIRONMENT VARIABLES TO SAVE TIME
export IP=12.12.12.122
echo $IP
ping $IP
ssh student@$IP -p 2222
```

## history

```shell
history
  547  git add --all
  548  git commit -m "offsec pen200 2 complete"
  549  git push
  550  git pull
  551  echo $PATH
  552  cd ~/Documents

# you can execute a previous command by referencing its line number
# this will execute the "git pull" command from my history
!550 

# what was the last command we ran?
!!
sudo systemctl restart apache2
!!

# reverse-i-search shows the latest command in your history that contains the letter a
[ctrl] + [r] a
nano .bashrc
```

## 3.2 Piping and redirection

Every program run from the command line has three data streams connected to it that serve as communication channels with the external environment. These streams are defined as follows:

| Stream Name               | Description                                    |
| ------------------------- | ---------------------------------------------- |
| Standard Input (STDIN)    | Data fed into the program                      |
| Standard Output (STDOUT)  | Output from the program (defaults to terminal) |
| Standard Error (STDERR)   | Error messages (defaults to terminal)          |

Piping (using the | operator) and redirection (using the > and < operators) connects these streams between programs and files to accommodate a near infinite number of possible use cases.

### redirect to a new file

```shell
echo "test" > myoutput.txt

# append to the file
echo "-ing here" >> myoutput.txt

```

### redirect from a file

```shell
# redirect the contents of myfile.txt to the wc -m to count the characters
wc -m < myfile.txt
89

```

### redirect STDERR

```shell

ls ./test
ls cannot access '/test' no such file or directory

# redirect stderr
ls ./test 2>error.txt

cat error.txt
ls cannot access '/test' no such file or directory

```

### piping

```shell
# cat the contents of error.txt then pipe to wc and count the characters and output that to txt
cat error.txt | wc -m > charcount.txt

```

## 3.3 Text searching and manipulation

### grep

grep searches text files for the occurrence of a given regular expression and outputs any line containing a match to the standard output

- -r recursive
- -i case insensitive

```shell
ls -la /usr/bin | grep zip

-rwxr-xr-x  3 root root   34480 Jan 29  2017 bunzip2
-rwxr-xr-x  3 root root   34480 Jan 29  2017 bzip2
-rwxr-xr-x  1 root root   13864 Jan 29  2017 bzip2recover
-rwxr-xr-x  2 root root    2301 Mar 14  2016 gunzip
-rwxr-xr-x  1 root root  105172 Mar 14  2016 gzip
```

### sed

sed performs text editing on a stream of text, either a set of specific files or standard output

```shell
echo "I need to try hard" | sed 's/hard/harder/'
I need to try harder

```

### cut

is used to extract a section of text from a line and output it to the standard output.

- -f field number
- -d field delimiter

```shell
echo "I hack binaries,web apps,mobile apps, and just about anything else"| cut -f 2 -d ","
web apps

# get the usernames out of the /etc/passwd file
geoclue
Debian-snmp
sslh
ntpsec
redsocks
rwhod
```

### awk

AWK is a programming language designed for text processing and is typically used as a data extraction and reporting tool.

```shell
#split string on -F "::" and then print cols 1 and 3
echo "hello::there::friend" | awk -F "::" '{print $1, $3}'
hello friend
```

## Practical Example

Let's take a look at a practical example that ties together many of the commands we have explored so far.

We are given an Apache HTTP server log (http://www.offensive-security.com/pwk-files/access_log.txt.gz), that contains evidence of an attack. Our task is to use Bash commands to inspect the file and discover various pieces of information, such as who the attackers were and what exactly happened on the server.

First, we'll use the head and wc commands to take a quick peek at the log file to understand its structure. The head command displays the first 10 lines in a file and the wc command, along with the -l option, displays the total number of lines in a file.

```shell
kali@kali:~$ gunzip access_log.txt.gz

kali@kali:~$ mv access_log.txt access.log

kali@kali:~$ head access.log
201.21.152.44 - - [25/Apr/2013:14:05:35 -0700] "GET /favicon.ico HTTP/1.1" 404 89 "-" "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.64 Safari/537.31" "random-site.com"
70.194.129.34 - - [25/Apr/2013:14:10:48 -0700] "GET /include/jquery.jshowoff.min.js HTTP/1.1" 200 2553 "http://www.random-site.com/" "Mozilla/5.0 (Linux; U; Android 4.1.2; en-us; SCH-I535 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30" "www.random-site.com"
...

kali@kali:~$ wc -l access.log
1173 access.log
```

Notice that the log file is text-based and contains different fields (IP address, timestamp, HTTP request, etc.) that are delimited by spaces. This is a perfectly "grep friendly" file and will work well for all of the tools we have covered so far. We'll begin by searching through the HTTP requests made to the server for all the IP addresses recorded in this log file. We'll do this by piping the output of the cat command into the cut and sort commands. This may give us a clue about the number of potential attackers we will need to deal with.

```shell
kali@kali:~$ cat access.log | cut -d " " -f 1 | sort -u
201.21.152.44
208.115.113.91
208.54.80.244
208.68.234.99
70.194.129.34
72.133.47.242
88.112.192.2
98.238.13.253
99.127.177.95
```

We see that less than ten IP addresses were recorded in the log file, although this still doesn't tell us anything about the attackers. Next, we use uniq and sort to show unique lines, further refine our output, and sort the data by the number of times each IP address accessed the server. The -c option of uniq will prefix the output line with the number of occurrences.

```shell
kali@kali:~$ cat access.log | cut -d " " -f 1 | sort | uniq -c | sort -urn
1038 208.68.234.99
59 208.115.113.91
22 208.54.80.244
21 99.127.177.95
8 70.194.129.34
1 201.21.152.44
```

A few IP addresses stand out but we will focus on the address that has the highest access frequency first. To filter out the 208.68.234.99 address and display and count the resources that were being requested by that IP, we can use the following sequence:

```shell
kali@kali:~$ cat access.log | grep '208.68.234.99' | cut -d "\"" -f 2 | uniq -c
1038 GET //admin HTTP/1.1
```

From this output, it seems that the IP address at 208.68.234.99 was accessing the /admin directory exclusively. Let's inspect this further.

```shell
kali@kali:~$ cat access.log | grep '208.68.234.99' | grep '/admin ' | sort -u
208.68.234.99 - - [22/Apr/2013:07:51:20 -0500] "GET //admin HTTP/1.1" 401 742 "-" "Teh Forest Lobster"
208.68.234.99 - admin [22/Apr/2013:07:51:25 -0500] "GET //admin HTTP/1.1" 200 575 "-" "Teh Forest Lobster"
...

kali@kali:~$ cat access.log|grep '208.68.234.99'| grep -v '/admin '
kali@kali:~$
```

Apparently 208.68.234.99 has been involved in an HTTP brute force attempt against this web server. Furthermore, after about 1000 attempts, it seems like the brute force attempt succeeded, as indicated by the "HTTP 200" message.


## 3.5 Comparing files

### comm
The commcommand compares two text files, displaying the lines that are unique to ech one as well as the lines they have in common. It outputs three space-offset columns
column 1 - first file
column 2 - second file
column 3 - common lines

- -n switch to supress columns

### diff

The diff command is used to detecte differences between files siliar to the com command. Diff is much more complex and supports many output formats.

- -c context format
- -u unified format

```shell
kali@kali:~$ diff -c scan-a.txt scan-b.txt
*** scan-a.txt	2018-02-07 14:46:21.557861848 -0700
--- scan-b.txt	2018-02-07 14:46:44.275002421 -0700
***************
*** 1,5 ****
  192.168.1.1
- 192.168.1.2
  192.168.1.3
  192.168.1.4
  192.168.1.5
--- 1,5 ----
  192.168.1.1
  192.168.1.3
  192.168.1.4
  192.168.1.5
+ 192.168.1.6

kali@kali:~$ diff -u scan-a.txt scan-b.txt
--- scan-a.txt	2018-02-07 14:46:21.557861848 -0700
+++ scan-b.txt	2018-02-07 14:46:44.275002421 -0700
@@ -1,5 +1,5 @@
 192.168.1.1
-192.168.1.2
 192.168.1.3
 192.168.1.4
 192.168.1.5
+192.168.1.6
```

## 3.6 Managing processes

### background processes

Sending commands to the background can let you continue work in the terminal by adding the & symbol to the end. Pipe to file instead of screen to keep control.

```shell
ping -c 4000 localhost > pingresults.txt &

# to list the jobs
jobs

#switch to a job
fg %1fg

```

If you forget to add the &, you can suspend the job using [CTRL]+[z]. Once suspended we can resume it in the background by using the bg command

### process control

```shell
ps -ef
ps -fC qterminal

# stop a process by using its process id
kill 1307

```

## 3.7 File and command monitoring

### tail
is used to monitor log file entries as they are being writtin
- -f continuously updates the output as the target grows
- -nX outputs the last number of lines instead of the default 10

```shell
sudo tail -f /var/log/apache2/access.log
127.0.0.1 - - [02/Feb/2018:12:18:14 -0500] "GET / HTTP/1.1" 200 3380 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
127.0.0.1 - - [02/Feb/2018:12:18:14 -0500] "GET /icons/openlogo-75.png HTTP/1.1" 200 6040 "http://127.0.0.1/" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
127.0.0.1 - - [02/Feb/2018:12:18:15 -0500] "GET /favicon.ico HTTP/1.1" 404 500 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
```

### watch
the watch command is used to run a designated command at a regular interval (by default 2 seconds)

- -n X can be used to specify the interval -n 5 = 5 seconds

```shell
watch -n 5 w

```
## 3.8 Downloading files

### wget

downloads files using the HTTP/HTTPS and FTP protocols

- -o output file
- 
```shell

wget -O report_wget.pdf https://www.offensive-security.com/reports/penetration-testing-sample-report-2013.pdf

```

### curl

curl is a tool to transfer data to or from a server using a host of protocols including IMAP/S, POP3/S, SCP, SFTP, SMB/S, SMTP/S, TELNET, TFTP, and others. A penetration tester can use this to download or upload files and build complex requests.

- -o output file

```shell
curl -o report.pdf https://www.offensive-security.com/reports/penetration-testing-sample-report-2013.pdf

```

### axel

axel is a download accelerator that transfers a file from a FTP or HTTP server through multiple connections. This tool has a vast array of features, but the most common is -n, which is used to specify the number of multiple connections to use.

- -a more concise progress
- -o output name
- -n number of connections to use

```shell
axel -a -n 20 -o report_axel.pdf https://www.offensive-security.com/reports/penetration-testing-sample-report-2013.pdf
Initializing download: https://www.offensive-security.com/reports/penetration-testing-sample-report-2013.pdf
File size: 26.4091 Megabyte(s) (27691955 bytes)
Opening output file report_axel.pdf
Starting download

Connection 3 finished
Connection 6 finished
Connection 10 finished
Connection 4 finished
Connection 13 finished
Connection 18 finished
Connection 19 finished
Connection 2 finished

Downloaded 26.4091 Megabyte(s) in 8 second(s). (3038.59 KB/s)

```

## 3.9. Customizing the Bash Environment

### history

The HISTCONTROL variable defines whether or not to remove duplicate commands, commands that begin with spaces from the history, or both. By default, both are removed but you may find it more useful to only omit duplicates.

```shell
export HISTCONTROL=ignoredups

# The HISTIGNORE variable is particularly useful for filtering out basic commands that are run frequently, such as ls, exit, history, bg, etc:

export HISTIGNORE="&:ls:[bf]g:exit:history"

# HISTTIMEFORMAT controls date and/or time stamps in the output of the history command
export HISTTIMEFORMAT='%F %T '

```

### alias

**ALIASES CAN OVERWRITE CURRENT COMMANDS eg. mkdir or ls**

An alias is a string we can define that replaces a command name. Aliases are useful for replacing commonly-used commands and switches with a shorter command, or alias, that we define. In other words, an alias is a command that we define ourselves, built from other commands. An example of this is the ls command, where we typically tend to use ls -la (display results in a long list, including hidden files). Let's take a look at how we can use an alias to replace this command:

```shell
alias lsa='ls -la'
lsa
total 8308
........
-rw-------  1 kali kali     5542 Jan 22 09:56 .bash_history
-rw-r--r--  1 kali kali     3391 Apr 25  2017 .bashrc
drwx------  9 kali kali     4096 Oct  2 21:29 .cache
........

# to remove an alias
unalias mkdir

```

### persistant bash customization

The behavior of interactive shells in Bash is determined by the system-wide bashrc file located in /etc/bash.bashrc. The system-wide Bash settings can be overridden by editing the .bashrc file located in any user's home directory.

```shell

cat ~/.bashrc

```
