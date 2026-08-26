
Import-Module ActiveDirectory

$groupName = "RG_WS_USB_WriteAccess"
$group = Get-ADGroup -Identity $groupName

function Get-ADGroupMemberFix {
    [CmdletBinding()]
    param(
        [Parameter(
            Mandatory = $true,
            ValueFromPipeline = $true,
            ValueFromPipelineByPropertyName = $true,
            Position = 0
        )]
        [string[]]
        $Identity,

        [string]
        $Server
    )

    begin {
        $additionalArguments = @{}
        if($PSBoundParameters.ContainsKey('Server')){
            $additionalArguments['Server'] = $Server
        }
    }

    process {
        foreach ($GroupIdentity in $Identity) {
            $Group = $null
            $Group = Get-ADGroup -Identity $GroupIdentity -Properties Member @additionalArguments
            if (-not $Group) {
                continue
            }
            Foreach ($Member in $Group.Member) {
                Get-ADObject $Member 
            }
        }
    }
}

$d = Get-ADGroupMemberFix -Identity $group.Name


foreach ($i in $d) {
    try {
        $SID = New-Object System.Security.Principal.SecurityIdentifier($i.Name)
        $User = $SID.Translate([System.Security.Principal.NTAccount])
        write-host $User.Value        
    }
    catch {
       write-host $i.Name, " failed to retrieve"
    }
}