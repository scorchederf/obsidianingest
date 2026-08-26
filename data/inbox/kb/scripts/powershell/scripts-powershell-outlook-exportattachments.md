---
aliases:
tags:
---
create a folder inside your inbox called `export` and copy the files you want to export to there

```powershell

# Define the folder to save attachments
$savePath = "$env:USERPROFILE\Desktop\EmailAttachmentsExport"

# Create the folder if it doesn't exist
if (-not (Test-Path $savePath)) {
    New-Item -ItemType Directory -Path $savePath | Out-Null
}

# Connect to Outlook
$outlook = New-Object -ComObject Outlook.Application
$namespace = $outlook.GetNamespace("MAPI")

# Choose the folder (e.g., Inbox or a subfolder)
$folder = $namespace.GetDefaultFolder([Microsoft.Office.Interop.Outlook.OlDefaultFolders]::olFolderInbox)
$folder = $folder.Folders.Item("export")

# Loop through all emails in the folder
foreach ($mail in $folder.Items) {

    # Skip if it’s not a MailItem (e.g., meeting requests)
    if ($mail -is [Microsoft.Office.Interop.Outlook.MailItem]) {
        foreach ($att in $mail.Attachments) {

	        # Format the SentOn date as YYYYMMDD
	        $datePrefix = $mail.SentOn.ToString("yyyyMMdd")
	
	        # Build the new filename
	        $fileName = "$datePrefix-$($att.FileName)"
	        $filePath = Join-Path $savePath $fileName
	
			# Avoid overwriting files with same name
			if (Test-Path $filePath) {
				$timestamp = (Get-Date).ToString("yyyyMMdd_HHmmss")
				$filePath = Join-Path $savePath "$timestamp`_$fileName"
	        }
	
	        # Save the attachment
	        $att.SaveAsFile($filePath)
	        Write-Host "Saved: $filePath"
	    }
	}
}
Write-Host "✅ All attachments saved to: $savePath"
```