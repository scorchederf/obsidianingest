$summary="test"
Send-MailMessage `
-From 'UCQ Reminders <reminders@ucareqld.com.au>' `
-To  'adam.stein@ucareqld.com.au' `
-Subject "All Bluecare normal accounts Password expiry Summary -P001" `
-BodyAsHtml $summary `
-SmtpServer mail.uchealth.com.au