---
id: tools-scp
tags: ["kali", "tool", "exfiltration", "secure"]
created: 2023-01-12 11:56
---
# tools-scp

backlinks: [[]]

sources:

---

```shell

scp -P 2222 student@$IP:/home/student/access-logs.tar.gz /home/kali/Documents/git/bravo/offsec/pen200/3/access-logs.tar.gz

```

```bash
-r      # transfer directory 
-v      # see the transfer details
-C      # copy files with compression
-l 800  # limit bandwith with 800
-p      # preserving the original attributes of the copied files
-P      # connection port
-q      # hidden the output
```

### Commands

```bash
$ scp file user@host:/path/to/file                        # copying a file to the remote system using scp command
$ scp user@host:/path/to/file /local/path/to/file         # copying a file from the remote system using scp command
```

```bash
$ scp file1 file2 user@host:/path/to/directory            # copying multiple files using scp command
$ scp -r /path/to/directory user@host:/path/to/directory  # Copying an entire directory with scp command
```