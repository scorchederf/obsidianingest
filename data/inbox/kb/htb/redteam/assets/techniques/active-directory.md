# active directory
























## scripts
- nested groups for user
```powershell

function Get-NestedGroupsForUser {
    param (
        [Parameter(Mandatory = $true)]
        [string]$Username,

        [Parameter(Mandatory = $false)]
        [string]$Server
    )

    Write-Host "🔍 Looking up user: $Username"
    $checkedGroups = @{}
    $queue = [System.Collections.Queue]::new()

    $userParams = @{ Identity = $Username; Properties = 'MemberOf' }
    if ($Server) { $userParams.Server = $Server }

    try {
        $user = Get-ADUser @userParams
    } catch {
        Write-Error "❌ Failed to get user '$Username'. $_"
        return
    }

    if (-not $user) {
        Write-Error "❌ User '$Username' not found."
        return
    }

    Write-Host "✅ Found user: $($user.DistinguishedName)"
    Write-Host "📦 Initial direct group memberships:"
    foreach ($groupDN in $user.MemberOf) {
        Write-Host "  - $groupDN"
        $queue.Enqueue($groupDN)
    }

    while ($queue.Count -gt 0) {
        $currentGroupDN = $queue.Dequeue()

        if ($checkedGroups.ContainsKey($currentGroupDN)) {
            Write-Host "🔁 Already processed: $currentGroupDN"
            continue
        }

        Write-Host "➡️ Processing group: $currentGroupDN"
        $checkedGroups[$currentGroupDN] = $true

        $groupParams = @{ Identity = $currentGroupDN; Properties = 'MemberOf' }
        if ($Server) { $groupParams.Server = $Server }

        try {
            $group = Get-ADGroup @groupParams
            if ($group.MemberOf) {
                Write-Host "  ↪️ Nested in:"
                foreach ($parentDN in $group.MemberOf) {
                    Write-Host "    - $parentDN"
                    $queue.Enqueue($parentDN)
                }
            } else {
                Write-Host "  ⛔ No parent groups."
            }
        } catch {
            Write-Warning "⚠️ Could not retrieve group: $currentGroupDN. $_"
        }
    }

    Write-Host "`n🎯 All resolved groups for: " $($user.DistinguishedName)
    foreach ($groupDN in $checkedGroups.Keys) {
        $outputParams = @{ Identity = $groupDN }
        if ($Server) { $outputParams.Server = $Server }

        try {
            $group = Get-ADGroup @outputParams
            Write-Host "  - $($group.Name) ($groupDN)"
        } catch {
            Write-Host "  - [Unknown or deleted group] ($groupDN)"
        }
    }
}


# Usage:
Get-NestedGroupsForUser -Username "bob" -server "contoso"



```
    - 