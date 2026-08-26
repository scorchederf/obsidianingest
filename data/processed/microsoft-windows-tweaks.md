---
aliases:
tags:
source:
desc:
references:
---
# #windows11 restore old right click context menu

`reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve`




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


