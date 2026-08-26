





# get mfa numbers for all users (untested)
```powershell
Import-Module Microsoft.Graph.Users
Connect-MgGraph
$mgUsers = Get-MgUser -All
$contacts = @()
foreach ($user in $mgUsers) {
    $contacts += (Get-MgUserAuthenticationPhoneMethod -UserId $user.UserPrincipalName | Select-Object -Property @{ N='UserPrincipalName'; E={ $user.UserPrincipalName }}, PhoneNumber, PhoneType)
}
```