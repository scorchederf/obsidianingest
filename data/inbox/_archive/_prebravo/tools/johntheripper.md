---
id: tools-johntheripper
tags: ["kali", "tool", "password", "crack"]
created: 2023-01-12 11:56
---
# tools-johntheripper

backlinks: [[]]

sources:
 
- <https://www.csoonline.com/article/3564153/john-the-ripper-explained-an-essential-password-cracker-for-your-hacker-toolkit.html>

---



John the Ripper (JtR) is a password cracking tool originally produced for UNIX-based systems. It was designed to test password strength, brute-force encrypted (hashed) passwords, and crack passwords via dictionary attacks.

alter configuration
/etc/john/john.conf 


## Examples

### Cracking passwd/shadow files (untested)
Because passwd/shadow files are regarded highly confidential for obvious reasons (and stored with restrictive file permissions, 644), the first step is combining these two files into a single file that JtR will work on. This can be done by running the following command:
```shell
umask 077
unshadow /etc/passwd /etc/shadow > shadow.txt 
```
Brute force the shadow.txt file
```shell
sudo john shadow.txt --format=crypt --wordlist=rockyou.txt
sudo john shadow.txt --show
```


### Cracking a zip/rar password protected file
Get the password hash and save to zip.hash
```shell
zip2john test.zip > zip.hash
```
Brute force the password hash
```shell
john --format=zip zip.hash
```


### create wordlist from input
sudo nano /etc/john/john.conf

go to the [List.Rules:Wordlist] section and at the bottom add

# Add two numbers to the end of each password
$[0-9]$[0-9]

john --wordlist=megacorp-cewl.txt --rules --stdout > mutated.txt

