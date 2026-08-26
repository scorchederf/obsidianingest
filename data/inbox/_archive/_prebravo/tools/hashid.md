---
id: tools-hashid
tags: ["kali", "tool", "hashid", "hashes", "python", "crack"]
created: 2023-01-12 11:56
---
# tools-hashid

backlinks: [[]]

---

Identify the different types of hashes used to encrypt data and especially passwords.

hashID is a tool written in Python 3.x which supports the identification of over 175 unique hash types using regular expressions. It is able to identify a single hash or parse a file and identify the hashes within it. There is also a nodejs version of hashID available which is easily set up to provide online hash identification.

https://www.kali.org/tools/hashid/


## Examples
What type is hash is this (string)
```shell
hashid '$P$8ohUJ.1sdFw09/bMaAQPTGDNi2BIUt1'
Analyzing '$P$8ohUJ.1sdFw09/bMaAQPTGDNi2BIUt1'
[+] Wordpress ≥ v2.6.2
[+] Joomla ≥ v2.5.18
[+] PHPass' Portable Hash
```
What are the hashes in the file hashes.txt
```shell
hashid hashes.txt

--File 'hashes.txt'--
Analyzing '*85ADE5DDF71E348162894C71D73324C043838751'
[+] MySQL5.x
[+] MySQL4.1
Analyzing '$2a$08$VPzNKPAY60FsAbnq.c.h5.XTCZtC1z.j3hnlDFGImN9FcpfR1QnLq'
[+] Blowfish(OpenBSD)
[+] Woltlab Burning Board 4.x
[+] bcrypt
--End of file 'hashes.txt'--
```