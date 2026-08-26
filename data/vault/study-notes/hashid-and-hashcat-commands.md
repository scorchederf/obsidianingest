---
title: HashiD and Hashcat Commands
aliases: []
tags:
- study-notes/hashing
- tool/hashid
- tool/hashcat
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: cheatsheet-20.md
related_tools:
- '[[hashid]]'
- '[[hashcat]]'
- '[[crunch]]'
- '[[cupp]]'
- '[[kwp]]'
- '[[cewl]]'
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

# HashiD and Hashcat Commands

## Command Usage
```
- `pip install hashid`
  Install the `hashid` tool

- `hashid <hash>` OR `hashid <hashes.txt>`
  Identify a hash with the `hashid` tool

- `hashcat -example-hashes`
  View a list of `Hashcat` hash modes and example hashes

- `hashcat -b -m <hash mode>`
  Perform a `Hashcat` benchmark test of a specific hash mode

- `hashcat -b`
  Perform a benchmark of all hash modes

- `hashcat -O`
  Optimization: Increase speed but limit potential password length

- `hashcat -w 3`
  Optimization: Use when Hashcat is the only thing running, use 1 if running Hashcat on your desktop. Default is 2

- `hashcat -a 0 -m <hash type> <hash file> <wordlist>`
  Dictionary attack

- `hashcat -a 1 -m <hash type> <hash file> <wordlist1> <wordlist2>`
  Combination attack

- `hashcat -a 3 -m 0 <hash file> -1 01 'ILFREIGHT?l?l?l?l?l?l20?1?d'`
  Sample Mask attack

- `hashcat -a 7 -m 0 <hash file> -1=01 '20?1?d' rockyou.txt`
  Sample Hybrid attack

- `crunch <minimum length> <maximum length> <charset> -t <pattern> -o <output file>`
  Make a wordlist with `crunch`

- `python3 cupp.py -i`
  Use `Cupp` interactive mode

- `kwprprocessor -s 1 baseschars/full.base keymaps/en-us.keymap routes/2-to-10-max-3-direction-changes.route`
  `Kwprprocessor` example

- `cewl -d <depth to spider> -m <minimum word length> -w <output wordlist> <url of website>`
  Sample `Cewl` command

- `hashcat -a 0 -m 100 hash rockyou.txt -r rule.txt`
  Sample `Hashcat` rule syntax

- `./cap2hccapx.bin input.cap output.hccapx`
  `cap2hccapx` syntax

- `hcxpcaptool -z pmkidhash_corp cracking_pmkid.cap`
  `hcxpcaptool` syntax
```

