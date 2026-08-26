---
id: tools-apache2
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-apache2

backlinks: [[]]

sources:

---

Masscan1 is arguably the fastest port scanner; it can scan the entire Internet in about 6 minutes, transmitting an astounding 10 million packets per second! While it was originally designed to scan the entire Internet, it can easily handle a class A or B subnet, which is a more suitable target range during a penetration test.

```shell
# install
sudo apt install masscan

# scan large internal network looking for tcp port 80 
sudo masscan -p80 10.0.0.0/8

# class c network scan --rate to specify rate of packet transmissino -e for raw ethernet --router-ip to specify the ip address for the gateway
sudo masscan -p80 10.11.1.0/24 --rate=1000 -e tap0 --router-ip 10.11.0.1
```
