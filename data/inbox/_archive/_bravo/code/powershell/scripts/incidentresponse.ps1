
Connect-MgGraph -Scopes Directory.AccessAsUser.All

$csvFile = "c:\dev\list.csv"

$csvData = import-csv -Path $csvFile

foreach ($row in $csvData){
    $name = $row.Name
    $email = $row.Email

    write-host ("the users name is $name")
}