---
title: Data Transformation Techniques
aliases: []
tags:
- topic/data-transformation
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: microsoft-powerbi.md
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

# Data Transformation Techniques

## Date Conversion
- convert filename prefix to date (20250501-myfile.csv)
  - split the column on char "-"
  - the "date" field is a whole number so needs to be converted to text
    - change type -> text
  - now change type -> date

## Timestamp Conversion
- convert "@timestamp" (unix) to datetime
  - ensure @timestamp column is whole number eg. `1.73268E+12`
  - add new column
    - `#datetime(1970, 1, 1, 0, 0, 0) + #duration(0, 0, 0, [timestamp]/1000)`
  - make sure to change type to date/time

## Bytes to Megabytes Conversion
- convert bytes to mbytes
  - rename bytes column to `bytes`
  - add new column `mbytes = [bytes] / 1048576`
  - change column type to decimal

