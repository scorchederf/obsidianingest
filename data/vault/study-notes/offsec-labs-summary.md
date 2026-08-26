---
title: Offsec Labs Summary
aliases: []
tags:
- topic/offsec-labs
- topic/bash
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: lab.md
related_tools:
- '[[bash]]'
- '[[ss]]'
- '[[systemctl]]'
- '[[nano]]'
- '[[ls]]'
- '[[cat]]'
- '[[sort]]'
- '[[history]]'
- '[[xargs]]'
- '[[xxd]]'
- '[[gzip]]'
- '[[tar]]'
- '[[grep]]'
- '[[cut]]'
- '[[awk]]'
- '[[sed]]'
- '[[diff]]'
- '[[find]]'
- '[[ps]]'
- '[[kill]]'
- '[[curl]]'
- '[[watch]]'
- '[[wget]]'
- '[[axel]]'
related_techniques:
- '[[t1003]]'
- '[[t1089]]'
- '[[t1059]]'
- '[[t1132]]'
related_tactics:
- '[[t1003]]'
- '[[t1089]]'
- '[[t1059]]'
- '[[t1132]]'
- '[[Monitoring]]'
related_services:
- '[[apache2]]'
- '[[ssh]]'
- '[[ftp]]'
- '[[http]]'
- '[[https]]'
- '[[smtp]]'
- '[[mysql-1787747546]]'
- '[[nginx]]'
- '[[web-server]]'
- '[[web-technologies]]'
related_os:
- '[[etc-passwd]]'
- '[[/home/kali/sortedpasswd]]'
- '[[/challenge/end]]'
- '[[/challenge/to-redirect-and-search]]'
- '[[/home/student/access-logs.tar.gz]]'
- '[[/home/student/logs/access-logs.tar.gz]]'
- '[[/home/student/logs/access-log0.txt]]'
- '[[/home/student/logs/access-log1.txt]]'
- '[[/home/student/logs/access-log2.txt]]'
- '[[/home/student/logs/access-log3.txt]]'
- '[[/home/student/logs/access-log4.txt]]'
- '[[/home/student/logs/access-log5.txt]]'
- '[[/home/student/logs/access-log6.txt]]'
- '[[/var/lib/tpm]]'
- '[[/var/lib/snmp]]'
- '[[/var/run/speech-dispatcher]]'
- '[[/var/lib/lightdm]]'
- '[[/var/lib/colord]]'
- '[[/home/kali/passwd]]'
- '[[field_of_flags.csv]]'
- '[[values_and_flags.txt]]'
- '[[access-logA.txt]]'
- '[[access-logB.txt]]'
- '[[/challenge/scans.tar.gz]]'
- '[[/challenge/access-logA.txt]]'
- '[[/challenge/access-logB.txt]]'
- '[[var-log-apache2-access-log]]'
- '[[/challenge/watchman]]'
- '[[flag-txt]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Offsec Labs Summary

## Bash Environment Exercises
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

3. Start the VM #1 and look around.

```shell
env
SSH_CONNECTION=192.168.119.166 44858 172.18.0.2 22
FLAG=OS{ea7d6c90d271ed27361f4e84b38a9163}
TERM=xterm-256color
LESS_TERMCAP_mb=
LESS_TERMCAP_me=
```

4. Navigate to the /challenge folder on the VM #2 and find the flag.

```shell
ls -trh | tail -1
/challenge/a62D3E4D1F743C7479508A475F8ECD9045332751B5189EEEEC0DD559D73F82F458898CAEDE62C56E35C0E686E10BD1DCA708E3F1628D11C2CE1664B4C983908A88853E41573597A74E4A29F/.b37C599C C6745117 F0462E876E  7257E C1FADA1135B3 5B9F3BE341798FBF6 F64CA80B9DCB79CAAB 6887131A25BB5F9D626215568A74CDD4AD7F829CB 162431C05E9C2CA336C0762/cfcf\eCbaeaAEfadBgFb dffg bFFCgc'aceFFEGEf'C\BB'eEadd 'ddAcdbcddg dBfEBAFDGaDAEBDgCE G\efebfgGEAeAE'fcAe AE E fBfgfA ccdCdECAcgBFfA 'e'cFeaEdGdbBFD\Ddg/

## Text Searching and Manipulation
Exercises

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
cat field_of_flags.csv | cut -d "," -f 13 | awk 1 ORS='' The flag is: OS{24642cda394480eaee599cdc49c7b811}
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

## Comparing Files
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
diff access-logA.txt access-logB.txt | grep "<"| grep ">" | cut -d " " -f 2 | awk 1 ORS="" OS{076dfd984d81695ea16b079677260321}
```

## Managing Processes
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

## File and Command Monitoring
Exercises

(To be performed on your own Kali VM - Reporting is required for these exercises)

1. Start your apache2 web service and access it locally while monitoring its access.log file in real-time.

```shell
# start the service
sudo systemctl start apache2
```

## Monitoring Traffic
To monitor traffic on the Apache2 access log, use the following command:

```shell
sudo watch -n 5 cat /var/log/apache2/access.log
```

To monitor the most CPU-intensive processes in real time, use the following commands:

```shell
# top 3 processes by cpu usage
ps aux --sort -%cpu | head -n 4

watch -n 1 ps aux --sort -%cpu | head -n 4
```

These commands should be performed with the Topic Exercises VMs under 'Resources'.

## Using Watchman
On VM #1, find the watchman program in the /challenge folder. Use the following command to monitor changes and potentially find a flag:

```shell
watch -n 5 -d -p "./watchman && cat flag.txt"
```

After running the command, a screenshot was taken and the flag was manually typed in: `OS{e0995f13eb7fb8cceb9e8ce0184a9f17}`.

## Downloading Files
Download the PoC code for an exploit from Exploit-DB using the following commands:

```shell
# get the oldest exploit from 1988 https://www.exploit-db.com/exploits/19028
curl -o 19028.curl $EXPLOIT
wget -o 19028.wget $EXPLOIT
axel -o -n 10 19028.axel $EXPLOIT
```

The IP address of the VM is `192.168.153.52`. Use curl to access the website and retrieve the flag:

```shell
echo $IP
192.168.163.52
curl $IP
OS{e452f1ec9cf139b011b1e5bc2639e1ed}
```

Reporting is required for these exercises.

## Customizing Bash
Create an alias to change to the parent directory and make it persistent across terminal sessions:

```shell
alias '..'='cd ../'
```

Permanently configure the history command to store 10000 entries and include the full date in its output:

```shell
HISTSIZE=10000
HISTFILESIZE=10000
export HISTTIMEFORMAT='%F %T ' 
```

These settings should be added to the .bashrc file.

