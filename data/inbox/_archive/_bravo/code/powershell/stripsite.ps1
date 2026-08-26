
$min = 501
$max = 1000


$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
$session.Cookies.Add((New-Object System.Net.Cookie("_hc", "falcon.us-2.crowdstrike.com", "/", ".crowdstrike.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("CloudFront-Key-Pair-Id", "APKAIB6YEO3HAGB3R7TA", "/", ".falcon.us-2.crowdstrike.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("cs_J5DUVADSGO4PEITKIC46STZQN4_session_id_8000", "b8295cc9bac171ac5e2d1db39f7fb24179a32b63", "/", "falcon.us-2.crowdstrike.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("cs_J5DUVADSGO4PEITKIC46STZQN4_splunkweb_csrf_token_8000", "9685867658607597097", "/", "falcon.us-2.crowdstrike.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("cs_J5DUVADSGO4PEITKIC46STZQN4_splunkd_8000", "ZEQetygQ2bl7HpRMNdltLa^209HdRj3CmIbHbdIbejgicnfYrWbUiqKsLxsyPuvt6uDXYrICYN7Gk0dnUmaQuFyxVmPvsKHNQenqoQkKogrnWGiutjwf2ucZFVTt49ed", "/", "falcon.us-2.crowdstrike.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("id", "MTY5NTE4OTUyNXxMd3dBTEZwVVQyWkRaVzkwWkhCelpURnZlSGxrZEhoWk9GYzFNRWx2UzFrME1EVjRkakEyUWtsR1MwazJhMUU5fB41HUDrE--hbH7q6PST6ElfWw6WtaHOcT_OmN5q7dpt", "/", ".falcon.us-2.crowdstrike.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("CloudFront-Policy", "eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9hc3NldHMuZmFsY29uLnVzLTIuY3Jvd2RzdHJpa2UuY29tLyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2OTUxOTMxMjV9fX1dfQ__", "/", ".falcon.us-2.crowdstrike.com")))
$session.Cookies.Add((New-Object System.Net.Cookie("CloudFront-Signature", "UO6TeDHvhLHYMBhOuoj9i9cG5mvTdBWZ1XFy0om0gfCQrGWUGOP0BVaxCvfIsanhpLpl6wlmtlNkVGqyeLXr7CGNesOPTGmTJ~~qU~h~PLhekWAwBKO95lmT~wD7lC5Bnow2ZMmeNv1dKgWX6wVFNj16yusI2zS22dsq3-TQkHcUr7yxcz5JumhPXdJ7PsLYkjPm0OXW8q0lomyB97JsM1fXpzLU7VmJnWaFmvXnsRL~fKNGSGfzfu4kDdN~60VfLE6okdU~lEa-8TUKsCJ7rRsRi9YlFjDy-pY3vFpUNVP1lRr86tTyEsI2PfHqSvyu67b6Aiy7FR24BM3q~agbNg__", "/", ".falcon.us-2.crowdstrike.com")))


for ($i=$min; $i -le $max; $i++) 
{

    #Start-Sleep -s 5
    write-host "starting $i"
    $iwr = $null
    try {
        $iwr = Invoke-WebRequest -UseBasicParsing -Uri "https://falcon.us-2.crowdstrike.com/api2/cspmregistration/settings/entities/policy-details/v1?ids=$i" `
        -WebSession $session `
        -Headers @{
            "authority"="falcon.us-2.crowdstrike.com"
        "method"="GET"
        "path"="/api2/cspmregistration/settings/entities/policy-details/v1?ids=$i"
        "scheme"="https"
        "accept"="application/json"
        "accept-encoding"="gzip, deflate, br"
        "accept-language"="en-US,en;q=0.9"
        "cache-control"="no-cache"
        "pragma"="no-cache"
        "sec-ch-ua"="`"Chromium`";v=`"116`", `"Not)A;Brand`";v=`"24`", `"Google Chrome`";v=`"116`""
        "sec-ch-ua-mobile"="?0"
        "sec-ch-ua-platform"="`"Windows`""
        "sec-fetch-dest"="empty"
        "sec-fetch-mode"="cors"
        "sec-fetch-site"="same-origin"
        "x-csrf-token"="yRuyswTpQMrbP7CtxXE8lKfbwGU=373022eef388e0e8650d8778eb91287e2e8e8cb1f6dacd386ae4c93dc2ab554d418a842070fc8ae63240136843e0cacda819587b"
        } `
        -ContentType "application/json"
        Add-Content C:\temp\cscloudpolicies.json ",`n`n`n"
        Add-Content C:\temp\cscloudpolicies.json $iwr.Content
        write-host "`t success"
    }
    catch {
        write-host "`t failed"
    }

}
