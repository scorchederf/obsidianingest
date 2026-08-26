---
id: windows-defender-delete-signatures-sql
tags: [windows, defender, remove definitions, signatures]
created: 2023-01-12 11:56
---
# windows-defender-delete-signatures

backlinks: [[]]

sources:

- <https://twitter.com/Alh4zr3d/status/1611005101262389250>

---

![Tweet](_archive/_prebravo/mitre/defenseevasion/image.png)


Red Teamers: a bit messy, but if Windows Defender is causing you a big headache, rather than disabling it (which alerts the user), you should just neuter it by deleting all the signatures:

```powershell
"%Program Files%\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All
```
