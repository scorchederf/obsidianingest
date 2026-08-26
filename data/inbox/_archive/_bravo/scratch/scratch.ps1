
$src = "C:\Users\adams\Desktop\entities.json"
$data = get-content -Raw $src | Out-String | ConvertFrom-Json
$entityCol = @()
$fqdnCol = @()
$cidrCol = @()
foreach ($itm in $data) {
    #write-host $itm.guid, $itm.name
    #enforce consistent naming standards
    $entityCol += @{
        ucqEntityGuid       = ("ucq-" + $itm.guid)
        ucqEntityName       = $itm.name            # internal smtp server for sending emails
        ucqEntityDesc       = $itm.desc
    }
    
    foreach ($fqdn in $itm.fqdn){
        #write-host "`t", $fqdn
        $fqdnCol += @{
            ucqEntityGuid   = $itm.guid
            fqdn            = $fqdn
        }
    }
    foreach ($cidr in $itm.cidr){
        #write-host "`t", $fqdn
        $cidrCol += @{
            ucqEntityGuid   = $itm.guid
            cidr            = $cidr
        }
    }    
}

$exportCol = @{}
$exportCol.Add("ucq-entity", $entityCol)
$exportCol.Add("ucq-fqdn", $fqdnCol)
$exportCol.Add("ucq-cidr", $cidrCol)


foreach ($itm in $exportCol.Keys) {
    $outfile = "C:\Users\adams\Desktop\EntitiesToJson\$itm.json"
    $col = $exportCol[$itm] 
    $col | ConvertTo-Json -Depth 100 -Compress | Out-File $outfile -Encoding utf8
}
