---
title: redis
aliases: []
tags:
- tool/redis-cli
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: redis.md
related_tools:
- '[[redis-cli]]'
related_techniques: []
related_tactics: []
related_services: []
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: ''
port: '6379'
protocol: tcp
os: ''
---

# redis

## Connection
- connect `redis-cli -h $ip -p 6379`
    - `redis-cli -h $ip -p 6379 -a password`

## Commands
- info `info`
- list all keys `keys *`
- select database `select 0`
- get values `get "flag"`

