<#

#>
write-host "powershell profile loaded"

function Get-DateClipboard() {
       Get-Date -Format "yyyy-MM-dd" | Set-Clipboard
}
Set-Alias -Name dte -Value Get-DateClipboard
