---
title: Excel Time and Date Functions
aliases: []
tags:
- topic/excel-functions
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: excel.md
related_tools: []
related_techniques: []
related_tactics: []
related_services: []
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: ''
protocol: ''
os: ''
---

# Excel Time and Date Functions

## Date and Time Conversions
### Convert Epoch Milliseconds to Date
```
=(A2/86400000)+DATE(1970,1,1) + TIME(0,0,0)
=(A2/86400/1000)+25569
```

### Convert UTC Time to Excel
```
=DATEVALUE(LEFT(G9,10))+TIMEVALUE(MID(G9,12,8))
```

## Pivot Table Options
### Add Zero to Empty Fields in Pivot Table
Pivot table options
![](assets/attachments/kb/htb/redteam/assets/tools/excel/Replace-Blank-Cells-with-Zeros-Pivot-Tables-Enter-0.png)

## String Manipulation
### Split String on Char and Get Last Instance
`=CHOOSECOLS(TEXTSPLIT(B2, ""), -1)`

### Replace in String
`=SUBSTITUTE(B2, "\Device\HarddiskVolume6", "")`

## Time Format
### Time Format
`dd/mm/yyyy h:mm:ss.000`

