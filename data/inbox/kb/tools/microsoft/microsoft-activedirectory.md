---
aliases:
tags:
source:
desc:
references:
title: Active Directory
templateVersion: 1
---

![[windows_event_monitoring_combined_full.csv]]


```yaml
      - name: Application
        onlyEventIDs: [1518, 1511, 1000, 1001, 1002, 95, 1022, 1033]
      - name: Security
        excludeEventIDs: [4689, 4688, 5156, 5158, 5446, 5447, 4658, 5058, 5061, 600, 4656, 4661]
      - name: System
        onlyEventIDs: [7022, 7023, 7024, 7026, 7031, 7032, 7034, 6, 7045, 7000, 19, 1, 13, 12]

```
	
- find out which port is used for rdp
	- `reg query "HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp"`
- remote desktop connection cmd
	- `mstsc /v:10.1.2.3`
	- `mstsc /v:server01.domain.local`




# accounts


- compare to user accounts
  ```powershell
$user1 = 'adm_alice'
$user2 = 'adm_bob'

$u1Groups = (Get-ADUser $user1 -Properties MemberOf).MemberOf
$u2Groups = (Get-ADUser $user2 -Properties MemberOf).MemberOf

Compare-Object $u1Groups $u2Groups -IncludeEqual  

  ```








---
Related notes based on filename
```dataviewjs
const root = dv.current().file.name;

const pages = dv.pages("")
  .where(p => p.file.name.startsWith(root + "-"))
  .sort(p => p.file.name);

const tree = {};

for (const p of pages) {
  const parts = p.file.name.replace(root + "-", "").split("-");

  const child = parts[0];
  const grandchild = parts.slice(1).join("-");

  if (!tree[child]) tree[child] = { node: null, children: [] };

  if (parts.length === 1) {
    tree[child].node = p;
  } else {
    tree[child].children.push(p);
  }
}

const output = [];

for (const key of Object.keys(tree)) {
  const entry = tree[key];

  if (entry.node) {
    output.push(`- ${entry.node.file.link}`);

    for (const gc of entry.children) {
      output.push(`  - ${gc.file.link}`);
    }
  }
}

dv.paragraph(output.join("\n"));
```


