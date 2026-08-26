---
id: offsec labs
tags: [offsec, labs]
created: 2023-01-13 19:19
---
# offsec labs

backlinks: [[snippets-bash]]

sources:

---

## PEN-200: 5.7.1 Practical Bash Usage – Example 1

we want to find all the subdomains listed on the main megacorpone.com web page and find their corresponding IP addresses

- retrieve html file, find subdomains and get their ip address

USE HOST INSTEAD OF PING WHICH IS MAGNITUDES FASTER

```shell

wget www.megacorpone.com

list=$( grep "<a href" index.html | awk -F "//" '{print $2}' | awk -F "[/\"]" '{print $1}' | grep "megacorpone.com" | sort -u)

echo $list
admin.megacorpone.com
beta.megacorpone.com
intranet.megacorpone.com
mail2.megacorpone.com
mail.megacorpone.com
siem.megacorpone.com
support.megacorpone.com
syslog.megacorpone.com
test.megacorpone.com
vpn.megacorpone.com
www2.megacorpone.com
www.megacorpone.com



for i in $(echo $list); do; echo $(ping -n -c 1 $i | head -n 1 | cut -d ")" -f 1 | cut -d "(" -f 2) $i; done; 

51.222.169.208 admin.megacorpone.com
51.222.169.209 beta.megacorpone.com
51.222.169.211 intranet.megacorpone.com
51.222.169.213 mail2.megacorpone.com
51.222.169.212 mail.megacorpone.com
51.222.169.215 siem.megacorpone.com
51.222.169.218 support.megacorpone.com
51.222.169.217 syslog.megacorpone.com
51.222.169.219 test.megacorpone.com
51.222.169.220 vpn.megacorpone.com
149.56.244.87 www2.megacorpone.com
149.56.244.87 www.megacorpone.com



for i in $(echo $list); do; echo $(host $i | head -n 1 | cut -d ")" -f 1 | cut -d "(" -f 2) $i; done; 
admin.megacorpone.com has address 51.222.169.208 admin.megacorpone.com
beta.megacorpone.com has address 51.222.169.209 beta.megacorpone.com
intranet.megacorpone.com has address 51.222.169.211 intranet.megacorpone.com
mail2.megacorpone.com has address 51.222.169.213 mail2.megacorpone.com
mail.megacorpone.com has address 51.222.169.212 mail.megacorpone.com
siem.megacorpone.com has address 51.222.169.215 siem.megacorpone.com
support.megacorpone.com has address 51.222.169.218 support.megacorpone.com
syslog.megacorpone.com has address 51.222.169.217 syslog.megacorpone.com
test.megacorpone.com has address 51.222.169.219 test.megacorpone.com
vpn.megacorpone.com has address 51.222.169.220 vpn.megacorpone.com
www2.megacorpone.com has address 149.56.244.87 www2.megacorpone.com
www.megacorpone.com has address 149.56.244.87 www.megacorpone.com

```

## PEN-200: 5.7.2 Practical Bash Usage – Example 2

This windows machine we realize it may be vulnerable to an exploit that we read about that began with the letters a, f, and d but we can't remember the full name of the exploit so we need to search for it using searchsploit. we will need to search https://www.exploit-db.com for "afd windows", download the exploits that match our search criteria, and inspect them until we find the proper one

```bash

searchsploit afd windows -w -t

#my solution
for i in $( searchsploit afd windows -w -t | grep "http" | awk -F "|" '{print $2}' | sed 's/exploits/raw/' ); do; expname=$( $i | cut -d '/' -f 5); wget -q --no-check-certificate $i; done 



#ANSWER
for e in $(searchsploit afd windows -w -t | grep http | cut -f 2 -d "|"); do exp_name=$(echo $e | cut -d "/" -f 5) && url=$(echo $e | sed 's/exploits/raw/') && wget -q --no-check-certificate $url -O $exp_name; done


```

## PEN-200: 5.7.1.3 Practical Bash Usage – Example 3

we are tasked with scanning a class C subnet to identify web servers and determine whether or not they present an interesting attack surface. Port scanning is the process of inspecting TCP or UDP ports on a remote machine with the intention of detecting what services are running on the target and potentially what attack vectors exist.

```bash

# scan
# -A for aggressive scanning, 
# -p to specify the port or port range, 
# --open to only return machines with open ports, and 
# -oG to save the scan results in greppable format
sudo nmap -A -p80 --open 10.11.1.0/24 -oG nmap-scan_10.11.1.1-254


cat nmap-scan_10.11.1.1-254

cat nmap-scan_10.11.1.1-254 | grep 80

cat nmap-scan_10.11.1.1-254 | grep 80 | grep -v "Nmap"

cat nmap-scan_10.11.1.1-254 | grep 80 | grep -v "Nmap" | awk '{print $2}'

for ip in $(cat nmap-scan_10.11.1.1-254 | grep 80 | grep -v "Nmap" | awk '{print $2}'); do cutycapt --url=$ip --out=$ip.png;done

# ---------
cat ./pngtohtml.sh

#!/bin/bash
# Bash script to examine the scan results through HTML.

echo "<HTML><BODY><BR>" > web.html

ls -1 *.png | awk -F : '{ print $1":\n<BR><IMG SRC=\""$1""$2"\" width=600><BR>"}' >> web.html

echo "</BODY></HTML>" >> web.html

# ---------

chmod +x ./pngtohtml.sh

firefox web.html

![Alt text](image-1.png)


```

- For this first challenge, you simply need to write a Bash script that prints Hello World!. The script must print this exactly and nothing else. As described eaarlier, this script must start with #!/bin/bash and be executable. Once created, upload this script to the upload your script to the Kali VM #1 student's home folder and run /challenge/hello_world with your script's location as the first argument to get the flag.

```shell

└─$ cat helloworld.sh                                                                                                                                                                       
#!/bin/bash
echo "Hello World!"

# -----------


/challenge/hello-world /home/student/helloworld. sh                                                                                                                                      
Great job. Here is your flag: 
OS{fcea90e5ff8893e93ed3919579abea70}



```

Create a Bash script that simply prints the name of the script and nothing else. Upload your script to the Kali VM #2 student's home folder and run /challenge/scriptname with your script's location as the first argument to get the flag.

```shell


└─$ cat scriptname.sh 
#1/bin/bash
echo $0

# -------

/challenge/scriptname /home/student/scriptname.sh                                                                                                                                       
Great job. Here is your flag: 
OS{8e26b646fb5e06725cc28833678d9d62}

Press any key to continue...





```

Create a Bash script that prints the argument count (i.e. the number of arguments passed to the Bash script). The script should print exactly This script has _ arguments where the _ (the blank) is the number of arguments and nothing else. Upload or your script to Kali VM #3 student's home folder and run /challenge/argument-count with your script's location as the first argument to get the flag.

```shell


─$ nano -ilm args.sh                                                                                                                                                                       

┌──(student㉿5546df22aa45)-[~]
└─$ chmod +x sar
chmod: cannot access 'sar': No such file or directory

┌──(student㉿5546df22aa45)-[~]
└─$ chmod +x args.sh                                                                                                                                                                        

┌──(student㉿5546df22aa45)-[~]
└─$ args.sh                                                                                                                                                                                 
-bash: args.sh: command not found

┌──(student㉿5546df22aa45)-[~]
└─$ ./args.sh                                                                                                                                                                               
This script has 0 arguments

┌──(student㉿5546df22aa45)-[~]
└─$ ls -la /challenge/                                                                                                                                                                      
total 32
drwxr-xr-x 2 root root  4096 Jan 23 09:24 .
drwxr-xr-x 1 root root  4096 Jan 23 09:24 ..
---s--x--x 1 root root 18808 Jan 23 09:24 argument-count
-r-------- 1 root root    37 Jan 23 09:24 flag.txt

┌──(student㉿5546df22aa45)-[~]
└─$ /challenge/argument-count /home/student/args.sh 
Great job. Here is your flag: 
OS{633001638f95120d66045ba4a59b4547}

Press any key to continue...


┌──(student㉿5546df22aa45)-[~]
└─$ cat args.sh 
#!/bin/bash

echo "This script has $# arguments" 





```

Our files are having an existential crisis. Can you help us determine if they really exist? Create a Bash script that takes a file name as input. If that file exists, print File exists and if not, print File does not exist. Upload your script to the Kali VM #4 student's home folder and run /challenge/do-i-exist with your script's location as the first argument to get the flag.

```bash
─$ cat script.sh 
#!/bin/bash
file=$1
if test -f $file
then
    echo  "File exists"
else
    echo "File does not exist"
fi

# --------


└─$ /challenge/do-i-exist script.sh
Great job. Here is your flag: 
OS{ae2422eb97a09fec1213a0c5ce998b7d}



```

Create a Bash script which extracts JavaScript file names from any access log file. This access-log file will be the first argument to this script. Make sure the file names DO NOT include the path, are unique, and are sorted. Upload your script to the Kali VM #5 student's home folder and run /challenge/access-log with your script's location as the first argument to get the flag.

```bash

┌──(student㉿7abb67989e4c)-[~]
└─$ /challenge/access-log script.sh 
Passed Basic Test Case.
Passed Intermediate Test Case.
Passed Full Test Case.
Great job. Here is your flag: 
OS{3717ef23ee0f0f4762ac481824beb251}

Press any key to continue...


┌──(student㉿7abb67989e4c)-[~]
└─$ cat ./script.sh

# -----------------
#!/bin/bash
file=$1
grep "\.js" $file | cut -d '"' -f 2 | cut -d ' ' -f 2 | cut -d '?' -f 1 | rev | cut -d '/' -f 1 | rev | sort -u

┌──(student㉿7abb67989e4c)-[~]
└─$                                                       



```

Create a short Bash script that will validate a user's membership in a specified group. This script will not take any arguments and, instead, will prompt the user to enter a username and a group. This script will first check to see if the username and group are found on this system (simply exist in their respective /etc/ files). If BOTH ARE NOT FOUND, the script will respond Both are not found - why are you even asking me this?. If ONLY ONE IS FOUND, it will respond One exists, one does not. You figure out which. If BOTH ARE FOUND, it will also check to see if the user is a part of the group. If the USER IS A MEMBER OF THE GROUP, the script will respond Membership valid!; otherwise, it will respond Membership invalid but available to join. To be clear, the script will initially prompt twice for user input (the prompt does not matter) and then only respond once with one of the four specified responses. Once complete, upload your script to the Kali VM #7 student's home folder and run /challenge/group-membership with your script's location as the first argument to get the flag.

Script Functionality Example:

kali@kali:~$ ./group-membership.sh
student
student
Membership valid!

kali@kali:~$ ./group-membership.sh
doesnotexist
alsodoesnotexist
Both are not found - why are you even asking me this?

kali@kali:~$ ./group-membership.sh
student
doesnotexist
One exists, one does not. You figure out which.

kali@kali:~$ ./group-membership.sh
student
root
Membership invalid but available to join.

```bash

┌──(student㉿e4c330c099f6)-[~]
└─$ /challenge/group-membership script.sh 
Great job. Here is your flag: 
OS{59a9566894aa13db4a5cb51bbfd65c69}

Press any key to continue...


┌──(student㉿e4c330c099f6)-[~]
└─$ cat script.sh
#!/bin/bash
 
read -p "" username
read -p "" usergroup

if [ $( getent passwd $username ) ]
then
  userexists=true
else
  userexists=false
fi

if [ $(getent group $usergroup) ]
then
    groupexists=true
else
    groupexists=false
fi

#echo "username $username exists $userexists"
#echo "usergroup $usergroup exists $groupexists"

if [ $userexists = 'true' ] && [ $groupexists = 'true' ]
then
    # check if user already in group
    if [[ $( groups $username | grep $usergroup ) ]]
    then
        echo 'Membership valid!'
    else
        echo 'Membership invalid but available to join.'
    fi
else 
    if [ $userexists = 'false' ] && [ $groupexists = 'false' ]
    then
        echo 'Both are not found - why are you even asking me this?'
    else
        echo 'One exists, one does not. You figure out which.'
     fi 
fi



```


Write a short Bash script to perform a ping sweep of a target IP address range. This script will only print the IP addresses of any valid responses (one IP address per line) and nothing else. To make this script more broadly applicable, you will not hardcode the IP address range. Instead, this script will require three arguments: the first three octets of the IP address, the starting value of the last octet, and the ending value of the last octet (see below for examples). You DO NOT need to do any error checking (but feel free to do so). Upload your script to the Kali VM #8 student's home folder and run /challenge/ping-sweep with your script's location as the first argument to get the flag.

NOTE: you can utilize a portion of the 127.0.0.0/8 local address space as a test example for this exercise.

Script Functionality Example:

kali@kali:~$ ./ping-sweep.sh 127.0.0 1 4
127.0.0.1
127.0.0.2
127.0.0.3
127.0.0.4

```shell
┌──(student㉿c2c7a8122892)-[~]
└─$ /challenge/ping-sweep script.sh
Starting test 1.
Starting test 2 - this one is longer and may take several seconds depending on your script.

Great job. Here is your flag: 
OS{1b1c1eb99c50a970b9e7302b1cf243e9}

Press any key to continue...

┌──(student㉿c2c7a8122892)-[~]
└─$ cat ./script.sh
#!/bin/bash

threeocts=$1
start=$2
end=$3


for ip in $(seq $start $end); 
do 
    ip="$threeocts.$ip"
    if ping -c 1 $ip &> /dev/null
    then
        echo $ip
    #   else
    #   echo "error"
    fi

    #echo 10.11.1.$ip; 
done

┌──(student㉿c2c7a8122892)-[~]
└─$                                                                           


```






Re-write Ping Sweep in Python3. Do not use non-standard libraries in your code as they are not guaranteed to be installed on the shell server (you do not need them for this problem). Same as before, write a short script to perform a ping sweep of a target IP address range. This script will only print the IP addresses of any valid responses (one IP address per line) and nothing else. To make this script more broadly applicable, you will not hardcode the IP address range. Instead, this script will require three arguments: the first three octets of the IP address, the starting value of the last octet, and the ending value of the last octet (see below for examples). You DO NOT need to do any error checking (but feel free to do so). Upload your script to the target VM #9 and run /challenge/ping-sweep-2 with your script's location as the first argument to get the flag.

```python
import sys
import shlex #only needed if apachelogs cannot be pip'd
import os 
import subprocess

#USAGE
#  python3 ./ApacheLogParser.py access.log output.log

def check_ping(ip):
    try:
        subprocess.check_call(
            ['ping', '-c', '1', '-q', ip], stdout=subprocess.DEVNULL
        )
        #subprocess.check_call(
        #    ['ping', '-c', '1', ip],
        #    "/dev/null",  # suppress output
        #    "/dev/null"
        #)
        return True
    except subprocess.CalledProcessError:
        return False

threeocts = sys.argv[1]
start=int(sys.argv[2])
end=int(sys.argv[3])


while start <= end:
    ip=threeocts+"."+str(start)
    if check_ping(ip):
        print (ip)
    start += 1


```

```shell

──(student㉿78457ed72bbc)-[~]
└─$ /challenge/ping-sweep-2 script.py
Testing your script now
Starting test 1.
Starting test 2 - this one is longer and may take several seconds depending on your script.
Great job. Here is your flag: 
OS{780090cf61bce0be844fb2b6deb8797a}

Press any key to continue...


```
