---
aliases:
tags:
---
-  convert ISO-8601 UTC to AEST `2025-10-14T13:54:31.6203189Z`
	- We are 10 hours ahead so add 10 hours to the datetime
		`=SUBSTITUTE(LEFT(A2,19),"T"," ") + TIME(10,0,0)`
	- Convert the column to this format
	  `yyyy-mm-dd hh:mm:ss`
- 