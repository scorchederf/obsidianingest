Testing Scope
The scope of an assessment is the collection of the client's testing objectives. This includes which applications are being testing, what access the assessors have at the start of the assessment, and the "rules" of the test, including what can and can't be done, such as phishing.1

During an assessment, one or more assessors attempt to identify and exploit misconfigurations and vulnerabilities based on approved objectives. These objectives can be as broad, such as "find all vulnerabilities in the application", or very application-specific, such as "can you capture credit card numbers during the payment flow".

Each assessment has different assumptions, such as the level of application access provided to the assessor or the availability of source code. Some assessment owners might want to limit access or knowledge to better mimic an actual attacker. However, providing information to the assessors can often result in more thorough testing coverage.

Web Application Assessment vs Penetration Test
Some components of web application assessments overlap with penetration tests, but they are not the same thing. Web application assessments tend to have broad objectives on a small group of applications or servers. Penetration tests tend to have very specific goals and include most, if not all, applications, servers, and employees of the organization.

Penetration testers may seek to compromise a web application to gain initial access, in which case, many of the steps performed will be very similar to a web application assessment. However, if part of the scope, the penetration testers could also phish users for initial access to the internal network, completely bypassing external web applications.

Phases of a Web Application Assessment
There are different security testing standards, each of which use different definitions for the phases (or sections) of a security assessment. The different terminologies can be confusing when we compare two different standards. For example, the Penetration Testing Execution Standard (PTES),1, has seven sections. While the OWASP's Web Application Security Testing2 methodology considers testing to be passive or active, with active testing divided into 12 categories.

Regardless of the naming conventions, we will cover web application assessments from five conceptual phases: Enumeration, Vulnerability Discovery, Exploitation, Post-Exploitation, and Reporting.

Web Stacks and Technologies
A web stack1 is the combination of software that runs and supports an application. For web applications, the stack is typically comprised of a server, an operating system, a database, and a programming language. Not every application will fit this definition, but it remains a useful concept.

LAMP2 was one of the most common web stacks for many years. Its components are Linux, Apache, MySQL, and PHP. While we will often encounter applications running on LAMP stacks, it can be difficult to quantify every application's stack. A website that seems to be one application can utilize many different microservices,3 each built with different technologies.

For example, an application might use NodeJS for the main UI, an API written in Python for user authentication, and an API written in Java for handling eCommerce transactions. If the application makes the API calls, rather than our browser, we might not know the different APIs exist.

During enumeration, we're not trying to identify a specific stack. Rather, we should use the concept of a stack as a guiding principle to identify the components of the application that we can interact with. We can do this by inspecting browser requests and server responses for useful information. If we can identify some of the software the application uses, we can search for any known vulnerabilities during the Vulnerability Discovery phase.

There are different actions we can take to try to identify different components of a web application. Let's begin with trying to identify what OS and web server we are enumerating.

The Server and X-Powered-By response headers can leak the server software (including version number), and the application's programming language. Some JavaScript libraries will include an X-Requested-With header on requests. We can inspect server response headers using curl with the -i flag to include headers in the output or with -I to send a HEAD4 request and only display the response headers. However, not all servers will respond to a HEAD request.

Let's review an example.

kali@kali:~$ curl -I http://www.megacorpone.com
HTTP/1.1 200 OK
Date: Tue, 28 Sep 2021 14:40:27 GMT
Server: Apache/2.4.38 (Debian)
Last-Modified: Wed, 06 Nov 2019 15:04:14 GMT
ETag: "390b-596aedca79780"
Accept-Ranges: bytes
Content-Length: 14603
Vary: Accept-Encoding
Content-Type: text/html
Listing 1 - Using curl to inspecting server response

In Listing 1, the server response included a Server header which lists the server software (Apache), version (2.4.38), and operating system (Debian). Not every server will include this header at all or include all three values.

Next we can move on to the programming languages and frameworks used. We can infer these based on file extensions used in URLs, such as .php indicating PHP and .jsp indicating Java. However, with modern frameworks supporting programmatic routing,5 we will often encounter applications that do not include file extensions in their URLs.

Depending on the application, there may be a database we want to examine. Determining an application's database can be difficult unless we can generate an error message that includes an identifier. Most databases use unique error codes, such as Oracle error IDs starting with 'ORA', which we can use to identify the database.

It is more difficult to manually enumerate the operating system of an application without a verbose error message that indicates the OS or a file path. However, many scanning tools, such as nmap,6 can guess a server's OS based on TCP fingerprinting. We will cover automated tools in a later section.

User Enumeration
Once we have an idea of the technologies used by the application, we should try to enumerate the application's users. We may want to target these users with a client-side exploit or attempt to brute force their passwords during the Exploitation phase.

But first we need to get some usernames. Depending on the site, we might be able to crawl the site and harvest public usernames through forums, reviews, or similar functionality. Some web applications will leak valid user accounts through error messages during login, password resets, or account creation. For example, an application might respond with "Invalid username" if the username submitted isn't valid and "Invalid password" if the username is valid, but the password provided is incorrect.

If enterprise users use the web application, we should check for patterns in usernames. Many companies will enforce a standard naming pattern for usernames. If we can reasonably deduce the patterns used in usernames, we can turn a list of employees into a list of usernames.

For the following exercise, consult the listing below.

mark.styles
l.draupadi
kenneth.force
t.paran
Listing 2 - A list of usernames


Automated Enumeration Scans
We've mainly focused on manual enumeration techniques so far. However, automated tools can be very useful during enumeration. Let's discuss a few types of automated scanning tools that are useful during enumeration.

We previously mentioned the network scanner and security tool nmap. While primarily a port scanner, nmap includes a scripting engine and numerous scripts that can be used to test for security misconfigurations and vulnerabilities.

But there is a vast array of other tools. Some tools will "crawl" a site and follow links to discover content. Other tools will attempt to brute-forcing, or "bust", content by sending a series of HTTP requests based on wordlists. This process can generate a lot of traffic. In contrast, a crawler generates traffic similar to normal users. Dirb,1 dirbuster,2 and gobuster3 are all discovery tools.

Vulnerability scanners4 are specialized tools that test applications and servers for security misconfigurations and vulnerabilities. Some of these scanners check for vulnerabilities using signatures, such as service banners or by inspecting the operating system as an authenticated, local user. Other tools will perform a series of tests to identify vulnerabilities rather than relying on a signature alone. One very popular scanner is Nessus.5

Many security tools are multi-purpose. For example, Burp Suite Professional6 includes a scanner that will "crawl" a site (following links to discover all the content) and audit any discovered pages and forms for vulnerabilities. The Community Edition of Burp Suite lacks the crawler and scanner functionality but is still an essential tool for manual testing.


Attack Surface
Once we've enumerated the application and its users, we need to determine its attack surface.1 This is all the components that allows us to enter data, retrieve data, or otherwise interact with the application. We don't need to be authenticated to start looking at the attack surface.

We want to identify any behavior in the application that seems unusual and places where the application processes data we provide. We'll focus on these parts of the application as we move on to the next phase, Vulnerability Discovery.

Automated scans
We briefly covered automated scanning during the enumeration phase. It is important to remember that automated tools can increase our productivity during web application assessments or penetration tests, but we must also understand manual exploitation techniques. Specialized tools, such as SQLmap, have their place in our toolbox. However, tools will not always be available in every situation and may mistakenly identify a vulnerability that doesn't exist, also known as a false positive, or fail to find a vulnerability that does exist, also known as a false negative.

Manual techniques offer greater flexibility and customization. It is important to remember that tools and automation make our job easier, but they don't do the job for us.

Manual Testing
During manual testing, we can use a proxy tool, such as Burp Suite, or the developer tools built-in to our browser to inspect and modify HTTP requests to cause the web application to respond in unusual ways. For example, we might try sending alpha characters in a field that should only contain numbers. If the application response changes based on this input, we might be able to infer how the application handles errors. We can then test the error handling for misconfigurations or vulnerabilities.

In addition to testing how the application handles unexpected input, we should also verify that access controls are working by attempting to access restricted content and test for specific vulnerabilities, such as cross-site scripting (XSS)1 or SQL injection.2 The WEB-200 course covers these types of vulnerabilities in-depth.

Source Code Analysis
Source code analysis is the process of reviewing application source code for misconfigurations and security vulnerabilities. This can be difficult and time-consuming but often identifies impactful vulnerabilities. We can perform code analysis manually or be assisted by static analysis1 software.

As the name suggests, we need actual source code to analyze. We can easily access code for open-source projects. For closed source applications, we may need to decompile2 or reverse engineering3 an application to obtain readable code. These processes can sometimes include artifacts of uncompiled code, but they are useful for providing some recoverable code.

Components with Known Vulnerabilities
If we identify any components of the application's tech stack during enumeration, we can search the Internet for public vulnerabilities, such as those compiled at the CVE Project1 or Exploit Database.2 We may need to modify or update published proof-of-concept exploits, but they can often be a very effective way to compromise an out-of-date system.

We can also check any dependencies for known vulnerabilities if we have access to the application's source code. OWASP Dependency-Check,3 and retire.js4 are two examples of applications that can check dependencies for known vulnerabilities.

Once we have one or more vulnerabilities, we can move on to the Exploitation phase. If our attacks fail in the Exploitation phase, we may need to revisit Vulnerability Discovery.

Authentication Bypass
Authentication1 in web applications occur when users provide something that proves their identity. It could be an API token or the combination of a username and password. Authentication Bypass exploits allow an attacker to gain access to parts of an application or data normally restricted to other users. These attacks might use default credentials developers forgot to change or exploit flaws in the login or password reset flows. For example, an application might use static or easily guessable tokens during password resets. If an attacker can guess or predict the next token, they could be able to reset another user's password and gain access to their account.

Forced Browsing2 vulnerabilities, are another type of authentication bypass that can occur when applications only checks authentication or authorization on certain pages or resources under the assumption that users cannot directly browse or access them. We can identify these resources using web content scanners.

Applications may be vulnerable to Insecure Direct Object References (IDOR)3 if they provide access to a resource, or data, without verifying if the requestor should have access. We can exploit these vulnerabilities to gain access to other users' data or other restricted resources. If an application uses easily guessable identifiers, such as sequential numbers, attackers will have an easier time exploiting this vulnerability.

Session Hijacking
Session Hijacking1, while conceptually similar to Authentication Bypass attacks, rely on gaining access to an existing user's session.2 To use this attack, we might be able to use a cross-site scripting vulnerability to steal a user's session cookie. Applications can also leak session identifiers through URLs.

If attackers can hijack an administrative user's session, they may be able to compromise the entire application and underlying server, depending on the administrative functionality.

Session Hijacking
Session Hijacking1, while conceptually similar to Authentication Bypass attacks, rely on gaining access to an existing user's session.2 To use this attack, we might be able to use a cross-site scripting vulnerability to steal a user's session cookie. Applications can also leak session identifiers through URLs.

If attackers can hijack an administrative user's session, they may be able to compromise the entire application and underlying server, depending on the administrative functionality.

Data Exfiltration
Once attackers have access to an application, they will often attempt to steal sensitive data. This process is referred to as Data Exfiltration.1 Sensitive data might include user credentials, financial information (such as credit card numbers), or other personally identifiable information (PII)2. Attackers can use such data in future attacks or otherwise monetize the data.

Remote Code Execution
The ultimate objective for most attackers is to achieve Remote Code Execution (RCE),1 also referred to as Arbitrary Code Execution. RCE allows attackers to run any command on the server, which frequently leads to the attacker gaining a shell on the server and compromising the server and any application or database running on it.

Once we have successfully exploited an application and gained a shell on the server, we can move into the Post-Exploitation Phase.

Persistence
Once we have access to the server via a shell, we need to make sure we can get a new shell if we lose our connection. Establishing another way to obtain a new shell is known as persistence. Sometimes the initial exploit that created our shell will be repeatable. However, if an exploit required user interaction or other special conditions, we may want an easier way to get a new shell.

If the server has SSH or RDP enabled, we could add our own SSH key or create a new user with RDP privileges. Alternatively, we could add a new service with a vulnerability, but this approach is more inline with a penetration test or red team1 engagement than a web application assessment.

Privilege Escalation
Privilege Escalation1 is the process of exploiting the operating system or an application to gain access to a higher permission user. On a Linux host, we would typically try to become the root user. On a Windows host, we would target the SYSTEM2 user.

Pivoting
In the context of post-exploitation, pivoting is using our access one machine to target another machine. When we compromise a web application and its server, we may be able to access other servers that are behind a firewall or otherwise don't allow remote access. For example, most web applications interact with databases. If the database is running on another server, we usually cannot access it directly as a remote user. However, if we've compromised the web application server, we can likely access the database server from our position on the web application server.

If we do pivot to other systems, we essentially start our attack process over with a new Enumeration phase on the new targets. There may be credentials or other useful material on the compromised server that we can use to easily access other systems, such as the database credentials used by the web application.

Knowing Your Audience
We should always try to adjust our report to match the audience that will be reviewing it. If our client has an internal security team, we may not need to include as many external references as we would to a client with a small IT team and no full-time security team.

Classifying Vulnerabilities
There are many ways to classify and group vulnerabilities. Where possible, we should use industry-standard vulnerability names in our reports so our clients can easily find additional information online if necessary.

Common Weakness Enumeration (CWE)1 is a commonly used list of software and hardware flaws and vulnerabilities. The CWE list has over a thousand entries categorized into several different views. One drawback of using CWEs to classify vulnerabilities is that the items on the list can be either too specific or overly broad. For example, there are several different CWEs for path traversal2 based on the type of payload. Despite these drawbacks, many tools will reference CWEs, so it is important to familiarize ourselves with them.

Another common grouping of vulnerabilities for web applications is the OWASP Top Ten. Refer to the Web Topic for more details on the OWASP Top Ten.

Assessing Impact and Severity
Many organizations will rank vulnerability severities as High, Medium, or Low. Some will also include Critical and Informational. Regardless of which values we use, it is important not to overstate the severity of a vulnerability. We must consider several factors when determining the severity of a vulnerability.

We should think about the impact of an attacker exploiting the vulnerability. How many users would be affected? What type of data could the attacker access? Could the vulnerability disrupt the ability to perform normal business operations?

We also need to consider the likelihood of an attacker exploiting the vulnerability. Is the vulnerability difficult to discover or exploit? Are custom tools or insider knowledge required to exploit the vulnerability?

Vulnerabilities that are highly likely to be exploited and have the potential to impact business operations may be Critical or High. On the other hand, if a vulnerability that is difficult to discover and exploit has little or negligible impact, it might be considered Low.

We can use a framework, like the Common Vulnerability Scoring System (CVSS),1 to remove some of the guesswork of calculating severity. CVSS v3.1 uses fifteen metrics across Base, Temporal, and Environmental groups to calculate a score from 0 to 10. Organizations can use that numeric value as is or translate it to their ranking system of choice.

