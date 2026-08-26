$EmailFrom = "whistleblower@ccc.qld.gov.au"
$EmailTo = "adamjstein@gmail.com"
$Subject = "Import update regarding your email"
$Body = "Please see attached document - <img src='http://canarytokens.com/tags/static/2vedqtn4p3cnrk61hh7d2apq5/submit.aspx' height=1 width=1 />"
$SMTPServer = "smtp.gmail.com"
$SMTPClient = New-Object Net.Mail.SmtpClient($SmtpServer, 587)
$SMTPClient.EnableSsl = $true
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential("adamjstein@gmail.com", "Coveting-Anointer-Repeated9");
$SMTPClient.Send($EmailFrom, $EmailTo, $Subject, $Body)

