---
aliases:
tags:
source:
desc:
references:
title: CrowdStrike NextGen Siem
templateVersion: 1.1
---

# ngsiem

```
#repo=xdr_indicatorsrepo
| Ngsiem.event.subtype = "result_event"
| Ngsiem.alert.id = ?alertid
| drop([
    #ecs.version, #repo, #repo.cid, #type, #Vendor,
    Ngsiem.alert.id, Ngsiem.detection.id, Ngsiem.event.product, Ngsiem.event.subtype, Ngsiem.event.type, Ngsiem.event.vendor, Ngsiem.indicator.id, Ngsiem.metadata, "Ngsiem.parent.indicator.id[0]",
    Vendor.EventType,
    @id, @ingesttimestamp, @timestamp.nanos, @timezone, @rawstring
])
```


# add custom fields to notification emails

![[assets/attachments/kb/tools/crowdstrike/crowdstrike-ngsiem/image-20260409100208215.png]]

```yml
# This is an exported workflow. Editing this file is not recommended.

name: ucq-wfl-NotifyCyberByEmail
description: if detection rule matches *ucq-dtr-test-* it will branch to TRUE else will send standard email
disconnected_nodes:
    - '{"id":"notes_48d1b99d-75a6-4e90-80a3-294f91b0e27a","position":{"x":289.15244347690657,"y":1424.5331564807166},"node_type":"notes","comment":"\u003c!-- LACHY - THIS GETS THE DATA FROM THE EVENT QUERY --\u003e\n\n\n\u003c!-- ${Workflow name} --\u003e\n\u003ctable\u003e\n\u003ctr\u003e\u003ctd\u003eAlert Name\u003c/td\u003e\u003ctd\u003e${Name}\u003c/td\u003e\u003c/tr\u003e\n\u003ctr\u003e\u003ctd\u003eDescription\u003c/td\u003e\u003ctd\u003e${Description}\u003c/td\u003e\u003c/tr\u003e\n\u003ctr\u003e\u003ctd\u003eSeverity\u003c/td\u003e\u003ctd\u003e${Severity}\u003c/td\u003e\u003c/tr\u003e\n\u003ctr\u003e\u003ctd\u003eURL\u003c/td\u003e\u003ctd\u003e${Source event URL}\u003c/td\u003e\u003c/tr\u003e\n\u003c/table\u003e\n\n${cs.table.html(\n\tdata[''activity_d9fa15b5-09ef-44ad-bbd4-2711f8c9a43c.LogScale.SearchResult.ucq-qry-ngSiemResultEventByAlertID.raw_results''],\n\t''.'',\n\t''None''\n)}"}'
    - '{"id":"notes_f586abe0-3917-402b-aa6e-600e0081e569","position":{"x":298.4277169440895,"y":1184.427985770668},"node_type":"notes","comment":"// LACHY - Not as clumsy or random as a blaster; an elegant weapon for a more civilized age.\n// this is not magic, just getting the alert details, then returning the root and ucq nodes in the output\n\n// ucq-qry-ngSiemResultEventByAlertID\n\n#repo=xdr_indicatorsrepo\n| Ngsiem.event.subtype = \"result_event\"\n| Ngsiem.alert.id = ?alertid\n| drop([\n    #ecs.version, #repo, #repo.cid, #type, #Vendor,\n    Ngsiem.alert.id, Ngsiem.detection.id, Ngsiem.event.product, Ngsiem.event.subtype, Ngsiem.event.type, Ngsiem.event.vendor, Ngsiem.indicator.id, Ngsiem.metadata, \"Ngsiem.parent.indicator.id[0]\",\n    Vendor.EventType,\n    @id, @ingesttimestamp, @timestamp.nanos, @timezone, @rawstring\n])\n\n\n\n// output\n/*\n{\n  \"type\": \"object\",\n  \"$schema\": \"https://json-schema.org/draft-07/schema\",\n  \"required\": [\n    \"ucq\"\n  ],\n  \"properties\": {\n    \"ucq\": {\n      \"type\": \"object\",\n      \"properties\": {}\n    }\n  },\n  \"description\": \"Generated response schema\"\n}\n*/"}'
trigger:
    next:
        - 34name_matches_ucq_dtr_test_3434name_matches_adam34
    event: Investigatable/NGSIEM
    name: Detection > NG-SIEM Detection
    type: Signal
actions:
    activity_32a6fa6d-e7b8-4ddf-aaeb-c51ac358bf93:
        id: 07413ef9ba7c47bf5a242799f59902cc
        name: Send email - 4
        properties:
            msg: |
                <!-- ${Workflow.Definition.Name} -->
                <table>
                <tr><td>Alert Name</td><td>${Trigger.Category.Investigatable.Name}</td></tr>
                <tr><td>Description</td><td>${Trigger.Category.Investigatable.Description}</td></tr>
                <tr><td>Severity</td><td>${Trigger.Category.Investigatable.Severity}</td></tr>
                <tr><td>URL</td><td>${Trigger.SourceEventURL}</td></tr>
                </table>
            msg_type: html
            subject: '[ALERT:${Trigger.Category.Investigatable.Severity}] ${Trigger.Category.Investigatable.Name}'
            to: []
    activity_343df31c-8caf-4147-b35d-8c1c268ce965:
        id: 07413ef9ba7c47bf5a242799f59902cc
        name: Send email - 3
        properties:
            msg: |-
                <!-- ${Workflow.Definition.Name} -->
                <table>
                <tr><td>Alert Name</td><td>${Trigger.Category.Investigatable.Name}</td></tr>
                <tr><td>Description</td><td>${Trigger.Category.Investigatable.Description}</td></tr>
                <tr><td>Severity</td><td>${Trigger.Category.Investigatable.Severity}</td></tr>
                <tr><td>URL</td><td>${Trigger.SourceEventURL}</td></tr>
                </table>
            msg_type: html
            subject: '[ALERT:${Trigger.Category.Investigatable.Severity}] ${Trigger.Category.Investigatable.Name}'
            to: []
    activity_722f6aa4-f13b-45c5-8fd0-c73c27607f6b:
        id: 07413ef9ba7c47bf5a242799f59902cc
        name: Send email - 5
        properties:
            msg: |-
                <!-- ${Workflow.Definition.Name} -->
                <table>
                <tr><td>Alert Name</td><td>${Trigger.Category.Investigatable.Name}</td></tr>
                <tr><td>Description</td><td>${Trigger.Category.Investigatable.Description}</td></tr>
                <tr><td>Severity</td><td>${Trigger.Category.Investigatable.Severity}</td></tr>
                <tr><td>URL</td><td>${Trigger.SourceEventURL}</td></tr>
                </table>

                ${cs.table.html(
                	data['activity_d9fa15b5-09ef-44ad-bbd4-2711f8c9a43c.LogScale.SearchResult.ucq-qry-ngSiemResultEventByAlertID.raw_results'],
                	'.',
                	'None'
                )}
            msg_type: html
            subject: '[ALERT:${Trigger.Category.Investigatable.Severity}] ${Trigger.Category.Investigatable.Name}'
            to: []
    activity_59523b93-0b1f-4e11-895e-b8ece140f81f:
        id: 7b77cb5d5ff2651cc51c7c4c610d54d1
        name: Add comment to alert
        next:
            - name_matches_ucq_dtr_
        properties:
            comment: |+
                executing ucq-wkf-NotifyCyberByEmail


            investigatable_id: ${Trigger.Category.Investigatable.InvestigatableID}
    activity_d9fa15b5-09ef-44ad-bbd4-2711f8c9a43c:
        id: 38e69a5ba0d542cfbbaf877c80b2934d_38e69a5ba0d542cfbbaf877c80b2934d_74b1898929924b068aec6034ef5d2104
        name: Event Query - ucq-qry-ngSiemResultEventByAlertID
        next:
            - activity_722f6aa4-f13b-45c5-8fd0-c73c27607f6b
        properties:
            alertid: ${Trigger.Category.Investigatable.InvestigatableID}
            output_files_only: false
            workflow_export_event_query_results_to_csv: false
conditions:
    34name_matches_ucq_dtr_test_3434name_matches_adam34:
        next:
            - activity_343df31c-8caf-4147-b35d-8c1c268ce965
        expression: (Trigger.Category.Investigatable.Name:*'ucq-dtr-test-*'),(Trigger.Category.Investigatable.Name:*'*adam*')
        display:
            - '[[&#34;Name matches ucq-dtr-test-*&#34;],[&#34;Name matches *adam*&#34;]]'
        else:
            - activity_59523b93-0b1f-4e11-895e-b8ece140f81f
    name_matches_ucq_dtr_:
        next:
            - activity_d9fa15b5-09ef-44ad-bbd4-2711f8c9a43c
        expression: Trigger.Category.Investigatable.Name:*'ucq-dtr-*'
        display:
            - Name matches ucq-dtr-*
        else:
            - activity_32a6fa6d-e7b8-4ddf-aaeb-c51ac358bf93



```


# RansomwareOpenFile

```
#event_simpleName=RansomwareOpenFile
 
\Device\HarddiskVolume1\Program Files\CrowdStrike\{5dc635d1-287b-11f1-9059-0050569264a3}.key
 
That file is a Canary File (also known as a honeyfile), and seeing a RansomwareOpenFile event associated with it means the "trap" worked exactly as intended. CrowdStrike places these bait files in strategic locations—including its own program folders and common user directories—to catch malicious processes in the act of discovery or encryption. Why this file exists? The {guid}.key file is designed to look like a high-value target for ransomware. Most modern ransomware variants don't just encrypt everything at once; they crawl the file system looking for specific extensions like .docx, .pdf, or .key (cryptographic keys).  By placing a file with a .key extension in a protected directory, the Falcon sensor creates a "tripwire."

```







![[assets/attachments/kb/tools/crowdstrike/crowdstrike-ngsiem/image-20260409091012744.png]]


![[assets/attachments/kb/tools/crowdstrike/crowdstrike-ngsiem/image-20260323143337589.png]]




![[assets/attachments/kb/tools/crowdstrike/crowdstrike-ngsiem/image-20260323170003393.png]]

![[assets/attachments/kb/tools/crowdstrike/crowdstrike-ngsiem/image-1-20260323170134981.png]]


