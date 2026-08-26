---
aliases:
tags:
source:
  - https://osticket.com/
desc: is an open-source support ticketing system comparable to Jira, OTRS, Request Tracker, and Spiceworks
---
- osTicket is a platform-independent web-based application, meaning it is compatible with all operating systems. To install and run osTicket the following components are required;
	- Web Server: Apache or IIS
	- PHP Versions:  
		- osTicket 1.17 Series: 8.0-8.2  
		- osTicket 1.18 Series: 8.1-8.2  
	- MySQL Database: 5.5+
- osTicket is a web application that is highly maintained and serviced. If we look at the CVEs found over decades, we will not find many vulnerabilities and exploits that osTicket could have. 
- the application is open-source


# discovery

- creates `OSTSESSID` cookie when visiting
- check the page footer for "Powered By osTicket" or "Support Ticket System"

# social engineering

- user input 
	- the core function of osTicket is to inform the company's employees about a problem so that a problem can be solved with the service or other components
		- use social engineering to create a problem and "play dumb" and contact the company's staff.
- As staff or administrators, they try to reproduce significant errors to find the core of the problem. Processing is finally done internally in an isolated environment that will have very similar settings to the systems in production. Suppose staff and administrators suspect that there is an internal bug that may be affecting the business. In that case, they will go into more detail to uncover possible code errors and address more significant issues.
- Depending on the depth of the problem, it is very likely that other staff members from the technical departments will be involved in the email correspondence. This will give us new email addresses to use against the osTicket admin panel (in the worst case) and potential usernames with which we can perform OSINT on or try to apply to other company services.
- check dehashed for user credentials
	- other than an exploit, this is the best approach


# attack

- https://www.cvedetails.com/vendor/2292/Osticket.html
- - Suppose we find an exposed service such as a company's Slack server or GitLab, which requires a valid company email address to join. Many companies have a support email such as `support@inlanefreight.local`, and emails sent to this are available in online support portals that may range from Zendesk to an internal custom tool. Furthermore, a support portal may assign a temporary internal email address to a new ticket so users can quickly check its status.
	- ![[new_ticket-20251209082846308.png]]
	- temporary email created
	  ![[ticket_email-20251209082846940.png]]
	- Now, if we log in, we can see information about the ticket and ways to post a reply. If the company set up their helpdesk software to correlate ticket numbers with emails, then any email sent to the email we received when registering, `940288@inlanefreight.local`, would show up here. With this setup, if we can find an external portal such as a Wiki, chat service (Slack, Mattermost, Rocket.chat), or a Git repository such as GitLab or Bitbucket, we may be able to use this email to register an account and the help desk support portal to receive a sign-up confirmation email.
	- 


