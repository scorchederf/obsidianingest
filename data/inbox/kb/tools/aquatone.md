---
aliases:
tags:
source:
  - https://github.com/michenriksen/aquatone
  - https://github.com/shelld3v/aquatone
desc: Aquatone is a tool for visual inspection of websites across a large amount of hosts and is convenient for quickly gaining an overview of HTTP-based attack surface.
references:
---
Aquatone is a tool for visual inspection of websites across a large amount of hosts and is convenient for quickly gaining an overview of HTTP-based attack surface.

Original version is no longer in development, new fork done by shelld3v

- Aquatone can make a report on hosts scanned with the [Nmap](https://nmap.org/) or [Masscan](https://github.com/robertdavidgraham/masscan) portscanner. Simply feed Aquatone the XML output and give it the `-nmap` flag to tell it to parse the input as Nmap/Masscan XML
	- `cat scan.xml | aquatone -nmap`
- install via extraction
	- `cd opt; sudo wget https://github.com/michenriksen/aquatone/releases/download/v1.7.0/aquatone_linux_amd64_1.7.0.zip`
	- `sudo unzip aquatone_linux_amd64_1.7.0.zip`
- execute using output from nmap
	- `cat web_discovery.xml | ./aquatone -nmap`
- 






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
