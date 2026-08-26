---
id: offsec labs
tags: [offsec, labs]
created: 2023-01-13 19:19
---
# offsec labs

backlinks: [[snippets-bash]]

sources:

---

## PEN-200: 3.1.4 The Bash Environment

 Exercises

(To be performed on your own Kali VM - Reporting is required for these exercises)

1. Inspect your bash history and use history expansion to re-run a command from it.

```shell
history
538  git pull
539  man ss
540  systemctl --help

!539
man ss
```

2. Execute different commands of your choice and experiment browsing the history through the shortcuts as well as the reverse-i-search facility.

```shell
[ctrl] + [r] a
nano .bashrc
```

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

3. You should get to know your environment - Who knows, you might even find a flag. Start the VM #1 and look around.

```shell
env
SSH_CONNECTION=192.168.119.166 44858 172.18.0.2 22
FLAG=OS{ea7d6c90d271ed27361f4e84b38a9163}
TERM=xterm-256color
LESS_TERMCAP_mb=
LESS_TERMCAP_me=

```

4. There is a really long journey ahead of you. All you need to do is complete the path. Start at the /challenge folder on the VM #2. You will find the flag at the end.

```shell

cd "$(ls -trh | tail -1)"

# final path
/challenge/a62D3E4D1F743C7479508A475F8ECD9045332751B5189EEEEC0DD559D73F82F458898CAEDE62C56E35C0E686E10BD1DCA708E3F1628D11C2CE1664B4C983908A88853E41573597A74E4A29F/.b37C599C C6745117 F0462E876E  7257E C1FADA1135B3 5B9F3BE341798FBF6 F64CA80B9DCB79CAAB 6887131A25BB5F9D626215568A74CDD4AD7F829CB 162431C05E9C2CA336C0762/cfcf\eCbaeaAEfadBgFb dffg bFFCgc'aceFFEGEf'C\BB'eEadd 'ddAcdbcddg dBfEBAFDGaDAEBDgCE G\efebfgGEAeAE'fcAe AE E fBfgfA ccdCdECAcgBFfA 'e'cFeaEdGdbBFD\Ddg/"d'Dg cg\FDC\bB"fgb f DEECDfA"gegGFd""g"GFeDBAFDCcbEgG"\"g'd\\'"DcfF"fGDbbbGeegCeGdG e\fBd\caBBB'EDDbbgEE"'FCECbfdGbC'gAAfdA \DDbB  \fCaBD\gA'g  aa\"E\"

ls -la
drwxr-xr-x 2 root root 4096 Jan 18 07:56 .
drwxr-xr-x 3 root root 4096 Jan 18 07:56 ..
-rwxr-xr-x 1 root root   53 Jan 18 07:56 end

cat end
T1N7NGMwN2YxNGY3NTY4YWYxZjc4YzlmN2ZmOWMzMzZjNjh9Cg==

#looks like base64 == on the end
base64 -d end
OS{4c07f14f7568af1f78c9f7ff9c336c68}

```

5. This Kali Linux shell has a complicated past - learn more about it to find the flag on the VM #3. In solving this problem, try to use expansion instead of copy and paste.

```shell

history
1  echo 'wait.... that's it? what now?
2  echo '4f537b64353365656466613432386433646466393234653533313961363230363034377d0a0a' | xxd -r -p
3  echo '1'
4  echo '2'
5  echo '3'

echo '4f537b64353365656466613432386433646466393234653533313961363230363034377d0a0a' | xxd -r -p
OS{d53eedfa428d3ddf924e5319a6206047}

```

## PEN-200: 3.2.6 Piping and redirection

Exercises

(To be performed on your own Kali VM - Reporting is required for these exercises)

1. Use the cat command in conjunction with sort to reorder the content of the /etc/passwd file on your Kali Linux system.

```shell
cat /etc/passwd | sort 
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
avahi:x:111:117:Avahi mDNS daemon,,,:/run/avahi-daemon:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin

```

2. Redirect the output of the previous exercise to a file of your choice in your home directory.

```shell
cat /etc/passwd | sort >> /home/kali/sortedpasswd

```

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

3. We have a cyber-criminal on our hands, and we need your help to crack the case! After you start the below challenge, you will find a program in the /challenge directory that outputs an exact copy of the access-logs.tar.gz. This file is a tarballed and GNU zipped (gzipped) copy of a directory containing several logs (access-log[#].txt) that were collected as evidence on a case. We believe the key to cracking this case (i.e. the flag) is somewhere in these logs. On VM #1, redirect the output of this program to a file in the /home/student folder, uncompress that file, and then find the flag to solve this case.

```shell

cd /challenge
./to-redirect-and-search > /home/student/access-logs.tar.gz
cd /home/student
mkdir logs
cp access-logs.tar.gz logs/access-logs.tar.gz
cd logs
gzip -d access-logs.tar.gz
tar -xf access-logs.tar
cd access-logs
ls -la

total 4032
drwxr-xr-x 2 student student	4096 Jan 19 00:08 .
drwxr-xr-x 3 student student	4096 Jan 19 00:15 ..
-rw-r--r-- 1 student student  431432 Jan 19 00:08 access-log0.txt
-rw-r--r-- 1 student student   47543 Jan 19 00:08 access-log1.txt
-rw-r--r-- 1 student student  751324 Jan 19 00:08 access-log2.txt
-rw-r--r-- 1 student student  495199 Jan 19 00:08 access-log3.txt
-rw-r--r-- 1 student student 1933248 Jan 19 00:08 access-log4.txt
-rw-r--r-- 1 student student  404508 Jan 19 00:08 access-log5.txt
-rw-r--r-- 1 student student   45366 Jan 19 00:08 access-log6.txt

grep -r "{"
access-log4.txt:198.205.17.200 - - [23/Apr/2013:09:42:46 -0700] "GET /images/thisweek.png HTTP/1.1" 200 1683 "http://www.random-site.com/dallas/" "Mozilla/4.0 OS{e20c3a1568896ff255b4ddd594c8d2c2}

```

##  PEN-200: 3.3.6 Text Searching and Manipulation

Exercises

(To be performed on your own Kali VM - Reporting is required for these exercises)

1. Using /etc/passwd, extract the user and home directory fields for all users on your Kali machine for which the shell is set to /bin/false. Make sure you use a Bash one-liner to print the output to the screen. The output should look similar to Listing 26 below:

```shell
kali@kali:~$ **YOUR COMMAND HERE**
The user mysql home directory is /nonexistent
The user Debian-snmp home directory is /var/lib/snmp
The user speech-dispatcher home directory is /var/run/speech-dispatcher
The user Debian-gdm home directory is /var/lib/gdm3
```

Answer
```shell
sudo cat /etc/passwd | grep false | cut -d : -f 1,6 | awk -F ":" '{print "The user", $1, "home directory is", $2 }'
The user tss home directory is /var/lib/tpm
The user speech-dispatcher home directory is /run/speech-dispatcher
The user lightdm home directory is /var/lib/lightdm
The user mysql home directory is /nonexistent
The user Debian-snmp home directory is /var/lib/snmp

```

2. Copy the /etc/passwd file to your home directory (/home/kali).

```shell
cp /etc/passwd $HOME/passwd
```

3. Use cat in a one-liner to print the output of the /kali/passwd and replace all instances of the "Gnome Display Manager" string with "GDM".

```shell
cat passwd | grep -i color | sed 's/colord colour management/CCM/' 
colord:x:119:127:CCM daemon,,,:/var/lib/colord:/usr/sbin/nologin
```

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

4. Extract the 13th field from the file located on the Kali VM #1 in the challenge folder in order to solve this problem challenge. Try to get the complete flag with a single one-liner (i.e. with no extra processing needed to submit).

```shell
cat field_of_flags.csv | cut -d "," -f 13 | awk 1 ORS='' 
The flag is: OS{24642cda394480eaee599cdc49c7b811}   
```

5. There's a pile of assorted flags in the VM #2 /challenge folder. It's nice to have a lot of flags, but the right one is the shortest one. Sort the pile in order to find it.

```shell
awk '{print length, ",", $1}' values_and_flags.txt | sort -n | head
45 , OS{cf348f625a8766b3283e5240a8465264},16042054
47 , {{01d60354e52f58447db2a8af1c9d6ebae}},491110537
47 , {{027e41d8e5994d76135f0ad0743317afa6}},81920235
47 , {{04ba9c8da326f89abd5bed81dfd11cb8fc}},40768265
47 , {{0665bbe786949ca0b0a5d8a0ada3e29508}},71957423
48 , {{0
48 , {{0165345fe91945653221c5f884b5ccb036}},659993126
48 , {{0170171bef9ff97cba50b9820b8339530}},2890248548
48 , {{03ad25d49b2f65899747962cbcd3556980}},721195172
48 , {{04979c95a97e1207056c4a77469e3e552}},3215387382
```

##  PEN-200: 3.5 Comparing files

Exercises

(To be performed on your own Kali VM - Reporting is required for these exercises)

1. Download the archive from the following URL https://offensive-security.com/pwk-files/scans.tar.gz

```shell
curl -o scans.tar.gz https://offensive-security.com/pwk-files/scans.tar.gz
gzip -d scans.tar.gz
tar -xf scans.tar

--suppress-common-lines

```

2. This archive contains the results of scanning the same target machine at different times. Extract the archive and see if you can spot the differences by diffing the scans.

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

3. It takes different strokes for different folks to get good at comparing files with the command line. On the VM #1 in the /challenge/ folder, you will find two access-logs, access-logA and access-logB. Spot the differences (and ONLY the differences) in order of appearance in their respective files to get this flag.

```shell

diff access-logA.txt access-logB.txt | grep "<\|>" | cut -d " " -f 2 | awk 1 ORS=""
OS{076dfd984d81695ea16b079677260321}

```

##  PEN-200: 3.6 Managing processes

 Exercises

(To be performed on your own Kali VM - Reporting is required for these exercises)

1. Find files that have changed on your Kali virtual machine within the past 7 days by running a specific command in the background.

```shell
find / -atime 7 2>/dev/null 1> find.txt &    
```

2. Re-run the previous command and suspend it; once suspended, background it.

```shell
find / -atime 7 2>/dev/null 1> find.txt &
ctrl+z
bg    
```

3. Bring the previous background job into the foreground.

4. Start the Firefox browser on your Kali system. Use ps and grep to identify Firefox's PID.

```shell
firefox
```

5. Terminate Firefox from the command line using its PID.

```shell
ps ea | grep firefox
   2533 ?        Sl     1:17 /usr/lib/firefox-esr/firefox-esr
   2657 ?        Sl     0:00 /usr/lib/firefox-esr/firefox-esr -contentproc -parentBuildID 20221205141915 -prefsLen 31555 -prefMapSize 219100 -appDir /usr/lib/firefox-esr/browser 2533 true socket
   2715 ?        Sl     0:01 /usr/lib/firefox-esr/firefox-esr -contentproc -childID 1 -isForBrowser -prefsLen 31696 -prefMapSize 219100 -jsInitLen 277276 -parentBuildID 20221205141915 -appDir /usr/lib/firefox-esr/browser 2533 true tab
   2859 ?   

kill 2533
```

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

6. We need your help to complete some dirty jobs. These jobs are available on the VM #1 within the /challenge folder. Follow the instructions given by the dirty-jobs program to learn how to complete these jobs and get the flag.

```shell

ctrl+z wont work in terminal???
https://unix.stackexchange.com/questions/322976/ctrlz-and-fg-with-ssh-why-doesnt-it-work

```

##  PEN-200: 3.7.3 File and command monitoring

 Exercises

(To be performed on your own Kali VM - Reporting is required for these exercises)

1. Start your apache2 web service and access it locally while monitoring its access.log file in real-time.

```shell
# start the service
sudo systemctrl start apache2

# watch traffic on the apache2 access log
sudo watch -n 5 cat /var/log/apache2/access.log
```

2. Use a combination of watch and ps to monitor the most CPU-intensive processes on your Kali machine in a terminal window; launch different applications to see how the list changes in real time.

```shell
# top 3 processes by cpu usage
ps aux --sort -%cpu | head -n 4

watch -n 1 ps aux --sort -%cpu | head -n 4  

```

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

3. ou will find watchman on the VM #1 in the /challenge folder. Use this program to keep watch over the world. Maybe, over time, your actions will make a difference (and you will find the flag). The change you will make is brief. Check out the man page for any further tips.

```shell

watch -n 5 -d -p "./watchman && cat flag.txt"   

# was able to screenshot and manually type in the flag
OS{e0995f13eb7fb8cceb9e8ce0184a9f17}

```

## PEN-200: 3.8.4 Downloading files

Exercises

(To be performed on your own Kali VM - Reporting is required for these exercises)

1. Download the PoC code for an exploit from https://www.exploit-db.com using curl, wget, and axel, saving each download with a different name.

```shell
# get the oldest exploit from 1988 https://www.exploit-db.com/exploits/19028

curl -o 19028.curl $EXPLOIT 
wget -o 19028.wget $EXPLOIT
axel -o -n 10 19028.axel $EXPLOIT


```


(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

We made a cool website dedicated to C Web. It is available on VM #1 on port 80 and can be surfed through curl as well.

```shell
echo $IP
192.168.153.52

curl $IP
OS{e452f1ec9cf139b011b1e5bc2639e1ed}

```
## PEN-200: 3.9 Customizing bash

1. Create an alias named ".." to change to the parent directory and make it persistent across terminal sessions.

```shell
alias ".."="cd ../"

```

Permanently configure the history command to store 10000 entries and include the full date in its output.

