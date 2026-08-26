---
title: username-anarchy
aliases: []
tags:
- tool/username-anarchy
category: tools
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: usernameAnarchy.md
related_tools:
- '[[username-anarchy]]'
related_techniques: []
related_tactics: []
related_services: []
related_os: []
related_notes: []
mitre_tactic: ''
mitre_technique: ''
real_path: /usr/share/username-anarchy/username-anarchy
port: ''
protocol: ''
os: linux
---

# username-anarchy

## Description
username-anarchy is a tool designed to generate potential usernames or user account names based on a given name. It can be particularly useful in social engineering or reconnaissance activities.

## Installation
To install username-anarchy, run the following commands:

```sh
sudo apt install ruby
```

Then, clone the repository from GitHub:

```sh
git clone https://github.com/urbanadventurer/username-anarchy.git
```

## Usage
To use the tool, navigate to the directory containing the script and run it with a name as an argument. For example:

```sh
/usr/share/username-anarchy/username-anarchy Jane Smith
```

The tool will output a list of potential usernames based on the provided name. Here is an example output:

```sh
└─$ /usr/share/username-anarchy/username-anarchy Jane Smith
jane
janesmith
jane.smith
janesmit
janes
j.smith
jsmith
sjane
s.jane
smithj
smith
smith.j
smith.jane
js
```

## References
- https://github.com/urbanadventurer/username-anarchy

