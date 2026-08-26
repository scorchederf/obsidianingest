import-module psexcel 

$configs = new-object System.Collections.ArrayList
$path = 'C:\temp\CrowdStrike Cloud Policies.xlsx'
$filedata = Import-XLSX -Path $path -RowStart 1


write-host $filedata.Count
write-host $filedata.GetType()

## $filedata.default_severity | sort -Unique

foreach ($fd in $filedata) {
    $fd | Add-Member -MemberType NoteProperty -Name "sevnum" -Value 4
    $sevnum = 1
    switch ($fd.default_severity) {
        "critical"         {$sevnum = 1}
        "high"             {$sevnum = 2}
        "medium"           {$sevnum = 3}
        "informational"    {$sevnum = 4}
    }
    $fd.sevnum = $sevnum
}

##  $filedata | where-object { $_.cloud_platform_type -eq "azure" }  | Sort-Object -Property cloud_platform_type,cloud_service_type,sevnum | Out-GridView


$output = ""
$head1 = ""
foreach ($e in ($filedata | where-object { $_.cloud_platform_type -eq "azure" }  | Sort-Object -Property cloud_platform_type,cloud_service_type,sevnum)) {
    if ($e.cloud_service_type -ne $head1){
        $output += "`n`n" + "# " + $e.cloud_service_type
        $head1 = $e.cloud_service_type
    }
    $color = ""
    switch ($fd.default_severity) {
        "critical"         {$color = "red"}
        "high"             {$color = "tomato"}
        "medium"           {$color = "beer"}
        "informational"    {$color = "lightblue"}
    }
    
    $output += "`n`n## " + $e.policy_statement
    $output += "`n`n" + $e.default_severity.ToUpper()
    $output += "`n`n" + $e.description
    $output += "`n`n" + "**Alert Logic**" + "`n`n" + $e.alert_logic.Replace("|", "`n")
    $output += "`n`n" + "**Remediation Steps**" + "`n`n" + $e.policy_remediation.Replace("|", "`n").Replace("Step ", "")




}

$output > c:\temp\policies.md






