$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
#   Primmary domain controller maps to the PdcRoleOwner name
$PrimaryDomainController = ($domainObj.PdcRoleOwner).Name
#   DistinguishedName will consist of our domain name ('corp.com') broken down into individual domain components
$DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"          
#   we can now query against the LDAPProviderPath
$LDAPProviderPath = "LDAP://" + $PrimaryDomainController + "/" + $DistinguishedName

#   we have to specify a SearchRoot, which is the node in the Active Directory hierarchy where searches start
$dirSearcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$LDAPProviderPath)
                                  
$dirEntry = New-Object System.DirectoryServices.DirectoryEntry($LDAPProviderPath)
#   with credentials
#   New-Object System.DirectoryServices.DirectoryEntry (string? path, string? username, string? password);  
#   $dirEntry = New-Object System.DirectoryServices.DirectoryEntry($LDAPProviderPath, "corp.com\offsec", "lab")

#   When no arguments are passed to the constructor, the SearchRoot will indicate that every search should return results from the entire Active Directory
$dirSearcher.SearchRoot = $dirEntry


#   https://learn.microsoft.com/en-au/windows/win32/adschema/a-samaccounttype
<#
SAM_DOMAIN_OBJECT               0x0
SAM_GROUP_OBJECT                0x10000000
SAM_NON_SECURITY_GROUP_OBJECT   0x10000001
SAM_ALIAS_OBJECT                0x20000000
SAM_NON_SECURITY_ALIAS_OBJECT   0x20000001
SAM_USER_OBJECT                 0x30000000
SAM_NORMAL_USER_ACCOUNT         0x30000000
SAM_MACHINE_ACCOUNT             0x30000001
SAM_TRUST_ACCOUNT               0x30000002
SAM_APP_BASIC_GROUP             0x40000000
SAM_APP_QUERY_GROUP             0x40000001
SAM_ACCOUNT_TYPE_MAX            0x7fffffff
#>

#   ADD FILTERS
#   needs to be converted from hex to decimal to query
$samObject = [uint32]"0x10000000"           
$dirSearcher.filter="samAccountType=" + $samObject

#   OR
#   $dirSearcher.filter="name=*adam*"           #search for name
#   OR
#   $dirSearcher.filter="(objectClass=Group)"   #list all groups
#   OR
#   $dirSearcher.filter="(name=Secret_Group)"   # group name       
# REMEMBER TO DIG INTO NESTED GROUPS

$dirSearcher.filter="serviceprincipalname=*http*"