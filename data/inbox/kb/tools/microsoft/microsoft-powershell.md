---
aliases:
tags:
source:
desc:
---


- check if internet is up
	- `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; iwr -uri https://www.google.com -verbose`