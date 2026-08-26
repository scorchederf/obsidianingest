---
id: offsec labs
tags: [offsec, labs]
created: 2023-01-13 19:19
---
# offsec labs

backlinks: [[snippets-bash]]

sources:

---

## PEN-200: 2.4.4 Getting Comfortable with Kali Linux

Exercises

(To be performed on your own Kali VM - Reporting is required for these exercises)

Use man to look at the man page for one of your preferred commands.

```
man tmux
```

Use man to look for a keyword related to file compression.

```
man -f compression  
compression: nothing appropriate.

man -f zip
zip (1)              - package and compress (archive) files
```

Use which to locate the pwd command on your Kali virtual machine.

```
which pwd
pwd: shell built-in command
```

Use locate to locate wce32.exe on your Kali virtual machine.

```
locate wce32.exe
/usr/share/windows-resources/wce/wce32.exe
```

Use find to identify any file (not directory) modified in the last day, NOT owned by the root user and execute ls -l on them. Chaining/piping commands is NOT allowed!

```
#   -type f means type is file
#   -mtime 1 modified in the last day
#   ! -user root    not the root user
#   -exec ls -la {} \;      exec ls -la and pipe to console
#   2>/dev/null     very very noisy with permission errors

find -type f -mtime 1 ! -user root -exec ls -la {} \; 2>/dev/null 
```

```shell
#   example results
-rw-r--r-- 1 kali kali 127033 Jan 12 19:39 ./home/kali/Documents/git/bravo/raw/img/2023-01-12-04-39-16.png
-rw-r--r-- 1 kali kali 127033 Jan 12 19:39 ./home/kali/Documents/git/bravo/raw/img/2023-01-12-04-39-15.png
-rw-r--r-- 1 kali kali 568 Jan 12 19:06 ./home/kali/Documents/git/bravo/mitre/defenseevasion/defender-delete-signatures.md
-rw-r--r-- 1 kali kali 1840 Jan 12 19:06 ./home/kali/Documents/git/bravo/mitre/privilegeescalation/linux-suid.md
-rw-r--r-- 1 kali kali 1137 Jan 12 19:06 ./home/kali/Documents/git/bravo/mitre/exfiltration/shell-base64.md
-rw-r--r-- 1 kali kali 658 Jan 12 19:06 ./home/kali/Documents/git/bravo/mitre/credentialaccess/windows-wificredentials.md
-rw------- 1 kali kali 3747 Jan 12 19:32 ./home/kali/.cache/thumbnails/normal/3ab00b3f052e1346d85189a677068347.png

```

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

6. On the Kali VM #1, a flag.txt is missing. Can you find discover it?


```
find / -iname flag.txt -type f
locate flag.txt
/var/tpm/lost/files/flag.txt

└─$ cat /var/tpm/lost/files/flag.txt
OS{674115f423d8bc145e6c01083ff589e7}
```

Another flag is missing on the Kali VM #2. The file name is unknown, but we do know it is exactly 64 bytes in size. The flag is also base64 encoded. For each file you find that matches 64 bytes in size, decode the file to find the flag. Try to solve this challenge without chaining/piping commands.

```
find / -type f -size 64c -exec base64 -d  {} \; 2>/dev/null
��\�)���\������鿶)��OS{bdaee473f78df92255c225f88ae1139e}    

```

We created this amazing new game, Pan Mages - the most awesome mage game in the world! It is in the very early stages of development, but you might want to check it out. Run panmages on the Kali VM #3 to learn more about this amazing new program game.

```
panmages
man pagemages
OS{cb42298229e0fefb38082db5bb5821ba}
```

Since Pan Mages has so much hype, some die-hard fans went ahead and already started the development of a game guide for the most awesome mage game ever! Since the game is still lacking in actual content, there was not much for these fans to do, but they did create a reference manual for their guide. Unfortunately, they were throwing around so many apropos awesome names for this guide, but we forgot what they settled on. Find the flag on the Kali VM #4.

```
find / -name "*mage*"
/usr/games/mageguide
man mageguide
OS{a20f72a4a09b3a349753fbd07e9329af}

```

After creating the initial reference manual for the game guide, these super fans decided to push forward with the creation of the actual game guide. They settled on pmgg as the game guide name. Run this command pmgg on Kali VM #5 and then use a command to determine which program is being run when you execute the command. .

```
which pmgg
/usr/local/games/pmgg

cd /usr/local/games/ && ls -la
-rwxr-xr-x 1 root root 14416 Jan 17 08:14 pmgg
-rw-r--r-- 1 root root   136 Jan 17 08:14 pmgg-notes.txt

cat pmgg-notes.txt
FUTURE PLANS FOR PANMAGES GAME GUIDE

1. Improve awesomeness of title
2. ?
3. Profit

The flag is:
OS{2486a9bde14947f3ba4c790e5d0075f8}
```


## PEN-200: 2.5.3 Managing Kali Linux Service

 Exercises

(To be performed on your own Kali VM - Reporting is not required for these exercises)

- Practice starting and stopping various Kali services.
- Enable the SSH service to start on system boot.

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

Find the location of the try-harder.mp3 file and then, start an HTTP service on the Kali VM #1. Next, serve this song so that it is available for download at http://127.0.0.1/try-harder.mp3. Once complete, run try-harder-web-service to verify the completion of this task and get your flag.

```
find / try-harder
/challenge
/challenge/try-harder.mp3

find / -iname "try-harder-web-service" 2>/dev/null
/usr/bin/try-harder-web-service

cd /var/www/html
cp /challenge/try-harder.mp3 try-harder.mp3

ls -la
-rw-r--r-- 1 root    root      10701 Nov 30  2021 index.html
-rw-r--r-- 1 root    root    8200276 Jan 17 09:00 try-harder.mp3

/usr/bin/try-harder-web-service 
 * Verifying that a service is listening at 127.0.0.1 on port 80.
 * Attempting to download try-harder.mp3 via HTTP from 127.0.0.1 Port 80.
Great job. Here is your flag: 
OS{269c34cb919e7e1f4042a1ae3b0526bb}
Press any key to continue...

```


## PEN-200: 2.6.7 Searching, Installing, and Removing Tools

 Exercises

(To be performed on your own Kali VM - Reporting is not required for these exercises)

- Take a snapshot of your Kali virtual machine (optional).
- Search for a tool not currently installed in Kali.
- Install the tool.
- Remove the tool.
- Revert Kali virtual machine to previously taken snapshot (optional).

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

We have developed a special package for you just to help with PWK! (note - this package does not actually help). Install pwkpackage_1.0-1.deb that resides on your Kali VM #1 in the /challenge folder and then run pwkpackage to solve this challenge.

```shell
sudo dpkg -i /challenge/pwkpackage_1.0-1.deb
Selecting previously unselected package pwkpackage.
(Reading database ... 11509 files and directories currently installed.)
Preparing to unpack .../challenge/pwkpackage_1.0-1.deb ...
Unpacking pwkpackage (1.0-1) ...
Setting up pwkpackage (1.0-1) ...

pwkpackage
Great job installing the package. Here is your flag: 
OS{84fe6a63ba81eb0cbf72df81a88d7fa5}
```

Turns out, that special package was not as special as we initially thought. On Kali VM #2, go ahead and uninstall pwkpackage_1.0-1.deb. Once complete, run a-special-package-2 from the /challenge folder to verify you removed pwkpackage_1.0-1.deb and get your flag.

```shell
# bit trickier as we dont have permission to exec sudo 
# or do we
sudo -l
Matching Defaults entries for student on 1fab16db4c8a:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User student may run the following commands on 1fab16db4c8a:
    (ALL) NOPASSWD: /usr/bin/apt purge pwkpackage

#need to provide direct path exec
/usr/bin/apt purge pwkpackage
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  pwkpackage*
0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] yes
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
(Reading database ... 11512 files and directories currently installed.)
Removing pwkpackage (1.0-1) ...
dpkg: warning: while removing pwkpackage, directory '/usr/local' not empty so not removed


./a-special-package-2 
Great job. Here is your flag: 
OS{112261be7da1796f4cd4e985fa88e999}
Press any key to continue...
```
