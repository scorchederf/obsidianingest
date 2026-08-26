[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

#$domains = @("UHC.UC.COM.AU","LCCQ.ORG.AU","UC.COM.AU","INT.UCQ.COM.AU","EXT.UCQ.COM.AU","10.20.1.25")
$csvFile = "c:\temp\terminated.csv"
$csvOutFile = "c:\temp\terminated-updated.csv"

#HACK email to domain mapping
$domainInt = "int.ucq.com.au"
$domainLccq = "lccq.org.au"
$domainBc = "bluecare.org.au", "qld.bluecare.org.au"
$domainUhc = "uhc.uc.com.au", "uccommunity.org.au", "uchealth.com.au", "ucareqld.com.au"

$limit = 10000
$dataset = Import-Csv -Path $csvFile
$out = @()

foreach ($item in $dataset| Select-Object -First $limit) {
    $server = "NOT IDENTIFIED"
    if ($item.Email.Length -gt 0) {
        $domain = $item.Email.Split("@")[1].ToLower()
        if ($domain -in $domainUhc)     { $server = "uhc.uc.com.au";        $filter = 'mail -like "' + $item.Email + '"' }
        if ($domain -in $domainBc)      { $server = "qld.bluecare.org.au";  $filter = 'mail -like "' + $item.Email + '"' }
        if ($domain -in $domainLccq)    { $server = "lccq.org.au";          $filter = 'mail -like "' + $item.Email + '"' }
        if ($domain -in $domainInt)     { $server = "int.ucq.com.au" }
    } else {
        if ($item.Company -eq "Blue Care")                      { $server = "qld.bluecare.org.au";      $filter='name -like "' + $item.Worker + '"' }
        if ($item.Company -eq "Family and Disability Services" -or $item.Company -eq "UnitingCare Hospita") { $server = "uhc.uc.com.au";            $filter='name -like "' + $item.Worker + '"' }
    }
    try {
        if ($server -eq "NOT IDENTIFIED") {
            throw "server not found, skipping"
        } else {
            ##$filter = 'mail -like "' + $item.Email + '"'
            # add additional properties
            
            $data = get-aduser -filter $filter -Properties * -Server $server
            $item | Add-Member -Name 'aadLastSignInDateTime'    -Type NoteProperty -Value $data.extensionAttribute5
            $item | Add-Member -Name 'adIsEnabled'              -Type NoteProperty -Value $data.Enabled
            $item | Add-Member -Name 'adWasFound'               -Type NoteProperty -Value $true
            $out += $item
            #write-host $item -ForegroundColor Green
        }

        # write-host $item.Email, $server -ForegroundColor Green
    }
    catch {
        $item | Add-Member -Name 'adWasFound'          -Type NoteProperty -Value $false
        $item | Add-Member -Name 'status'              -Type NoteProperty -Value "caught error, not found"
        $out += $item
        write-host $item -ForegroundColor Red
    }

}


$out | Export-Csv -NoTypeInformation -Path $csvOutFile
