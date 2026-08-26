---
title: Running Services on Windows
aliases: []
tags:
- service/windows
- os/windows
category: services
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: malciousservice2.txt
related_tools: []
related_techniques: []
related_tactics: []
related_services:
- '[[adws]]'
- '[[appreadiness]]'
- '[[appxsvc]]'
- '[[bfe]]'
- '[[BrokerInfrastru]]'
- '[[camsvc]]'
- '[[cbdhsvc_1bd1d3]]'
- '[[cdpsvc]]'
- '[[CDPUserSvc_1bd1d3]]'
- '[[certpropsvc]]'
- '[[clipsvc]]'
- '[[comsysapp]]'
- '[[CoreMessagingRe]]'
- '[[cryptsvc]]'
- '[[dcomlaunch]]'
- '[[defragsvc]]'
- '[[dfs]]'
- '[[dfsr]]'
- '[[dhcp]]'
- '[[diagtrack]]'
- '[[DispBrokerDeskt]]'
- '[[dns]]'
- '[[dnscache]]'
- '[[dps]]'
- '[[dsmsvc]]'
- '[[dssvc]]'
- '[[edgeupdate]]'
- '[[eventlog]]'
- '[[eventsystem]]'
- '[[fontcache]]'
- '[[gpsvc]]'
- '[[ikeext]]'
- '[[iphlpsvc]]'
- '[[ismserv]]'
- '[[kdc]]'
- '[[keyiso]]'
- '[[lanmanserver]]'
- '[[lanmanworkstation]]'
- '[[lmhosts]]'
- '[[lsm]]'
- '[[mpssvc]]'
- '[[msdtc]]'
- '[[ncbservice]]'
- '[[netlogon]]'
- '[[netman]]'
- '[[netprofm]]'
- '[[netsetupsvc]]'
- '[[nlasvc]]'
- '[[nsi]]'
- '[[pcasvc]]'
- '[[plugplay]]'
- '[[policyagent]]'
- '[[power]]'
- '[[profsvc]]'
- '[[rasman]]'
- '[[rpceptmapper]]'
- '[[rpcss]]'
- '[[samss]]'
- '[[schedule]]'
- '[[sens]]'
- '[[sessionenv]]'
- '[[shellhwdetection]]'
- '[[smphost]]'
- '[[spooler]]'
- '[[sppsvc]]'
- '[[sstpsvc]]'
- '[[staterepository]]'
- '[[storsvc]]'
- '[[svchost]]'
- '[[sysmain]]'
- '[[systemeventsbroker]]'
- '[[tabletinputservice]]'
- '[[termservice]]'
- '[[themes]]'
- '[[timebrokersvc]]'
- '[[tokenbroker]]'
- '[[trustedinstaller]]'
- '[[ualsvc]]'
- '[[umrdpservice]]'
- '[[usermanager]]'
- '[[usosvc]]'
- '[[vds]]'
- '[[vgauthservice]]'
- '[[vm3dservice]]'
- '[[vmtools]]'
- '[[w32time]]'
- '[[waasmedicsvc]]'
- '[[wcmsvc]]'
- '[[wdisystemhost]]'
- '[[WinHttpAutoProx]]'
- '[[winmgmt]]'
- '[[winrm-1787747908]]'
- '[[wlidsvc]]'
- '[[wpnservice]]'
- '[[WpnUserService_]]'
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: windows
---

# Running Services on Windows

## Running Services
PS C:\Users\Student> get-service | where-object {$_.status -eq "Running"}

Status   Name               DisplayName
------   ----                -----------
Running  ADWS               Active Directory Web Services
Running  AppReadiness       App Readiness
Running  AppXSvc            AppX Deployment Service (AppXSVC)
Running  BFE                Base Filtering Engine
Running  BrokerInfrastru... Background Tasks Infrastructure Ser...
Running  camsvc             Capability Access Manager Service
Running  cbdhsvc_1bd1d3     Clipboard User Service_1bd1d3
Running  CDPSvc             Connected Devices Platform Service
Running  CDPUserSvc_1bd1d3  Connected Devices Platform User Ser...
Running  CertPropSvc        Certificate Propagation
Running  ClipSVC            Client License Service (ClipSVC)
Running  COMSysApp          COM+ System Application
Running  CoreMessagingRe... CoreMessaging
Running  CryptSvc           Cryptographic Services
Running  DcomLaunch         DCOM Server Process Launcher
Running  defragsvc          Optimize drives
Running  Dfs                DFS Namespace
Running  DFSR               DFS Replication
Running  Dhcp               DHCP Client
Running  DiagTrack          Connected User Experiences and Tele...
Running  DispBrokerDeskt... Display Policy Service
Running  DNS                DNS Server
Running  Dnscache           DNS Client
Running  DPS                Diagnostic Policy Service
Running  DsmSvc             Device Setup Manager
Running  DsSvc              Data Sharing Service
Running  edgeupdate         Microsoft Edge Update Service (edge...
Running  EventLog           Windows Event Log
Running  EventSystem        COM+ Event System
Running  FontCache          Windows Font Cache Service
Running  gpsvc              Group Policy Client
Running  IKEEXT             IKE and AuthIP IPsec Keying Modules
Running  iphlpsvc           IP Helper
Running  IsmServ            Intersite Messaging
Running  Kdc                Kerberos Key Distribution Center
Running  KeyIso             CNG Key Isolation
Running  LanmanServer       Server
Running  LanmanWorkstation  Workstation
Running  lmhosts            TCP/IP NetBIOS Helper
Running  LSM                Local Session Manager
Running  mpssvc             Windows Defender Firewall
Running  MSDTC              Distributed Transaction Coordinator
Running  NcbService         Network Connection Broker
Running  Netlogon           Netlogon
Running  Netman             Network Connections
Running  netprofm           Network List Service
Running  NetSetupSvc        Network Setup Service
Running  NlaSvc             Network Location Awareness
Running  nsi                Network Store Interface Service
Running  PcaSvc             Program Compatibility Assistant Ser...
Running  PlugPlay           Plug and Play
Running  PolicyAgent        IPsec Policy Agent
Running  Power              Power
Running  ProfSvc            User Profile Service
Running  RasMan             Remote Access Connection Manager
Running  RpcEptMapper       RPC Endpoint Mapper
Running  RpcSs              Remote Procedure Call (RPC)
Running  SamSs              Security Accounts Manager
Running  Schedule           Task Scheduler
Running  SENS               System Event Notification Service
Running  SessionEnv         Remote Desktop Configuration
Running  ShellHWDetection   Shell Hardware Detection
Running  smphost            Microsoft Storage Spaces SMP
Running  Spooler            Print Spooler
Running  sppsvc             Software Protection
Running  SstpSvc            Secure Socket Tunneling Protocol Se...
Running  StateRepository    State Repository Service
Running  StorSvc            Storage Service
Running  svcHost            svcHost
Running  SysMain            SysMain
Running  SystemEventsBroker System Events Broker
Running  TabletInputService Touch Keyboard and Handwriting Pane...
Running  TermService        Remote Desktop Services
Running  Themes             Themes
Running  TimeBrokerSvc      Time Broker
Running  TokenBroker        Web Account Manager
Running  TrustedInstaller   Windows Modules Installer
Running  UALSVC             User Access Logging Service
Running  UmRdpService       Remote Desktop Services UserMode Po...
Running  UserManager        User Manager
Running  UsoSvc             Update Orchestrator Service
Running  vds                Virtual Disk
Running  VGAuthService      VMware Alias Manager and Ticket Ser...
Running  vm3dservice        VMware SVGA Helper Service
Running  VMTools            VMware Tools
Running  W32Time            Windows Time
Running  WaaSMedicSvc       Windows Update Medic Service
Running  Wcmsvc             Windows Connection Manager
Running  WdiSystemHost      Diagnostic System Host
Running  WinHttpAutoProx... WinHTTP Web Proxy Auto-Discovery Se...
Running  Winmgmt            Windows Management Instrumentation
Running  WinRM              Windows Remote Management (WS-Manag...
Running  wlidsvc            Microsoft Account Sign-in Assistant
Running  WpnService         Windows Push Notifications System S...
Running  WpnUserService_... Windows Push Notifications User Ser...
PS C:\Users\Student>

