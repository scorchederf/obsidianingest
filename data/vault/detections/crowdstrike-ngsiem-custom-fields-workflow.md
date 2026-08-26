---
title: CrowdStrike ngsiem Custom Fields Workflow
aliases: []
tags:
- detection/ngsiem
- tool/crowdstrike
category: detections
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: crowdstrike-ngsiem.md
related_tools:
- '[[ngsiem]]'
- '[[CrowdStrike]]'
related_techniques: []
related_tactics: []
related_services: []
related_os:
- '[[\Device\HarddiskVolume1\Program Files\CrowdStrike\{5dc635d1-287b-11f1-9059-0050569264a3}.key]]'
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# CrowdStrike ngsiem Custom Fields Workflow

## Description
This chunk of the document describes the configuration of the CrowdStrike NextGen SIEM (ngsiem) for filtering and custom field addition in notification emails.

The first section shows a search query for filtering events in ngsiem. The query filters events with a specific subtype and alert ID, and then drops certain fields from the event data.

The second section provides instructions on adding custom fields to notification emails.

This is an event related to the detection of a ransomware attempt using a Canary File (also known as a honeyfile). The file in question is located at `\Device\HarddiskVolume1\Program Files\CrowdStrike\{5dc635d1-287b-11f1-9059-0050569264a3}.key`. This file is designed to look like a high-value target for ransomware, as it has a `.key` extension, which is a common target for ransomware variants that crawl the file system looking for specific extensions like `.docx`, `.pdf`, or `.key`. The presence of this file in a protected directory serves as a 'tripwire' for the Falcon sensor, indicating that a malicious process has attempted to interact with it.

## Workflow Description
This is an exported workflow. Editing this file is not recommended.

name: ucq-wfl-NotifyCyberByEmail
description: if detection rule matches *ucq-dtr-test-* it will branch to TRUE else will send standard email

The workflow contains several actions, each with properties for sending emails and adding comments to alerts.

## Workflow Configuration
```yaml
# This is an exported workflow. Editing this file is not recommended. (continued)

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
            - '[["Name matches ucq-dtr-test-*"],["Name matches *adam*"]]
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

## References
- assets/attachments/kb/tools/crowdstrike/crowdstrike-ngsiem/image-20260409091012744.png
- assets/attachments/kb/tools/crowdstrike/crowdstrike-ngsiem/image-20260323143337589.png
- assets/attachments/kb/tools/crowdstrike/crowdstrike-ngsiem/image-20260323170003393.png
- assets/attachments/kb/tools/crowdstrike/crowdstrike-ngsiem/image-1-20260323170134981.png

