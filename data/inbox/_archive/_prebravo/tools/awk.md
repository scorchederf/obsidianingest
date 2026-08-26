---
id: tools-scp
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-scp

backlinks: [[]]

sources:

---

AWK is a programming language designed for text processing and is typically used as a data extraction and reporting tool.

```shell
#split string on -F "::" and then print cols 1 and 3
echo "hello::there::friend" | awk -F "::" '{print $1, $3}'
hello friend
```
