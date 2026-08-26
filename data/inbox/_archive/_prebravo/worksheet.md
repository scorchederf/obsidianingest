```shell
TARGET=192.168.207.12
mkdir target
#search first target and then all hosts around it
sudo nmap -sC -sV -oA target/quick -v $TARGET
grep -E "open|report|\||Host script results:" target/quick.nmap -h | sed "s/Nmap scan report for /\n\n# /" | awk '!/^#/{sub(/^/, "\t"); print;next;}{print}' | awk '/\|/{sub("/\|", "\t\t"); print; next;}{print}' | tee -a target/network.md
sudo nmap -sn -T4 -v -n -oA target/host $TARGET/24 --open
grep "Up" target/host.gnmap | awk -F " " '{print $2}' >> target/hosts.lst
sudo nmap -sC -sV -T3 -oA target/hostscan -iL target/hosts.lst
grep -E "open|report|\||Host script results:" target/hostscan.nmap -h | sed "s/Nmap scan report for /\n\n# /" | awk '!/^#/{sub(/^/, "\t"); print;next;}{print}' | awk '/\|/{sub("/\|", "\t\t"); print; next;}{print}' | tee -a target/network.md

```



# 192.168.207.12
        135/tcp open  msrpc         Microsoft Windows RPC
        139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
        445/tcp open  microsoft-ds?
        Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .


# 192.168.207.11
        135/tcp open  msrpc         Microsoft Windows RPC
        139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
        445/tcp open  microsoft-ds?


# 192.168.207.12
        135/tcp open  msrpc         Microsoft Windows RPC
        139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
        445/tcp open  microsoft-ds?


# 192.168.207.13
        22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
        139/tcp  open  netbios-ssn Samba smbd 4.6.2
        443/tcp  open  http        Apache httpd 2.4.49 ((Unix))
        445/tcp  open  netbios-ssn Samba smbd 4.6.2
        9999/tcp open  http        Apache httpd 2.4.49 ((Unix))
        Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
