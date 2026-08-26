---
title: osTicket
aliases: []
tags:
- topic/osTicket
- tool/osTicket
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: osTicket.md
related_tools:
- '[[osTicket]]'
related_techniques: []
related_tactics: []
related_services: []
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# osTicket

## Description
- osTicket is an open-source support ticketing system comparable to Jira, OTRS, Request Tracker, and Spiceworks.
- It is a platform-independent web-based application compatible with all operating systems.
- Required components for installation and running:
  - Web Server: Apache or IIS
  - PHP Versions: 8.0-8.2 for osTicket 1.17 Series, 8.1-8.2 for osTicket 1.18 Series
  - MySQL Database: 5.5+
- The application is highly maintained and serviced, with few known vulnerabilities and exploits.
- It is open-source.

## Discovery
- Creates `OSTSESSID` cookie when visiting.
- Check the page footer for 'Powered By osTicket' or 'Support Ticket System'.

## Social Engineering
- Core function: Inform company employees about problems to be solved.
- Use social engineering to create a problem and contact company staff.
- Staff and administrators try to reproduce significant errors to find the core of the problem.
- Involve other technical department staff in email correspondence.
- Potential for new email addresses and usernames for OSINT or other company services.
- Check dehashed for user credentials.

## Attack
- Exposed services like company Slack or GitLab require valid company email addresses.
- Support emails such as `support@inlanefreight.local` are available in online support portals.
- Temporary email created during ticket registration.
- If the company correlates ticket numbers with emails, any email sent to the registered email (`940288@inlanefreight.local`) would show up in the helpdesk software.
- Use external portals like Wiki, chat services, or Git repositories to register an account and receive a sign-up confirmation email.

## References
- https://osticket.com/

