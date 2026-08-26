---
id: activeinformationgathering
tags: [bash, cheatsheet]
created: 2023-01-26
---
# active-information-gathering

backlinks: [[snippets-bash]]

sources:
- <https://danielmiessler.com/study/vulnerability-database-resources/>

- Active Directory
  - is a service that allows system administrators to update and manage operating systems, applications, users, and data access on a large scale
  - The domain controller (windows 2000-2019 with Active Directory Domain Services role installed) is the hub and core of Active Directory because it stores all information about how the specific instance of Active Directory is configured. It also enforces a vast variety of rules that govern how objects within a given Windows domain interact with each other, and what services and tools are available to end users. The power and complexity of Active Directory is founded on incredible granularity of controls available to network administrators.
    - when an instance of active directory is configured a domain is created such as corp.com where corp is the name of the organisation
    - Organisational Units (OU) are comparable to system folders in that they are used to store and group other objects. 
      - Computer objects represent servers and workstations that are domain joined.
      - User objects represent employees of the organisation (firstname, surname, username, etc)
  - An Active Directory environment has a very critical dependency on a Domain Name System (DNS) service. As such, a typical domain controller in an AD will also host a DNS server that is authoritative for a given domain. Please note that in the labs, you may also find DNS servers that are not related to Active Directory and provide a lookup service for other computers.
  - Group Policy settings are stored as Group Policy objects in Active Directory. A Group Policy object can be associated with one or more Active Directory containers, such as a site, domain, or organizational unit.
  - Active directory enumeration
    - once a foothold is established, our goal is to advance our privilege level until we gain control of the domain
      - Domain Admins group has complete control of every single computer in the domain
      - compromise the domain controller so we can
        - modify all domain joined computers or execute applications on them
        - crack the password hashes
    - what domain am I on? ```shell  systeminfo | findstr /B "Domain"```
      - if not joined to a domain you will see Domain: WORKGROUP
    - traditional approach
      - local accounts ```shell net user```
      - domain users ```shell net user /domain```
      - individual user ```shell net user jeff_admin /domain```
      - all groups on the domain ```shell net group /domain```
    - modern approach
      - A Primary domain controller emulator is one of the five operations master roles or FSMO roles performed by domain controllers. Technically speaking, the property is called PdcRoleOwner and the domain controller with this property will always have the most updated information about user login and authentication.
      - get the domain object for the current user ```shell [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()```
        - name property = the domain name
        - pdcRoleOwner = the primary domain controller name
    - PowerView
      - tailor our enumeration to consider not only Domain Admins but also potential avenues of "chained compromise" including a hunt for a so-called derivative local admin
      - import the module ```shell import-module .\PowerView.ps1```
      - ```shell get-netuser``` # gets all users in the domain
      - If we manage to compromise Bob's account (through a client side attack for example), we could pivot from CLIENT512 to target Alice on CLIENT621. By extension, we may be able to pivot again to compromise Jeff on SERVER21, gaining domain access. We must tailor our enumeration to consider not only Domain Admins but also potential avenues of "chained compromise" including a hunt for a so-called derivative local admin.![Alt text](_archive/_prebravo/offsec/pen200/21-ActiveDirectory/image.png)
      - check users active logon sessions on a domain controller or file server
        - NetWkstaUserEnum requires administrative permissions <https://learn.microsoft.com/en-au/windows/win32/api/lmwksta/nf-lmwksta-netwkstauserenum?redirectedfrom=MSDN>
        - NetSessionEnum can execute under a standard user account <https://learn.microsoft.com/en-us/windows/win32/api/lmshare/nf-lmshare-netsessionenum>
      - After compromising a domain machine, we should enumerate every computer in the domain looking for logged in users
      - ```shell Get-NetLoggedon -ComputerName client251``` targets an individual workstation
      - ```shell Get-NetSession -ComputerName dc01``` targets the domain controller
    - Enumeration through service principal names aka service accounts
      - samaccountname is set to iis_service, indicating the presence of a web server and serviceprincipalname is set to HTTP/CorpWebServer.corp.com. This all seems to suggest the presence of a web server
      - nslookup CorpWebServer.corp.com
  - active directory authentication
    - NTLM authentication
      - NTLM authentication is used when a client authenticates to a server by IP address (instead of by hostname),1 or if the user attempts to authenticate to a hostname that is not registered on the Active Directory integrated DNS server
      - NTLM authentication process
        - A user accesses a client computer and provides a domain name, user name, and password. The client computes a cryptographic hash  (NTLM hash) of the password and discards the actual password.
        - The client sends the user name to the server (in plaintext).
        - The server generates a 8-byte random number, called a challenge or nonce, and sends it to the client.
        - The client encrypts this challenge with the hash of the user's password and returns the result to the server. This is called the response.
        - The server sends the following three items to the domain controller [User name, Challenge sent to the client, Response received from the client]
        - The domain controller uses the user name to retrieve the hash of the user's password from the Security Account Manager database. It uses this password hash to encrypt the challenge.
        - The domain controller compares the encrypted challenge it computed (in step 6) to the response computed by the client (in step 4). If they are identical, authentication is successful.
    - Kerberos Authentication
      - has been used as Microsoft's primary authentication mechanism since Windows Server 2003
      - advantages are
        - Plain text passwords are never sent across an insecure network.
        - Every login has three stages of authentication.
        - Encryption protects all access keys and tickets.
        - Authentication is mutual, so both users and providers are safe from scams.
      - Since Microsoft's implementation of Kerberos makes use of single sign-on, password hashes must be stored somewhere in order to renew a TGT request. In current versions of Windows, these hashes are stored in the Local Security Authority Subsystem Service (LSASS) memory space. If you can gain access to the hashes, we could crack them to obtain the plaintext password or reuse them to perform various actions.
      - Kerberos authentication process such as wanting to read a document on a network file server ![Alt text](_archive/_prebravo/offsec/pen200/21-ActiveDirectory/image-1.png)
        - user issues an encrypted request to the authentication server (AS) or is usually the Domain Controller. The authentication server searches for the password in the kerberos db based on the user id and attempts to decrypt the request. The Authentication Server Request (AS_REQ) also contains a timestamp. If the timestamp is not a duplication (a potential replay attack)
        - Authentication server sends back a Ticket Granting Ticket (TGT). The TGT contains information regarding the user, including group memberships, the domain, a time stamp, the IP address of the client, and the session key. Default validity is 10 hours.
        - User sends the TGT to the Ticket Granting Server (TGS) which decrypts the ticket with the secret key shared with the authentication server
        - If the TGT is valid, the Ticket Granting Server issues a service ticket to the user
        - The user sends the service ticket to the file server which decrypts the ticket with the secret shared with the Ticket Granting Server (TGS)
        - If the secret keys match, the file server allows the user to open the document.
      - Local Security Authority Subsystem Service (LSASS) process is part of the operating system and runs as SYSTEM, we need SYSTEM (or local administrator) permissions to gain access to the hashes stored on a target.
        - Mimikatz is a post-exploitation tool that dumps passwords from memory, as well as hashes, PINs and Kerberos tickets. Other useful attacks it enables are pass-the-hash, pass-the-ticket or building Golden Kerberos tickets.
          - requires a command prompt with elevated privileges
          - set ```shell privilege::debug``` which will allow us to interact with a process owned by another account
          - using the Sekurlsa module, dump the credentials of all logged on users ```shell sekurlsa::logonpasswords```
            - ![Alt text](_archive/_prebravo/offsec/pen200/21-ActiveDirectory/image-2.png)
          - Can also exploit TGT and service tickets by using the sekurlsa:tickets module
            - ```shell sekurlsa::tickets```
    - Service Account attacks
      - A service principal name (SPN) is a unique identifier of a service instance. Kerberos authentication uses SPNs to associate a service instance with a service sign-in account. Doing so allows a client application to request service authentication for an account even if the client doesn't have the account name.
      - when the user wants to access a resource hosted by a SPN the client requests a service ticket that is generated by the domain controller. The service ticket is then decrypted and validated by the application server, since it is encrypted through the password hash of the SPN
      - When requesting the service ticket from the domain controller, no checks are performed on whether the user has any permissions to access the service hosted by the service principal name. These checks are performed as a second step only when connecting to the service itself. This means that if we know the SPN we want to target, we can request a service ticket for it from the domain controller. Then, since it is our own ticket, we can extract it from local memory and save it to disk.
        - Abusing the service ticket and attempt to crack the password of the service account
          - we know that the registered SPN for the Internet Information Services web server in the domain is HTTP/CorpWebServer.corp.com
          - import the System.IdentityModel and pass the HTTP/CorpWebServer.corp.com as an argument
            - ```shell 
            Add-Type -AssemblyName System.IdentityModel
            New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList 'HTTP/CorpWebServer.corp.com````
          - After execution, the requested service ticket should be generated by the domain controller and loaded into the memory of the Windows 10 client. 
          - To download the service ticket with Mimikatz, we use the kerberos::list command
            - ```kerberos::list /export```
            - ```\* Saved to file     : 1-40a50000-offsec@HTTP~CorpWebServer.corp.com-CORP.COM.kirbi```
          - Instead of executing Mimikatz all the time, we can also use the built-in klist command to display all cached Kerberos tickets for the current user
            - ```shell klist``
          - Kerberoasting - According to the Kerberos protocol, the service ticket is encrypted using the SPN's password hash. If we are able to request the ticket and decrypt it using brute force or guessing (in a technique known as Kerberoasting7), we will know the password hash, and from that we can crack the clear text password of the service account.
            - Install the kerberoast tool
              - ```shell sudo apt update && sudo apt install kerberoast```
            - run tgsrepcrack.py by supplying a wordlist and the downloaded service ticket
              - ```shell python /usr/share/kerberoast/tgsrepcrack.py wordlist.txt 1-40a50000-Offsec@HTTP~CorpWebServer.corp.com-CORP.COM.kirbi```
              - ```shell found password for ticket 0: Qwerty09!  File: 1-40a50000-Offsec@HTTP~CorpWebServer.corp.com-CORP.COM.kirbi /r/n All tickets cracked!```
            - The Invoke-Kerberoast.ps1 script extends this attack, and can automatically enumerate all service principal names in the domain, request service tickets for them, and export them in a format ready for cracking in both John the Ripper and Hashcat, completely eliminating the need for Mimikatz in this attack.
              - ```shell https://github.com/EmpireProject/Empire/blob/master/data/module_source/credentials/Invoke-Kerberoast.ps1```
    - Low and slow password guessing
      - When performing a brute-force or wordlist authentication attack, we must be aware of account lockouts since too many failed logins may block the account for further attacks and possibly alert system administrators.
      - lets check the domain password policy
        - ```shell net accounts```
        - Checking the lockout threshhold we can see it = 5 so we can make 4 attempts before the account is locked
        - Checking the Lockout observation window we can see that it resets after 30 minutes which means we can try again 30 minutes after the last failed login
        - 192 logins per 24 hours
        - An attack like this would allow us to compile a short list of very commonly used passwords and use it against a massive amount of users, which in practice, reveals quite a few weak account passwords in the organization.
        - using powershell
```shell
$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
$PDC = ($domainObj.PdcRoleOwner).Name
$SearchString = "LDAP://"
$SearchString += $PDC + "/"
$DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
$SearchString += $DistinguishedName
New-Object System.DirectoryServices.DirectoryEntry($SearchString, "jeff_admin", "Qwerty09!")
```
        - if password matches, the object is created. If not, you will receive a powershell error message such as "username password is incorrect"
        - using the .\Spray-Passwords.ps1 -Pass Qwerty09! -Admin we can supply a wordlist and a user list 
  - Active Directory Lateral Movement
    - Pass the Hash
      - The Pass the Hash (PtH) technique allows an attacker to authenticate to a remote system or service using a user's NTLM hash instead of the associated plaintext password. Note that this will not work for Kerberos authentication but only for server or service using NTLM authentication.
      - 
