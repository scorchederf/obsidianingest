---
title: Get-NestedGroupsForUser PowerShell Script
aliases: []
tags:
- tool/powershell
- technique/t1098
- os/windows
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: active-directory.md
related_tools:
- '[[powershell]]'
- '[[Get-ADUser]]'
- '[[Get-ADGroup]]'
related_techniques:
- '[[T1098]]'
related_tactics:
- '[[ta0003]]'
related_services: []
related_os: []
related_notes: []
mitre_tactic: TA0003
mitre_technique: T1098
real_path: ''
port: ''
protocol: ''
os: windows
---

# Get-NestedGroupsForUser PowerShell Script

## Description
This PowerShell script is designed to retrieve the nested group memberships for a specified user in an Active Directory environment. It uses the `Get-ADUser` and `Get-ADGroup` cmdlets to traverse the group hierarchy and display all groups that the user is a member of, including nested groups.

## Syntax
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

## Usage
```powershell
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

## Examples
```powershell
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

## Notes
The script uses a queue to process nested groups and a hash table to keep track of processed groups to avoid infinite loops. It also handles potential errors and warnings during the execution.

