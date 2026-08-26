---
aliases:
tags:
source:
desc:
references:
title:
templateVersion: 1.1
---






Summon the beast...




---
references
```dataviewjs
// === Live tree with friendly names, no tags, markdown-only ===
async function renderLiveTreeClean(rootFileName) {
  const pages = dv.pages("")
    .where(p => p.file.name.startsWith(rootFileName + "-"))
    .sort(p => p.file.name);

  const tree = {};

  // Build tree
  for (const p of pages) {
    const parts = p.file.name.replace(rootFileName + "-", "").split("-");
    let current = tree;

    for (let i = 0; i < parts.length; i++) {
      const part = parts[i];
      if (!current[part]) current[part] = { _page: null, _children: {} };

      if (i === parts.length - 1) {
        current[part]._page = p;
      }

      current = current[part]._children;
    }
  }

  // friendly display name
  function friendlyName(p) {
    if (!p) return "";
    if (p.title) return p.title;
    return p.file.name.replace(rootFileName + "-", "")
             .replace(/-/g, " ")
             .replace(/\b\w/g, l => l.toUpperCase());
  }

  // link with friendly name only
  function linkWithFriendlyName(p) {
    return p ? `[[${p.file.path}|${friendlyName(p)}]]` : "";
  }

  // recursive render
  function render(node, depth=0) {
    let out = [];
    for (const key of Object.keys(node).sort()) {
      const entry = node[key];
      const indent = "  ".repeat(depth);
      if (entry._page) out.push(`${indent}- ${linkWithFriendlyName(entry._page)}`);
      else out.push(`${indent}- **${key.replace(/\b\w/g, l => l.toUpperCase())}**`);
      out.push(...render(entry._children, depth+1));
    }
    return out;
  }

  dv.paragraph(render(tree).join("\n"));
}

// === Live-refresh wrapper ===
async function liveTreeClean(rootFileName) {
  await renderLiveTreeClean(rootFileName);

  if (!window.__liveTreeCleanRegistered) {
    window.__liveTreeCleanRegistered = true;

    app.vault.on("modify", async (file) => {
      const root = dv.current().file.name;
      if (file.path.startsWith(root)) {
        await renderLiveTreeClean(root);
      }
    });
  }
}

// Start live markdown tree
await liveTreeClean(dv.current().file.name);



```


