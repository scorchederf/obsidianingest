---
id: tools-grep
tags: ["linux", "tool", "grep", "search"]
created: 2023-01-12 11:56
---
# tools - grep

backlinks: [[]]

---

- -r recursive
- -i case insensitive


- count the number of ip addresses in log file

```shell
#example data
201.21.152.44 - - [25/Apr/2013:14:05:35 -0700] "GET /favicon.ico HTTP/1.1" 404 89 "-" "Mozilla/S.@ (Windows NT 6.2; WOW64) AppleWebKit/537.31 (KHTML, like Geck0) Chrome/26.0.1410.64 Safari/537.31" "random-site.com"
70.194.129.34 - - [25/Apr/2013:14:10:48 -0700] "GET /include/jquery.jshowoff.min.js HTTP/1.1" 200 2553 "http://www.random-site.com/" "Mozilla/5.0 (Linux; U; Android 4.1.2; en-us; SCH-I535 Build/JZ0S4k) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30" "www.random-site.com"
70.194.129.34 - - [25/Apr/2013:14:10:48 -0700] "GET /include/main.css HTTP/1.1" 304 - "http://www.random-site.com/" "Mozilla/S.0 (Linux; U; Android 4.1.2; en-us; SCH-I535 Build/JZ0S4K) AppleWebKit/534.30 (KHTML, Like Gecko) Version/4.0 Mobile Safari/534.30" "www.random-site.com"
70.194,129.34 - - [25/Apr/2013:14:10:49 -0700] "GET /images/menu/2ny.png HTTP/1.1" 200 2732 "http: //www.random-site.com/" "Mozilla/5.0 (Linux; U; Android 4.1.23 en-us; SCH-I535 Build/JZ0S4K) AppleWebKit/534.30 (KHTML, Like Gecko) Version/4.0 Mobile Safari/534.30" "www.random-site.com"
70.194,129.34 - - [25/Apr/2013:14:10:58 -0700] "GET /chicago/ HTTP/1.1" 200 7451 “http: //www.random-site.com/" "Mozilla/S.0 (Linux; U; Android 4.1.2; en-us; SCH-I535 Build/JZ0S4K) AppleWebKit/534.30 (KHTML, Like Gecko) Version/4.0 Mobile Safari/534.30" "random-site.com"
70.194,129.34 - - [25/Apr/2013:14:10:58 -0700] "GET /include/jquery.js HTTP/1.1" 304 - "http: //random-site.com/chicago/" "Mozilla/5.0 (Linux; U; Android 4.1.2;en-us; SCH-I535 Build/JZ054k) AppleWebKit/534.30 (KHTML, Like Gecko) Version/4.0 Mobile Safari/534.30" "random-site.com"
70.194,129.34 - - [25/Apr/2013:14:10:59 -0700] "GET /images/header.png HTTP/1.1" 200 13610 "http: //random-site.com/chicago/" "Mozilla/S.@ (Linux; U; Android 4.1.2; en-us; SCH-I535 Build/JZ0S4K) AppleWebKit/534.30 (KHTML, Like Gecko) Version/4.0 Mobile Safari/534.30" "random-site.com"
70.194,.129.34 - - [25/Apr/2013:14:11:00 -@700] "GET /favicon.ico HTTP/1.1" 404 89 "http: //random-site.com/chicago/" "Mozilla/S.0 (Linux; U; Android 4.1.2; en-uSs; SCH-I535 Build/JZ054K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30" "random-site.com'
88.112.192.2 - - [25/Apr/2013:14:11:13 -0700] "GET / HTTP/1.1" 200 4135 "http: //startupli fe. fi /you-know-you-are-in-san-francisco-when-your-favorite-spare-time-activities-include-eating-or-drinking/" "Mozilla/S.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.31 (KHTML, Like Gecko) Chrome/26.0.1410.65 Safari/537.3
88.112.192.2 - - [25/Apr/2013:14:11:14 -0700] "GET /include/jquery.jshowoff.min.js HTTP/1.1" 200 6227 "http://www.random-site.com/" "Mozilla/5.@ (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.65 Safari/537.31" "www.random-site.com"

 

cat access.log | cut -d " " -f 1 | sort | uniq -c | sort -urn
1038  208.68.234.99
 559  208.115.113.91
  21  99.127.177.95
  10  70.194.129.34

```shell

#filter the ip address and sort
cat access.log | grep '208.68.234.99' | grep '/admin' | sort -u

208.68.234.99 - - [25/Apr/2013:14:10:59 -0700] "GET //admin HTTP/1.1" 401 742 //ommitted
208.68.234.99 - - [25/Apr/2013:14:11:18 -0700] "GET //admin HTTP/1.1" 200 575 //ommitted

# the attacker has tried to brute force the //admin page and was receiving 401''s until they managed to guess
# the password and got a 200 status code 

```