---
title: Inject CSS for Prefixed Headings
aliases: []
tags:
- study-notes
- technique/
- web-shell
category: study_notes
status: draft
date_created: '2026-08-26'
date_modified: '2026-08-26'
source: javascript-injection.md
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

# Inject CSS for Prefixed Headings

## Inject CSS for Prefixed Headings
```js
const injectCSS = css => {
  let el = document.createElement('style');
  el.type = 'text/css';
  el.innerText = css;
  document.head.appendChild(el);
  return el;
};

injectCSS('h1,h1:before{color:#ff0}h2,h2:before{color:#fd0}h3,h3:before{color:#fb0}h4,h4:before{color:#f90}h5,h5:before{color:#f70}h6,h6:before{color:#f50}h1:before{content:"1. "}h2:before{content:"2. "}h3:before{content:"3. "}h4:before{content:"4. "}h5:before{content:"5. "}h6:before{content:"6. "}');
```

