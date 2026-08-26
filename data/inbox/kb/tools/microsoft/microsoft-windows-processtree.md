---
aliases:
tags:
source:
desc:
references:
title: Process Tree
templateVersion: 1
---
# Windows Process Tree

  

hostname  

└─ System  

   └─ smss.exe  

      └─ winlogon.exe  

         └─ userinit.exe  

            └─ explorer.exe  

               └─ powershell.exe  

                  └─ powershell.exe  

                     └─ powershell.exe  

                        └─ reg.exe  

  

---

  

## System

- **PID 4**: kernel-level process, created at boot.  

- Manages core Windows functions: threads, scheduling, I/O, drivers.  

- Runs in **kernel mode**, not user mode.  

- Always present; if it’s missing or replaced → critical compromise.

  

---

  

## smss.exe (Session Manager Subsystem)

- First user-mode process created by the kernel.  

- Responsibilities:  
  - Starts **CSRSS (Client/Server Runtime Subsystem)** and **Winlogon**.  
  - Creates environment variables.  
  - Manages paging file setup.  
  - Handles creation of Windows sessions (Session 0 for system, Session 1+ for users).  
- Normally runs from `C:\Windows\System32\smss.exe`.  
- Rare to see more than one instance. Multiple or odd paths = suspicious.

  

---

  

## winlogon.exe (Windows Logon Application)

- Responsible for the **logon experience**:  
  - Secure Attention Sequence (Ctrl+Alt+Del).  
  - User authentication.  
  - Loading user profile.  
- Also monitors keyboard activity for locking/unlocking.  
- Launches `userinit.exe` after login.  
- Location: `C:\Windows\System32\winlogon.exe`.

  

---

  

## userinit.exe

- One-time initialization process after login.  
- Tasks:  
  - Runs Group Policy logon scripts.  
  - Restores mapped network drives.  
  - Launches the Windows shell (`explorer.exe`).  
- Normally exits once its work is done — explorer persists as the user’s session.  
- Location: `C:\Windows\System32\userinit.exe`.

  

---

  
## explorer.exe

- Windows **desktop shell**.  
- Provides:  
  - Desktop, taskbar, Start menu.  
  - File Explorer windows.  
  - Handles file associations and drag/drop.  
- Often becomes the parent for processes launched via double-click or Start menu.  
- Location: `C:\Windows\explorer.exe`.









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


