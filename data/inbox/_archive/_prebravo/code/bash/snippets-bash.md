---
id: snippets-bash
tags: [bash, snippets]
created: 2023-01-12 11:56
---
# snippets-bash

backlinks: [[cheatsheet-bash]]

---

## Read each line of a file into an array

```python
lines=[ x.strip() for x in open('input.txt').read().split('\n') if x ]

```
