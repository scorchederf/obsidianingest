
for ($i=1; $i -lt 200; $i++) {
    $session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
    $session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    $session.Cookies.Add((New-Object System.Net.Cookie("_gcl_au", "1.1.859846632.1695611032", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("ajs_anonymous_id", "917880bc-371f-4e36-b223-1a66f2a30713", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("hubspotutk", "a7e3b27dcd3b8919528223b0d0f4c65f", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("intercom-id-awwxrc0h", "6b6d16c5-4e9b-4ceb-858f-7686f17a2585", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("intercom-device-id-awwxrc0h", "a3b34fc8-835e-4e24-8bfc-4b8cc833bdf7", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d", "eyJpdiI6IlRSYlc0ejFUYkMwWDVvVUlyVEtvaFE9PSIsInZhbHVlIjoiRlZnbkNTVlROUGYwWDBmcVRGRytqbzUxZ0JJdHB5MTI2endFbzFRY25JQTRScmNRMDQ1bmxWMTUweHFGakFHbWRMWkt5Q0NETTJTd0Z1dlYrcGUvYlVUQmxVKzhRbEFINFFlVmNtWnJyZTRWbWY3RzdRZGl5dlV5c1luRTk4TXFkV1pxWVFPNG9KNTEyUTE3SmtuOUdwaFdhN0ZwdEU4Y0QrNkI2MHRiNDZuSzhwNEFmUHVoc3Q0RDAvVnZSSWNJRmRPSi9yNGU1TnlRUnlQRmhuSFhjRU1UK1I3SUVONTNWWlNpZ2U3cktMaz0iLCJtYWMiOiJlNTRmYjdlYTFhNTc2NGZjNDdmZDM5MjZmOTQ4ODNiMDQ2ZTE0OWEyMmU2NzQwNzYwMzU2NTRhZjg0Y2MyODY4IiwidGFnIjoiIn0%3D", "/", "academy.hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("ajs_user_id", "6f4839dff796511fcc59aa77acd7fb54", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("messagesUtk", "1bd89ddaa43e4d0fa3563b585316a4f2", "/", ".academy.hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("__hssrc", "1", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("cf_clearance", "wMQKdPS_meERJjZ92KHM5.dNJmb8PYR7Vjx08MnhnxA-1696140234-0-1-200ecf5a.da34b87a.770f90ba-250.0.0", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("__gtm_referrer", "https%3A%2F%2Fwww.google.com%2F", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_hjSessionUser_2732698", "eyJpZCI6ImIwN2I0ZWExLTMwNzMtNWQ1My1hNzdhLTRlNWYyNzJlZDQ5NSIsImNyZWF0ZWQiOjE2OTU2MTEwMzE4NTQsImV4aXN0aW5nIjp0cnVlfQ==", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_ga_0W7E9P1F2V", "GS1.1.1696833470.3.1.1696833606.50.0.0", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_ga_BFR4KR7D60", "GS1.2.1696988374.15.0.1696988374.60.0.0", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_ga", "GA1.2.551493364.1695611034", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("__hstc", "186608822.a7e3b27dcd3b8919528223b0d0f4c65f.1695611034608.1696834387148.1696988376833.15", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_ga_TKKV7WGJ6V", "GS1.1.1697083121.17.0.1697083121.0.0.0", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("_gid", "GA1.2.53551599.1697083126", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("ln_or", "eyIxMzQxNTkzIjoiZCJ9", "/", "academy.hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("intercom-session-awwxrc0h", "aStzTVpFY3psU041MXBVVHBUTmZ3S05HSmtBYnFuc0hCdk1hUmc1WUdpbEFnUmcwMGJFUjhmOTZxeVJtRGl0ZS0tSEpoSWU2Znp2Y1dpWEUzSVFtRUJSZz09--e51d5975f17eeff5e86963491d50f6c7ab126d58", "/", ".hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("XSRF-TOKEN", "eyJpdiI6IlQzQ2l4aFBnMXorbXB1NUlDcW9UeHc9PSIsInZhbHVlIjoid1E4U2R2N2RiK1M1T1hIb3lRUSswcHBSRmhicWllNFI2LytIZ1hMTFJmYTIxM09UaFkvcFRaZWhSVEo5RVVib2ZOaHE0NmRvRFBOYjZGTGRZa0Q3dGNKNTE0UXlCeERIR2RuZWlUL3ZYR05uWDc1VGMxZmxwUUZEYzNCR1ZWN2UiLCJtYWMiOiIwNmY3YzQxNWM5MmZmZDFiNzI4ZWM2YzYxMTYwYWU0NzAxNDg5MDUzOTI1YTQ5NWI5ZjRkZDYwMjAxNjE2NDEzIiwidGFnIjoiIn0%3D", "/", "academy.hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("htb_academy_session", "eyJpdiI6IjBDUDlzVTI5REd3NEpzS2FZU1hBTkE9PSIsInZhbHVlIjoieW0yUGNUeFNxTDlWR0tuMldmUXhCQ1ZOUkZnU0x2NG1VdlV4eXIrL3UvVnRCNSs4Z2tDOEYwcy9UYmJuR2ZyUEV2REs3eW5KaG9naysvVW1ka2pFamlZTVNkMTRDQ0poU1hsY0lsQTlBcFJWdjRhcE9XKzBPS3g2TVMvOSs5U3IiLCJtYWMiOiI5YjVmYmRlZTgwOTkxZGFjMDQxZDhlZDkwMGY3YzZkNTg3Y2ExMDk4NWI2MWExNGQxODA4ZjlmNWNkNmYyY2QzIiwidGFnIjoiIn0%3D", "/", "academy.hackthebox.com")))
    $session.Cookies.Add((New-Object System.Net.Cookie("__cf_bm", "nBZRfbpxqOAkHvUNn4ZiG5UEAfYHZGlfWSmDyPv5ZPw-1697084075-0-AUdErtRvtEQltXnIcOJYJ+vcd12Yb/3o65Kkh1RZzF5K6m+yTBi0WB1nW7WRhJ2dSJ7rFY8L9I++EFnqZNUEgqQ=", "/", ".hackthebox.com")))
    $request = Invoke-WebRequest -UseBasicParsing -Uri "https://academy.hackthebox.com/module/cheatsheet/$i" -WebSession $session -Headers @{
        "authority"="academy.hackthebox.com"
        "method"="GET"
        "path"="/module/cheatsheet/$i"
        "scheme"="https"
        "accept"="text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        "accept-encoding"="gzip, deflate, br"
        "accept-language"="en-US,en;q=0.9"
        "referer"="https://academy.hackthebox.com/module/112/section/1185"
        "sec-ch-ua"="`"Google Chrome`";v=`"117`", `"Not;A=Brand`";v=`"8`", `"Chromium`";v=`"117`""
        "sec-ch-ua-mobile"="?0"
        "sec-ch-ua-platform"="`"Windows`""
        "sec-fetch-dest"="document"
        "sec-fetch-mode"="navigate"
        "sec-fetch-site"="same-origin"
        "sec-fetch-user"="?1"
        "upgrade-insecure-requests"="1"
    }
    #write-host $request.Content
    
    if ($request.Links.Count -le 0 ){
        write-host "saving $i"
        $request.Content >> c:\temp\cheatsheet-$i.md
    } else {
        write-host "$i html no save"
    }
    Start-Sleep -Seconds 10

    
}