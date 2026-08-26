---
title: Attacking Web Applications with Ffuf
aliases: []
tags:
- study-notes
- tool/ffuf
category: study_notes
status: draft
date_created: '2026-08-27'
date_modified: '2026-08-27'
source: 15-54-AttackingWebApplicationsWithFfuf-02-WebFuzzing.pdf
related_tools:
- '[[ffuf]]'
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

# Attacking Web Applications with Ffuf

## Introduction
In this study note, we will explore how to use Ffuf, a powerful tool for discovering hidden web paths and directories in web applications. Ffuf is a fast and efficient tool that can be used to identify potential vulnerabilities and hidden resources on a web server.

## Installing Ffuf
To install Ffuf, you can use the following command:

```bash
$ go get -u github.com/ffuf/ffuf
```

This command will download and install the latest version of Ffuf on your system.

## Using Ffuf
Ffuf can be used to perform a variety of tasks, such as discovering hidden directories and files. Here is an example of how to use Ffuf to discover hidden paths on a web server:

```bash
$ ffuf -u http://example.com/FUZZ -w /path/to/wordlist.txt
```

In this example, `http://example.com/FUZZ` is the base URL that Ffuf will use to perform the request, and `/path/to/wordlist.txt` is the wordlist file that contains the paths to test. Ffuf will send a request to each path in the wordlist and output the results to the console.

## Advanced Usage
Ffuf supports a wide range of options to customize its behavior. Here are some of the most commonly used options:

- `-c`: Follow redirects
- `-u`: Base URL
- `-w`: Wordlist file
- `-t`: Number of concurrent requests
- `-mc`: Only show responses with specific HTTP status codes

For example, to follow redirects and only show responses with HTTP status codes 200 or 302, you can use the following command:

```bash
$ ffuf -u http://example.com/FUZZ -w /path/to/wordlist.txt -c -mc 200,302
```

This command will follow any redirects and only output the results with HTTP status codes 200 or 302.

## References
- https://academy.hackthebox.com/module/54/section/496

