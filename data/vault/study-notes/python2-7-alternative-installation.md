---
title: Python2.7 Alternative Installation
aliases: []
tags:
- study-notes/alias-files
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: python2.7.md
related_tools:
- '[[curl]]'
- '[[pyenv]]'
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

# Python2.7 Alternative Installation

## Description
Alternative installation of Python 2.7 using pyenv.

## Installation Steps
```sh
curl https://pyenv.run | bash
$ echo 'export PYENV_ROOT="\$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="\$PYENV_ROOT/bin:\$PATH"' >> ~/.bashrc
echo 'eval "\$\(pyenv init -\)"' >> ~/.bashrc
source ~/.bashrc
pyenv install 2.7
pyenv shell 2.7
```

## Usage
- Activate Python 2 only for this shell (works on HTB):
  ```sh
  pyenv shell 2.7.18
  python2 34992.py
  ```

## References
- https://pyenv.run

