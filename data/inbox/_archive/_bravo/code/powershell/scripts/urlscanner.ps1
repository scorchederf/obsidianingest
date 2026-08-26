[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# based on this site - https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000Cm5hCAC
$jsonConfig = @"
{
    "http": {
        "port": [80, 443],
        "category": [
            {
                "name": "test",
                "ioc": [
                    "https://www.google.com"
                ]
            },
            {
                "name": "adult",
                "ioc": [
                    "https://www.playboyplus.com",
                    "https://www.redtube.com",
                    "https://pornhubs.video/"
                ]
            },
            {
                "name": "drugs",
                "ioc": [
                    "https://www.greenrush.com",
                    "https://www.magicmushroom.com"
                ]
            },
            {
                "name": "dating",
                "ioc": [
                    "https://www.match.com",
                    "https://www.okcupid.com"
                ]
            }
        ]
    },
    "ssh": {
        "port": [22]
    }
}
"@

$config = ConvertFrom-Json $jsonConfig





foreach ($service in $config.PSObject.Properties) {
    $serviceName = $service.Name
    if ($serviceName -eq "http") {
        foreach ($category in $service.Value.category) {
            $catName = $category.name
            foreach ($ioc in $category.ioc) {
                try {
                    $headers = @{
                        "User-Agent"="Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36)"
                    }
                    $r = Invoke-WebRequest $ioc -MaximumRedirection 10 -Headers $headers
                    $rcl = $r.RawContentLength
                    $title = ($r.ParsedHtml.title).Trim()
                    Write-Host "$catName`t$ioc`t`ttitle=$title`trawcontentlength=$rcl"
                } catch {
                    $e = $_.Exception
                    #write-host $e.Message
                    Write-Host "$catName`t$ioc`t`t$e.Message"

                }
            }
        }
    }
}