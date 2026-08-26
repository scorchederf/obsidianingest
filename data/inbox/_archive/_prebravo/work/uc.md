


# crowdstrike
- can install on devices which are are not joined to the domain but are not managed by group policy
- generally the falcon agent doesn require whitelisting due to the way it interacts in the agent
- 


# service now
- 
We cannot provide access based on a mirror id. Please provide a full list of applications/servers that the new user might need access to and the business justification for the same. For server access, please confirm the access type as well i.e. rdp only or rdp with local admin
- 
USB write access presents a significant security risk to UnitingCare ICT environments as it can be leveraged in breaching any number of security controls including the use of potentially infected, insecure drives, root kits allowing remote control of systems and the loss of confidential information on removable media drives. As a general principle, the Security team's position is that unless you can demonstrate the inability to use the existing cloud based file share platforms in place, this is the recommended option and USB write access will not be provided for general use.

The ShareFile platform will provide the functionality you are looking for with improved security controls in place over the use of removable drives.

To request access to sharefile, please submit a request through - https://ucareqld.service-now.com/ucqp?id=sc_cat_item&sys_id=00feccf0db1b6854400bbd16f49619fd and select ShareFile via the Application Details section.

- USB group = RG_WS_USB_WriteAccess



# ! todo

- [ ] Falcon scheduled report that reports all the vulnerablities for assests that are tagged as developer laptops
  - Henry and Han will be contacts
- WRIKE assessment 
  - emailed supplier assessment to Brenda Lohe on 20230728
  - 








  

- seven devices in runzero that dont have crowdstrike installed
  - check runzero


Task List
- [x] CrowdStrike - Update Deployment Sensor Version
- [x] Cyber-AccountExpiryADM
  - [ ] renamed to cyber_ad_expiringaccounts_admins
- [x] Cyber-ADSearchSensitiveInfo
  - [ ] Cyber-CertCheck.ps1
    - [ ] needs a rewrite
  - [ ] Cyber-CompromisedSiteCheck.ps1
    - [ ] ignored
- [x] Cyber-CrowdStrike-CompromisedPassword-Admins
- [ ] Cyber-CrowdStrike-CompromisedPassword-Users
- [x] Cyber-CrowdStrike-CrowdScoreDailyStatistics.ps1
- [x] Cyber-CrowdStrike-RemoveDuplicateHosts.ps1
  - [ ] Cyber-CrowdStrike-ReportUpload.ps1
- [x] Cyber-CrowdStrike-SpotlightDailyStatistics.ps1
- [ ] Cyber-EarlyWarning.ps1
- [x] Cyber-KVBackup
- [ ] Cyber-MonitoringNewSystem
  - [ ] Cyber-NotificationService.ps1
- [ ] Cyber-PasswordExpiryADM
- [ ] Cyber-PasswordExpiryVMP.ps1
- [ ] Cyber-Tenable-ReportUpload.ps1
- [ ] Cyber-TEST-PermissionPassthrough.ps1



# 2023-07-18
- cybercx report to get us to a three
- Shaun finishes up on Friday 07-21
- 18 August - wipro siem turned off


# 2023-08-08
- put together a blurb to remind the admins that they need to configure the security recommendations for cloud misconfiguration reports
  - Please ensure that when implementing these changes that the principal of least privilege be applied to accounts, access to resources is restricted through adequate network rules and data is stored with the appropriate controls based on its classification.
- data centre of excellence 
  - being created, going through idea gathering
- logscale 
  - working on additional 100gb per day ingestion
- chatgpt usage
  - is there a contract we can use to ensure people dont upload 
  - guideline
  - palo - is there an appropriate warning message we can display before users hit the sites?
    - warning - use of open ai technologies blah blah blah
- go one platform
  - Rohan to organise access
- send through ideas or tasks we have done to Rohan for inclusion into the NIST cyber security risk papers



# 2023-08-15
- cyber ideas being sent to comms
- bumblebee
  - prd pii data in test environments
  - ipad
    - temps get two apps
    - perms get nine apps
- 






# Axway
- Chandra Brata
- Manikumar Kunnamareddy
- sftp
- account created in axway
  - payroll 
  - krunos 
  - kris21 
  - ucqdocs
  - smartcom
  - coopa
  - dmr
  - finance bank details
- hosted internally on linux 
  - account and path to ucqdocs
- patched under usual process
- axway console
  - accounts
  - log/audit
- prod
  - ucq-axwedg-p002
  - ucq-axwsrv-p002
- dev
  - ucq-axwstsrv-d001
  - ucq-axwstedg-d002
  - 