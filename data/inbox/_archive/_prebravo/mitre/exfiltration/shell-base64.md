---
id: shell-base64
tags: [windows, base64, exfiltration]
created: 2023-01-12 11:56
---
# shell-base64

backlinks: [[]]

sources:

- <https://www.systanddeploy.com/2021/02/use-powershell-to-convert-your-files.html>

---

## powershell

Converting an object to its base-64 representation can be a really quick way to exfiltrate single files.
i - you may need to modify the console buffer size using the below command

```powershell
$host.UI.RawUI.BufferSize = New-Object System.Management.Automation.Host.Size(160,5000)
```

Convert a file to base-64

```powershell
write-output(-join("$","data='",[System.Convert]::ToBase64String([System.IO.File]::ReadAllBytes("c:\temp\test.pdf")),"'"))
```

Convert a base-64 string back to a file (make sure you paste the output of the above command)

```powershell
$out='c:\temp\test2.pdf';[System.IO.File]::WriteAllBytes($out,[convert]::FromBase64String($data))
```

Images can be displayed in html - copy output to html file and open in browser.
```shell
echo -n "<html><body><img src='data:image/png;base64,$(cat input_image.png | base64 | tr -d '\r\n')' /></body></html>" > outputimage.html
```
