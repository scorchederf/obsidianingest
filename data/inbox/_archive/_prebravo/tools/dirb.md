---
id: tools-apache2
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-dirb

backlinks: [[]]

sources:

---

DIRB is a web content scanner that uses a wordlist to find directories and pages by issuing requests to the server. DIRB can identify valid web pages on a web server even if the main index page is missing.

- flags
  - -r          non recursive
  - -z 10       millisecond gap between requests
  - -X          specifies a csv list of file extension -X ".php,.bak"
  - -o          output file
  - -a          custom user agent eg -a "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"
  - -p          proxy
  - -u "username:password"          dirb will include the username:password string encoded in base64.
  -  -c "COOKIE:ABC"



```shell
# -r to scan non-recursively, and -z 10 to add a 10 millisecond delay to each request
dirb http://www.megacorpone.com -r -z 10

# watch traffic on the apache2 access log
sudo watch -n 5 cat /var/log/apache2/access.log

```
