---
aliases:
tags:
---
Initially based on https://learn.microsoft.com/en-us/defender-endpoint/mde-sec-ops-guide

# daily
- run the sopo script
- ngsiem
	- [crowdstrike-ngsiem-dashboards](https://falcon.us-2.crowdstrike.com/investigate/search/custom-dashboards?search=ucq-dsh)
		- `ucq-dsh-Mitre-Exfiltration` 
			- look for large amounts of data being copied to usbs or file sharing services
			  ![[Pasted image 20251021151828-20251021151830416.png]]
			- look for sudden jumps in file transfers on http/s, dns, ftp
			  ![[Pasted image 20251021151914-20251021151914999.png]]
	- [crowdstrike-ngsiem-detections](https://falcon.us-2.crowdstrike.com/unified-detections/)
		- use daily filter
			- `IOAName != Email: Info Alert`
			- `Technique != Unknown`
	- [crowdstrike-cloud-dashboard](https://falcon.us-2.crowdstrike.com/cloud-security/cspm/dashboard)
		- look for increases in CRITICAL and HIGH misconfigurations
	- [crowdstrike-endpoint-activity](https://falcon.us-2.crowdstrike.com/dashboards-v2/dashboard/9D5413A9-50CB-4242-8DE4-F32C23534A3B)
- servicenow
	- [privilege access requests (PAR)](https://ucareqld.service-now.com/nav_to.do?uri=%2Fsysapproval_approver_list.do%3Fsysparm_query%3Dapprover%3D94bea2f2db45895009b4fcd1f39619da%5Estate%3Drequested%26sysparm_first_row%3D1%26sysparm_view%3D)
	- [tasks](https://ucareqld.service-now.com/nav_to.do?uri=%2Ftask_list.do%3Fsysparm_query%3Dassignment_group%3D76b50ad5db3eac10400bbd16f496195e%5EstateNOT%20IN3,4,6,-16,7,8,18,19,14,-2,-101,-102,-30,-29,-23%5EnumberNOT%20LIKEGAP%26sysparm_first_row%3D1%26sysparm_view%3D)
	- [incidents](https://ucareqld.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Factive%3Dtrue%26sysparm_query%3Dactive%3Dtrue%5EstateIN1,21,2,9,16,11%5EEQ)
- mimecast
	- check and release emails caught in [mimecast-heldmessages](https://login-au.mimecast.com/admin#message-center/held-messages)


# weekly
- 



# monthly
- manually patch servers we own
	- UCQ-RUMBAG-P001, UCQ-RUMBAG-P002, UCQ-RUMBAG-P003
		- post patch ensure runzero services are running
	- UCQ-CYBER-P001, UCQ-CYBER-P002
		- check updates from microsoft online
	- UCQ-LS01-P001, UCQ-LS02-P001, UCQ-LS01-P002, UCQ-LS02-P002
		- post patch, verify collectors are running