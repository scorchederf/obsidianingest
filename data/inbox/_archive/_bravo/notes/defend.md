

- linux
  - [fail2ban](https://github.com/fail2ban/fail2ban)

- ftp
  - disable anonymous
  - vsftp
    - `hide_ids=YES` will hide user and group ids in directory listings and replaced with "ftp"
      - can reduce the risk of brute forcing with known passwords
[windows persistence](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Persistence.md)


# setting file as hidden
`attrib +h c:\autoexec.bat`

# clear system or security logs
`cmd.exe /c wevtutil.exe cl System`
`cmd.exe /c wevtutil.exe cl Security`


# hide exposed ssid names
no need to expose them to everyone



# Events To Watch For:
- File uploads 
  - Especially with Web Applications, file uploads are a common method of acquiring a shell on a host besides direct command execution in the browser. Pay attention to application logs to determine if anyone has uploaded anything potentially malicious. The use of firewalls and anti-virus can add more layers to your security posture around the site. Any host exposed to the internet from your network should be sufficiently hardened and monitored.
- Suspicious non-admin user actions 
  - Looking for simple things like normal users issuing commands via Bash or cmd can be a significant indicator of compromise. When was the last time an average user, much less an admin, had to issue the command whoami on a host? Users connecting to a share on another host in the network over SMB that is not a normal infrastructure share can also be suspicious. This type of interaction usually is end host to infrastructure server, not end host to end host. Enabling security measures such as logging all user interactions, PowerShell logging, and other features that take note when a shell interface is used will provide you with more insight.
- Anomalous network sessions 
  - Users tend to have a pattern they follow for network interaction. They visit the same websites, use the same applications, and often perform those actions multiple times a day like clockwork. Logging and parsing NetFlow data can be a great way to spot anomalous network traffic. Looking at things such as top talkers, or unique site visits, watching for a heartbeat on a nonstandard port (like 4444, the default port used by Meterpreter), and monitoring any remote login attempts or bulk GET / POST requests in short amounts of time can all be indicators of compromise or attempted exploitation. Using tools like network monitors, firewall logs, and SIEMS can help bring a bit of order to the chaos that is network traffic.
